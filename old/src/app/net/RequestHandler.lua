local ns = namespace("net")

local RequestHandler = class("RequestHandler")
ns.RequestHandler = RequestHandler

----------------------------
-- 客户端协议处理层
-- RequestManager用于Request和Response的处理
-- 1. 匹配对应的request和response
-- 2. 检查response超时
-- 3. 网络等待通知
----------------------------
function RequestHandler:ctor(timeoutCallback)
    self._waitingRequests = {}      -- 等待响应的Request队列
    self._responseTimeoutTime = 5;  -- 响应超时时间
    self._updateTask = nil;
	self._timeoutCallback = timeoutCallback;
	

    -- 开始更新
    self:_startCheckTimeout();
end

-- 销毁实例
function RequestHandler:dispose()
	self:reset();
	
    -- 终止更新
    self:_endCheckTimeout();
end

-- 忽略当前所有缓存的Requesty以及Response
function RequestHandler:reset()
	for _, req in pairs(self._waitingRequests) do
		if req:getHasResponse() and req:getWaitForResponse() then
			dispatchGlobalEvent("EVENT_BUSY_RELEASE")
		end
	end
    self._waitingRequests = {};
end

-- -- remove 会删除,我只想清空
-- -- os.remove("../Client/src/__Message.lua")
local file = io.open("../Client/src/__Message.lua", "w")

if file then
	file:close()
end

--查找数据,并告诉你该数据的协议及传输过程
local findData = ""
local protoData = "CLCClubDataSYN"

--处理消息(记录消息,跟踪指定消息)
function RequestHandler:dealMessage(message,typeName)
	local file = io.open("../Client/src/__Message.lua", "a+")

	if file then
		file:write(os.date("%H:%M:%S", kod.util.Time.now())..typeName..tostring(message._protocol.class.__cname).."\n")
		
		if protoData ~= "" and tostring(message._protocol.class.__cname) == protoData then
			file:write(debug.traceback().."\n")
		end

	end
	local protocolBuf = message._protocol._protocolBuf
	if findData ~= "" and protocolBuf ~= nil then
		local isFindData = false

		local function tableFind(protocolBuf)
			for k,v in pairs(protocolBuf) do
				if string.lower(tostring(k)) == string.lower(findData) then
					isFindData = true
					break;
				elseif type(v) == "table" then
					tableFind(v)
				end	
			end
		end
	
		tableFind(protocolBuf)

		if isFindData and file then
			file:write(debug.traceback().."\n")
		end
	end
	
	if file then
		file:close()
	end
end


function RequestHandler:onRequest(req)
	self:dealMessage(req," 发送消息: ")
	if req:getHasResponse() then            
		-- 设置超时时间
		req:setTimeoutTime(kod.util.Time.now() + self._responseTimeoutTime);	

		-- 添加进等待队列
		Macro.assetFalse(self._waitingRequests[req:getId()] == nil)
		self._waitingRequests[req:getId()] = req;

		-- 如果需要等待回复, 增加等待计数
		if req:getWaitForResponse() then
			dispatchGlobalEvent("EVENT_BUSY_RETAIN")
		end
	end
end

-- 收到Response
-- @param response: Response
-- @return boolean
function RequestHandler:onResponse(resp)
    -- Logger.debug("Response %s", resp:toString());
	self:dealMessage(resp," 收到消息: ")

    -- 找到对应的request
    local req = self._waitingRequests[resp:getRequestId()];
    if req ~= nil then
        resp:setRequest(req)
		
		if req:getHasResponse() and req:getWaitForResponse() then
			dispatchGlobalEvent("EVENT_BUSY_RELEASE")
		end
	elseif Macro.assertTrue(resp:getRequestId() ~= 0) then
		-- 这条消息可能是断线重连之前的request返回的，已经找不到对应的request了，不用处理
		return
    end

	-- 执行Response
	local handlers = net.RequestManager.getInstance():getResponseHandler(resp:getTypeId());
	if handlers ~= nil then
		for _,handler in ipairs(handlers) do
			handler.func(handler.responder, resp);
		end
	end

	-- Mark request responded flag.	
	if req ~= nil then
		self._waitingRequests[req:getId()] = nil;
	end

    return true;
end

function RequestHandler:_startCheckTimeout()
    self:_endCheckTimeout();
	
    self._updateTask = cc.Director:getInstance():getScheduler():scheduleScriptFunc(function()

        -- 检测协议超时
        if self:_checkTimeout() then
            -- 等待响应response超时, 网络出了问题，直接断线重新登录
			if self._timeoutCallback ~= nil then
				self._timeoutCallback()
			end
            return;
        end
    end, 0, false)
end

function RequestHandler:_endCheckTimeout()
    if self._updateTask ~= nil then
        cc.Director:getInstance():getScheduler():unscheduleScriptEntry(self._updateTask);
        self._updateTask = nil;
    end
end

-- @param boolean
function RequestHandler:_checkTimeout()
	for _,req in pairs(self._waitingRequests) do
        if req:getTimeoutTime() ~= nil and kod.util.Time.now() > req:getTimeoutTime() then
            return true;
        end
    end

    return false;
end

return RequestHandler;