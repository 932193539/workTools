#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys,pysvn,ctypes
from Tkinter import *



		
def printhello(files):
	print("1")
	#self.content.insert(END,url.get("0.0", "end").strip() + files +"\n")

class Tools(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.pack()
		self.winfo_toplevel().title("对比小工具")
		self.createWidgets()

	def createWidgets(self):
		listFile = [ '\Client\src\__ClickButton.lua', '\Client\src\__DispatchEvent.lua' , '\Client\src\__Message.lua', '\Client\src\__OpenUI.lua']
		self.url = Text(self,width = 100, height = 1)
		self.url.grid(row = 1, column = 1, sticky="w")
		self.url.insert(1.0,"svn://172.16.1.201:3692/mahjong/src_quanguo/branches/branch_jinzhong_gameplay_20180827_0831")

		self.content = Text(self,width = 100, height = 50)
		self.content.grid(row = 2, column = 1, sticky="w")

		self.frm = Frame(self,width = 100, height = 1)
		self.frm.grid(row = 3, column = 1, sticky="w")

		self.clickButton = Button(self.frm,width = 24, text="ClickButton", command=lambda files=listFile[0] : printhello(files)).grid(row = 3, column = 1)
		self.dispatchEvent = Button(self.frm, width = 24,text="DispatchEvent", command=lambda files=listFile[1] : printhello(files)).grid(row = 3, column = 3)
		self.message = Button(self.frm,width = 24, text="Message", command=lambda files=listFile[2] : printhello(files)).grid(row = 3, column = 4)
		self.openUI = Button(self.frm, width = 24,text="OpenUI", command=lambda files=listFile[3] : printhello(files)).grid(row = 3, column = 5)

if __name__ == '__main__':
	tools = Tools()
	tools.mainloop()
		






