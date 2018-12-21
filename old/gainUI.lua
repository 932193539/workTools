local csbPath = "ui/csb/Club/UI_jlbyq.csb"
local super = require("app.game.ui.UIBase")
local UIClubGameInvitation = class("UIClubGameInvitation", super, function() return kod.LoadCSBNode(csbPath) end)

function UIClubGameInvitation:ctor()
	self._btnClose = nil
	self._textName = nil
	self._btnAgree = nil
	self._btnRefuse = nil
	self._textClubName = nil
	self._textGameRules = nil
	self._imageHead = nil
	self._imageFrame = nil
end

function UIClubGameInvitation:init()
	self._btnClose = seekNodeByName(self, "Button_Close", "ccui.Button")
	self._textName = seekNodeByName(self, "Text_Name", "ccui.Text")
	self._btnAgree = seekNodeByName(self, "Button_Agree", "ccui.Button")
	self._btnRefuse = seekNodeByName(self, "Button_Refuse", "ccui.Button")
	self._textClubName = seekNodeByName(self, "Text_Club_Name", "ccui.Text")
	self._textGameRules = seekNodeByName(self, "Text_Game_Rules", "ccui.Text")
	self._imageHead = seekNodeByName(self, "Image_head", "ccui.ImageView")
	self._imageFrame = seekNodeByName(self, "Image_frame", "ccui.ImageView")
	self:_registerCallBack()
end

function UIClubGameInvitation:_registerCallBack()
	bindEventCallBack(self._btnClose, handler(self, self._onClickClose), ccui.TouchEventType.ended)
	bindEventCallBack(self._btnAgree, handler(self, self._onClickAgree), ccui.TouchEventType.ended)
	bindEventCallBack(self._btnRefuse, handler(self, self._onClickRefuse), ccui.TouchEventType.ended)
end

function UIClubGameInvitation:_onClickClose(event)

end

function UIClubGameInvitation:_onClickAgree(event)

end

function UIClubGameInvitation:_onClickRefuse(event)

end

