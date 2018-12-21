# -*- coding:utf-8 -*-

import xml.dom.minidom

# 打开xml文档
dom = xml.dom.minidom.parse('UIChatPanel.csd')

# 得到文档元素对象
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