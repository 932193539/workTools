#-*- coding: utf-8 -*- 
#!/usr/bin/env python 
# ==================================================================== 
# 
# svnchanged_export.py 
# 
# Export Files in a revision Range 
# Usage: python SCRIPT_NAME.py -r beginRev:endRev [ --username user --password passwd ] svnurl site_version(a | s | p) 
# site_version: a [admin] s [static] p [platform] 
# 
# ==================================================================== 

import pysvn # http://pysvn.tigris.org/ 
import getopt, time, string, sys, shutil 
import os, urllib, tarfile, getpass 
import unicodedata 
from urllib.parse import urlparse 
from ftplib import FTP 

# Options by default 
date_folder=time.strftime(r"%Y%m%d%H%M%S", time.localtime()) 
#site_version="p" 
#targetPath = "."  # Current directory 
export_dir="D:\workTools" # Change into a folder you want to export, The store path relative to the script 
username = "lixiaoyu" 
password = "l!meHill89"
url = "svn://172.16.1.201:3692/mahjong/src_quanguo/branches/branch_cangzhou_gameplay_20180827_0831"  
ftp_host="xxx.xxx.xxx.xxx" 
ftp_port=xxx 
ftp_user='xxxx' 
ftp_pass='xxxx' 
revision_min = pysvn.Revision( pysvn.opt_revision_kind.number, 0 ) 
revision_max = pysvn.Revision( pysvn.opt_revision_kind.head ) 
hasRevision = False 
current_dir = os.getcwd() 
os.chdir(r'%s/%s' %(os.getcwd(),export_dir)) 
os.makedirs(r'%s' %(date_folder)) 
os.chdir('../') 
targetPath=(r"%s%s") % (export_dir,date_folder) 
try: 
    optlist, args = getopt.getopt (sys.argv[1:], "r:u:p:", 
                                   ["revision=", "username=", "password="]) 
    if len(args) == 1 or len(args) == 2: 
        url = args[0] 
        if len(args) == 2: 
            #targetPath = args[1] 
            site_version = args[1] 
    else: 
        raise Exception ("Input URL [site_version]") 
         
    for option, value in optlist: 
        if option == "--username" or option == "-u": 
            username = value             
        elif option == "--password" or option == "-p": 
            password = value 
        elif option == "--revision" or option == "-r": 
            revision = value 
            if str.find(value, ":") >= 0: 
                (revision_min0, revision_max0) = str.split(value, ":") 
                revision_min = pysvn.Revision( pysvn.opt_revision_kind.number, int(revision_min0) ) 
                if revision_max0 != "HEAD": 
                    revision_max = pysvn.Revision( pysvn.opt_revision_kind.number, int(revision_max0) ) 
                hasRevision = True 
            else: 
                raise Exception ("Please Input revision range " + str(option)) 
        else: 
            raise Exception ("Unknown option " + str(option)) 
             
    if hasRevision == False: 
        raise Exception ("Please Input Revision Range -r min:max") 
         
    #urlObject = urlparse(url) 
    #if urlObject.scheme == 'http' or urlObject.scheme == 'https': 
    #    url = urlObject.scheme+"://"+urlObject.netloc+urllib.quote(urlObject.path.decode(sys.stdin.encoding).encode('utf8')) 
    #else: 
        #url = unicode(url, sys.stdin.encoding) 
    #print (sys.stdin.encoding) 
    # print(url) 
    if not url.endswith("/"): 
        url = url + "/"         
         
except getopt.error as reason: 
 raise Exception("Usage: " + sys.argv[0] + ": " + str(reason)) 
f_list=[] 
f_list=os.listdir(targetPath) 
  
for f in f_list: 
    f_path=os.path.join(targetPath, f) 
    if os.path.isfile(f_path): 
        os.remove(f_path) 
        print (f_path+" removed.") 
    else: 
        shutil.rmtree(f_path) 
        print (f_path+ " removed.") 
print (targetPath+" is already empty.") 
     
def get_login(realm,user,may_save): 
    return True, username, password, False 
    
print ("SVN Path:"+url+'   '+"Diff file path:"+targetPath) 
client = pysvn.Client() 
if username != "" and password != "": 
    client.callback_get_login = get_login 
summary = client.diff_summarize(url, revision_min, url, revision_max) 
#print summary 
for changed in summary: 
    #path, summarize_kind, node_kind, prop_changed 
    #for key in changed.iterkeys(): 
    #    print key  
     
    if pysvn.diff_summarize_kind.delete == changed['summarize_kind']: 
      fullPath = targetPath+"/"+changed['path']    
      if os.path.exists(fullPath): 
        os.remove(fullPath) 
     
    if pysvn.diff_summarize_kind.added == changed['summarize_kind'] or pysvn.diff_summarize_kind.modified == changed['summarize_kind']:
        print (changed['summarize_kind'], changed['path']) 
        if changed['node_kind'] == pysvn.node_kind.file: 
             
            #uniPath = changed['path'].decode('utf8').encode() 
            file_text = client.cat(url+urllib.parse.quote(changed['path'].encode('utf8')), revision_max) 
             
            fullPath = targetPath+"/"+changed['path']     
            dirPath = fullPath[0:fullPath.rfind("/")] 
            if not os.path.exists(dirPath): 
                os.makedirs(dirPath) 
                         
            f = open(fullPath,'wb') 
            f.write(file_text) 
            f.close 
    #f = open(fullPath,'wb') 
    #f.write(file_text) 
            #f.close 
#f_tar="./"+os.path.basename(targetPath)+".tar" 
#if os.path.exists(f_tar): 
#    os.remove(f_tar) 
#    print (os.path.basename(f_tar)+" is removed.") 
#else: 
#    print (os.path.basename(f_tar)+" is not exists.")# Folder filter regulation 
os.chdir((r"%s") % targetPath) 
p_list = a_list = s_list = os.listdir(os.getcwd()) 
p_outer_list = list(filter(lambda x:x != "website" and x != "framework", p_list)) 
a_outer_list = list(filter(lambda x:x != "website" and x != "framework" and x != "service", a_list)) 
s_outer_list = list(filter(lambda x:x != "website", s_list)) 
os.chdir((r"%swebsite") % targetPath) 
p_inner_list = a_inner_list = s_inner_list = os.listdir(os.getcwd()) 
p_inner_list = list(filter(lambda x:x != "platform", p_inner_list)) 
a_inner_list = list(filter(lambda x:x != "admin" and x != "union", a_inner_list)) 
s_inner_list = list(filter(lambda x:x != "static", s_inner_list))def inner_filter(list_op): 
    for i in list_op: 
        shutil.rmtree((r"%swebsite%s") % (targetPath,i)) 
    os.chdir((r"%s") % t_path) 
    print (os.listdir(os.getcwd())) 
def filter_site(site_op): 
    if site_version == "p": 
        for p_o in p_outer_list: 
            shutil.rmtree((r"%s%s") % (targetPath,p_o)) 
        inner_filter(p_inner_list) 
    elif site_version == "a": 
        for a_o in a_outer_list: 
            shutil.rmtree((r"%s%s") % (targetPath,a_o)) 
        inner_filter(a_inner_list) 
    elif site_version == "s": 
        for s_o in s_outer_list: 
            shutil.rmtree((r"%s%s") % (targetPath,s_o)) 
        inner_filter(s_inner_list) 
    else: 
        raise Exception (("Unknown site_option: %s") % site_op) 
filter_site(site_version)print (("export file: %s_%s"+'.tar') % (site_version,date_folder)) 
def make_tar(folder_to_tar,dst_folder): 
    fold_name = os.path.basename(folder_to_tar) 
    dst_name = "%s_%s.tar" %(site_version,fold_name) 
    dst_path = os.path.join(dst_folder, dst_name) 
    tar = tarfile.TarFile.open(dst_path, 'w') 
    tar.add(folder_to_tar, fold_name) 
    tar.close() 
    return dst_path 

dst_file = make_tar(targetPath,'./') 
# print (dst_file) 
def upload_file(localfile): 
    ftp=FTP() 
    ftp.connect(ftp_host,ftp_port) 
    ftp.login(ftp_user,ftp_pass) 
    ftp.cwd('./') 
    file=open(localfile,'rb') 
    ftp.storbinary('STOR %s' % os.path.basename(localfile),file) 
    ftp.retrlines('LIST') 
    file.close() 
    ftp.close() 
    ftp.quit 
upload_file(dst_file) 
print ('File Upload Successful.')