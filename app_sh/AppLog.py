#!/bin/python2.7
#-*-coding:utf8-*-
from DygraphData import dygraph_data
from Map import *
import re, datetime, time
from shell_con import sh_control 
from Static import static

class app_log():
    def __init__(self):
        self.dy = dygraph_data()
        self.keys = [\
        HandleL2AuthReq, \
        HandleDeviceInfoIndication, \
        EAPServiceWorker_DoConfirmPolicyVersion,\
        EAPRpcService_OnDevicePolicyUpdated\
        ]
        self.ue_list = {}
        self.sh = sh_control()

    def ana_ue(self, fp):
        f = open (fp)
        com = f.readlines()
        f.close()
        self.ue_list[fp] = [] 
        for line in com:
            print line
            res = self.ana_log(line)
            if [] == res:
                pass
            else:
                self.ue_list[fp].append(res)

        self.show_ue(self.ue_list[fp])
        new = ue_time(self.ue_list[fp])
        return new
    def show_ue(self, ue):
        for i in ue:
            print i

    def ana_log(self, line):
        for key in self.keys:
            res = self.dy.check_line_source(line, key, 0)
            if type(0) == type(res):
                res = []
            else:
                return res
        return res
    def get_host_dir(self, dir_ue):
        self.ues = {}
        for fp in self.sh._com("ls %s" % dir_ue)[0].split("\n")[:-2]:
            ue_fp = "%s/%s" % (dir_ue, fp)
            ue = self.ana_ue(ue_fp)
            self.ues[fp] = ue

    def ana_end_ues(self):
        assert self.ues
        res = {\
               "1HandleL2AuthReq":[], \
               "2HandleDeviceInfoIndication":[], \
               "3EAPServiceWorker::DoConfirmPolicyVersion":[],\
               "4EAPRpcService::OnDevicePolicyUpdated":[]\
               #EAPRpcService::OnDevicePolicyUpdated
        }
        res_beg = {\
               "1HandleL2AuthReq":[], \
               "2HandleDeviceInfoIndication":[], \
               "3EAPServiceWorker::DoConfirmPolicyVersion":[],\
               "4EAPRpcService::OnDevicePolicyUpdated":[]\
               #EAPRpcService::OnDevicePolicyUpdated
        }
        res_err = {\
               "1HandleL2AuthReq":[], \
               "2HandleDeviceInfoIndication":[], \
               "3EAPServiceWorker::DoConfirmPolicyVersion":[],\
               "4EAPRpcService::OnDevicePolicyUpdated":[]\
        }
        res_pass = {\
               "1HandleL2AuthReq":[], \
               "2HandleDeviceInfoIndication":[], \
               "3EAPServiceWorker::DoConfirmPolicyVersion":[],\
               "4EAPRpcService::OnDevicePolicyUpdated":[]\
        }
        for i in self.ues:
            ue = self.ues[i]
            #ue.show()
            for list_key in self.keys:
                for key in list_key:
                    if "time" != key:
                        print key
                        end_res = ue.get_end_use_time(key)
                        use_time_s = ue.use_time(key) 
                        if None != end_res:
                            #res[key].append([end_res.strftime('%Y-%m-%d %I:%M:%S'), use_time_s])
                            res[key].append([end_res.strftime('2017-%m-%d %I:%M:%S'), use_time_s])
                            res_pass[key].append("beg pass %s" % i)
                        else:
                            res_err[key].append("beg err %s" % i)
                        beg_res = ue.get_beg_use_time(key)
                        
                        if None != beg_res:
                            res_beg[key].append([beg_res.strftime('2017-%m-%d %I:%M:%S'), use_time_s])
                            res_pass[key].append("end pass %s" % i)
                        else:
                            res_err[key].append("end err %s" % i)
        print "ue_num %d" % len(self.ues)
        return res, res_err, res_beg, res_pass

class ue_time():
    def __init__(self, lab_list):
        self.lab_list = lab_list
        self.ue_status()

    def get_end_use_time(self, key):
        try :
            res = self.status_list[key][1]
            use = self.use_time(key) 
        except KeyError:
            res = None
        return res

    def get_beg_use_time(self, key):
        try :
            res = self.begin_list[key][1]
            use = self.use_time(key) 
        except KeyError:
            res = None
        return res

    def use_time(self, key):
        try:
            end_time = self.status_list[key][1]
            beg_time = self.begin_list[key][1]
            res = (end_time - beg_time).total_seconds()
            print res
        except KeyError:
            res = -1
        return res

    def ue_status(self):
        self.status_list = {}
        self.begin_list = {}
        stop_key = u"end$|done|Version" 
        error_key = u"error"
        begin_key = u"begin|Version"
        for i in self.lab_list:
            for lab in i :
                if "time" == lab :
                    time = self.change_time(i["time"])
                else:
                    com = i[lab]
                    key = lab
                stop_res = re.findall(stop_key, com)                     
                err_res = re.findall(error_key, com)                     
                begin_res = re.findall(begin_key, com)                     
                            
            if [] != stop_res:
                self.status_list[key] = ["stop",time]
            if [] != err_res:
                self.status_list[key] = ["error",time]
            if [] != begin_res:
                self.begin_list[key] = ["begin",time]

        self.show()

    def change_time(self, time_lab):
        res = datetime.datetime.strptime(time_lab, '%m%d/%H%M%S:%f')
        return res

    def show(self):
        print "*" * 20
        for i in self.status_list:
            print "%s:%s" % (i, str(self.status_list[i]))
        for i in self.begin_list:
            print "%s:%s" % (i, str(self.begin_list[i]))

if __name__=="__main__":
    x = app_log()
    #x.ana_ue("app_host/84913_app.log")
    x.get_host_dir("app_host")
    
    res = x.ana_end_ues()
    print "res***************"
    for i in res[0]:
        print "0%s: num %d" % (i, len(res[0][i]))
        print res[0][i]

    print "res_beg***************" 
    for i in res[2]:
        print "%s: num %d" % (i, len(res[2][i]))
        print res[2][i]
    print "res_err***************"
    for j in res[1]:
        print "%s err %s" % (str(j), str(res[1][j]))
        print "%s err %s" % (str(j), str(res[3][j]))
