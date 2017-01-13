#-*-coding:utf8-*-
from DygraphData import dygraph_data
import sys, re, time
from RegMap import *
from Static import static
from ReportTemplet import *
from ReportMap import report_map
from ShellCon import sh_control
from ReportIfram import *

class mon_app():
    def __init__(self):
        self.dy = dygraph_data("None.db")
        self.static = static()
        self.sh = sh_control()
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
    
    def get_csv_app_proxy(self, fp, csv_fp, fphtml="x.html"):
        res = []
        data_res = []
        #统计数据
        for i in self.app_throughput(fp, APP_proxy):
            self.log(i)
            res.append([i[0]["time"], i[0]["url_use_time(us)"]])
            data_res.append(float(i[0]["url_use_time(us)"]))
        print res
        totle_num = len(data_res)
        #对res 按每秒内容排序统计
        static_res = self.static.statistics_list_avg(res)
        res = static_res
        run_time = "%s~%s" % (str(static_res[0][0][0]), str(static_res[0][-1][0])) # report use
        # num per second html
        self.save_log(res[0], csv_fp, row_name="time,num", key_name=1)
        print res[1]
        res = self.static.statistics_list(res[1])
        quartiles_res = self.static.quartiles(static_res[1])
        dl = {"Max":res[0], "Min":res[1] , "num": res[2], "avg": res[3], "stdev": res[4]}
        print dl
        app_proxy_num_list = [1, "proxy test(num per second)(个数)", res[1], res[3], res[0]]
        app_num_fphtml = "app_num_%s" % fphtml
        app_proxy_num_html_fp = self.get_report_html(res, quartiles_res, csv_fp, testtime_str = "proxy test ", des = "proxy test", title= "proxy test", fp=app_num_fphtml)

        # use_time per second html
        use_time_csv_fp = "%s_use_time" % str(csv_fp)
        self.save_log(static_res[0], use_time_csv_fp, row_name="time,avg(us),max(us),std(us)", key_name=[2,3,4])
        print static_res[2]
        res = self.static.statistics_list(static_res[2])
        quartiles_res = self.static.quartiles(static_res[2])
        dl = {"Max(us)":res[0], "Min(us)":res[1] , "num": res[2], "avg": res[3], "stdev": res[4]}
        print dl
        use_time_list = [2, "proxy test(use_time per second)(us)", res[1], res[3], res[0]]
        use_time_html_fp = self.get_report_html(res, quartiles_res, use_time_csv_fp, testtime_str = "proxy test (use_time per second)", des = "proxy test(use_time per second)", title= "proxy test(use_time per second)", fp="proxy_test_use_time_%s" % fphtml)
       
        print "app_proxy_num_html_fp: %s;\nuse_time_html_fp: %s" % (app_proxy_num_html_fp, use_time_html_fp)

        # Percentage of the requests served within a certain time (ms) [0.5，0.66，0.75，0.8，0.90，0.95，0.98，0.99，1]
        #pre_list = [0.5,0.66,0.75,0.8,0.90,0.95,0.98,0.99,1]
        pre_list = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.66,0.7,0.75,0.8,0.85,0.90,0.95,0.98,0.99,1]
        percent_res = self.static.percentage_avg(data_res, pre_list)
        percent_fp = "%s_percent" % str(csv_fp) 
        self.save_log(percent_res, percent_fp, row_name="percent, avg(us)", key_name=1)
        dl = [0,0,0,0,0,0,0]
        percent_html_fp = self.get_report_html(res, quartiles_res, percent_fp , testtime_str = "proxy test[%s]" % str(pre_list), des =     "proxy test[%s]" % str(pre_list), title= "proxy test[%s]" % str(pre_list), fp="precent_%s" % fphtml)
        
        #II app proxy report 
        II_tit = "app proxy report"
        II_des = "app proxy report"
        II_h4_des = "测试时间: %s;<br>总计访问次数:%s" % (run_time, str(totle_num))
        table_list_list = [app_proxy_num_list, use_time_list]
        html_des_list = [["num per second html", app_proxy_num_html_fp], ["use_time per second html", use_time_html_fp], ["Percentage of the requests", percent_html_fp]]
        II_fp = fphtml 
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
    x.get_testcase_name(report_map["log_dir"], report_map["backup_dir"])

