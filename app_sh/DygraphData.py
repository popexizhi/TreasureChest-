#!/bin/python2.7
#-*- coding:utf8 -*-
#收集 dygraph 的csv格式数据使用
import re, os, sys
class dygraph_data():
    def __init__(self):
        pass
    def check_line_source(self, source_str, reg_str, is_change_date=1):
        res = {}
        for reg_key in reg_str:
            value = re.findall(reg_str[reg_key], source_str)
            self.log("value %s" % str(value))
            if 0 == len(value):
                return 0
            if "time" == reg_key and 1 == is_change_date :
                res[reg_key] = self.chang_date(value[0])
            else:
                res[reg_key] = value[0]
        #return [res["time"], res["snd_data_indication_cnt"], res["rcv_data_indication_cnt"]]
        return res

    def get_file(self, fp):
        f = open(fp)
        com = f.readlines()
        f.close()
        return com
    
    def get_dir_file(self, dir_p, file_format):
        res = []
        for i in os.listdir(dir_p):
            if re.findall(file_format, i):
                res.append("%s/%s" % (dir_p, i))

        return res

    def process_file(self, fp):
        process_res = []
        for line in  self.get_file(fp):
            res = self.check_line_source(line, reg_str=REGMAP)
            if type(0) == type(res):
                return [] #空行代表无数据
            self.log(res)
            process_res.append([res])
        return process_res

    def process_db(self, fp):
        res = self.process_file(fp)
        self.db.insert_more(res,"fgw_relay","fgw")


    def chang_date(self, str_date, reg_str=u"\d\d"):
        self.year = "2016"
        self.log("str_date %s; reg_str %s" % (str(str_date), str(reg_str)))
        res = re.findall(reg_str, str_date)
        assert 5 == len(res)
        res = "%s/%s/%s %s:%s:%s" % (self.year, res[0], res[1], res[2], res[3], res[4])
        return res
    
    def log(self, mes, level="debug"):
        if "debug" == level:
            print "[dygraph_data] %s" % str(mes)

    def get_db_last_data(self, table_name):
        last_line = self.db.get_last_data(table_name)
        if 0 == len(last_line):
            last_line = ["0"]
        self.log(last_line[0])
        return last_line[0]
    
    def file_backup(self, fp, backup_dir):
        str_ = "mv %s %s" % (fp, backup_dir)
        self.sh._com(str_)

    def start_doing(self, logdir, table_name, ng_csv_file="fgw_relay.csv"):
        log_list = self.get_dir_file(logdir, file_format=".log")
        for i in log_list:
            last_line_db_time = self.get_db_last_data(table_name)
            res = self.process_file(i)
            index = 0
            for j in res:
                index = index + 1
                self.log(j)
                self.log(j[0]["time"])
                self.log(last_line_db_time[0])
                if j[0]["time"] == last_line_db_time[0]:
                    #当前index:-1为要插入的位置
                    self.db.insert_more(res[index:-1],table_name,table_name)
                    self.file_backup(i)
                    break
            if index == len(res):#整个文件为新内容
                self.db.insert_more(res, table_name, table_name)
                self.file_backup(i)
                
        
        res = self.db.select_all(table_name)       
        self.save_log(res, ng_csv_file)
        return res
    def save_log(self, res, new_fp, row_name):
        f =open(new_fp, "w")
        f.write("%s\n" % row_name)
        for i in res:
            f.write("%s,%s,%s\n" % (str(i[0]), str(i[1]), str(i[2])))

        f.close()
        
        backup_str = "scp %s slim@192.168.1.216:%s" % (new_fp, moniter_use["ng_dir"])
        self.sh._com(backup_str) 
if __name__=="__main__":
    try:
        argv = sys.argv[1]
    except IndexError:
        argv = "fgw"

    db_key =  "db_%s" % str(argv)   
    x = dygraph_data()
