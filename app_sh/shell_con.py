#-*- coding:utf8 -*-
import subprocess
import re, time, sys
import thread
class sh_control():
    def __init__(self):
        pass

    def log(self, message):
        print "*" * 20
        print message

    def app_provision(self, num):
        #self.appserver_cmd = './app_server -cfg="cfg/app_%d_alone.cfg" -db -server_provision -host="%d" ' % (num, num)
        self.appserver_cmd = './app_server.sh %d' % num
        self._com(self.appserver_cmd)

    def dev_provision(self, start , num):
        #self.dev_cmd = './slim_engine_test -cfg="cfg/dev_%d_alone.cfg" -db -provision -host="dev%d"  ' % (num, num)
        self.dev_cmd = './slim_engine_test.sh %d' % num
        self._com(self.dev_cmd)
    
    def dev_data(self, host_id):
        self.dev_cmd = './slim_engine_test_data.sh %d' % host_id
        self._com(self.dev_cmd)

    def kill_all(self):
        self.kill_cmd = './stop_app.sh'
        self._com(self.kill_cmd)

    def kill_dev(self):
        self.kill_cmd = './stop_dev.sh'
        self._com(self.kill_cmd)

    def back_up(self, num):
        self.back_up = './backall.sh %s' % num
        self._com(self.back_up)

    def back_up_app_dbII(self, num):
        """ fix NGS-604:
            35-release 代码中添加appserver中dev 的L2 key验证，增加provision test的copy appserver db在每次dev provision 成功后
        """
        com_list = ["cp nplServer1.* dbback//%s//" % str(num)]
        self._list_com(com_list)

    def back_up_app_db(self, num):
        #self.back_up = './appbackup.sh %s' % num
        com_list = ["mkdir dbback//%s" % str(num), "cp *.db dbback//%s//" % str(num), "ls -all dbback//%s" % str(num) ]
        self._list_com(com_list)
    
    def back_up_dev_db(self, server_id, dev_host):
        #self.back_up = './appbackup.sh %s' % num
        com_list = ["mkdir dbback//%s" % str(server_id), "cp npl1.db dbback//%s//npl%s.db" % (str(server_id), str(dev_host)), "cp npl1.bootstrap.db dbback//%s//npl%s.bootstrap.db" % (str(server_id), str(dev_host)), "ls -all dbback//%s" % str(server_id) , "mv log/ue_client_1.log.txt log/ue_client_%s.log.txt" % str(dev_host)]
        self._list_com(com_list)
    def load_back_up_dev_db(self, sooure_dev_host , server_id, dev_host):
        #self.back_up = './appbackup.sh %s' % num
        com_list = ["mkdir dbback//%s" % str(server_id), "mv npl%s.db dbback//%s//npl%s.db" % (str(sooure_dev_host), str(server_id), str(dev_host)), "mv npl%s.bootstrap.db dbback//%s//npl%s.bootstrap.db" % (str(sooure_dev_host), str(server_id), str(dev_host)), "ls -all dbback//%s" % str(server_id) , "mv log/ue_client_%s.log.txt dbback/err/ue_client_%s.log.txt" % (str(sooure_dev_host), str(dev_host))]
        self._list_com(com_list)
    
    def kill_all_dev(self):
        com_list = ["ps axu|grep slim_engine_test|cut -c 9-15|xargs kill -9"]
        self._list_com(com_list)

    def _list_com(self, com_list):
        for i in com_list:
            self._com(i)
    
    def remove_all_db(self):
        com_list = ["rm *.db", "ls -all |grep db"]
        self._list_com(com_list)
    
    def clear_uelog(self):
        com_list = ["rm log/ue_client_1.log.txt"]
        self._list_com(com_list)

    def back_use_cp(self):
        self.back_up = './use_back.sh'
        self._com(self.back_up)

    def _com(self, cmd):
        getchar = "a"
        #self.log(cmd)
        self.app_log_b = subprocess.Popen([cmd], shell=True,  stdout = subprocess.PIPE, stdin = subprocess.PIPE)
        # Send the data and get the output
        stdout, stderr = self.app_log_b.communicate(getchar)
        return stdout, stderr 
if __name__=="__main__" :
    std = int(sys.argv[1])
    #test_provision(std)
    a = sh_control()
    a.dev_data(std)

def test_provision(std):
    for i in xrange(1):
    #    thread.start_new_thread(app_provision,(i+1011, ))
    #    print "start ....%d" % i+1011
    #    time.sleep(1)
    #    std = int(sys.argv[1])
        a = sh_control()
        a.app_provision(i+std)
        a.dev_provision(i+std)
    
