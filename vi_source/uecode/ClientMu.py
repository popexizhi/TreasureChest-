# -*- coding:utf8 -*-
#!/usr/bin/python

import time, socket
from slimso_back import slim_socket
import threading
import struct
from Mapping import *

class client():
    slim_socket = None
    slim_cfg = None
    slim_isfir = 0
    @staticmethod
    def so_cdll(cfg, lib, tso= 0):
        if None == client.slim_socket:
            client.slim_socket = slim_socket(cfg, lib, tso= tso)        
            client.slim_cfg = cfg
             

    def __init__(self, hostid):
        assert client.slim_socket
        assert client.slim_cfg
        self.err = 0
        if 0 == client.slim_isfir:
            #首次使用要求调用NexusLibMainEntry
            res =  client.slim_socket.NexusLibMainEntry(hostid)
            if 0 == res:
                client.slim_isfir = 1
                self.so = client.slim_socket
                self.log("[mu ue test][L2 connect][_init_ :NexusLibMainEntry] hostid %s" % str(hostid))
            else:
                self.log("[mu ue test][L2 connect][_init_ :NexusLibMainEntry ERRRRRRR] hostid %s" % str(hostid))
                
        else:
            assert client.slim_socket
            self.so = client.slim_socket
            #非首次使用NexusLibCreateUe
            self.log("[mu ue test][_init_ :NexusLibCreateUe] hostid %s, cfg is %s" % (str(hostid), str(client.slim_cfg)))
            res = self.so.NexusLibCreateUe(hostid, client.slim_cfg)

        if -1 == res :
           self.err = 1 
        

    def SlimSocket(self, type_):
        assert self.so
        fd_ = self.so.SlimSocket(type_)
        self.log("[mu ue test][SlimSocket] fd_ %s" % fd_)
        assert fd_ > -1 #next 业务层判断
        return fd_

    def SlimBind(self, fd , port_i, host_id_i):
        assert self.so
        self.log("[mu ue test][SlimBind]fd %s ; host_id_i %s" % (str(fd), str(host_id_i)))
        res = self.so.SlimBind(fd, port_i, host_id_i)
        assert res > -1 #next 业务层引起
        return res

    def SlimConnect(self, fd, s_port, s_host_id_i):
        assert self.so
        res = self.so.SlimConnect(fd, s_port, s_host_id_i)
        assert res > -1
        return res

    def log(self, mes):
        assert self.so
        self.so.log(mes)


    def SlimSend(self, fd, send_str):
        assert self.so
        res = ""
        send_num = 0
        if send_num < len(send_str): #next send socket业务逻辑,移除
            self.log("new send length is %s" % str(len(send_str)))
            res = send_str[send_num:-1]
            self.log("new res is %s" % res)
            send_e_len = self.so.SlimSend(fd, res)

            send_num = send_num + send_e_len
        return send_num

    def SlimSendTo(self, fd, data, s_port, s_hostid):
        assert self.so
        return self.so.SlimSendTo(fd, data, s_port, s_hostid)

    def SlimReceive(self, fd):
        assert self.so
        return self.so.SlimReceive(fd)
    def SlimRecvFrom(self, fd):
        assert self.so
        return self.so.SlimRecvFrom(fd, None, None)

    def SlimClose(self, fd):
        assert self.so
        return self.so.SlimClose(fd)
        

class mu_clients(threading.Thread):
    def __init__(self, CsoClass, hostid, connection_id):
        threading.Thread.__init__(self)
        self.so = CsoClass
        self.hostid = hostid
        self.thread_stop = False  
        self.stop_res = None
        self.connection_id = connection_id 
    def log(self, message):
        print message
        f = open("uelog/%s_ue.log" % str(self.hostid),"a")
        f.write("%s\n" % str(message))
        f.close()

    def connect_c(self):
        #self.log("[mu ue test][tcp_c] hostid is %s; port is %s, s_port is %s; s_host_id_i is %s" % (str(self.hostid), str(self.port), str(self.s_port), str(self.s_host_id_i)))
        self.log("[mu ue test]hostid %s" % self.hostid)
        self.pm = self.so(self.hostid)
        if 1 == self.pm.err:
            self.stop("L2 too long time")
            return -1
    
    def tcp_c(self):
	self.connect_c()
        fd_i = self.pm.SlimSocket("SOCK_STREAM")
        self.log("[mu ue test] [be bind] fd_i %s hostid %s" % (str(fd_i), str(self.hostid))) 
        self.pm.SlimBind(fd_i, port_i = self.port , host_id_i=self.hostid)
        self.pm.SlimConnect(fd_i, self.s_port, self.s_host_id_i)
        self.log("[mu ue test][tcp SlimConnect pass] hostid is %s; port is %s, s_port is %s; s_host_id_i is %s" % (str(self.hostid), str(self.port), str(self.s_port), str(self.s_host_id_i)))
        return fd_i
    
    def udp_c(self):
        self.log("[mu ue test][udp_c] hostid is %s; port is %s, s_port is %s; s_host_id_i is %s" % (str(self.hostid), str(self.port), str(self.s_port), str(self.s_host_id_i)))
        #UDP创建前业务逻辑上此ue已经创建过tcp连接，这里不再需要初始化此类的了,所以注释
        #self.pm = self.so(self.hostid)
        #if 1 == self.pm.err:
        #    self.stop("L2 too long time")
        #    return -1
        self.log("udp SlimSocket")
        fd_i = self.pm.SlimSocket("SOCK_DGRAM")
        self.log("[mu ue test] [be bind] udp fd_i %s hostid %s" % (str(fd_i), str(self.hostid))) 
        self.pm.SlimBind(fd_i, port_i = self.port , host_id_i=self.hostid)
        self.log("[mu ue test][udp SlimBind pass] hostid is %s; port is %s, s_port is %s; s_host_id_i is %s" % (str(self.hostid), str(self.port), str(self.s_port), str(self.s_host_id_i)))
        
        return fd_i

    def set_tcp_use(self, port, s_port, s_host_id, s_udp_port):
        self.port = port
        self.s_port = s_port
        self.s_host_id_i = s_host_id
        self.s_udp_port = s_udp_port

    def run(self):
	self.connect_c()

    #def run(self):
    def send_run(self):
        fd = self.tcp_c()
        if -1 == fd :
            self.log("[popexizhi][mu ue] hostid %s; L2 too long time" % str(self.hostid))
        else:
            data2 = "[%s][fd%s]time here for me!" % (str(self.hostid), str(fd))
            self.SlimSend(fd, data2)
            self.log("[popexizhi][mu ue] hostid %s; tcp fd %s" % (str(self.hostid), str(fd)))
            #udp send
            self.port = self.port + 1
            self.s_port = 4000
            udp_fd = self.udp_c()
            
            stream_id = self.pm.so.SlimGetSocketStreamID(fd) # 获得stream_id
            self.log("[popexizhi][mu ue] hostid %s; tcp fd %s; stream_id %s" % (str(self.hostid), str(fd), str(stream_id)))
            data = get_UDPData(stream_id, self.connection_id)
            
            self.log("[popexizhi][mu ue] hostid %s get_UDPData %s" % (str(self.hostid), str(data))) #要发送的控制报文内容
            res = self.SlimSendTo(udp_fd, data, self.s_udp_port, self.s_host_id_i )
            self.log("[popexizhi][mu ue][udp sendto pass] hostid %s prot %s sendto udpfd %s, res %s" % (str(self.hostid), str(self.s_udp_port), str(udp_fd), str(res)))
            res = self.SlimRecvFrom(udp_fd)
            self.log("[popexizhi][mu ue][udp SlimRecvFrom pass] hostid %s {res:%s}" % (str(self.hostid), str(res)))
            self.log("[popexizhi][mu ue] [SlimRecvFrom] ufd %s; %s" % (str(udp_fd), str(res))) #此处业务要求接受到与发送相同的UDP协议包，为appserver被设置发送模型成功
            th1 = threading.Thread(target=self.SlimReceive, args=(fd,)) 
            th1.start()
        
            self.stop("pass")
    
    def stop(self, message):
        self.thread_stop = True
        self.stop_res = message
    
    def SlimSend(self, fd, data):
        return self.pm.SlimSend(fd, data)
    
    def SlimSendTo(self,fd, data, s_port, s_hostid):
        return self.pm.SlimSendTo(fd, data, s_port, s_hostid)

    def SlimReceive(self, fd):
        while 1:
            self.log("[popexizhi][mu ue][hostid: %s] tcp slimreceive fd:%s wait" % (str(self.hostid), str(fd)))
            res = self.pm.SlimReceive(fd) #开始接受tcp数据
            self.log("[mu ue][tcp SlimReceive][hostid: %s] [%s]res: %s " % (str(self.hostid), str(time.time() * 1000), str(res)))
            self.getbody(res)
            if 0 == res[0] :
                self.log("[mu ue][hostid:%s] closed stop.... " % str(self.hostid))
                break
    def getbody(self, res):
        self.log("[mu ue][getbody] pack:"+str(res))
        #fra_res = "!12siq%ds" % int(len(res[1])-24)
        #print fra_res
        #header, p_num, p_time, body = struct.unpack(fra_res, res[1])
        body = res[1].split()
        self.log("body %s" % str(body))

    def SlimRecvFrom(self, fd):
        return self.pm.SlimRecvFrom(fd)

def test_client():
    cfg="alone_dev.cfg"
    lib_p = SlimMAP["lib_path_ue"]#"/home/slim/bgw/Nexus/out/linux/libNexus_Engine_SDK.so"
    client.so_cdll(cfg, lib_p)
    res_list = {}
    host_l = hostid_list
    
    ue_host = host_l[0][0]
    appserver_host = 6062
    app_udp_port = 5000
    mu = mu_clients(client, ue_host, host_l[0][1])
    mu.set_tcp_use(2000, 3000, appserver_host, app_udp_port)
    
    fd = mu.tcp_c()
    mu.SlimSend(fd, "hi this is first hostid is %s" % str(ue_host)) #业务逻辑要求，先发送TCP一包后，才可使用SlimGetSocketStreamID
    print "[popexizhi][hostid: %s] send tcp" % str(ue_host)
    stream_id = mu.pm.so.SlimGetSocketStreamID(fd)
    mu_log("stream_id %s" % str(stream_id))
    
    
    mu.set_tcp_use(2001, app_udp_port, appserver_host, app_udp_port) #设置UDP连接参数
    udp_fd = mu.udp_c()
    #mu.SlimSendTo(udp_fd, "udp test", 9000, 114252 )
    data = get_UDPData(stream_id, host_l[0][1])
    print "[popexizhi][hostid: %s] get_UDPData %s" % (str(ue_host), str(data)) #要发送的控制报文内容
    res = mu.SlimSendTo(udp_fd, data, app_udp_port, appserver_host )
    print "[popexizhi][hostid: %s] port %s sendto udpfd %s, res %s" % (str(ue_host), str(app_udp_port), str(udp_fd), str(res))
    time.sleep(5)
    #assert 1 == 0
    res = mu.SlimRecvFrom(udp_fd)
    print "[popexizhi][hostid: %s] SlimRecvFrom" % str(ue_host)
    mu_log("[SlimRecvFrom] ufd %s; %s" % (str(udp_fd), str(res))) #此处业务要求接受到与发送相同的UDP协议包，为appserver被设置发送模型成功
    #mu.SlimReceive(fd) #开始接受tcp数据
    th1 = threading.Thread(target=mu.SlimReceive, args=(fd,)) 
    th1.start()

    ##while 1:
        #pass
    mu_log( "*****************************************************************************************************************")
    port = 2000
    #host_l = [(114253,490712898584140)]
    print "[popexizhi] hostid %d; conn %d" % (host_l[0][0], host_l[0][1])
    print "[popexizhi] hostid_list %d " % len(host_l)
    for h_c_i in host_l[1:]:
        i = h_c_i[0]
        connection_id = h_c_i[1]
        mu_log( "[popexizhi]************[hostid : %d, connection_id : %d]**************" % (i, connection_id), i)
        port = port + 1
        pm = mu_clients(client, i, connection_id)
        res_list[i] = pm
        fd = pm.set_tcp_use(port, 3000, appserver_host, app_udp_port)
        pm.start()
     
    for key in res_list:
        if None != res_list[key].stop_res:
            mu_log( "%s : %s" % (str(key), str(res_list[key].stop_res)))

def test_client_only_l2():
    cfg="alone_dev.cfg"
    lib_p = SlimMAP["lib_path_ue"]#"/home/slim/bgw/Nexus/out/linux/libNexus_Engine_SDK.so"
    client.so_cdll(cfg, lib_p)
    res_list = {}
    host_l = hostid_list
    
    ue_host = host_l[0][0]
    appserver_host = 6062
    app_udp_port = 5000
    mu = mu_clients(client, ue_host, host_l[0][1])
    mu.set_tcp_use(2000, 3000, appserver_host, app_udp_port)
    
    mu.connect_c()

    mu_log( "*****************************************************************************************************************")
    port = 2000
    #host_l = [(114253,490712898584140)]
    print "[popexizhi] hostid %d; conn %d" % (host_l[0][0], host_l[0][1])
    print "[popexizhi] hostid_list %d " % len(host_l)
    for h_c_i in host_l[1:]:
        i = h_c_i[0]
        connection_id = h_c_i[1]
        mu_log( "[popexizhi]************[hostid : %d, connection_id : %d]**************" % (i, connection_id), i)
        port = port + 1
        pm = mu_clients(client, i, connection_id)
        res_list[i] = pm
        #fd = pm.set_tcp_use(port, 3000, appserver_host, app_udp_port)
        pm.start()
     

def mu_log(mes, hostid=0):
    f = open("uelog/moreue_%d.log" % hostid, "a")
    f.write("%s\n" % str(mes))
    f.close()
    print "[mu_log] %s" % str(mes)

def get_UDPData(stream_id, connection_id):
    """
    {"data_direction":"s2c","packet_length":100,"packet_number_per_second":xx,"run_time_in_seconds":xx}
    """
    data = '{"data_direction":"s2c","packet_length":100,"packet_number_per_second":10,"run_time_in_seconds":300}'
    print "[UDPData]  stream_id %s, connection_id %s" %  (str(stream_id), str(connection_id))
    head_i = connection_id + stream_id
    print "head_i (%s) " % repr(head_i)
    head = struct.pack("Q", head_i)
    #p_d = struct.pack("Q", head_i)
    print "data leng %d" % len(str(data))
    print "head (%s) " % repr(head)
    print "head leng %s" % len(head)
    fra_pack = "12sQ%ds" % len(str(data))
    package = "PacketHeader"+ head + data
    #print "fra_pack %s" % fra_pack
    #package = struct.pack(fra_pack , "PacketHeader", head_i , str(data))
    print "package %s" % str(package)
    print "package" + repr(package)
    return package


if __name__ == "__main__":
    #test_client()
    test_client_only_l2()
    #get_UDPData(259)

