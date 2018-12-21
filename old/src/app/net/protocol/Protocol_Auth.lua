local ns = namespace("net.protocol")
local ProtocolBase = require("app.net.core.ProtocolBase")

----------------------------
-- 协议加密握手
----------------------------
local ICEncryptSYN = class("ICEncryptSYN", ProtocolBase)
ns.ICEncryptSYN = ICEncryptSYN
ICEncryptSYN.OP_CODE = net.ProtocolCode.P_IC_ENCRYPT_SYN
ICEncryptSYN.CLZ_CODE = "com.kodgames.message.proto.auth.ICEncryptSYN"

-- @param serverId: number
-- @param callback: number
function ICEncryptSYN:ctor(serverId, callback)
    self.super.ctor(self, ICEncryptSYN.OP_CODE, serverId, callback)
end

----------------------------
-- 热更新
----------------------------
local CIVersionUpdateREQ = class("CIVersionUpdateREQ", ProtocolBase)
ns.CIVersionUpdateREQ = CIVersionUpdateREQ

CIVersionUpdateREQ.OP_CODE = net.ProtocolCode.P_CI_VERSION_UPDATE_REQ
CIVersionUpdateREQ.CLZ_CODE = "com.kodgames.message.proto.auth.CIVersionUpdateREQ"

-- @param serverId: number
-- @param callback: number
function CIVersionUpdateREQ:ctor(serverId, callback)
	self.super.ctor(self, CIVersionUpdateREQ.OP_CODE, serverId, callback);
end

-- @param channel: string
-- @param username: string
function CIVersionUpdateREQ:setData(channel, subchannel, libVersion, proVersion)
	local protocolBuf = self:getProtocolBuf()
	protocolBuf.channel = channel
	protocolBuf.subchannel = subchannel
	protocolBuf.libVersion = libVersion
	protocolBuf.proVersion = proVersion
end

----------------------------
local ICVersionUpdateRES = class("ICVersionUpdateRES", ProtocolBase)
ns.ICVersionUpdateRES = ICVersionUpdateRES

ICVersionUpdateRES.OP_CODE = net.ProtocolCode.P_IC_VERSION_UPDATE_RES
ICVersionUpdateRES.CLZ_CODE = "com.kodgames.message.proto.auth.ICVersionUpdateRES"

-- @param serverId: number
-- @param callback: number
function ICVersionUpdateRES:ctor(serverId, callback)
    self.super.ctor(self, ICVersionUpdateRES.OP_CODE, serverId, callback);
end

----------------------------
-- 登录InterfaceServer
----------------------------
local CIAccountAuthREQ = class("CIAccountAuthREQ", ProtocolBase)
ns.CIAccountAuthREQ = CIAccountAuthREQ

CIAccountAuthREQ.OP_CODE = net.ProtocolCode.P_CI_ACCOUNT_AUTH_REQ;
CIAccountAuthREQ.CLZ_CODE = "com.kodgames.message.proto.auth.CIAccountAuthREQ"

-- @param serverId: number
-- @param callback: number
function CIAccountAuthREQ:ctor(serverId, callback)
	self.super.ctor(self, CIAccountAuthREQ.OP_CODE, serverId, callback);
end

-- @param channel: string
-- @param username: string
-- @param code: string
-- @param refreshToken: string
function CIAccountAuthREQ:setData(channel, username, code, refreshToken,area, subChannel, updateChannel)
	local protocolBuf = self:getProtocolBuf();
	protocolBuf.channel = channel;
	protocolBuf.username = username;
	protocolBuf.refreshToken = refreshToken;
	protocolBuf.code = code;
	protocolBuf.platform = game.plugin.Runtime.getPlatform();
	protocolBuf.proVersion = "100000" --tostring(game.service.UpdateService.getInstance():getProductVersion():getVersions()[1]);
	protocolBuf.libVersion = "100000"--game.plugin.Runtime.getBuildVersion()
	protocolBuf.appCode = tonumber(game.plugin.Runtime.getChannelId());
	protocolBuf.deviceId = game.plugin.Runtime.getDeviceId();
	protocolBuf.area = area;
	protocolBuf.subChannel = tonumber(game.plugin.Runtime.getSubChannelId());
	protocolBuf.updateChannel = tonumber(game.plugin.Runtime.getChannelId());
end

----------------------------
local ICAccountAuthRES = class("ICAccountAuthRES", ProtocolBase)
ns.ICAccountAuthRES = ICAccountAuthRES

ICAccountAuthRES.OP_CODE = net.ProtocolCode.P_IC_ACCOUNT_AUTH_RES;
ICAccountAuthRES.CLZ_CODE = "com.kodgames.message.proto.auth.ICAccountAuthRES"

-- @param serverId: number
-- @param callback: number
function ICAccountAuthRES:ctor(serverId, callback)
    self.super.ctor(self, ICAccountAuthRES.OP_CODE, serverId, callback);
end

--手机绑定登录相关
-- phone code response
local ICVerifyCodeRES = class("ICVerifyCodeRES", ProtocolBase)
ns.ICVerifyCodeRES = ICVerifyCodeRES
ICVerifyCodeRES.OP_CODE = net.ProtocolCode.P_IC_VERIFY_CODE_RES
ICVerifyCodeRES.CLZ_CODE = "com.kodgames.message.proto.auth.ICVerifyCodeRES"
function ICVerifyCodeRES:ctor(serverId, callback)
    self.super.ctor(self, ICVerifyCodeRES.OP_CODE, serverId, callback);
end

-- mobile to interface
local CIPhoneLoginREQ = class("CIPhoneLoginREQ", ProtocolBase)
ns.CIPhoneLoginREQ = CIPhoneLoginREQ
CIPhoneLoginREQ.OP_CODE = net.ProtocolCode.P_CI_PHONE_LOGIN_REQ;
CIPhoneLoginREQ.CLZ_CODE = "com.kodgames.message.proto.auth.CIPhoneLoginREQ"

function CIPhoneLoginREQ:ctor(serverId, callback)
	self.super.ctor(self, CIPhoneLoginREQ.OP_CODE, serverId, callback);
end

function CIPhoneLoginREQ:setData(channel, phone, verifyCode, token, area, subChannel, updateChannel)
	local protocolBuf = self:getProtocolBuf();
	protocolBuf.channel = channel;
	protocolBuf.phone = phone;
	protocolBuf.token = token;
	protocolBuf.verifyCode = verifyCode;
	protocolBuf.platform = game.plugin.Runtime.getPlatform();
	protocolBuf.proVersion = tostring(game.service.UpdateService.getInstance():getProductVersion():getVersions()[1]);
	protocolBuf.libVersion = game.plugin.Runtime.getBuildVersion()
	protocolBuf.appCode = tonumber(game.plugin.Runtime.getChannelId());
	protocolBuf.deviceId = game.plugin.Runtime.getDeviceId();
	protocolBuf.area = area;
	protocolBuf.subChannel = tonumber(game.plugin.Runtime.getSubChannelId());
	protocolBuf.updateChannel = tonumber(game.plugin.Runtime.getChannelId());
end

-- phonecode request
local CIVerifyCodeREQ = class("CIVerifyCodeREQ", ProtocolBase)
ns.CIVerifyCodeREQ = CIVerifyCodeREQ
CIVerifyCodeREQ.OP_CODE = net.ProtocolCode.P_CI_VERIFY_CODE_REQ
CIVerifyCodeREQ.CLZ_CODE = "com.kodgames.message.proto.auth.CIVerifyCodeREQ"
function CIVerifyCodeREQ:ctor(serverId, callback)
	self.super.ctor(self, CIVerifyCodeREQ.OP_CODE, serverId, callback);
end
function CIVerifyCodeREQ:setData(phone, type)
	local protocolBuf = self:getProtocolBuf()
	protocolBuf.appCode = tonumber(game.plugin.Runtime.getChannelId())
	protocolBuf.phone = phone
	protocolBuf.type = type
end

-- phone bind req
local CIBindPhoneREQ = class("CIBindPhoneREQ", ProtocolBase)
ns.CIBindPhoneREQ = CIBindPhoneREQ
CIBindPhoneREQ.OP_CODE = net.ProtocolCode.P_CI_BIND_PHONE_REQ
CIBindPhoneREQ.CLZ_CODE = "com.kodgames.message.proto.auth.CIBindPhoneREQ"
function CIBindPhoneREQ:ctor(serverId, callback)
	self.super.ctor(self, CIBindPhoneREQ.OP_CODE, serverId, callback);
end
function CIBindPhoneREQ:setData(newphone,verifyCode,type,oldphone)
	local protocolBuf = self:getProtocolBuf()
	protocolBuf.phone = newphone
	protocolBuf.oldPhone = oldphone
	--2绑定 3更改
	protocolBuf.area = game.service.LocalPlayerService:getInstance():getArea()
	protocolBuf.verifyCode = verifyCode
	protocolBuf.type = type
	--todo
	protocolBuf.accountId = game.service.LocalPlayerService.getInstance():getDisplayId()
	dump(protocolBuf)
end


-- phone bind result respone
local ICBindPhoneRES = class("ICBindPhoneRES", ProtocolBase)
ns.ICBindPhoneRES = ICBindPhoneRES
ICBindPhoneRES.OP_CODE = net.ProtocolCode.P_IC_BIND_PHONE_RES
ICBindPhoneRES.CLZ_CODE = "com.kodgames.message.proto.auth.ICBindPhoneRES"
function ICBindPhoneRES:ctor(serverId, callback)
    self.super.ctor(self, ICBindPhoneRES.OP_CODE, serverId, callback);
end