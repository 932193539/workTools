# -*- coding:utf-8 -*-
import os
#proto文件
openFile = r"D:\svn\workspace\branch_jinzhong\Common\platform_jar\proto\club.proto"
#需要获取的proto协议
gainProto = ["CCLModifyConfirmedGameplaysOrderREQ","CLCModifyConfirmedGameplaysOrderRES"]
#使用该协议的service
serviceName = "ClubManagerService"



#写入文件
fw = open("protoInfo.lua", "w") 

protoInfo = []
for i in range(len(gainProto)):
	protoInfo.append([])

openFileName = openFile.replace(os.path.dirname(openFile),"").replace("\\","").replace(".proto","")	
	
#判断是否进入想获取的协议
def isProto(str):
	for i in range(len(gainProto)):
		if str.find("message " + gainProto[i]) != -1:
			return i
	return -1


#获取协议字段合并后的字符串
def combineProtoInfo(pInfo):
	str = ""
	for i in range(len(pInfo)):
		if i + 1 == len(pInfo):
			str = str + pInfo[i]
		else:
			str = str + pInfo[i] + ", "
			
	return str

f = open(openFile)      
line = f.readline()         
protoNameId = -1


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
	fw.write("--\n")
	fw.write("local %s = class(\"%s\", ProtocolBase)\n" % (protoName,protoName))
	fw.write("ns.%s = %s\n\n" % (protoName,protoName))
	fw.write("%s.OP_CODE = net.ProtocolCode.?????\n" % (protoName))
	fw.write("%s.CLZ_CODE = \"com.kodgames.message.proto.%s.%s\"\n\n" % (protoName,openFileName,protoName))
	fw.write("function %s:ctor(serverId, callback)\n" % (protoName))
	fw.write("	self.super.ctor(self, %s.OP_CODE, serverId, callback)\n" % (protoName))
	fw.write("end\n\n")

	#setData
	if protoName.find("REQ") != -1:
		fw.write("function %s:setData(" % (protoName))
		fw.write(combineProtoInfo(protoInfo[i]) + ")\n")
			
	for j in range(len(protoInfo[i])):
		fw.write("	self:getProtocolBuf().%s = %s\n" % (protoInfo[i][j],protoInfo[i][j]))
		
	if protoName.find("REQ") != -1:
		fw.write("end\n\n")
				
	
fw.write("===================================\n\n")	
	
for i in range(len(gainProto)):
	protoName = gainProto[i]
	
	if protoName.find("REQ") != -1:
		fw.write("--\n")
		fw.write("function %s:send%s(%s)\n" % (serviceName,protoName,combineProtoInfo(protoInfo[i])))
		fw.write("	local request = net.NetworkRequest.new(net.protocol.%s, self.?????:getClubServiceId())\n" % (protoName))
		fw.write("	request:getProtocol():setData(%s)\n" % (combineProtoInfo(protoInfo[i])))
		fw.write("	game.util.RequestHelper.request(request)\n")
		fw.write("end\n\n")
		fw.write("===================================\n\n")	
	else:
		fw.write("--\n")
		fw.write("function %s:_on%s(response)\n" % (serviceName,protoName))
		fw.write("	local protocol = response:getProtocol():getProtocolBuf()\n\n\n")
		fw.write("end\n\n")
		fw.write("===================================\n\n")	
		fw.write("requestManager:registerResponseHandler(net.protocol.%s.OP_CODE, self, self._on%s)\n\n" % (protoName,protoName))
		fw.write("===================================\n\n")	
 
 
f.close() 