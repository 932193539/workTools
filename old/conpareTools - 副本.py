#!/usr/bin/python
# -*- coding: UTF-8 -*-
# ============================================================================================ 
# 该工具用于每次版本更新前,把项管发来的对比文件与svn中实际修改的文件进行对比,并输出差异文件
# 李晓雨 2018-08-23
# ============================================================================================ 
import os, sys,pysvn
from Tkinter import *


#所需用户填写的数据(svn地址,svn开始版本号,svn结束版本号,通过对比文件,本次对比的差异)
user_data_min = 89132	 #89907
user_data_max = 90008 
user_data_url = "svn://172.16.1.201:3692/mahjong/src_quanguo/branches/branch_jinzhong_gameplay_20180820_0823"  
user_compare_file = r'D:\workTools\compare.txt'
user_compare_result_dir = r"D:\workTools\compareResult.txt"


COMPARE_OK = "compare success"
REMOVE_FILE = [".proto",".udf","mahjong.ccs",".xml"]
CUT_LINE = "=========================================================================================="

revision_min = pysvn.Revision( pysvn.opt_revision_kind.number, user_data_min ) 
revision_max = pysvn.Revision( pysvn.opt_revision_kind.number, user_data_max ) 
#revision_max = pysvn.Revision( pysvn.opt_revision_kind.head ) 


class Tools(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.pack()
		self.createWidgets(findDir,findFiles)

	def createWidgets(self,findDir,findFiles):
		Label(self, text = 'test').grid(row = 1, column = 1, sticky="w")
		

#打开项管给的对比文件,并逐行格式化成约定格式
fileHandle = open ( user_compare_file ) 
compareList = fileHandle.readlines()  

for i in range(len(compareList)):
	compareList[i] = compareList[i].encode('ascii')
	compareList[i] = compareList[i].replace("'","")
	if compareList[i][0:1] == '/':
		compareList[i] = compareList[i][1:len(compareList[i])]
	if compareList[i][0:7] == 'res/ui/':
		compareList[i] = compareList[i][7:len(compareList[i])]
	compareList[i] = compareList[i].replace("\n","")
	if compareList[i].count("/pb/") == 1:
		compareList[i] = compareList[i].split("/pb/")[1]
		
fileHandle.close()  
	
	
# 初始化svn连接
def get_login(realm,user,may_save): 
    return True, "lixiaoyu", "l!meHill89", False 
client = pysvn.Client()
client.callback_get_login = get_login 
# 获取svn日志数据
svnDataListObject = client.diff_summarize(user_data_url, revision_min, user_data_url, revision_max) 


#先提取出svn中的所有提交文件,并个格式化成约定格式
svnDataList = []
for data in svnDataListObject: 
	
	isRemoveData = False
	tempData = data['path'].encode('ascii')
	for removeData in REMOVE_FILE: 
		if tempData.count(removeData) > 0:
			isRemoveData = True
		
	if data['node_kind'] != pysvn.node_kind.dir and isRemoveData == False:		
			if tempData[0:1] == '/':
				tempData = tempData[1:len(tempData)]
			if tempData[0:7] == 'Client/':
				tempData = tempData[7:len(tempData)]
			if tempData.count("/cocosstudio/") == 1:
				tempData = tempData.split("/cocosstudio/")[1]
			if tempData.count("/sound/") == 1:
				tempData = "res/sound/" + tempData.split("/sound/")[1]
			if tempData.count("/pb/") == 1:
				tempData = tempData.split("/pb/")[1]
			svnDataList.append(tempData.replace(".csd",".csb").replace(".png",".webp").replace(".jpg",".webp"))
			

#开始比对		
sameFileCount = 0

for i in range(len(svnDataList)):
	for j in range(len(compareList)): 
		if svnDataList[i] == compareList[j]:
			svnDataList[i] = svnDataList[i] + COMPARE_OK
			compareList[j] = compareList[j] + COMPARE_OK
			sameFileCount = sameFileCount + 1
			break	
			

#写入文件
fw = open(user_compare_result_dir, "w") 
fw.write("(版本号在" + str(user_data_min) + "-" + str(user_data_max) + "间)svn中共修改了" + str(len(svnDataList)) + "个文件,对比文件中共有" + str(len(compareList)) + "个文件,两者对比差异如下:\n\n\n")
fw.write("对比文件中存在但svn中却没有的文件共 " + str(len(compareList)-sameFileCount) + " 个(重要!!!)\n")

for i in range(len(compareList)): 
	if compareList[i].count(COMPARE_OK) == 0:
		fw.write(compareList[i]+"\n")
	
fw.write("\n\n" + CUT_LINE + "\n\n\n")
fw.write("svn记录中存在但对比文件中却没有的文件共 "+ str(len(svnDataList)-sameFileCount) + " 个\n")
fw.write("(仅供参考:可能是个别改动被revert导致svn中仍有记录或仅提交了'空格'等对比文件中不会记录的改动等原因)\n")

for i in range(len(svnDataList)): 
	if svnDataList[i].count(COMPARE_OK) == 0:
		fw.write(svnDataList[i]+"\n")


fw.write("\n\n" + CUT_LINE + "\n\n\n")
fw.write("svn中和对比文件中都存在的文件共 "+ str(sameFileCount) + " 个\n")	
		
for i in range(len(svnDataList)): 
	if svnDataList[i].count(COMPARE_OK) == 1:
		fw.write(svnDataList[i].replace(COMPARE_OK,"")+"\n")

if __name__ == '__main__':


	tools = Tools()
	tools.mainloop()
		
		
		
fw.close()


	
	
	
	
