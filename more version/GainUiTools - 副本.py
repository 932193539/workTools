# -*- coding:utf-8 -*-

import xml.dom.minidom

#记录csb中控件类型与lua中控件类型的对照关系(也包含在lua中控件命名的前缀)
contrastList = {'ImageViewObjectData' :  ["ccui.ImageView","_image"],'TextObjectData' :  ["ccui.Text","_text"] ,'ButtonObjectData' : ["ccui.Button","_btn"],'ParticleObjectData' : ["cc.ParticleSystemQuad","_particle"],'PanelObjectData' : ["ccui.Layout","_panel"],'ListViewObjectData' : ["ccui.ListView","_listView"],'TextBMFontObjectData' : ["ccui.TextBMFont","_textBMFont"],'TextFieldObjectData' : ["ccui.TextField","_textFiled"],'CheckBoxObjectData' : ["ccui.CheckBox","_checkBox"],'ScrollViewObjectData' : ["ccui.ScrollView","_scrollView"],'SingleNodeObjectData' : ["cc.Node","_node"],'SpriteObjectData' : ["cc.Sprite","_sprite"]}

gainNodeList = ["BitmapFontLabel_fs_Chat","Button_fs_Chat"]

# 打开xml文档
dom = xml.dom.minidom.parse('C:/workTools/UIChatPanel.csd')

# 得到文档元素对象
root = dom.documentElement


Nodes = root.getElementsByTagName('AbstractNodeData')

fo = open("ui.txt", "w")

#记录button的
buttonList = []

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
			
			fo.write( "self." + name + " = seekNodeByName(self, \""+ gainNodeList[j] + "\", \"" + contrastList[nodeType][0] + "\")\n")

			
			
fo.write("\n===================================\n\n")
	
for i in range(len(buttonList)):		
	fo.write("bindEventCallBack(self._btn" + buttonList[i] + ", handler(self, self._onClick" + buttonList[i] + "), ccui.TouchEventType.ended)\n")

fo.write("\n===================================\n\n")
			
			
for i in range(len(buttonList)):	
	fo.write("function UIClubRoom_onClick" + buttonList[i] + "(event)\n\nend")

	
			
fo.close()

#BitmapFontLabel_fs_Chat












