#!/usr/bin/python
# -*- coding: UTF-8 -*-
# ============================================================================================ 
# 该工具用于每次版本更新前,把项管发来的对比文件与svn中实际修改的文件进行对比,并输出差异文件
# 李晓雨 2018-08-23
# ============================================================================================ 
import os, sys,pysvn,ctypes
from Tkinter import *
COMPARE_FILE_NAME = r"\compareResult.txt"
COMPARE_OK = "compare success"
REMOVE_FILE = [".proto",".udf","mahjong.ccs",".xml"]
CUT_LINE = "=========================================================================================="

#所需用户填写的数据(svn地址,svn开始版本号,svn结束版本号,通过对比文件,本次对比的差异)
#user_data_min = 90014	 #89907
#user_data_max = 90804 
#user_data_url = "svn://172.16.1.201:3692/mahjong/src_quanguo/branches/branch_cangzhou_gameplay_20180827_0831"  
#user_compare_file = r'D:\workTools\compare.txt'
#user_compare_result_dir = r"D:\workTools"

def startCompare(user_data_url,user_data_min,user_data_max,user_compare_file,user_compare_result_dir):

	'''
	if os.path.isfile(r'' + user_compare_file) != True : 
		ctypes.windll.user32.MessageBoxA(0,u"对比结果路径存在问题".encode('gb2312'),u' 信息'.encode('gb2312'),0)
		return False	
	elif os.path.isdir(user_compare_result_dir) != True:
		ctypes.windll.user32.MessageBoxA(0,u"对比文件路径存在问题".encode('gb2312'),u' 信息'.encode('gb2312'),0)
		return False	
	el'''
	if len(str(user_data_min)) != 5 or len(str(user_data_max)) != 5:
		ctypes.windll.user32.MessageBoxA(0,u"版本号位数不对".encode('gb2312'),u' 信息'.encode('gb2312'),0)
		return False	

	revision_min = pysvn.Revision( pysvn.opt_revision_kind.number, user_data_min ) 
	revision_max = pysvn.Revision( pysvn.opt_revision_kind.number, user_data_max ) 
	#revision_max = pysvn.Revision( pysvn.opt_revision_kind.head ) 
	user_compare_result_dir = r'' + user_compare_result_dir + COMPARE_FILE_NAME

	# 初始化svn连接
	def get_login(realm,user,may_save): 
		return True, "lixiaoyu", "l!meHill89", False 
	client = pysvn.Client()
	client.callback_get_login = get_login 
	# 获取svn日志数据
	svnDataListObject = None
	try:
		svnDataListObject = client.diff_summarize(user_data_url, revision_min, user_data_url, revision_max) 
	except:
		ctypes.windll.user32.MessageBoxA(0,u"svn路径存在问题".encode('gb2312'),u' 信息'.encode('gb2312'),0)
		return False

	#先提取出svn中的所有提交文件,并格式化成约定格式
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
		compareList[i] = compareList[i].replace(".png",".webp").replace(".jpg",".webp")
			
	fileHandle.close()  

	#开始比对,记录两者都存在的文件数量	
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
	fw.write("对比文件在svn中均有记录,麻烦大家花5分钟确认下自己的svn提交记录\n")
	fw.write("提交记录有问题的人在群里发下,5分钟后没人发,没什么问题大家就都可以撤退啦\n\n\n\n")

	
	fw.write("svn路径:" + str(user_data_url) + "\n")
	fw.write("(版本号在" + str(user_data_min) + "-" + str(user_data_max) + "间)svn中共修改了" + str(len(svnDataList)) + "个文件,对比文件中共有" + str(len(compareList)) + "个文件,具体信息如下:\n")
	fw.write("(注意:大家一定要确认一下自己的提交记录中是否存在误提交或漏提交的文件,这些特殊情况并不容易被排查出来)\n")
	fw.write("以下是对比文件中存在但svn中却没有记录的文件共 " + str(len(compareList)-sameFileCount) + " 个(重要!!!)\n\n\n")

	for i in range(len(compareList)): 
		if compareList[i].count(COMPARE_OK) == 0:
			fw.write(compareList[i]+"\n")
		
	fw.write("\n\n" + CUT_LINE + "\n\n\n")
	fw.write("以下是svn记录中存在但对比文件中却没有的文件共 "+ str(len(svnDataList)-sameFileCount) + " 个\n")
	fw.write("(仅供参考:可能是个别改动被revert导致svn中仍有记录或仅提交了'空格'等对比文件中不会记录的改动等原因)\n")

	for i in range(len(svnDataList)): 
		if svnDataList[i].count(COMPARE_OK) == 0:
			fw.write(svnDataList[i]+"\n")

	fw.write("\n\n" + CUT_LINE + "\n\n\n")
	fw.write("以下是svn中和对比文件中都存在的文件共 "+ str(sameFileCount) + " 个\n")	

	for i in range(len(svnDataList)): 
		if svnDataList[i].count(COMPARE_OK) == 1:
			fw.write(svnDataList[i].replace(COMPARE_OK,"")+"\n")
		
	ctypes.windll.user32.MessageBoxA(0,u"对比完成".encode('gb2312'),u' 信息'.encode('gb2312'),0)				
	
	fw.close()
	

#tk窗口
class Tools(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.pack()
		self.winfo_toplevel().title("对比小工具")
		self.createWidgets()
		
	def compareButtonClick(self):	
		startCompare(self.svnUrl.get("0.0", "end").strip(),	self.svnStartVersion.get("0.0", "end").strip(),	self.svnEndVersion.get("0.0", "end").strip(),self.svnCompareFile.get("0.0", "end").strip(),	self.svnCompareResultDir.get("0.0", "end").strip())
		
	def createWidgets(self):
		self.svnUrl = Text(self, width = 100, height = 2)
		self.svnUrl.grid(row = 1, column = 1, sticky="w")
		self.svnUrl.insert(1.0,"svn://172.16.1.201:3692/mahjong/src_quanguo/branches/branch_jinzhong_gameplay_20180827_0831")
		Label(self, text = 'svn地址',width = 20, height = 2).grid(row = 1, column = 2, sticky="w")
		
		self.svnStartVersion = Text(self, width = 60, height = 2)
		self.svnStartVersion.grid(row = 2, column = 1, sticky="w")
		self.svnStartVersion.insert(1.0,"90129")
		Label(self, text = 'svn起始版本号',width = 20, height = 2).grid(row = 2, column = 2, sticky="w")
		
		self.svnEndVersion = Text(self, width = 60, height = 2)
		self.svnEndVersion.grid(row = 3, column = 1, sticky="w")
		self.svnEndVersion.insert(1.0,"91060")
		Label(self, text = 'svn结束版本号',width = 20, height = 2).grid(row = 3, column = 2, sticky="w")
		
		self.svnCompareFile = Text(self, width = 60, height = 2)
		self.svnCompareFile.grid(row = 4, column = 1, sticky="w")
		self.svnCompareFile.insert(1.0,"D:\workTools\change.txt")
		Label(self, text = '对比文件路径',width = 20, height = 2).grid(row = 4, column = 2, sticky="w")
		
		self.svnCompareResultDir = Text(self, width = 60, height = 2)
		self.svnCompareResultDir.grid(row = 5, column = 1, sticky="w")
		self.svnCompareResultDir.insert(1.0,"D:\workTools")
		Label(self, text = '对比结果保存路径',width = 20, height = 2).grid(row = 5, column = 2, sticky="w")
		
		Button(self, text = '开始比对',width = 10,command =lambda :self.compareButtonClick()).grid(row = 6, column = 1, sticky="w")

#入口函数
if __name__ == '__main__':
	#tk窗口
	tools = Tools()
	tools.mainloop()
		

	
	
	
	
