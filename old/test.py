#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 从svn repos里 获取当天的日志  
  
import pysvn  
import time  
SVNURL = "svn://172.16.1.201:3692/mahjong/src_quanguo/branches/branch_cangzhou_gameplay_20180827_0831"  
#SVNURL = "D:\svn\workspace\branch_cangzhou_gameplay_20180820_0823"  
g_LogList = []  
TodayTime =  time.strftime("%Y-%m-%d", time.localtime())   
Repos_NUM = 0  
  
  
def print_reposinfo(reposInfo):  
    ReposComitTime = time.strftime("%Y-%m-%d", time.localtime(reposInfo.date)) ;  
    #print reposInfo.author  
    #print ReposComitTime  
    #print reposInfo.message.encode("bg2312")  
    #print reposInfo.revision.number  
def getTody_log() :  
    global g_LogList  
    g_LogList = []   
    client = pysvn.Client()  
    def get_login(realm,user,may_save): 
        return True, "lixiaoyu", "l!meHill89", False 
    client.callback_get_login = get_login 
    revision_start=pysvn.Revision( pysvn.opt_revision_kind.head )  
      
    bContinue = True  
    while bContinue :  
          
        LogList = client.log(SVNURL, revision_start, limit=30) ;  
        #print "LogList: %s" % (TodayTime)  
        Number = LogList[len(LogList)-1].revision.number  
          
        revision_start = pysvn.Revision( pysvn.opt_revision_kind.number, Number )  
          
        for LogInfo in LogList: 
            for test in LogInfo:
                print test
            LogTime = time.strftime("%Y-%m-%d", time.localtime(LogInfo.date))  
            #print LogTime  
            if LogTime==TodayTime:  
                #print LogInfo  
                g_LogList.append(LogInfo) ;  
            else:  
                bContinue = False ;  
              
        if len(g_LogList)==0:  
            break ;  
      
      
def WritLog():  
    f = open("./ChangLog.txt", "wb") ;  
       
      
    for Log in g_LogList : 
        f.write( Log.author ) ;
        f.write("\n1\n") 
        f.write( Log.message ) ;  
        f.write("\n2\n") 
        f.write( str(Log.revision) ) ;  
        f.write("\n3\n") 
        f.write( str(Log.has_children) ) ;  
        f.write("\n4\n") 
        f.write( str(Log.revprops) ) ;  
        f.write("\n5\n") 
        f.write( str(Log.changed_paths) ) ; 
        f.write("\n6\n") 
        f.write( str(Log.date) ) ;  
        f.write("\n7\n")  
		
        print Log.changed_paths
			
    if len(g_LogList) == 0:  
        f.write("没有修改日志")  
          
    f.close()  
          
if __name__ == '__main__':  
    getTody_log()  
    WritLog()  