# -*- coding:utf-8 -*-
#������UI·��������Ҫ�ڴ�����ʹ�õĿؼ����Ұ��������ɻ����Ŀؼ�����
import xml.dom.minidom,os

#UI·���Ϳؼ�����
uiDir = r'D:\svn\workspace\branch_trunk_function_20180903_0914\Skins\quanguobao_guiyang\cocosstudio\csb\UI_jlbyq.csd'
gainNodeList = ["Image_frame","Image_head","Text_Name","Text_Club_Name","Text_Game_Rules","Button_Refuse","Button_Agree","Button_Close"]#,,"Image_18""changeText","changeText","changeText","changeText","changeText"]

#��¼csb�пؼ�������lua�пؼ����͵Ķ��չ�ϵ(Ҳ������lua�пؼ�������ǰ׺)
CONTRAST_LIST = {'ImageViewObjectData' :  ["ccui.ImageView","_image"],'TextObjectData' :  ["ccui.Text","_text"] ,'ButtonObjectData' : ["ccui.Button","_btn"],'ParticleObjectData' : ["cc.ParticleSystemQuad","_particle"],'PanelObjectData' : ["ccui.Layout","_panel"],'ListViewObjectData' : ["ccui.ListView","_listView"],'TextBMFontObjectData' : ["ccui.TextBMFont","_textBMFont"],'TextFieldObjectData' : ["ccui.TextField","_textFiled"],'CheckBoxObjectData' : ["ccui.CheckBox","_checkBox"],'ScrollViewObjectData' : ["ccui.ScrollView","_scrollView"],'SingleNodeObjectData' : ["cc.Node","_node"],'SpriteObjectData' : ["cc.Sprite","_sprite"]}

# ��xml�ĵ�
dom = xml.dom.minidom.parse(uiDir)
# �õ��ĵ�Ԫ�ض���
Nodes = dom.documentElement.getElementsByTagName('AbstractNodeData')
# �洢lua�жԿؼ�������
luaUiName = []
# ��¼�ؼ���button������
buttonList = []
# ��ȡUI����
uiName = uiDir.replace(os.path.dirname(uiDir) + "\\","").replace(".csd","")

fo = open("gainUI.lua", "w")
fo.write("local csbPath = \"ui/csb/Club/%s.csb\"\nlocal super = require(\"app.game.ui.UIBase\")\nlocal %s = class(\"%s\", super, function() return kod.LoadCSBNode(csbPath) end)\n\n" % (uiName,uiName,uiName))

writeInitText = ""
#��������
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
			writeInitText = writeInitText + "	self.%s = seekNodeByName(self, \"%s\", \"%s\")\n" % (name,gainNodeList[j],CONTRAST_LIST[nodeType][0])

			
#self:ctor()
fo.write("function %s:ctor()\n" % (uiName))		
for i in range(len(luaUiName)):
	fo.write("	self." + luaUiName[i] + " = nil\n")
fo.write("end\n\n")
			
			
#self:init()	
fo.write("function %s:init()\n" % (uiName))
fo.write(writeInitText)		
fo.write("	self:_registerCallBack()\n")
fo.write("end\n\n")


if len(buttonList) > 0:
	#self:_registerCallBack()
	fo.write("function %s:_registerCallBack()\n" % (uiName))
	for i in range(len(buttonList)):		
		fo.write("	bindEventCallBack(self._btn%s, handler(self, self._onClick%s), ccui.TouchEventType.ended)\n" % (buttonList[i],buttonList[i]))
	fo.write("end\n\n")
	#���ð�ť����¼�
	for i in range(len(buttonList)):	
		fo.write("function %s:_onClick%s(event)\n\nend" % (uiName,buttonList[i]))
		
		
		
		
fo.write("\n\n")	
fo.close()






