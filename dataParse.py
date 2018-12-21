#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys,pysvn,ctypes
from Tkinter import *
WORKSPACE_PATH = 'D:/svn/workspace'
LIST_FILE = ['\Client\src\__Message.lua', '\Client\src\__ClickButton.lua' ,'\Client\src\__OpenUI.lua', '\Client\src\__DispatchEvent.lua']

class Tools(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.url = ""
		self.pack()
		self.winfo_toplevel().title("游戏数据解析工具")
		self.createWidgets()

	def openfile(self,fileID):
		index = self.lb.curselection()
		url = ""
		if len(index) == 0:
			url = self.url
		else:
			url = self.lb.get(index) 
			self.url = url

		fo = open(r'' + url + LIST_FILE[fileID], "r")
		self.content.delete(0.0, END)
		for line in fo.readlines():                          #依次读取每行  
			line = line.strip()                             #去掉每行头尾空白  
			self.content.insert(END,line +"\n")
		self.content.see(END)

	def createWidgets(self):

		self.lb = Listbox(self,width = 100,height = 8)
		self.lb.grid(row = 1, column = 1, sticky="w")
		
		for d in os.listdir(WORKSPACE_PATH):
			if os.path.isdir(WORKSPACE_PATH + "\\" + d):
				self.lb.insert(END,WORKSPACE_PATH + "\\" + d)

		scrl = Scrollbar(self)
		self.lb.configure(yscrollcommand=scrl.set)   # 指定Listbox的yscrollbar的回调函数为Scrollbar的set，表示滚动条在窗口变化时实时更新
		scrl['command'] = self.lb.yview  # 指定Scrollbar的command的回调函数是Listbar的yview


		self.content = Text(self,width = 100, height = 50)
		self.content.grid(row = 2, column = 1, sticky="w")

		self.frm = Frame(self,width = 100, height = 1)
		self.frm.grid(row = 3, column = 1, sticky="w")

		self.clickButton = Button(self.frm,width = 24, text="Message", command=lambda fileID=0 : self.openfile(fileID)).grid(row = 3, column = 1)
		self.dispatchEvent = Button(self.frm, width = 24,text="ClickButton", command=lambda fileID=1 : self.openfile(fileID)).grid(row = 3, column = 3)
		self.message = Button(self.frm,width = 24, text="OpenUI", command=lambda fileID=2 : self.openfile(fileID)).grid(row = 3, column = 4)
		self.openUI = Button(self.frm, width = 24,text="DispatchEvent", command=lambda fileID=3 : self.openfile(fileID)).grid(row = 3, column = 5)

if __name__ == '__main__':
	tools = Tools()
	tools.mainloop()
		






