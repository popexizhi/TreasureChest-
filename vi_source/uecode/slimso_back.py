# -*- coding:utf8 -*-
#!/usr/bin/python

import sys, os, copy
from ctypes import *
import ctypes
import time, socket, struct
from monlog import monlog


PEXWAIT={"SlimSocket":True}
SlimMAP={"SlimL2_wait_time" : 600,# L2 连接等待时间
         "lib_path_ue":"/home/slim/bgw/Nexus/out/linux/libNexus_Engine_SDK.so", #ue.so
}
SlimTAGLOG={"L2Register":"SlimSocketAgent::SocketManagerRegister start, host_id=" #ue协议栈初始化完成标志,使用hostid匹配

}

class in_addr(Structure):
 _fields_= [
  ('s_addr', ctypes.c_uint),]

class outStructAddr(Structure):
 _fields_= [
    ('sin_len', ctypes.c_char),
    ('sa_family', ctypes.c_ushort),
    ('sin_port', ctypes.c_ushort),
    ('sin_addr_p', ctypes.POINTER(in_addr)),
    ('sin_zero', ctypes.c_char*8),
    ]

class slim_socket():
    def __init__(self, cfg, lib_path, tso=0, isServer=0, pplog="pp.log"):

        self.cfg = cfg
        self.argv = None
        self.host_id_list = None #NexusLibCreateUe use
        self.hostid = None
        self.ut_so = tso # unittest use ,0: 使用真实的so, 1:使用NULL
        #self.pplog = pplog

        self.log("lib_path is %s" % lib_path)
        self.so = self._cdll(lib_path)
        self.isServer = isServer
    
    def _cdll(self, lib_path):
        if 0 == self.ut_so:
            return ctypes.CDLL(lib_path)
    
    def log(self, message, meg_doc = ""):
        sp = "*** " * 20
        mes ="[slim_socket][%s]\t%s\t%s " % (str(time.time()), meg_doc , str(message))
        print sp
        print mes
        f = open("slimlog.log", "a")
        f.write(sp + "\n")
        f.write(mes + "\n")
        f.close()

    def NexusLibMainEntry(self, ue_host_id):
        """
            int __attribute__((visibility("default"))) NexusLibMainEntry(int argc, char *argv[])
            由于原代码中  return 0; # noc/engine/slim_engine_test.cc
            当前判断L2是否建立成功作为返回值
        """
        self.set_hostid(ue_host_id)
        if 0 != self.ut_so:
            return 0 # unittest use

        num_numbers = len(self.argv)
        array_type = ctypes.c_char_p * num_numbers
        self.log("array_type is %s "% str(array_type))
        
        res = self.so.NexusLibMainEntry(ctypes.c_int(num_numbers), array_type(*self.argv))
        assert 0 == res #如果此问题报错，请检查so方法是否修改
        self.host_id_list = []
        wait_res = self._wait_l2(self.get_hostid())
        return wait_res
    def set_hostid(self, hostid):
        """
            set hostid
        """
        if None == self.argv :
            self.hostid = hostid
            self.argv = ['slimtest.py', '-cfg=%s' % self.cfg, '-host=%s' % str(hostid)]
        else:
            self.hostid = hostid
        self.log("len self.argv is %d" % len(self.argv))
        self.log("self.argv is %s" % str(self.argv))

        self.pplog = "log/ue_client_%s.log.txt" % str(self.hostid)
        self.log("ue log is %s" % str(self.pplog))

    def get_hostid(self):
        """
        get hostid
        """
        if None == self.hostid: #unittest use 
           self.hostid = self.argv[2].split("host=")[1]

        return self.hostid

    def _wait_l2(self, host_id_i):
        """
        pp.log 中出现L2连接成功标准
        """
        #l2 data 
        log_m = monlog()
        res = log_m.sh_grep(SlimTAGLOG["L2Register"]+str(host_id_i), self.pplog) 
        wait_time = 0
        while "" == res and 0 == self.isServer :
            wait_time = wait_time + 1
            if wait_time > SlimMAP["SlimL2_wait_time"]:
                self.log("[wait time is too long]")
                return -1
            time.sleep(1)
            res = log_m.sh_grep(SlimTAGLOG["L2Register"]+str(host_id_i), self.pplog) 
            self.log("wait l2 register for Bind %s" % str(SlimTAGLOG["L2Register"]+str(host_id_i)))
        self.log("[DEBUG***************wait:%s]res is %s" % (str(wait_time), res))
        return 0

    def NexusLibCreateUe(self, ue_host_id, cfg_file):
        """ 
            int  __attribute__((visibility("default"))) NexusLibCreateUe(int ue_host_id )
            由于原代码中  return 0; # noc/engine/slim_engine_test.cc
            当前判断L2是否建立成功作为返回值
        """
        #self.log("NexusLibCreateUe ue_host_id:%s" % str(ue_host_id))
        self.log("NexusLibCreateUe ue_host_id:%s; cfg_file:%s" % (str(ue_host_id), str(cfg_file)))
        assert ue_host_id
        self.hostid = ue_host_id
        if 0 != self.ut_so:
            return 0 # unittest use
        
        c_ui_host_id = ctypes.c_uint(ue_host_id)#host_id范围也可能使用c_int
        c_char_p_cfg_file = ctypes.c_char_p(cfg_file)
        log_use = "c_ui_host_id is %r \t c_char_p_cfg_file is %s" % (c_ui_host_id , c_char_p_cfg_file )
        self.log(log_use) 
        #res = self.so.NexusLibCreateUe(c_ui_host_id)  
        res = self.so.NexusLibCreateUe(c_ui_host_id, c_char_p_cfg_file) 
        assert 0 == res #如果此问题报错，请检查so方法是否修改

        wait_res = self._wait_l2(self.get_hostid())
        return wait_res
     

    def NexusAPPMainEntry(self):
        """sever use """
        self.NexusAPPMainEntry_WT = 10 #10s
        num_numbers = len(self.argv)
        array_type = ctypes.c_char_p * num_numbers
        self.log("array_type is %s "% str(array_type))

        #provision
        #self.so.NexusAPPMainEntry.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_char_p))
        self.so.NexusAPPMainEntry(ctypes.c_int(num_numbers), array_type(*self.argv))        
        time.sleep(self.NexusAPPMainEntry_WT)

    def SlimSocket(self, __type = "SOCK_STREAM"):
        """extern int SlimSocket(int __domain, int __type, int __protocol) ;"""
        if "SOCK_STREAM" == __type: 
            fd_ = self.so.SlimSocket(socket.AF_INET, socket.SOCK_STREAM, ctypes.c_int(0))
        if "SOCK_DGRAM" == __type:
            fd_ = self.so.SlimSocket(socket.AF_INET, socket.SOCK_DGRAM, ctypes.c_int(0))
            
        self.log("SlimSocket res fd_ is %s; type %s" % (str(fd_), str(__type)))
        self.fd_ = fd_
        return fd_
    
    def SlimBind(self , fd = -1 , port_i = 9000, host_id_i = 2104 ):
        """
        extern int  SlimBind (int __fd, const struct sockaddr * __addr, socklen_t __len)
        """
        self.port_i = port_i
        self.host_id_i = host_id_i
        sockaddr_in = struct.pack("HHI",socket.AF_INET, socket.ntohs(self.port_i), socket.htonl(self.host_id_i))
        sockaddr_in_len = 16 #16 is long for sockaddr_in 
        self.c_addr_in_len = ctypes.c_int(sockaddr_in_len)

        #fd_ = self.fd_ if -1 == fd else fd #next 业务层引起,移除
        fd_ = fd
        self.log("sockaddr_in is %s; sockaddr_in len is %s, fd_ is %s" % (repr(sockaddr_in), len(sockaddr_in), str(fd_)))
        
        res = self.so.SlimBind(fd_, sockaddr_in, 16 )
        self.log(res, " SlimBind res is ")
        return res
    
    def SlimListen(self, listen_num = 1):
        """serever use  """
        self.SlimListen_WT = 1 # 1s
        assert self.fd_
        res = self.so.SlimListen(self.fd_, ctypes.c_int(listen_num))
        time.sleep(self.SlimListen_WT)
        self.log("listen res is %d" % res)
        assert res > -1
    
    def SlimAccept(self):
        """server accept """
        self.SlimAccept_WT = 1 # 1s
        assert self.fd_
    
        c_addr = outStructAddr()
        c_i_addr_len = 0
        self.so.SlimAccept.argtypes= [ctypes.c_int, ctypes.POINTER(outStructAddr), ctypes.POINTER(ctypes.c_int)]
        self.newfd = self.so.SlimAccept(self.fd_, ctypes.byref(c_addr), ctypes.byref(ctypes.c_int(c_i_addr_len)))        
        
        log_use = "SlimAccept newfd is "+ str(self.newfd) + "\t c_addr"+ repr(c_addr) + "\t len is "+ str(c_i_addr_len)
        self.log(log_use)
        self.log("c_addr is ")
        self.log(c_addr)
        self.log("c_addr.sin_len is ")
        self.log(c_addr.sin_len)
        self.log("c_addr.sa_family is ")
        self.log(c_addr.sa_family)
        self.log("c_addr.sin_port is ")
        self.log(c_addr.sin_port)
        time.sleep(self.SlimAccept_WT)

        return self.newfd

    def SlimConnect(self, fd= -1, s_port = 3000, s_host_id_i = 2102 ):
        """
        extern int  SlimConnect (int __fd, const struct sockaddr * __addr, socklen_t __len);
        """
        self.s_port_i = s_port
        self.s_host_id_i = s_host_id_i
        sockaddr_in = struct.pack("HHI",socket.AF_INET, socket.ntohs(self.s_port_i), socket.htonl(self.s_host_id_i))
        sockaddr_in_len = 16 #16 is long for sockaddr_in 
        self.s_addr_in_len = ctypes.c_int(sockaddr_in_len)        
        
        self.log("[SlimConnect] \t sockaddr_in is %s; sockaddr_in len is %s" % (repr(sockaddr_in), len(sockaddr_in)))
        fd_ = self.fd_ if -1 == fd else fd 
        res = self.so.SlimConnect(fd_, sockaddr_in, self.s_addr_in_len )
        self.log(res, "SlimConnect res is")
        return res

    def SlimSend(self, fd , send_str):
        """
        int  SlimSend (int __fd, const void *__buf, size_t __len, int __flags );
        """
        self.c_send_str_length_i = ctypes.c_int(len(send_str))
        self.c_char_p_send_str = ctypes.c_char_p(send_str)
        
        self.log("[SlimSend] start send ...")
        send_num = self.so.SlimSend(fd, self.c_char_p_send_str, self.c_send_str_length_i, 0)
        self.log("send_num is %d" % send_num)
       
        self.log("[SlimSend] end send ...")
        return send_num
    
    def SlimSendTo(self, fd , send_str, s_port, s_host_id_i):
        """
        int SlimSendTo(int __fd, void *__buf, size_t __len, unsigned int __flags, struct sockaddr * __to, int __tolen);
        """
        c_send_str_length_i = ctypes.c_int(len(send_str))
        c_char_p_send_str = ctypes.c_char_p(send_str)
        
        sockaddr_in = struct.pack("HHI",socket.AF_INET, socket.ntohs(s_port), socket.htonl(s_host_id_i))
        sockaddr_in_len = 16 #16 is long for sockaddr_in 
        s_addr_in_len = ctypes.c_int(sockaddr_in_len)        
        self.log("[SlimSendTo]\t[fd %s] sockaddr_in is %s; sockaddr_in len is %s" % (str(fd), repr(sockaddr_in), len(sockaddr_in)))
        
        self.log("[SlimSendTo] start send ...")
        send_num = self.so.SlimSendTo(fd, c_char_p_send_str, c_send_str_length_i, 0, sockaddr_in, s_addr_in_len)
        self.log("send_num is %d" % send_num)
        self.log("udp send data %r" % repr(send_str)) 
        self.log("udp send data %r" % send_str) 
        self.log("udp send data %s" % send_str) 
        self.log("[SlimSend] end send ...")
        return send_num
    
    
    def SlimClose(self, nfd):
        """ close fd """
        assert nfd
        self.log("[SlimClose] fd is %d" % nfd)
        res = self.so.SlimClose(nfd)
        self.log("[SlimClose] res is %s" % str(res))
        return res

    def SlimReceive(self, nfd):
        """ 
            int SlimReceive (int __fd, void *__buf, size_t __len, int __flags);
        """
        self.log("[SlimReceive]")
        fd_ = nfd
        #self.so.SlimReceive.argtypes= [ctypes.c_int, ctypes.c_char_p , ctypes.c_int, ctypes.c_int]

        
        self.log("[SlimReceive]")
        rec_num = -1
        res = ""
        int_list = " "*1000
        while 10000 == rec_num or rec_num < 0:
            #c_int_sizeof = ctypes.sizeof(ctypes.c_int)
            rcv_buf = ctypes.c_char_p(" "*10000)
            
            #rcv_buf = ctypes.c_void_p(ctypes.c_char(" ")* 1000)
            self.log("[SlimReceive] start")
            rec_num = self.so.SlimReceive(ctypes.c_int(fd_), rcv_buf, ctypes.c_int(10000), ctypes.c_int(0)) # next这里固定读取1000 ,没有做全都读取的处理
            #self.log("rcv_buf is (%r)" % repr(rcv_buf))
            #self.log("rcv_buf.value is (%r) " % rcv_buf.value)
            #self.log("rcv_buf[] is (%r)" % repr(rcv_buf.value[0:rec_num]))
            #self.log("rec_num is %d" % rec_num)
            
            new = copy.deepcopy(rcv_buf.value)
            res = res + repr(new)
            #res = res + repr(rcv_buf.value)
        #被动关闭处理
        if 0 == rec_num:
            self.SlimClose(fd_)
            self.log("[SlimSocket %d is closed ]" % fd_)
            return rec_num, ""
         
        #res_da = copy.deepcopy(res[0:rec_num])
        self.log("res is(leng %d) %s" % (len(repr(res)), repr(res)))
        self.log("rcv_buf is(leng %d) %s" % (len(repr(rcv_buf.value)), repr(rcv_buf.value)))
        return rec_num, res


    def SlimRecvFrom(self, nfd, s_port, s_host_id_i):
        """ 
           int  SlimRecvFrom(int __fd, void *__buf, size_t __len, unsigned int __flags, struct sockaddr  *__from, socklen_t *__fromlen);
        """
        fd = nfd
        
        #sockaddr_in = struct.pack("HHI",socket.AF_INET, socket.ntohs(s_port), socket.htonl(s_host_id_i))

        c_sockaddr = outStructAddr()
        c_i_sockaddr_in_len = 0 
        self.log("[SlimReceiveFrom]\t[fd %s] sockaddr_in is %s; sockaddr_in len is %s" % (str(fd), repr(c_sockaddr), str(c_i_sockaddr_in_len)))
        
        #self.so.SlimReceiveFrom.argtypes= [ctypes.c_int, ctypes.c_char_p , ctypes.c_int, ctypes.c_int, ctypes.c_]
        
        rcv_buf = c_char_p(" "*1000)
        self.log("[SlimReceiveFrom] start")
        self.so.SlimRecvFrom.argtypes= [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_uint , ctypes.POINTER(outStructAddr), ctypes.POINTER(ctypes.c_int)]
        # ctypes.byref(ctypes.c_int(c_i_addr_len))
        rec_num = self.so.SlimRecvFrom(fd, rcv_buf , 1000, 0, ctypes.byref(c_sockaddr), ctypes.byref(ctypes.c_int(c_i_sockaddr_in_len))) # next这里固定读取1000 ,没有做全都读取的处理
        self.log("[SlimReceiveFrom] end")
        self.log("rcv_buf is %s" % rcv_buf.value)
        self.log("rec_num is %d" % rec_num)
        
        self.log("c_addr is ")
        self.log(c_sockaddr)
        self.log("c_addr.sin_len is ")
        self.log(c_sockaddr.sin_len)
        self.log("c_addr.sa_family is ")
        self.log(c_sockaddr.sa_family)
        self.log("c_addr.sin_port is ")
        self.log(c_sockaddr.sin_port)
        #被动关闭处理
        if 0 == rec_num:
            self.SlimClose(fd_)
            self.log("[SlimSocket %d is closed ]" % fd_)
            return rec_num, ""
        res = copy.deepcopy(rcv_buf.value)
         
        #res_da = copy.deepcopy(res[0:rec_num])
        self.log("res is %s" % res)
        return rec_num, res


    def wait_so(self, wait_str):
        while PEXWAIT[wait_str]:
            self.log("wait %s" % wait_str)
            time.sleep(1)

        return 0
    def SlimGetSocketStreamID(self, fd):
        """
            int  SlimGetSocketStreamID(int nexus_fd);
        """
        fd_i = ctypes.c_int(int(fd))
        self.log("[SlimGetSocketStreamID] fd_i is %s" % str(fd_i))
        res = self.so.SlimGetSocketStreamID(fd_i)
        self.log("[SlimGetSocketStreamID] res is %s" % str(res))
        return res
def test_client():
    #cmd = ["slimtest.py", '-cfg=alone_dev.cfg', "-host=113031"]
    cfg="alone_dev.cfg"
    lib_p = SlimMAP["lib_path_ue"]#"/home/slim/bgw/Nexus/out/linux/libNexus_Engine_SDK.so"
    x = slim_socket(cfg, lib_p, "testso.log")
    x.NexusLibMainEntry(113031)
    fd = x.SlimSocket()
    x.SlimBind(fd, host_id_i=113031)
    streamID = x.SlimGetSocketStreamID(fd)
    print "$" * 20
    print streamID
#    x.SlimConnect(fd, s_port =9000, s_host_id_i = 113030)
#    data = "hi ,i am here .Unu wir statas vi!"
#    x.SlimSend(fd, data)
#    x.SlimClose(fd)
    
if __name__ == "__main__":
    test_client()
