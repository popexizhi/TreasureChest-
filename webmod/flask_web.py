# -*- coding:utf8 -*-
from flask import Flask, request, jsonify
import threading, time, json, re
from dbget import db_mod 
import copy

app = Flask(__name__)

@app.route('/cluter_list/<list_name>', methods=['GET', 'POST'])
def cluter_list(list_name):
    content = request.json
    print "%s,%s" % (str(list_name), str(content))
    report_test = ""
    report_test = index_html()
    #return jsonify({'res': 'ok', 'report': report_test })
    return report_test

@app.route('/cluter_test/<report_name>', methods=['GET', 'POST'])
def cluter_test(report_name):
    content = request.json
    print "%s,%s" % (str(report_name), str(content))
    report_test = ""
    report_test = job_doing(report_name, report_test)
    #return jsonify({'res': 'ok', 'report': report_test })
    return jsonify(report_test)


def job_doing(report_name, report_test):
    assert report_name
    x = get_report()
    #th1 = threading.Thread(target=x.get_report_data, args=(report_name, report_test) )
    #th1.start()
    #return x.get_report_data(report_name, report_test)
    return x.get_report_data_json(report_name, report_test)

def index_html():
    x = get_report()
    return x.get_report_index() 


class get_report():
    def __init__(self):
        self.modfile="webmod/cluster_test_report_template.html"
        self.index_mod="webmod/index.html"
        self.db = db_mod("load_test", "192.168.1.41", "root", "password")

    def log(self, str_):
        print "[get_report]%s" % str(str_)

    def get_report_data(self, report_name, report_data):
        report_data=self.db.get_report_data(report_name)
        self.log(report_data)
        #替换html模板数据
        return self.get_mod(self.modfile, report_data)
        #return report_data
    
    def get_report_data_json(self, report_name, report_data):
        report_data=self.db.get_report_data(report_name)
        self.log(report_data)
        return self.get_json(report_data) 
    
    def get_report_index(self):
        index_list = self.db.get_report_names()
        self.log(index_list)
        #return index_list
        #替换html模板数据
        return self.get_index(self.index_mod, index_list)
    
    def get_json(self, data):
        res_json = []
        res = {}
        for line in data:
            #res[line[0]]=str(line[1])
            res["key"] = str(line[0])
            res["value"] = str(line[1])
            res_json= res_json + [copy.deepcopy(res)]
        self.log(str(res_json))
        return res_json

    def get_index(self, modfile, report_data):
        f=open(modfile)
        modstr = "" 
        for line in f.readlines():
            modstr = "%s\n%s" % (str(modstr), str(line))
        f.close()
        res = str(modstr)
        report_list="'%s'" % str(report_data[0][0])
        for key in report_data[1:]:
            self.log(key[0])
            report_list = """%s,'%s'""" % (report_list, str(key[0]))
            self.log(report_list)
        link2 = re.compile("@cluster_list_arr")
        res = re.sub(link2, report_list, res)
        return res

    def get_mod(self, modfile, report_data):
        f=open(modfile)
        modstr = "" 
        for line in f.readlines():
            modstr = "%s\n%s" % (str(modstr), str(line))
        f.close()
        res = str(modstr)
        self.log(len(report_data))
        for key in report_data:
            self.log(key[0])
            self.log(key[1])
            link2 = re.compile(str(key[0]))
            res = re.sub(link2, str(key[1]), res)
        return res

if __name__=='__main__':
    app.run(host="192.168.1.207", port=8999, debug=True)
