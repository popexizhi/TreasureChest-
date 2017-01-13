#-*-coding:utf8-*-
from DygraphData import dygraph_data
import sys, re, time, copy
from Static import static
from ReportTemplet import *
from ReportTempletX import * # templet_data_table use
from ReportMap import report_map
from ReportIfram import *
from AppLog import app_log 
from Map import *
class mon_app():
    def __init__(self):
        self.static = static()
        self.lab = str(time.time())

    def app_throughput(self, fp, REG):
        process_res = []
        for line in  self.get_file(fp):
            res = self.dy.check_line_source(line, reg_str=REG)
            if type(0) == type(res):
                #return [] 
                pass #空行代表无数据
            else:
                self.log(res)
                process_res.append([res])
        return process_res
    
    def get_file(self, fp):
        f = open(fp)
        com = f.readlines()
        f.close()
        return com
    

    def log(self, mes, level="debug"):
        if "debug" == level:
            print "[MonApp] %s" % str(mes)

    def save_log(self, res, new_fp, row_name, key_name=1):
        f =open(new_fp, "w")
        f.write("%s\n" % row_name)
        for i in res:
            if type([]) == type(key_name):
                com = str(i[key_name[0]])
                for j in key_name[1:]:
                    com = "%s,%s" % (com, str(i[j]))
                f.write("%s,%s\n" % (str(i[0]), str(com)))
            else:
                if "all" == key_name:
                    f.write("%s,%s,%s\n" % (str(i[0]), str(i[1]), str(i[2])))
                else:
                    f.write("%s,%s\n" % (str(i[0]), str(i[key_name])))

        f.close()

    def get_csv_app_l2_con(self, fp, csv_fp, fphtml="x.html"):
        res = []
        data_res = []
        for i in self.app_throughput(fp, APP_L2_connection_REG):
            res.append([i[0]["time"]])
        #self.log(res)
        res, data_res = self.static.static_second_num(res)
        self.save_log(res, csv_fp, row_name="time,app_l2_connection")
    
        #static
        res = self.static.statistics_list(data_res)
        quartiles_res = self.static.quartiles(data_res)
        dl = {"Max":res[0], "Min":res[1] , "num": res[2], "avg": res[3], "stdev": res[4]}
        print dl
        self.get_report_html(res, quartiles_res, csv_fp, testtime_str = "每秒可建立 L2 连接数", des ="appserver 每秒可建立 L2 连接数", title="APP_L2_connection", fp=fphtml)

    def get_csv_app_th(self, fp, csv_fp, fphtml="x.html"):
        res = []
        data_res = []
        for i in self.app_throughput(fp, APP_throughput_REG):
            res.append([i[0]["time"], i[0]["Tcp Model Test tcp server send data"]])
            data_res.append(float(i[0]["Tcp Model Test tcp server send data"]))
        self.save_log(res, csv_fp, row_name="time,app throughput(Kbps)")

        #static
        res = self.static.statistics_list(data_res)
        quartiles_res = self.static.quartiles(data_res)
        dl = {"Max(Kbps)":res[0], "Min(Kbps)":res[1] , "num": res[2], "avg": res[3], "stdev": res[4]}
        print dl
        self.get_report_html(res, quartiles_res, csv_fp, testtime_str = "最大 L2 数据收发速率", des = "appserver 最大 L2 数据收发速率", title= "L2 max send data", fp=fphtml)
   

    def save_b_e_one_file(self, b_list, e_list):
        """按b_list,e_list中[0]的顺序合成新的list，
            新list中
                [0]为顺序排列,
                [1]为b_list中[1]的累增数列
                [2]为e_list中[1]的累增数列
        """ 
        res_list = []
        row_line = "time,begin,end"
        res = []
        totle = 0
        b_list.sort()
        print b_list
        for i in b_list:
            totle =  totle + i[1]
            #res.append([i[0], i[1], 0]) #no totle
            res.append([i[0], totle, 0])
        totle = 0
        e_list.sort()
        print e_list
        for j in e_list:
            totle =  totle + j[1]
            #res.append([j[0], 0, j[1]])
            res.append([j[0], 0, totle])

        res.sort()
        old = res[0]#[None, 0, 0]
        old_b = old[1]
        old_n = old[2]
        index = 0
        for u in res[1:]:
            print "u:%s" % str(u)
            if old[0] == u[0]:
                #合并相同时间的统计内容
                old = [old[0], old[1]+u[1], old[2]+u[2]]
                old_b = old[1]
                old_n = old[2]
                #print old
            else:
                res_list.append(old)
                if old_b < u[1]:
                    old_b = u[1] #next
                if old_n < u[2]:
                    old_n = u[2] 
                old = [u[0], old_b, old_n]
                print old
                print old_b
                print old_n
                index = index + 1
        res_list.append(old) #the last one  
        print "A " * 20
        print res
        print "A " * 20
        print "~ ~ "*20
        for t in res_list:
            print t
        print "~ ~ "*20

        return  row_line, res_list

    def save_all_num(self, key_res):
        """将key_res按key分列存入一个list """
        row_line = "time,HandleL2AuthReq_b,HandleL2AuthReq_e,\
        HandleDeviceInfo_b,HandleDeviceInfo_e,\
        DoConfirm_b,DoConfirm_e,\
        PolicyUpdated_b,PolicyUpdated_e"
        res = []
        diff_ = []
        for i in key_res:
            if [] == key_res[i]:
                var = ["9999-12-30 ", -1]
            else:
                if "1HandleL2AuthReq" == i:
                    for j in key_res[i]:
                        res.append([j[0], j[1], j[2], 0, 0, 0, 0, 0, 0])
                if "2HandleDeviceInfoIndication" == i:
                    for j in key_res[i]:
                        res.append([j[0], 0, 0, j[1],j[2], 0, 0, 0, 0])
                if "3EAPServiceWorker::DoConfirmPolicyVersion" == i:
                    for j in key_res[i]:
                        res.append([j[0], 0, 0, 0, 0, j[1], j[2], 0, 0])
                if "4EAPRpcService::OnDevicePolicyUpdated" == i:
                    for j in key_res[i]:
                        res.append([j[0], 0, 0, 0, 0, 0, 0, j[1], j[2]])
        # get min diff_
        res.sort()
        old = res[0]
        res_last = []
        old_1 = old[1:]

        for u in res[1:]:
            print "u:%s" % str(u)
            for j in range(9):
                if old_1[j-1] > u[j]:
                    old[j] = old_1[j-1]
                else:
                    if 0 == j :
                        pass
                    else:
                        old_1[j-1] = old[j]
                             
            if old[0] == u[0]:
                #合并相同时间的统计内容
                old = [old[0], old[1]+u[1], old[2]+u[2], old[3]+u[3], old[4]+u[4], old[5]+u[5], old[6]+u[6], old[7]+u[7], old[8]+u[8]]
                old_1 = old[1:]
            else:
                if 0!= old[0]:
#                    for j in range(9):
#                        if 0 == old[j]:
#                            old[j] = old_1[j-1]
#                        else:
#                            if 0 == j :
#                                pass
#                            else:
#                                old_1[j-1] = old[j]
                    #assert 1 == 0 
                    res_last.append(old)
                old = u
               
        res_last.append(old)
        print "~ ~ "*20
        for t in key_res:
            print t
            print key_res[t]
        print "~ ~ "*20
        for t in res:
            print t
        print "~ ~ "*20
        for t in res_last:
            print t
        print "~ ~ "*20
               
        return row_line, res_last
    
    def save_fp_html(self, key):
        pass

    def get_csv_app_provision(self, app_dir, csv_dir, fphtml):
        res = []
        data_res = []
        #统计数据
        applog = app_log()
        applog.get_host_dir(app_dir)
        res_list = applog.ana_end_ues() 
        key_res = res_list[0]
        key_res_err = res_list[1]
        key_beg_res = res_list[2]
        key_des = {}
        key_res_html = []
        key_app_proxy_num_list = []
        key_all_list = {}
       
        res_html_table = [["id","预期成功个数","真实成功个数","此步骤未结束失败个数","全部失败个数"]] #html中图形表下部的table
        #将provision count 加入为首个图表
        app_provision_count_fphtml = "%s/%s_num_count.html" % (csv_dir, fphtml)
        count_csv_fp = "%s/%s_count.csv" % (csv_dir, fphtml) #真实保存的文件地址 
        count_csv_fp_file = "%s_count.csv" % (fphtml) #html中使用文件地址
        key_res_html.append(["all_count_num", app_provision_count_fphtml])
        
        for key in Key_list:
            res = key_res[key]
            #对res 按每秒内容排序统计
            static_res = self.static.statistics_list_avg(res)
            res = static_res
            print "~" * 20
            print static_res
            if [] == static_res:
                # key 为 空, 做异常处理
                 
                continue
            #assert 1 == 0
            csv_fp = "%s/%s_%s" % (csv_dir, self.lab, key)
            csv_fp_file = "%s_%s" % (self.lab, key) 
            run_time = "%s~%s" % (str(static_res[0][0][0]), str(static_res[0][-1][0])) # report use
            # num per second html
            self.save_log(res[0], csv_fp, row_name="time,num", key_name=1)
            key_res[key] = res[0]
            print res[1]
            res = self.static.statistics_list(res[1])
            quartiles_res = self.static.quartiles(static_res[1])
            dl = {"Max":res[0], "Min":res[1] , "num": res[2], "avg": res[3], "stdev": res[4]}
            print dl
            key_des[key] = dl
            app_proxy_num_list = [key, "%s(个数)" % key, res[1], res[3], res[0]]
            key_app_proxy_num_list.append(app_proxy_num_list)
            app_num_fphtml = "%s/%s_num_%s.html" % (csv_dir, fphtml, key)
            app_proxy_num_html_fp = self.get_report_html(res, quartiles_res, csv_fp_file, testtime_str = key, des = key, title= key, fp=app_num_fphtml)
            key_res_html.append([key, app_proxy_num_html_fp])
            

            res_beg = key_beg_res[key]
            #对res 按每秒内容排序统计
            static_res_beg = self.static.statistics_list_avg(res_beg)
            res_beg = static_res_beg
            print "~" * 20
            print static_res_beg
            if [] == static_res_beg:
                # key 为 空, 做异常处理
                continue
            csv_fp = "%s/%s_%s_b" % (csv_dir, self.lab, key)
            csv_fp_file = "%s_%s_b" % (self.lab, key) 
            run_time = "%s~%s" % (str(static_res[0][0][0]), str(static_res[0][-1][0])) # report use
            
            data_list = self.save_b_e_one_file(static_res_beg[0], static_res[0]) 
            key_all_list[key] = copy.deepcopy(data_list[1])
            if key == "1HandleL2AuthReq":
                totle_num = data_list[1][-1][1] #结束点的count
            
            begin_key = ["%s_num" % key, totle_num, data_list[1][-1][1] , float(data_list[1][-1][1])-float(data_list[1][-1][1]) , float(totle_num) - float(data_list[1][-1][1])]
            res_html_table.append(begin_key) 
            
            if key == "4EAPRpcService::OnDevicePolicyUpdated":
                data_list = self.save_all_num(key_all_list)
                self.save_log(data_list[1], count_csv_fp, data_list[0], key_name=[1,2,3,4,5,6,7,8]) #next 只存一个count 图表
                key_des[key] = dl
                app_proxy_num_list = [key, "%s(beg个数)" % key, res[1], res[3], res[0]]
                key_app_proxy_num_list.append(app_proxy_num_list)
                #title, csvfp, testtime_str, da_table_list, des, fp):
                self.get_report_table_html("all_count_num", count_csv_fp_file, testtime_str = "pp provision all count", da_table_list = res_html_table, des = "app provision all count",  fp=app_provision_count_fphtml)

            # use_time per second html
            use_time_csv_fp = "%s/%s_%s_use_time" % (str(csv_dir), key , self.lab)
            use_time_csv_fp_file = "%s_%s_use_time" % (key , self.lab)
            self.save_log(static_res[0], use_time_csv_fp, row_name="time,avg,max,std", key_name=[2,3,4])
            print static_res[2]
            res = self.static.statistics_list(static_res[2])
            quartiles_res = self.static.quartiles(static_res[2])
            dl = {"Max":res[0], "Min":res[1] , "num": res[2], "avg": res[3], "stdev": res[4]}
            print dl
            use_time_list = [key, "provision(%s use_time per second)(s)" % key, res[1], res[3], res[0]]
            key_app_proxy_num_list.append(use_time_list)
            use_time_html_fp = self.get_report_html(res, quartiles_res, use_time_csv_fp_file, testtime_str = "%s test (use_time per second)" % key, des = "%s test(use_time per second)" % key, title= "%s test(use_time per second)" % key, fp="%s/%s_%s_use_time.html" % (csv_dir, key, fphtml))      
            print "app_proxy_num_html_fp: %s;\nuse_time_html_fp: %s" % (app_proxy_num_html_fp, use_time_html_fp)
            key_res_html.append(["%s_use_time" % key, use_time_html_fp])

            # Percentage of the requests served within a certain time (ms) [0.5，0.66，0.75，0.8，0.90，0.95，0.98，0.99，1]
            pre_list = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.66,0.7,0.75,0.8,0.85,0.90,0.95,0.98,0.99,1]
            percent_res = self.static.percentage_avg(static_res[2], pre_list)
            percent_fp = "%s/%s_%s_percent" % (str(csv_dir), key, self.lab)
            percent_fp_file = "%s_%s_percent" % (key, self.lab)
            self.save_log(percent_res, percent_fp, row_name="percent, use_time(s)", key_name=1)
            dl = [0,0,0,0,0,0,0]
            percent_html_fp = self.get_report_html(res, quartiles_res, percent_fp_file , testtime_str = "provision test[%s]" % str(pre_list), des =     "provision test[%s]" % str(pre_list), title= "provision test[%s]" % str(pre_list), fp="%s/precent_%s_%s.html" % (csv_dir, key, fphtml))
            key_res_html.append(["%s_percent" % key, percent_html_fp])
#        
        #data_list = self.save_all_num(key_all_list)
        #self.save_log(data_list[1], "tt.log", data_list[0], key_name=[1,2,3,4])

        #II app proxy report 
        II_tit = "app provision report"
        II_des = "app provision report"
        II_h4_des = "测试时间: %s;<br>总计访问次数:%s" % (run_time, str(totle_num))
        table_list_list = key_app_proxy_num_list#use_time_list]
        html_des_list = key_res_html
        II_fp = "%s.html" % fphtml 
        print self.output_IIht_report(II_tit, II_des, II_h4_des , table_list_list, html_des_list, II_fp)

    def output_IIht_report(self, html_title, proxy_app_des, proxy_app_h4, dlist, htmlrp_des_list, fp):
       
        return output_html(html_title, proxy_app_des, proxy_app_h4, dlist, htmlrp_des_list, fp)

    def get_report_html(self, res, quartiles_res, csvfp, testtime_str, des, title, fp):
        da_min = res[1]
        da_avg = res[3]
        da_max = res[0]
        da_med = quartiles_res[1]
        da_std = res[4]
        des = des#" 最大 L2 数据收发速率"
        title = title #"L2 max send data"
        return templet_data(title, csvfp, testtime_str, da_min, da_avg, da_max, da_med, da_std, des, fp)
    def get_report_table_html(self, title, csvfp, testtime_str, da_table_list, des, fp):
        """get_report_table_html is save list_list in <table> ,[0] 为table title name """
        return templet_data_table(title, csvfp, testtime_str, da_table_list, des, fp)

    def get_testcase_name(self, dir_log, backup_dir):
        res = self.sh.get_testcase_name(dir_log)
        self.log(res)
        for i in res:
            if "" == i:
                break
            if re.findall(u"app_L2_connection",i):
                self.get_csv_app_l2_con("%s/%s" % (dir_log, i), "%s/%s_%s.csv" % (backup_dir, i, self.lab), "%s_%s.html" % (i, self.lab))
            if re.findall(u"app_l2_max_send_data", i):
                self.get_csv_app_th("%s/%s" % (dir_log, i), "%s/%s_%s.csv" % (backup_dir, i, self.lab), "%s_%s.html" % (i, self.lab))
            if re.findall(u"app_proxy", i):
                self.get_csv_app_proxy("%s/%s" % (dir_log, i), "%s/%s_%s.csv" % (backup_dir, i, self.lab), "%s_%s.html" % (i, self.lab))

            self.sh._com("mv %s/%s %s" % (dir_log, i, backup_dir))
            self.sh.back_test("*%s_%s.html" % (i, self.lab), backup_dir, report_map["ng_dir"])
if __name__=="__main__":
    x = mon_app()

    x.get_csv_app_provision("app_host", csv_dir= "htmltest", fphtml="app_ue%s" % str(time.time()))

    #x.get_testcase_name(report_map["log_dir"], report_map["backup_dir"])

