# -*- coding:utf-8 -*-
import os


openFile = r"D:\svn\workspace\trunk_quanguo\Common\platform_jar\proto\club.proto"
gainProto = ["CCLAddManagerActivityREQ","CLCAddManagerActivityRES"]


#判断是否进入想获取的协议
def isProto(str):
	for i in range(len(gainProto)):
		if str.find("message " + gainProto[i]) != -1:
			return gainProto[i]
	return False



f = open(openFile)      
line = f.readline()         
protoName = ""
isSetData = False

#写入文件
fw = open("test.lua", "w") 

while line: 

	line = line.lstrip()
	
	if line.find("{") != -1:
		line = f.readline() 
		continue
	
	if protoName != False and protoName != "":
		#进入了一个想要获取的协议中，我们构造它
		
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
			protoName = False
	else:
		protoName = isProto(line)

	line = f.readline() 
 
 
 
f.close() 