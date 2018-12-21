#!/usr/bin/python
# -*- coding: UTF-8 -*-
#生成客户端常用文件快捷打开方式
import os, sys
from Tkinter import *
import multiprocessing
import time,pysvn,ctypes

WORKSPACE_PATH = 'D:/svn/workspace'
#想要查找的路径
FIND_PATH = ['Client','src','Skins']
#想查找的文件
FIND_FILE = ['startgame.bat','lion.py']
#不想查找的路径
REMOVE_FILE = ['webpconv',".svn","baseversion"]
#特别需要的路径
SPECIAL_FILE = ['D:\workTools\DelLocal.bat','D:\svn\workspace','C:\workTools\GainUiTools.py','C:\workTools\gainUI.lua','C:\workTools\protoTools.py','C:\workTools\protoInfo.lua']
#置顶的文件
PROJECT_TOP = ['trunk_quanguo','trunk_chaoshan_0608']
FILE = 'FILE'
DIR = 'DIR'

# 初始化client
client = pysvn.Client()
client.set_default_username("lixiaoyu")
client.set_default_password("l!meHill89")

#更新项目

def updateSvn(localPath):
	revision = None
	try:
		revision = client.update(localPath)
	except:
		ctypes.windll.user32.MessageBoxA(0,u"更新失败".encode('gb2312'),u' 信息'.encode('gb2312'),0)
	#if not os.path.exists(os.path.join(localPath, ".svn")):
	#	ctypes.windll.user32.MessageBoxA(0,u"更新失败".encode('gb2312'),u' 信息'.encode('gb2312'),0)

	if revision:
		print "update success"

#搜索要查找的文件，确认当前文件是否是要检索的文件
def searchFindFile(filename,searchFiles):
	for seaFiles in searchFiles:
		if seaFiles == filename:
			file = root + '\\' + seaFiles
			if bRemoveFile(file) == None:
				return file
			else:
				break
			break;
	return None
	
#判断当前文件是不是不需要检索的文件
def bRemoveFile(file):
	bRemoveFile = None
	for RM in REMOVE_FILE: 
		if file.find(RM) != -1:
			bRemoveFile = 1
	return bRemoveFile

#打开程序
def openFile(file):
	filepath = os.path.dirname(file)
	#需要先进入所在文件夹再打开，否则可能存在路径错误问题
	os.chdir(r'' + filepath)
	os.system(os.path.sep.join(file.split(r'/')))

#打开文件夹或文件(py脚本,bat脚本都有)
def download(file):
	if os.path.isfile(file):
		p = multiprocessing.Process(target=openFile, args = (file,))
		p.start()
	elif os.path.isdir(file):
		os.startfile(file)
	else:
		print "路径错误"
		
class Tools(Frame):
	def __init__(self,findDir,findFiles):
		Frame.__init__(self)
		self.pack()
		self.createWidgets(findDir,findFiles)
		
	def createWidgets(self,findDir,findFiles):
		rowCount = len(PROJECT_TOP)
			
		for key in findFiles:
			colCount = 0
			tempCount = rowCount
			if PROJECT_TOP.count(key) > 0:
				#设置置顶的项目
				tempCount = PROJECT_TOP.index(key)
			
			for value in findDir[key]:
				if value.find("update") == -1:
					Button(self, text = value,width = 10, command=lambda files=r'' + findDir[key][value] : download(files)).grid(row = tempCount, column = colCount)
				else:
					Button(self, text = value,width = 10, command=lambda files=r'' + findDir[key][value] : updateSvn(files)).grid(row = tempCount, column = colCount)
				colCount = colCount + 1
			for value in findFiles[key]:
				Button(self, text = value,width = 10, command=lambda files=r'' + findFiles[key][value] : download(files)).grid(row = tempCount, column = colCount)
				colCount = colCount + 1
	
			Label(self, text = ' << ' + key).grid(row = tempCount, column = colCount+1, sticky="w")
			if tempCount == rowCount:
				#如果没有设置置顶项目,这可以把行数+1,设置下一行的数据
				rowCount = rowCount + 1
			
		colCount = 0
		for key in SPECIAL_FILE:
			file =  r'' + key
			file = file.replace(r'' + os.path.dirname(file), "")
			Button(self, text = file.replace("\\",""),width = 10, command=lambda files=r'' + key : download(files)).grid(row = rowCount, column = colCount)
			colCount = colCount + 1
		
		#清空tk
		#self.pack_forget()

if __name__ == '__main__':

	file =  r'' + SPECIAL_FILE[1]
	file.replace(os.path.dirname(file)+"\\", "")
	
	projectDir = []
	projectAbsoDir = []
	#需要生产快捷打开方式的文件和文件夹要分开存储
	findFiles = {FILE : {} , DIR : {}}
	count = 0
	
	#检索保存所有项目文件夹
	for d in os.listdir(WORKSPACE_PATH):
		if os.path.isdir(WORKSPACE_PATH + "\\" + d):
			projectDir.append(d)
			projectAbsoDir.append(WORKSPACE_PATH + "\\" + d)

	for proDir in projectAbsoDir:
		findFiles[FILE][projectDir[count]] = {}
		findFiles[DIR][projectDir[count]] = {}
		findFiles[DIR][projectDir[count]]['目录update'] = proDir
		for root, dirs, files in os.walk(proDir):
			for filename in files:   
				file = searchFindFile(filename,FIND_FILE)
				if file != None:
					findFiles[FILE][projectDir[count]][filename] = file.replace("/", '\\')
			for dirname in dirs:
				file = searchFindFile(dirname,FIND_PATH)
				if file != None:
					findFiles[DIR][projectDir[count]][dirname] = file.replace("/", '\\')
		count = count + 1
		
	tools = Tools(findFiles[DIR],findFiles[FILE])
	tools.mainloop()
		
		


	
	
	
