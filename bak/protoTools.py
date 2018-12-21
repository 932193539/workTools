# -*- coding:utf-8 -*-
import os
#proto�ļ�
openFile = r"D:\svn\workspace\branch_trunk_dev_201808130817_functions\Common\platform_jar\proto\replay.proto"
#��Ҫ��ȡ��protoЭ��
gainProto = ["CRPersonalClubHistoryREQ","RCPersonalClubHistoryRES"]
#ʹ�ø�Э���service
serviceName = "ClubHistoryService"



#д���ļ�
fw = open("protoInfo.lua", "w") 

protoInfo = []
for i in range(len(gainProto)):
	protoInfo.append([])

openFileName = openFile.replace(os.path.dirname(openFile),"").replace("\\","").replace(".proto","")	
	
#�ж��Ƿ�������ȡ��Э��
def isProto(str):
	for i in range(len(gainProto)):
		if str.find("message " + gainProto[i]) != -1:
			return i
	return -1


#��ȡЭ���ֶκϲ�����ַ���
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
		#������һ����Ҫ��ȡ��Э���У����ǹ�����
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