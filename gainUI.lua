local csbPath = "ui/csb/Club/UIClubExamine.csb"
local super = require("app.game.ui.UIBase")
local UIClubExamine = class("UIClubExamine", super, function() return kod.LoadCSBNode(csbPath) end)

function UIClubExamine:ctor()
	self._textName = nil
	self._btnConfirm = nil
	self._textId = nil
	self._btnRefuse = nil
end

function UIClubExamine:init()
	self._textName = seekNodeByName(self, "Text_Name", "ccui.Text")
	self._btnConfirm = seekNodeByName(self, "Button_Confirm", "ccui.Button")
	self._textId = seekNodeByName(self, "Text_ID", "ccui.Text")
	self._btnRefuse = seekNodeByName(self, "Button_Refuse", "ccui.Button")
	self:_registerCallBack()
end

function UIClubExamine:onShow(...)

end

function UIClubExamine:_registerCallBack()
	bindEventCallBack(self._btnConfirm, handler(self, self._onClickConfirm), ccui.TouchEventType.ended)
	bindEventCallBack(self._btnRefuse, handler(self, self._onClickRefuse), ccui.TouchEventType.ended)
end

function UIClubExamine:_onClickConfirm(event)

endfunction UIClubExamine:_onClickRefuse(event)

end

return UIClubExamine

