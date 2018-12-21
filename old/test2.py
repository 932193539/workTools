#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlwt
import os
class baseLog:
    def __init__(self):
        self.revision = ""
        self.author = ""
        self.time = ""
        self.message = ""
    def setRevision(self, revision):
        self.revision = revision
    def setAuthor(self, author):
        self.author = author
    def setTime(self, time):
        self.time = time
    def setMessage(self, msg):
        self.message = msg
    def getRevision(self):
        return self.revision
    def getAuthor(self):
        return self.author
    def getTime(self):
        return self.time
    def getMessage(self):
        return self.message
    def __str__(self):
        str = ("Revision : %s\nTime : %s\nAuthor : %s\nMessage : %s\n") %(self.revision, self.time, self.author, self.message)
        return str

def readSVNLog():

    rootDir = "svn://172.16.1.201:3692/mahjong/src_quanguo/branches/branch_cangzhou_gameplay_20180820_0823"    ## svn路径

    startDate = "{2018-08-21T14:35:06}"  ## 开始时间
    endDate = "{2018-08-23T14:35:06}"    ## 终止时间
    xlsx = "D:\\Book1.xlsx"  ## 保存的excel路径以及文件名

    command  = "svn log " + "-r" + startDate + ":" + endDate + "  " + rootDir
    print(command)
    rootLogList = os.popen(command)

    res = rootLogList.read()
    rootLogList.close()

    i = 0
    log = baseLog()
    message = ""
    result = []
    for line in res.splitlines():
        if line is None or (len(line) < 1):
            continue
        if '--------' in line:
            continue
        i = i + 1
        if line.count("|") >= 3:
            log.setMessage(message)
            message = ""
            if len(log.getMessage()) > 0:
                result.append(log)
            log = baseLog()
            tmpList = line.split("|")
            log.setRevision(tmpList[0])
            log.setAuthor(tmpList[1])
            log.setTime(tmpList[2])
        else:
            message = message + line
    log.setMessage(message)
    result.append(log)

    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet("log", cell_overwrite_ok=True)
    j = 0
    for i in result:
        tmpStr = str(i)
        sheet.write(j, 0, tmpStr)
        j = j + 1
    book.save(xlsx)

if __name__ == '__main__':
    readSVNLog()