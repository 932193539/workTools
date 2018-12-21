# -*- coding:utf-8 -*-
import os


openFile = r"D:\svn\workspace\trunk_quanguo\Common\platform_jar\proto\club.proto"
gainProto = ["CCLAddManagerActivityREQ","CLCAddManagerActivityRES"]


#�ж��Ƿ�������ȡ��Э��
def isProto(str):
	for i in range(len(gainProto)):
		if str.find("message " + gainProto[i]) != -1:
			return i
	return -1



f = open(openFile)      
line = f.readline()         
protoNameId = -1
isSetData = False

#д���ļ�
fw = open("test.lua", "w") 

while line: 

	line = line.lstrip()
	
	if line.find("{") != -1:
		line = f.readline() 
		continue
	
	if protoNameId >= 0:
		protoName = gainProto[protoNameId]
		#������һ����Ҫ��ȡ��Э���У����ǹ�����
		if isSetData == False:
			fw.write("local %s = class(\"%s\", ProtocolBase)\n" % (protoName,protoName))
			fw.write("ns.%s = %s)\n\n" % (protoName,protoName))
			fw.write("%s.OP_CODE = net.ProtocolCode.!!!!!)\n" % (protoName))
			fw.write("%s.CLZ_CODE = \"com.kodgames.message.proto.club.%s\")\n\n" % (protoName,protoName))
			fw.write("function %s:ctor(serverId, callback))\n" % (protoName))
			fw.write("	self.super.ctor(self, %s.OP_CODE, serverId, callback))\n" % (protoName))
			fw.write("end)\n\n")
			if protoName.find("REQ") != -1:
				fw.write("function %s:setData(clubId, optype, activityId)\n" % (protoName))
		
		tempData = line.split(" ")
		if len(tempData) > 3 :
			isSetData = True
			if protoName.find("REQ") != -1:
				fw.write("	self:getProtocolBuf().%s = %s\n" % (tempData[2],tempData[2]))
		else:
			if protoName.find("REQ") != -1:
				fw.write("end")
			fw.write("\n\n")
			isSetData = False
			protoNameId = -1
	else:
		protoNameId = isProto(line)

	line = f.readline() 
 
 
 
f.close() 