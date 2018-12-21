#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys,pysvn,ctypes
from Tkinter import *

class Tools(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.pageId = 1
		self.pack()
		self.winfo_toplevel().title("游戏数据解析工具")
		self.createWidgets()

	def openfile(self,fileID):
		b=1
		index = self.lb.curselection()

		self.content.insert(END,self.lb.get(index) + "\n")
        #self.lb.get(index)
		'''
		self.fileID = 1
		listFile = [ '\Client\src\__ClickButton.lua', '\Client\src\__DispatchEvent.lua' , '\Client\src\__Message.lua', '\Client\src\__OpenUI.lua']
		fo = open(r'' + self.url.get("0.0", "end").strip() + listFile[fileID], "r")
		#self.content.insert(END,fo.name +"\n")
		self.content.delete(0.0, END)
		for line in fo.readlines():                          #依次读取每行  
			line = line.strip()                             #去掉每行头尾空白  
			self.content.insert(END,line +"\n")
			'''

	def createWidgets(self):

		var = StringVar()
		self.lb = Listbox(self,width = 100, selectmode=BROWSE, listvariable = var)
		self.lb.grid(row = 1, column = 1, sticky="w")
		
		list_item = ["s1","s2","s3"]
		for item in list_item:
			self.lb.insert(END,item)
		scrl = Scrollbar(self)
		self.lb.configure(yscrollcommand=scrl.set)   # 指定Listbox的yscrollbar的回调函数为Scrollbar的set，表示滚动条在窗口变化时实时更新
		scrl['command'] = self.lb.yview  # 指定Scrollbar的command的回调函数是Listbar的yview

		self.url = Text(self,width = 100, height = 1)
		self.url.grid(row = 1, column = 1, sticky="w")
		self.url.insert(1.0,r"D:\svn\workspace\branch_master_gameplay_jinzhong")

		self.content = Text(self,width = 100, height = 50)
		self.content.grid(row = 2, column = 1, sticky="w")

		self.frm = Frame(self,width = 100, height = 1)
		self.frm.grid(row = 3, column = 1, sticky="w")

		self.clickButton = Button(self.frm,width = 24, text="ClickButton", command=lambda fileID=0 : self.openfile(fileID)).grid(row = 3, column = 1)
		self.dispatchEvent = Button(self.frm, width = 24,text="DispatchEvent", command=lambda fileID=1 : self.openfile(fileID)).grid(row = 3, column = 3)
		self.message = Button(self.frm,width = 24, text="Message", command=lambda fileID=2 : self.openfile(fileID)).grid(row = 3, column = 4)
		self.openUI = Button(self.frm, width = 24,text="OpenUI", command=lambda fileID=3 : self.openfile(fileID)).grid(row = 3, column = 5)

if __name__ == '__main__':
	tools = Tools()
	tools.mainloop()
		






