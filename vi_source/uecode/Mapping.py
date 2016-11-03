# -*- coding:utf8 -*-
# ue db num
from db_Driver import sqlite_Driver  
from dirlist import hostlist
hostid_list = hostlist 
PEXWAIT={"SlimSocket":True}
SlimMAP={
        "SlimL2_wait_time" : 600,# L2 连接等待时间
        "lib_path_ue":"/home/slim/test/Nexus/out/linux/libNexus_Engine_SDK.so", #ue.so
}

SlimTAGLOG={
            "L2Register":"SlimSocketAgent::SocketManagerRegister start, host_id=" #ue协议栈初始化完成标志,使用hostid匹配
}

def get_hostid_L2_list(hostid_list):
    x = sqlite_Driver("npl1.db")
    res_list = []
    for i in hostid_list:
        db_p = "npl%s.db" % str(i)        
        conid = x.get_L2_connection_id(db_p)
        assert conid
        print "hostid %d; conid %d" % (i, conid)
        res_list.append([i, conid])
    return res_list


hostid_list=get_hostid_L2_list(hostid_list)
print len(hostid_list)


