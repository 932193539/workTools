# -*- coding:utf-8 -*-
#������UI·��������Ҫ�ڴ�����ʹ�õĿؼ����Ұ��������ɻ����Ŀؼ�����

import xml.dom.minidom
import os

#UI·���Ϳؼ�����
uiDir = r'D:\svn\workspace\branch_quanguo_0709_83447\Skins\quanguobao_guiyang\cocosstudio\csb\Club\UIClubRoom.csd'
gainNodeList = ["Text_wf","Button_szwf","Image_18"]#,"changeText","changeText","changeText","changeText","changeText"]


#��¼csb�пؼ�������lua�пؼ����͵Ķ��չ�ϵ(Ҳ������lua�пؼ�������ǰ׺)
contrastList = {'ImageViewObjectData' :  ["ccui.ImageView","_image"],'TextObjectData' :  ["ccui.Text","_text"] ,'ButtonObjectData' : ["ccui.Button","_btn"],'ParticleObjectData' : ["cc.ParticleSystemQuad","_particle"],'PanelObjectData' : ["ccui.Layout","_panel"],'ListViewObjectData' : ["ccui.ListView","_listView"],'TextBMFontObjectData' : ["ccui.TextBMFont","_textBMFont"],'TextFieldObjectData' : ["ccui.TextField","_textFiled"],'CheckBoxObjectData' : ["ccui.CheckBox","_checkBox"],'ScrollViewObjectData' : ["ccui.ScrollView","_scrollView"],'SingleNodeObjectData' : ["cc.Node","_node"],'SpriteObjectData' : ["cc.Sprite","_sprite"]}


# ��xml�ĵ�
dom = xml.dom.minidom.parse(uiDir)

# �õ��ĵ�Ԫ�ض���
root = dom.documentElement


Nodes = root.getElementsByTagName('AbstractNodeData')

fo = open("gainUI.lua", "w")

#��¼button��
buttonList = []


tempName = uiDir.replace(os.path.dirname(uiDir) + "\\","")
uiName = tempName.replace(".csd","")

fo.write("local csbPath = \"ui/csb/Club/%s.csb\"\nlocal super = require(\"app.game.ui.UIBase\")\nlocal %s = class(\"%s\", super, function() return kod.LoadCSBNode(csbPath) end)\n\n" % (uiName,uiName,uiName))


fo.write("function %s:init()\n" % (uiName))

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
				
			name = contrastList[nodeType][1] + name
			
			fo.write( "	self." + name + " = seekNodeByName(self, \""+ gainNodeList[j] + "\", \"" + contrastList[nodeType][0] + "\")\n")

	
fo.write("end\n\n")


if len(buttonList) > 0:


	fo.write("function " + uiName +":_registerCallBack()\n")

	for i in range(len(buttonList)):		
		fo.write("	bindEventCallBack(self._btn" + buttonList[i] + ", handler(self, self._onClick" + buttonList[i] + "), ccui.TouchEventType.ended)\n")

	fo.write("end\n\n")

	for i in range(len(buttonList)):	
		
		fo.write("function " + uiName + ":_onClick" + buttonList[i] + "(event)\n\nend")


	

			
fo.close()


file =  r'' + 'C:\workTools'
			
	
#BitmapFontLabel_fs_Chat












