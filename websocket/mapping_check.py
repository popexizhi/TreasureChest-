#-*- coding:utf8 -*-
import time
cascade_node = "/api/web/cascade/nodeTrend"
cascade_threatNameList_url = "/api/web/cascade/threatNameList"
cascade_incidentList_url = "/api/web/cascade/incidentList"
cascade_homeList_url = "/api/web/cascade/hostList"
ip = "192.168.103.81"
data_24 = {"time_range":"twenty_four_hours"}
data_7D = {"time_range":"seven_days"}
data_30D = {"time_range":"thirty_days"}
#data_list = [data_24]
check_time_list = [8, 24, 48, 72]
#check_time_list = [1]
#data_list = [data_24, data_7D]
data_list = [data_24, data_7D, data_30D]
cookie = "auth=eyJpZCI6IjJlZTU1ZGVjY2NjNzRlOTk4NjhmNTcyYzJkZmU5OTJjIiwibmFtZSI6InRkcCIsInJvbGUiOiJzdXBlcl9hZG1pbiIsInN0YXR1cyI6MCwic2lnbiI6IjY3MDkyMDEyYWQyMmVjYmY2ZGU3ZTJiOTY1Nzc5YTBmIiwidG9rZW4iOiI0MjRjZDM1OWQwYjA0NjdjOWIzM2U2MWY4YjMzMTkyMSIsImxvZ2luX3RpbWUiOiIyMDIwLTA3LTA3IDEwOjA1OjE0IiwidmFsaWRfdGlsbF9kZXNjIjoi6ZW/5pyfIiwicHdfdGltZV9kZXNjIjoiIn0=; JSESSIONID=C9D9FB81CAD52ADAE4D92BB54E76DB39; client_id=" 

node_name_list = [
 "193.1.10.254","193.1.11.254","193.1.12.254","193.1.13.254","193.1.14.254","193.1.15.254","193.1.16.254","193.1.17.254","193.1.18.254","193.1.19.254","193.1.110.254","193.1.111.254","193.1.112.254","193.1.113.254","193.1.114.254","193.1.115.254","193.1.116.254","193.1.117.254","193.1.118.254","193.1.119.254","193.1.120.254","193.1.121.254","193.1.122.254","193.1.123.254","193.1.124.254","193.1.125.254","193.1.126.254","193.1.127.254","193.1.128.254","193.1.129.254","193.1.130.254","193.1.131.254","193.1.132.254","193.1.133.254","193.1.134.254","193.1.135.254","193.1.136.254","193.1.137.254","193.1.138.254","193.1.139.254","193.1.140.254","193.1.141.254","193.1.142.254","193.1.143.254","193.1.144.254","193.1.145.254","193.1.146.254","193.1.147.254","193.1.148.254","193.1.149.254",]
device_id_list = [
"20CCDACF095494004E757C36DBDCA40","20CCDACF095494004E757C36DBDCA41","20CCDACF095494004E757C36DBDCA42","20CCDACF095494004E757C36DBDCA43","20CCDACF095494004E757C36DBDCA44","20CCDACF095494004E757C36DBDCA45","20CCDACF095494004E757C36DBDCA46","20CCDACF095494004E757C36DBDCA47","20CCDACF095494004E757C36DBDCA48","20CCDACF095494004E757C36DBDCA49","20CCDACF095494004E757C36DBDCA410","20CCDACF095494004E757C36DBDCA411","20CCDACF095494004E757C36DBDCA412","20CCDACF095494004E757C36DBDCA413","20CCDACF095494004E757C36DBDCA414","20CCDACF095494004E757C36DBDCA415","20CCDACF095494004E757C36DBDCA416","20CCDACF095494004E757C36DBDCA417","20CCDACF095494004E757C36DBDCA418","20CCDACF095494004E757C36DBDCA419","20CCDACF095494004E757C36DBDCA420","20CCDACF095494004E757C36DBDCA421","20CCDACF095494004E757C36DBDCA422","20CCDACF095494004E757C36DBDCA423","20CCDACF095494004E757C36DBDCA424","20CCDACF095494004E757C36DBDCA425","20CCDACF095494004E757C36DBDCA426","20CCDACF095494004E757C36DBDCA427","20CCDACF095494004E757C36DBDCA428","20CCDACF095494004E757C36DBDCA429","20CCDACF095494004E757C36DBDCA430","20CCDACF095494004E757C36DBDCA431","20CCDACF095494004E757C36DBDCA432","20CCDACF095494004E757C36DBDCA433","20CCDACF095494004E757C36DBDCA434","20CCDACF095494004E757C36DBDCA435","20CCDACF095494004E757C36DBDCA436","20CCDACF095494004E757C36DBDCA437","20CCDACF095494004E757C36DBDCA438","20CCDACF095494004E757C36DBDCA439","20CCDACF095494004E757C36DBDCA440","20CCDACF095494004E757C36DBDCA441","20CCDACF095494004E757C36DBDCA442","20CCDACF095494004E757C36DBDCA443","20CCDACF095494004E757C36DBDCA444","20CCDACF095494004E757C36DBDCA445","20CCDACF095494004E757C36DBDCA446","20CCDACF095494004E757C36DBDCA447","20CCDACF095494004E757C36DBDCA448","20CCDACF095494004E757C36DBDCA449"]
data_24_alter_trend = {
            "critical_count": 6*3, # alert_count*3
            "high_count": 3*3,
            "low_count": 139*3,
            "medium_count": 14*3,
            "suspicious_count": 0*3,
        }   
data_7D_alter_trend = {
            "critical_count": 6*6*4, # alert_count*6(次/h)*4h
            "high_count": 3*6*4,
            "low_count": 139*6*4,
            "medium_count": 14*6*4,
            "suspicious_count": 0*6*4,
        }   
data_30D_alter_trend = {
            "critical_count": 6*6*24, # alert_count*6(次/h)*24h
            "high_count": 3*6*24,
            "low_count": 139*6*24,
            "medium_count": 14*6*24,
            "suspicious_count": 0*6*24,
        }   
node_alter_trend = [data_24_alter_trend ,data_7D_alter_trend, data_30D_alter_trend]

data_24_flow_trend = {
            "value": 102400*3, # alert_count*3
        }   
data_7D_flow_trend = {
            "value": 102400*6*4, # alert_count*6(次/h)*4h
        }   
data_30D_flow_trend = {
            "value": 102400*6*24, # alert_count*6(次/h)*24h
        }   
node_flow_trend = [data_24_flow_trend ,data_7D_flow_trend, data_30D_flow_trend]

threat_name_list = [
"海莲花团伙".decode('utf-8'),
"PowerShell远程登录尝试".decode('utf-8'), 
"扫描黑客Webshell后门(base64传输)".decode('utf-8'), 
"端口扫描".decode('utf-8')]

####-------------------威胁事件--------------------------------
cascade_threatNameList = {"condition":{"time_from":1594195200,"time_to":1594281600,"direction":[],"device_id":["20CCDACF095494004E757C36DBDCA41"],"severity":[],"result":"","fuzzy":{"fieldlist":["threat.name"],"keyword":""}},"page":{"cur_page":1,"page_size":20}}

def get_threatNameList_data(stop_time, check_time, device_id):
    time_to = stop_time
    time_from = stop_time - check_time * 3600 #转换为小时

    cascade_threatName_mode_condition_res = {
        "in":{
             "condition" : {"condition":{"time_from": time_from,"time_to":time_to,"direction":["in"],"device_id":[device_id],"severity":[],"result":"","fuzzy":{"fieldlist":["threat.name"],"keyword":""}},"page":{"cur_page":1,"page_size":20}},
            "res":{
                "AXK8c4gWNIM4VuAx2LEU":{"alert_count": 14*6*check_time, "max_severity": 2},
            "TXK8rbK38YTKEr2p5sAY":{"alert_count": 139*6*check_time, "max_severity": 1},
        },},
        "lateral":{ # 内网渗透
            "condition" : {"condition":{"time_from": time_from,"time_to":time_to,"direction":["lateral"],"device_id":[device_id],"severity":[],"result":"","fuzzy":{"fieldlist":["threat.name"],"keyword":""}},"page":{"cur_page":1,"page_size":20}},
            "res":{
            "AXK8dWMcNIM4VuAx2La5":{"alert_count": 3*6*check_time, "max_severity": 3},
        },},
        "out":{ #失陷破坏
            "condition" : {"condition":{"time_from": time_from,"time_to":time_to,"direction":["out"],"device_id":[device_id],"severity":[],"result":"","fuzzy":{"fieldlist":["threat.name"],"keyword":""}},"page":{"cur_page":1,"page_size":20}},
            "res":{
            "AXK8dWMdNIM4VuAx2Lgf":{"alert_count": 6*6*check_time, "max_severity": 4},
        },},
    }
    return cascade_threatName_mode_condition_res 

def get_incidentList_data(stop_time, check_time, device_id):
    time_to = stop_time
    time_from = stop_time - check_time * 3600 #转换为秒
    cascade_incidentList_res = {
        "46e702b14138c70eb08b3ab7c333f4d8-1592303160":{
            "condition":   {"condition":{"time_from": time_from,"time_to": time_to,"is_target_attack":"","phase":[],"result":[],"device_id":[device_id],"fuzzy":{"fieldlist":["attacker_ip","host_ip","attack_name","attack_tool","incident_id"],"keyword": "46e702b14138c70eb08b3ab7c333f4d8-1592303160" }},"page":{"cur_page":1,"page_size":20,"sort":[{"sort_by":"attack_result","sort_order":"desc"},{"sort_by":"severity","sort_order":"desc"},{"sort_by":"last_time","sort_order":"desc"}]}},
            "res": {"page.total_num": 6 * check_time },
        },
        "2a622fbbd8f4e4245ad87c45d2cc191b-1587702077":{
            "condition":   {"condition":{"time_from": time_from,"time_to": time_to,"is_target_attack":"","phase":[],"result":[],"device_id":[device_id],"fuzzy":{"fieldlist":["attacker_ip","host_ip","attack_name","attack_tool","incident_id"],"keyword":  "2a622fbbd8f4e4245ad87c45d2cc191b-1587702077"}},"page":{"cur_page":1,"page_size":20,"sort":[{"sort_by":"attack_result","sort_order":"desc"},{"sort_by":"severity","sort_order":"desc"},{"sort_by":"last_time","sort_order":"desc"}]}},
            "res": {"page.total_num": 6 * check_time },
        },
    }
    return cascade_incidentList_res

def get_homeList_data(stop_time, check_time, device_id):
    time_to = stop_time
    time_from = stop_time - check_time * 3600 #转换为秒
    cascade_homeList_res = {
        "simple_device":{
           "condition":{"condition":{"time_from":time_from,"time_to":time_to,"device_id":[device_id],"direction":[],"severity":[],"machine_type":[],"fuzzy":{"fieldlist":["threat.name","external_ip","machine","assets.name","data","machine_name"],"keyword":""},"result":""},"page":{"cur_page":1,"page_size":20,"sort":[]}},
           "res":{
           "10.10.221.9": 
                {"threat_tags.[].name":["海莲花团伙".decode('utf-8'),
                                "PowerShell远程登录尝试".decode('utf-8') ]
                },
           "192.168.100.171":
                {"threat_tags.[].name":["扫描黑客Webshell后门(base64传输)".decode('utf-8'),
                                        "端口扫描".decode('utf-8')]
                },
           },
    },} 
    return cascade_homeList_res 

if __name__=="__main__":
    res = get_threatNameList_data(int(time.time()), 8, "aaaa")
    print(res)
    res = get_incidentList_data(int(time.time()), 8 , "bbbb")
    print(res)
    res = get_homeList_data(int(time.time()), 8 , "cbbbb")
    print(res)
