# -*- coding:utf-8 -*-

import xml.dom.minidom

# ��xml�ĵ�
dom = xml.dom.minidom.parse('UIChatPanel.csd')

# �õ��ĵ�Ԫ�ض���
root = dom.documentElement
print root.nodeName
print root.nodeValue
print root.nodeType
print root.ELEMENT_NODE

print "###########"


Nodes = root.getElementsByTagName('AbstractNodeData')

for index in range(len(Nodes)):
	print Nodes[index].getAttribute('Name')






#BitmapFontLabel_fs_Chat