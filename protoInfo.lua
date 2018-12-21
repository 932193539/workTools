--
local CCLModifyConfirmedGameplaysOrderREQ = class("CCLModifyConfirmedGameplaysOrderREQ", ProtocolBase)
ns.CCLModifyConfirmedGameplaysOrderREQ = CCLModifyConfirmedGameplaysOrderREQ

CCLModifyConfirmedGameplaysOrderREQ.OP_CODE = net.ProtocolCode.?????
CCLModifyConfirmedGameplaysOrderREQ.CLZ_CODE = "com.kodgames.message.proto.club.CCLModifyConfirmedGameplaysOrderREQ"

function CCLModifyConfirmedGameplaysOrderREQ:ctor(serverId, callback)
	self.super.ctor(self, CCLModifyConfirmedGameplaysOrderREQ.OP_CODE, serverId, callback)
end

function CCLModifyConfirmedGameplaysOrderREQ:setData(clubId, confirmedtGameplayKey)
	self:getProtocolBuf().clubId = clubId
	self:getProtocolBuf().confirmedtGameplayKey = confirmedtGameplayKey
end

--
local CLCModifyConfirmedGameplaysOrderRES = class("CLCModifyConfirmedGameplaysOrderRES", ProtocolBase)
ns.CLCModifyConfirmedGameplaysOrderRES = CLCModifyConfirmedGameplaysOrderRES

CLCModifyConfirmedGameplaysOrderRES.OP_CODE = net.ProtocolCode.?????
CLCModifyConfirmedGameplaysOrderRES.CLZ_CODE = "com.kodgames.message.proto.club.CLCModifyConfirmedGameplaysOrderRES"

function CLCModifyConfirmedGameplaysOrderRES:ctor(serverId, callback)
	self.super.ctor(self, CLCModifyConfirmedGameplaysOrderRES.OP_CODE, serverId, callback)
end

===================================

--
function ClubManagerService:sendCCLModifyConfirmedGameplaysOrderREQ(clubId, confirmedtGameplayKey)
	local request = net.NetworkRequest.new(net.protocol.CCLModifyConfirmedGameplaysOrderREQ, self.?????:getClubServiceId())
	request:getProtocol():setData(clubId, confirmedtGameplayKey)
	game.util.RequestHelper.request(request)
end

===================================

--
function ClubManagerService:_onCLCModifyConfirmedGameplaysOrderRES(response)
	local protocol = response:getProtocol():getProtocolBuf()


end

===================================

requestManager:registerResponseHandler(net.protocol.CLCModifyConfirmedGameplaysOrderRES.OP_CODE, self, self._onCLCModifyConfirmedGameplaysOrderRES)

===================================

