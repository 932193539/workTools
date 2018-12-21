# -*- coding:utf-8 -*-
import os


openFile = r"D:\svn\workspace\trunk_quanguo\Common\platform_jar\proto\club.proto"
gainProto = ["CCLAddManagerActivityREQ","CLCAddManagerActivityRES"]
protoInfo = []
for i in range(len(gainProto)):
	protoInfo.append([])

#判断是否进入想获取的协议
def isProto(str):
	for i in range(len(gainProto)):
		if str.find("message " + gainProto[i]) != -1:
			return i
	return -1



f = open(openFile)      
line = f.readline()         
protoNameId = -1

#写入文件
fw = open("test.lua", "w") 

while line: 
	line = line.lstrip()
	if line.find("{") != -1:
		line = f.readline() 
		continue
	
	if protoNameId >= 0:
		protoName = gainProto[protoNameId]
		#进入了一个想要获取的协议中，我们构造它
		tempData = line.split(" ")
		if len(tempData) > 3 :
			if protoName.find("REQ") != -1:
				protoInfo[protoNameId].append(tempData[2]) 
		else:
			protoNameId = -1
	else:
		protoNameId = isProto(line)

	line = f.readline() 
 

 
for i in range(len(gainProto)):
	protoName = gainProto[i]
	fw.write("local %s = class(\"%s\", ProtocolBase)\n" % (protoName,protoName))
	fw.write("ns.%s = %s)\n\n" % (protoName,protoName))
	fw.write("%s.OP_CODE = net.ProtocolCode.!!!!!)\n" % (protoName))
	fw.write("%s.CLZ_CODE = \"com.kodgames.message.proto.club.%s\")\n\n" % (protoName,protoName))
	fw.write("function %s:ctor(serverId, callback)\n" % (protoName))
	fw.write("	self.super.ctor(self, %s.OP_CODE, serverId, callback)\n" % (protoName))
	fw.write("end)\n\n")

	#setData
	if protoName.find("REQ") != -1:
		fw.write("function %s:setData(" % (protoName))

	for j in range(len(protoInfo[i])):	
		if j+1 == len(protoInfo[i]):
			fw.write("%s)\n" % (protoInfo[i][j]))
		else:
			fw.write("%s, " % (protoInfo[i][j]))
	
	for j in range(len(protoInfo[i])):
		fw.write("	self:getProtocolBuf().%s = %s\n" % (protoInfo[i][j],protoInfo[i][j]))
		
	if protoName.find("REQ") != -1:
		fw.write("end")
		
	fw.write("\n\n")			
			

 
 
 
f.close() 