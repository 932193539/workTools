# -*- coding:utf-8 -*-
import os


openFile = r"D:\svn\workspace\trunk_quanguo\Common\platform_jar\proto\club.proto"
gainProto = ["CCLActivityRankREQ","InvitationInfoProto"]


#判断是否进入想获取的协议
def isProto(str):
	for i in range(len(gainProto)):
		if str.find("message " + gainProto[i]) != -1:
			return gainProto[i]
	return False



f = open(openFile)      
line = f.readline()         
protoName = ""


#写入文件
fw = open("test.lua", "w") 

while line: 

	line = line.lstrip()
	if protoName != False and protoName != "":
		#进入了一个想要获取的协议中，我们构造它
		tempData = line.split(" ")
		if tempData[0].find("{") == -1:
			if len(tempData) > 3 :
				fw.write(tempData[2] + "\n")
			else:
				protoName = False
				fw.write("\n\n")
	else:
		protoName = isProto(line)

	line = f.readline() 
 
 
 
f.close() 