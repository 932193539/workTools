# -*- coding:utf-8 -*-
import os


openFile = r"D:\svn\workspace\trunk_quanguo\Common\platform_jar\proto\club.proto"
gainProto = ["CCLActivityRankREQ","InvitationInfoProto"]


#�ж��Ƿ�������ȡ��Э��
def isProto(str):
	for i in range(len(gainProto)):
		if str.find("message " + gainProto[i]) != -1:
			return gainProto[i]
	return False



f = open(openFile)      
line = f.readline()         
protoName = ""


#д���ļ�
fw = open("test.lua", "w") 

while line: 

	line = line.lstrip()
	if protoName != False and protoName != "":
		#������һ����Ҫ��ȡ��Э���У����ǹ�����
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