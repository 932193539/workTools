#!/usr/bin/python
# -*- coding: UTF-8 -*-
#生成客户端常用文件快捷打开方式
import os, sys
from Tkinter import *
import multiprocessing

WORKSPACE_PATH = 'D:/svn/workspace'
FIND_PATH = ['Client','src','Skins']
FIND_FILE = ['startgame.bat','lion.py']
REMOVE_FILE = ['webpconv',".svn","baseversion"]
SPECIAL_FILE = ['C:\Users\kod\AppData\Local\mahjong','C:\Users\kod\Desktop','D:\svn\workspace']
FILE = 'FILE'
DIR = 'DIR'

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
	def __init__(self,projectDir,findDir,findFiles):
		Frame.__init__(self)
		self.pack()
		self.createWidgets(projectDir,findDir,findFiles)
		
	def createWidgets(self,projectDir,findDir,findFiles):
		count = 0
				
		for key in findFiles:
			valCount = 0
			for value in findDir[key]:
				Button(self, text = value,width = 10, command=lambda files=r'' + findDir[key][value] : download(files)).grid(row = count, column = valCount)
				valCount = valCount + 1
			for value in findFiles[key]:
				Button(self, text = value,width = 10, command=lambda files=r'' + findFiles[key][value] : download(files)).grid(row = count, column = valCount)
				valCount = valCount + 1
	
			Label(self, text = ' << ' + key).grid(row = count, column = valCount+1, sticky="w")
			count = count + 1
			
		valCount = 0
		for key in SPECIAL_FILE:
			file =  r'' + key
			Button(self, text = file.replace(os.path.dirname(file)+"\\", ""),width = 10, command=lambda files=r'' + key : download(files)).grid(row = count, column = valCount)
			valCount = valCount + 1
			
			

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
		findFiles[DIR][projectDir[count]]['根目录'] = proDir
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

	tools = Tools(projectDir,findFiles[DIR],findFiles[FILE])
	tools.mainloop()
	'''
	
	'''
