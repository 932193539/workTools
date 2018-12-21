# -*- coding:utf-8 -*-
#告诉我UI路径和你想要在代码中使用的控件，我帮助你生成基本的控件代码

import xml.dom.minidom,os

#UI路径和控件名称
uiDir = r'D:\svn\workspace\branch_quanguo_0709_83447\Skins\quanguobao_guiyang\cocosstudio\csb\Club\UIClubRoom.csd'
gainNodeList = ["Panel_szwf_Tips","Image_szwf","Button_szwf_Tips_Close","Image_mask"]#,,"Image_18""changeText","changeText","changeText","changeText","changeText"]

#记录csb中控件类型与lua中控件类型的对照关系(也包含在lua中控件命名的前缀)
CONTRAST_LIST = {'ImageViewObjectData' :  ["ccui.ImageView","_image"],'TextObjectData' :  ["ccui.Text","_text"] ,'ButtonObjectData' : ["ccui.Button","_btn"],'ParticleObjectData' : ["cc.ParticleSystemQuad","_particle"],'PanelObjectData' : ["ccui.Layout","_panel"],'ListViewObjectData' : ["ccui.ListView","_listView"],'TextBMFontObjectData' : ["ccui.TextBMFont","_textBMFont"],'TextFieldObjectData' : ["ccui.TextField","_textFiled"],'CheckBoxObjectData' : ["ccui.CheckBox","_checkBox"],'ScrollViewObjectData' : ["ccui.ScrollView","_scrollView"],'SingleNodeObjectData' : ["cc.Node","_node"],'SpriteObjectData' : ["cc.Sprite","_sprite"]}

# 打开xml文档
dom = xml.dom.minidom.parse(uiDir)
# 得到文档元素对象
Nodes = dom.documentElement.getElementsByTagName('AbstractNodeData')
# 存储lua中对控件的命名
luaUiNameList = []
# 记录csd中button的名称
buttonList = []
# 记录csd中获取到的控件
csdGainUiList = []

tempName = uiDir.replace(os.path.dirname(uiDir) + "\\","")
uiName = tempName.replace(".csd","")

fo = open("gainUI.lua", "w")
fo.write("local csbPath = \"ui/csb/Club/%s.csb\"\nlocal super = require(\"app.game.ui.UIBase\")\nlocal %s = class(\"%s\", super, function() return kod.LoadCSBNode(csbPath) end)\n\n" % (uiName,uiName,uiName))
fo.write("function %s:init()\n" % (uiName))



#设置控件
for i in range(len(Nodes)):
	for j in range(len(gainNodeList)):
		if gainNodeList[j] == Nodes[i].getAttribute('Name'):
			nodeType = Nodes[i].getAttribute('ctype')
			tempStr = gainNodeList[j].split('_')
			name = ""

			for k in range(1,len(tempStr)):
				name = name + tempStr[k].capitalize()

			if nodeType == "ButtonObjectData":
				buttonList.append(name)
				
			name = CONTRAST_LIST[nodeType][1] + name
			luaUiName.append(name)
			luaUiName.append(name)

			
	
for i in range(len(luaUiNameList)):
	fo.write( "	self.%s = seekNodeByName(self, \"%s\", \"%s\")\n" % (name,gainNodeList[j],CONTRAST_LIST[nodeType][0]))
	
			
fo.write("	self:_registerCallBack()\n")
fo.write("end\n\n")



#设置按钮点击事件
if len(buttonList) > 0:
	fo.write("function %s:_registerCallBack()\n" % (uiName))
	for i in range(len(buttonList)):		
		fo.write("	bindEventCallBack(self._btn%s, handler(self, self._onClick%s), ccui.TouchEventType.ended)\n" % (buttonList[i],buttonList[i]))
	fo.write("end\n\n")
	for i in range(len(buttonList)):	
		fo.write("function %s:_onClick%s(event)\n\nend" % (uiName,buttonList[i]))
		
		
		
		
		

			
fo.close()






