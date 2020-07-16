#-*-coding:utf8-*-
import time,datetime
cur_time = int(time.time())
def get_new_time():
    cur_time = int(time.time())
    return cur_time

def get_second_time(sec):
    t = time.localtime(int(sec))
    r = time.strftime("%Y-%m-%d %H:%M:%S", t)
    return r


def get_data(device_id_n, cur_time, node_name, alert_list_cur):
    alert_list = alert_list_cur
    data_mode ={
        "action": "sum_data",
        "data": {
            "nodeInfo": {
                "version": "3.1.15",                               
                "flow": 102400,                                          # 时间段内的处理量
                "device_id": device_id_n,    # 设备ID，（每个设备必须不同）
                "node_name": node_name,
                "start_time":cur_time ,                           # 数据开始时间，最好以10分钟整开始
                "end_time": cur_time+120 ,
                "ioc_version": "20200616181115",
                "rule_version": "20200605133245",
                "module_version": "20200615172909",
                "ioc_update_time": 1592302974,
                "flow_count": 1,                                    # 已接入流量路数
                "syslog_count": 1                                   # 已接入syslog路数
            },
            "alertList": [                                          # 告警汇总列表
                {
                    #"id": "%sALL1" % str(alert_list),                   # 这个必须不同
                    #"id": "TXK8rbK38Y%s" % str(alert_list),                   # 这个必须不同
                    "id": "TXK8rbK38YTKEr2p5sAY",                   # 这个必须不同
                    "time": cur_time ,
                    "direction": "in",
                    "machine": "192.168.100.171",
                    "attacker": "6.160.247.70",
                    "victim": "192.168.100.171",
                    "data": "192.168.100.171",
                    "net": {
                        "proto": "TCP",
                        "type": "flow",
                        "http": {
                             
                        },
                       "src_ip": "6.160.247.70",
                        "src_port": 34048,
                        "real_src_ip": "6.160.247.70",
                        "dest_ip": "192.168.100.171",
                        "dest_port": 80
                    },
                    "threat": {
                        "name": "端口扫描",
                        "suuid": "S2018040007",
                        "msg": "使用ScanPort/Nmap -A进行端口扫描",
                        "level": "attack",
                        "result": "unknown",
                        "severity": 1,
                        "phase": "recon",
                        "type": "recon",
                        "confidence": 60,
                        "status": 0,
                        "module": "autocc",
                        "tag": [
                            "扫描"
                        ],
                        "is_apt": 0,
                        "is_connected": 0,
                        "type_desc": "侦察",
                        "severity_desc": "低",
                        "status_desc": "未处理"
                    },
                    "assets": {
                        "id": 80,
                        "ip": "192.168.0.0/16",
                        "name": "",
                        "section": "终端",
                        "location": "",
                        "level": 0,
                        "ext": "",
                        "mac": "",
                        "status": 1,
                        "source": "manual",
                        "sub_type": ""
                    },
                    "behave_uuid": "unix-socket-1682749366292407",
                    "input_type": "unix_socket",
                    "incident_id": "46e702b14138c70eb08b3ab7c333f4d8-1592303160",
                    "machine_name": "",
                    "machine_port": "80",
                    "external_ip": "6.160.247.70",
                    "external_port": "34048",
                    "data_type": "ip",
                    "event_type": "net",
                    "behave_source": "unix_socket-unix_socket_input-127.0.0.1",
                    "geo_data": {
                        "location": "中国-江苏-常州",
                        "Country": "中国",
                        "Province": "江苏",
                        "City": "常州",
                        "Org": "",
                        "Isp": "电信",
                        "Latitude": "31",
                        "Longitude": "119",
                        "TimeZone": "Asia/Shanghai",
                        "UTC": "UTC+8",
                        "ChinaCode": "320400",
                        "PhoneCode": "86",
                        "ISO2": "CN",
                        "Continent": "AP"
                    },
                    "is_black_ip": False,
                    "dest_assets": {
                        "id": 0,
                        "ip": "6.160.247.70",
                        "name": "",
                        "section": "",
                        "location": "",
                        "level": 0,
                        "ext": "",
                        "mac": "",
                        "status": 0,
                        "source": "",
                        "sub_type": ""
                    },
                    "assets_machine": "__192.168.100.171",
                    "dest_assets_machine": "__6.160.247.70",
                    "alert_count": 139,
                    "max_severity": 1,
                    "last_occ_time": cur_time+290,
                    "first_occ_time": cur_time,
                    "device_id": device_id_n,
                    "node_name":node_name, 
                    "last_occ_time_desc":get_second_time(cur_time+290) ,
                    "first_occ_time_desc":get_second_time(cur_time) ,
                    "threat_name": "端口扫描",
                    "time_desc":get_second_time(cur_time) ,
                    "direction_desc": "外部攻击",
                    "asset_name": "",
                    "geo_str": "中国-江苏-常州",
                    "is_server": False
                },

          {
          "id": "AXK8dWMcNIM4VuAx2La5",
          "time":cur_time, 
          "direction": "lateral",
          "machine": "10.10.221.9",
          "attacker": "10.10.221.9",
          "victim": "10.10.51.2",
          "data": "192.168.100.116/wsman",
          "net": {
            "proto": "TCP",
            "type": "http",
            "http": {
              "method": "POST",
              "protocol": "HTTP/1.1",
              "status": 401,
              "url": "/wsman?PSVersion=5.1.17134.228",
              "reqs_host": "192.168.100.116",
              "reqs_user_agent": "Microsoft WinRM Client",
              "reqs_content_length": 0,
              "reqs_line": "POST /wsman?PSVersion=5.1.17134.228 HTTP/1.1",
              "reqs_header": "Connection: Keep-Alive\r\nContent-Type: application/soap+xml;charset=UTF-8\r\nAuthorization: Negotiate TlRMTVNTUAABAAAAt4II4gAAAAAAAAAAAAAAAAAAAAAKAO5CAAAADw==\r\nUser-Agent: Microsoft WinRM Client\r\nContent-Length: 0\r\nHost: 192.168.100.116:5985\r\n\r\n",
              "resp_content_length": 0,
              "resp_line": "HTTP/1.1 401 ",
              "resp_header": "WWW-Authenticate: Negotiate TlRMTVNTUAACAAAADAAMADgAAAA1goribAZs2ACjQPQAAAAAAAAAAFAAUABEAAAABgGxHQAAAA9UAEkAUAAtAFAAQwACAAwAVABJAFAALQBQAEMAAQAMAFQASQBQAC0AUABDAAQADAB0AGkAcAAtAFAAQwADAAwAdABpAHAALQBQAEMABwAIAPHT6o37OdQBAAAAAA==\r\nServer: Microsoft-HTTPAPI/2.0\r\nDate: Wed, 22 Aug 2018 09:36:07 GMT\r\nContent-Length: 0\r\n\r\n"
            },
            "src_ip": "10.10.221.9",
            "src_port": 59917,
            "real_src_ip": "10.10.221.9",
            "dest_ip": "10.10.51.2",
            "dest_port": 5985
          },
          "threat": {
            "name": "PowerShell远程登录尝试",
            "suuid": "S2018072700",
            "msg": "检测到内网通过PowerShell（http）进行远程登陆尝试（set）",
            "level": "attack",
            "result": "failed",
            "severity": 3,
            "phase": "post_exploit",
            "type": "infil",
            "confidence": 60,
            "status": 0,
            "module": "autocc",
            "payload": "UE9TVCAvd3NtYW4/UFNWZXJzaW9uPTUuMS4xNzEzNC4yMjggSFRUUC8xLjENCkNvbm5lY3Rpb246IEtlZXAtQWxpdmUNCkNvbnRlbnQtVHlwZTogYXBwbGljYXRpb24vc29hcCt4bWw7Y2hhcnNldD1VVEYtOA0KQXV0aG9yaXphdGlvbjogTmVnb3RpYXRlIFRsUk1UVk5UVUFBQkFBQUF0NElJNGdBQUFBQUFBQUFBQUFBQUFBQUFBQUFLQU81Q0FBQUFEdz09DQpVc2VyLUFnZW50OiBNaWNyb3NvZnQgV2luUk0gQ2xpZW50DQpDb250ZW50LUxlbmd0aDogMA0KSG9zdDogMTkyLjE2OC4xMDAuMTE2OjU5ODUNCg0K",
            "tag": [
              "powershell"
            ],
            "is_apt": 0,
            "is_connected": 0,
            "status_desc": "未处理",
            "type_desc": "渗透",
            "severity_desc": "高"
          },
          "assets": {
            "id": 82,
            "ip": "10.0.0.0/8",
            "name": "",
            "section": "终端",
            "location": "",
            "level": 0,
            "ext": "",
            "mac": "",
            "status": 1,
            "source": "manual",
            "sub_type": ""
          },
          "behave_uuid": "unix-socket-1683732687447618",
          "input_type": "unix_socket",
          "machine_name": "",
          "machine_port": "59917",
          "external_ip": "10.10.51.2",
          "external_port": "5985",
          "data_type": "url",
          "event_type": "net",
          "behave_source": "unix_socket-unix_socket_input-127.0.0.1",
          "geo_data": {
            "location": "局域网-局域网",
            "Country": "局域网",
            "Province": "局域网",
            "City": "",
            "Org": "",
            "Isp": "",
            "Latitude": "0",
            "Longitude": "0",
            "TimeZone": "",
            "UTC": "",
            "ChinaCode": "",
            "PhoneCode": "",
            "ISO2": "",
            "Continent": ""
          },
          "is_black_ip": False,
          "dest_assets": {
            "id": 82,
            "ip": "10.0.0.0/8",
            "name": "",
            "section": "终端",
            "location": "",
            "level": 0,
            "ext": "",
            "mac": "",
            "status": 1,
            "source": "manual",
            "sub_type": ""
          },
          "assets_machine": "__10.10.221.9",
          "dest_assets_machine": "__10.10.51.2",
          "alert_count": 3,
          "max_severity": 3,
          "last_occ_time":cur_time+290,
          "first_occ_time": cur_time,
          "device_id": device_id_n, 
          "node_name": node_name,
          "src_ip": "127.0.0.1",
          "receive_time": cur_time+290,
          "first_occ_time_desc": get_second_time(cur_time) ,
          "threat_name": "PowerShell远程登录尝试",
          "last_occ_time_desc": get_second_time(cur_time+290),
          "asset_name": "",
          "geo_str": "局域网-局域网",
          "time_desc": get_second_time(cur_time+290),
          "direction_desc": "内网渗透",
          "is_server": False
          },
        {
          "id": "AXK8dWMdNIM4VuAx2Lgf",
          "time": cur_time ,
          "direction": "out",
          "machine": "10.10.221.9",
          "attacker": "",
          "victim": "10.10.221.9",
          "data": "ns1.clearddns.com",
          "net": {
            "proto": "UDP",
            "type": "dns",
            "http": {},
            "dns": {
              "type": "query",
              "id": 17658,
              "rrname": "ns1.clearddns.com",
              "rrtype": "A",
              "ttl": 0,
              "answer": False
            },
            "src_ip": "10.10.221.9",
            "src_port": 49975,
            "real_src_ip": "10.10.221.9",
            "dest_ip": "192.168.221.2",
            "dest_port": 53
          },
          "threat": {
            "name": "海莲花团伙",
            "suuid": "Te9ba06935ad98e4",
            "level": "attack",
            "result": "success",
            "severity": 4,
            "phase": "control",
            "type": "c2",
            "confidence": 85,
            "ioc": "clearddns.com",
            "status": 0,
            "module": "t_ioc",
            "tag": [
              "海莲花团伙"
            ],
            "is_apt": 1,
            "ioc_type": "domain",
            "source_type": "3",
            "basic_tag": "apt",
            "is_connected": 0,
            "status_desc": "未处理",
            "type_desc": "远控",
            "severity_desc": "严重"
          },
          "assets": {
            "id": 82,
            "ip": "10.0.0.0/8",
            "name": "",
            "section": "终端",
            "location": "",
            "level": 0,
            "ext": "",
            "mac": "",
            "status": 1,
            "source": "manual",
            "sub_type": ""
          },
          "behave_uuid": "unix-socket-1958425910887943",
          "input_type": "unix_socket",
          "machine_name": "",
          "machine_port": "49975",
          "external_ip": "167.114.44.156",
          "data_type": "domain",
          "event_type": "net",
          "behave_source": "unix_socket-unix_socket_input-127.0.0.1",
          "geo_data": {
            "location": "未知-未知-未知",
            "Country": "未知",
            "Province": "未知",
            "City": "未知",
            "Org": "",
            "Isp": "",
            "Latitude": "",
            "Longitude": "",
            "TimeZone": "",
            "UTC": "",
            "ChinaCode": "",
            "PhoneCode": "",
            "ISO2": "",
            "Continent": ""
          },
          "is_black_ip": False,
          "dest_assets": {
            "id": 80,
            "ip": "192.168.0.0/16",
            "name": "",
            "section": "终端",
            "location": "",
            "level": 0,
            "ext": "",
            "mac": "",
            "status": 1,
            "source": "manual",
            "sub_type": ""
          },
          "assets_machine": "__10.10.221.9",
          "dest_assets_machine": "__192.168.221.2",
          "alert_count": 6,
          "max_severity": 4,
          "last_occ_time": cur_time+290,
          "first_occ_time": cur_time,
          "device_id": device_id_n,
          "node_name":node_name, 
          "src_ip": "127.0.0.1",
          "receive_time": cur_time+290,
          "first_occ_time_desc": get_second_time(cur_time) ,
          "threat_name": "海莲花团伙",
          "last_occ_time_desc": get_second_time(cur_time+290),
          "asset_name": "",
          "geo_str": "未知-未知-未知",
          "time_desc": get_second_time(cur_time+290),
          "direction_desc": "失陷破坏",
          "is_server": False
        },
#       {
#          "id": "ALLTc4gWNIM4VuAx2LEU",
#          "time": cur_time, 
#          "direction": "in",
#          "machine": "12.13.10.17",
#          "attacker": "61.160.247.70",
#          "victim": "12.13.10.17",
#          "data": "12.13.10.17/909kk.php",
#          "net": {
#            "proto": "TCP",
#            "type": "http",
#            "http": {
#              "method": "POST",
#              "protocol": "HTTP/1.1",
#              "status": 200,
#              "url": "/909kk.php",
#              "reqs_host": "12.13.10.17",
#              "reqs_referer": "http://12.13.10.17/",
#              "reqs_user_agent": "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
#              "reqs_content_length": 715,
#              "reqs_body": "caidao=eval(base64_decode('QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtpZihQSFBfVkVSU0lPTjwnNS4zLjAnKXtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO307ZWNobygiWEBZIik7JG09Z2V0X21hZ2ljX3F1b3Rlc19ncGMoKTskcD0nL2Jpbi9zaCc7JHM9J2NkIC91c3Ivc2hhcmUvbmdpbngvaHRtbC87bHM7ZWNobyBbU107cHdkO2VjaG8gW0VdJzskZD1kaXJuYW1lKCRfU0VSVkVSWyJTQ1JJUFRfRklMRU5BTUUiXSk7JGM9c3Vic3RyKCRkLDAsMSk9PSIvIj8iLWMgXCJ7JHN9XCIiOiIvYyBcInskc31cIiI7JHI9InskcH0geyRjfSI7JGFycmF5PWFycmF5KGFycmF5KCJwaXBlIiwiciIpLGFycmF5KCJwaXBlIiwidyIpLGFycmF5KCJwaXBlIiwidyIpKTskZnA9cHJvY19vcGVuKCRyLiIgMj4mMSIsJGFycmF5LCRwaXBlcyk7JHJldD1zdHJlYW1fZ2V0X2NvbnRlbnRzKCRwaXBlc1sxXSk7cHJvY19jbG9zZSgkZnApO3ByaW50ICRyZXQ7O2VjaG8oIlhAWSIpO2RpZSgpOw%3D%3D'));",
#              "resp_body": "X@Y1.cdx\n163.com.zip\n404.html\n50x.html\n909kk.php\na.php.bak\na.txt\naaaa.xlsx\nabc.c\nindex.html\nindex.php\nnginx-logo.png\npen.MYD\npoweredby.png\n[S]\n/usr/share/nginx/html\n[E]\nX@Y",
#              "reqs_line": "POST /909kk.php HTTP/1.1",
#              "reqs_header": "X-Forwarded-For: 70.127.242.253\r\nReferer: http://12.13.10.17/\r\nContent-Type: application/x-www-form-urlencoded\r\nUser-Agent: Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)\r\nHost: 12.13.10.17\r\nContent-Length: 715\r\nCache-Control: no-cache\r\n\r\n",
#              "resp_content_length": 172,
#              "resp_line": "HTTP/1.1 200 OK",
#              "resp_header": "Server: nginx/1.12.2\r\nDate: Wed, 17 Oct 2018 07:07:46 GMT\r\nContent-Type: text/html; charset=UTF-8\r\nTransfer-Encoding: chunked\r\nConnection: keep-alive\r\nX-Powered-By: PHP/7.2.9\r\n\r\n\r\n"
#            },
#            "src_ip": "61.160.247.70",
#            "src_port": 1114,
#            "real_src_ip": "61.160.247.70",
#            "dest_ip": "12.13.10.17",
#            "dest_port": 80
#          },
#          "threat": {
#            "name": "扫描黑客Webshell后门(base64传输)",
#            "suuid": "S2018000016",
#            "msg": "检测到扫描菜刀后门行为(黑吃黑行为)，黑客以爆破方式大范围扫描别的黑客留下的后门",
#            "level": "attack",
#            "result": "unknown",
#            "severity": 0,
#            "phase": "exploit",
#            "type": "exploit",
#            "confidence": 60,
#            "status": 0,
#            "module": "autocc",
#            "payload": "UE9TVCAvOTA5a2sucGhwIEhUVFAvMS4xDQpYLUZvcndhcmRlZC1Gb3I6IDcwLjEyNy4yNDIuMjUzDQpSZWZlcmVyOiBodHRwOi8vMTkyLjE2OC4xMDAuMTcxLw0KQ29udGVudC1UeXBlOiBhcHBsaWNhdGlvbi94LXd3dy1mb3JtLXVybGVuY29kZWQNClVzZXItQWdlbnQ6IE1vemlsbGEvNS4wIChjb21wYXRpYmxlOyBCYWlkdXNwaWRlci8yLjA7ICtodHRwOi8vd3d3LmJhaWR1LmNvbS9zZWFyY2gvc3BpZGVyLmh0bWwpDQpIb3N0OiAxOTIuMTY4LjEwMC4xNzENCkNvbnRlbnQtTGVuZ3RoOiA3MTUNCkNhY2hlLUNvbnRyb2w6IG5vLWNhY2hlDQoNCmNhaWRhbz1ldmFsKGJhc2U2NF9kZWNvZGUoJ1FHbHVhVjl6WlhRb0ltUnBjM0JzWVhsZlpYSnliM0p6SWl3aU1DSXBPMEJ6WlhSZmRHbHRaVjlzYVcxcGRDZ3dLVHRwWmloUVNGQmZWa1ZTVTBsUFRqd25OUzR6TGpBbktYdEFjMlYwWDIxaFoybGpYM0YxYjNSbGMxOXlkVzUwYVcxbEtEQXBPMzA3WldOb2J5Z2lXRUJaSWlrN0pHMDlaMlYwWDIxaFoybGpYM0YxYjNSbGMxOW5jR01vS1Rza2NEMG5MMkpwYmk5emFDYzdKSE05SjJOa0lDOTFjM0l2YzJoaGNtVXZibWRwYm5ndmFIUnRiQzg3YkhNN1pXTm9ieUJiVTEwN2NIZGtPMlZqYUc4Z1cwVmRKenNrWkQxa2FYSnVZVzFsS0NSZlUwVlNWa1ZTV3lKVFExSkpVRlJmUmtsTVJVNUJUVVVpWFNrN0pHTTljM1ZpYzNSeUtDUmtMREFzTVNrOVBTSXZJajhpTFdNZ1hDSjdKSE45WENJaU9pSXZZeUJjSW5za2MzMWNJaUk3SkhJOUluc2tjSDBnZXlSamZTSTdKR0Z5Y21GNVBXRnljbUY1S0dGeWNtRjVLQ0p3YVhCbElpd2ljaUlwTEdGeWNtRjVLQ0p3YVhCbElpd2lkeUlwTEdGeWNtRjVLQ0p3YVhCbElpd2lkeUlwS1Rza1puQTljSEp2WTE5dmNHVnVLQ1J5TGlJZ01qNG1NU0lzSkdGeWNtRjVMQ1J3YVhCbGN5azdKSEpsZEQxemRISmxZVzFmWjJWMFgyTnZiblJsYm5SektDUndhWEJsYzFzeFhTazdjSEp2WTE5amJHOXpaU2drWm5BcE8zQnlhVzUwSUNSeVpYUTdPMlZqYUc4b0lsaEFXU0lwTzJScFpTZ3BPdyUzRCUzRCcpKTs=",
#            "tag": [
#              "扫描黑客后门"
#            ],
#            "is_apt": 0,
#            "is_connected": 0,
#            "status_desc": "未处理",
#            "type_desc": "漏洞利用",
#            "severity_desc": "信息"
#          },
#          "assets": {
#            "id": 80,
#            "ip": "192.168.0.0/16",
#            "name": "",
#            "section": "终端",
#            "location": "",
#            "level": 0,
#            "ext": "",
#            "mac": "",
#            "status": 1,
#            "source": "manual",
#            "sub_type": ""
#          },
#          "behave_uuid": "unix-socket-1693460780439527",
#          "input_type": "unix_socket",
#          "incident_id": "46e702b14138c70eb08b3ab7c333f4d8-1592299438",
#          "machine_name": "",
#          "machine_port": "80",
#          "external_ip": "61.160.247.70",
#          "external_port": "1114",
#          "data_type": "url",
#          "event_type": "net",
#          "behave_source": "unix_socket-unix_socket_input-127.0.0.1",
#          "geo_data": {
#            "location": "中国-台湾-常州",
#            "Country": "中国",
#            "Province": "台湾",
#            "City": "常州",
#            "Org": "",
#            "Isp": "电信",
#            "Latitude": "31",
#            "Longitude": "119",
#            "TimeZone": "Asia/Shanghai",
#            "UTC": "UTC+8",
#            "ChinaCode": "320400",
#            "PhoneCode": "86",
#            "ISO2": "CN",
#            "Continent": "AP"
#          },
#          "is_black_ip": False,
#          "dest_assets": {
#            "id": 0,
#            "ip": "61.160.247.70",
#            "name": "",
#            "section": "",
#            "location": "",
#            "level": 0,
#            "ext": "",
#            "mac": "",
#            "status": 0,
#            "source": "",
#            "sub_type": ""
#          },
#          "assets_machine": "__12.13.10.17",
#          "dest_assets_machine": "__61.160.247.70",
#          "alert_count": 14,
#          "max_severity": 0,
#          "last_occ_time":cur_time+290, 
#          "first_occ_time":  cur_time,
#          "device_id":device_id_n,
#          "node_name": node_name,
#          "src_ip": "127.0.0.1",
#          "receive_time":cur_time+290, 
#          "first_occ_time_desc": get_second_time(cur_time) ,
#          "threat_name": "扫描黑客Webshell后门(base64传输)",
#          "last_occ_time_desc": get_second_time(cur_time+290),
#          "asset_name": "",
#          "geo_str": "中国-台湾-常州",
#          "time_desc": get_second_time(cur_time+290),
#          "direction_desc": "外部攻击",
#          "is_server": False
#        },
       {
          "id": "AXK8c4gWNIM4VuAx2LEU",
          "time": cur_time, 
          "direction": "in",
          "machine": "192.168.100.171",
          "attacker": "61.160.247.70",
          "victim": "192.168.100.171",
          "data": "192.168.100.171/909kk.php",
          "net": {
            "proto": "TCP",
            "type": "http",
            "http": {
              "method": "POST",
              "protocol": "HTTP/1.1",
              "status": 200,
              "url": "/909kk.php",
              "reqs_host": "192.168.100.171",
              "reqs_referer": "http://192.168.100.171/",
              "reqs_user_agent": "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
              "reqs_content_length": 715,
              "reqs_body": "caidao=eval(base64_decode('QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtpZihQSFBfVkVSU0lPTjwnNS4zLjAnKXtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO307ZWNobygiWEBZIik7JG09Z2V0X21hZ2ljX3F1b3Rlc19ncGMoKTskcD0nL2Jpbi9zaCc7JHM9J2NkIC91c3Ivc2hhcmUvbmdpbngvaHRtbC87bHM7ZWNobyBbU107cHdkO2VjaG8gW0VdJzskZD1kaXJuYW1lKCRfU0VSVkVSWyJTQ1JJUFRfRklMRU5BTUUiXSk7JGM9c3Vic3RyKCRkLDAsMSk9PSIvIj8iLWMgXCJ7JHN9XCIiOiIvYyBcInskc31cIiI7JHI9InskcH0geyRjfSI7JGFycmF5PWFycmF5KGFycmF5KCJwaXBlIiwiciIpLGFycmF5KCJwaXBlIiwidyIpLGFycmF5KCJwaXBlIiwidyIpKTskZnA9cHJvY19vcGVuKCRyLiIgMj4mMSIsJGFycmF5LCRwaXBlcyk7JHJldD1zdHJlYW1fZ2V0X2NvbnRlbnRzKCRwaXBlc1sxXSk7cHJvY19jbG9zZSgkZnApO3ByaW50ICRyZXQ7O2VjaG8oIlhAWSIpO2RpZSgpOw%3D%3D'));",
              "resp_body": "X@Y1.cdx\n163.com.zip\n404.html\n50x.html\n909kk.php\na.php.bak\na.txt\naaaa.xlsx\nabc.c\nindex.html\nindex.php\nnginx-logo.png\npen.MYD\npoweredby.png\n[S]\n/usr/share/nginx/html\n[E]\nX@Y",
              "reqs_line": "POST /909kk.php HTTP/1.1",
              "reqs_header": "X-Forwarded-For: 70.127.242.253\r\nReferer: http://192.168.100.171/\r\nContent-Type: application/x-www-form-urlencoded\r\nUser-Agent: Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)\r\nHost: 192.168.100.171\r\nContent-Length: 715\r\nCache-Control: no-cache\r\n\r\n",
              "resp_content_length": 172,
              "resp_line": "HTTP/1.1 200 OK",
              "resp_header": "Server: nginx/1.12.2\r\nDate: Wed, 17 Oct 2018 07:07:46 GMT\r\nContent-Type: text/html; charset=UTF-8\r\nTransfer-Encoding: chunked\r\nConnection: keep-alive\r\nX-Powered-By: PHP/7.2.9\r\n\r\n\r\n"
            },
            "src_ip": "61.160.247.70",
            "src_port": 1114,
            "real_src_ip": "61.160.247.70",
            "dest_ip": "192.168.100.171",
            "dest_port": 80
          },
          "threat": {
            "name": "扫描黑客Webshell后门(base64传输)",
            "suuid": "S2019000016",
            "msg": "检测到扫描菜刀后门行为(黑吃黑行为)，黑客以爆破方式大范围扫描别的黑客留下的后门",
            "level": "attack",
            "result": "unknown",
            "severity": 2,
            "phase": "exploit",
            "type": "exploit",
            "confidence": 60,
            "status": 0,
            "module": "autocc",
            "payload": "UE9TVCAvOTA5a2sucGhwIEhUVFAvMS4xDQpYLUZvcndhcmRlZC1Gb3I6IDcwLjEyNy4yNDIuMjUzDQpSZWZlcmVyOiBodHRwOi8vMTkyLjE2OC4xMDAuMTcxLw0KQ29udGVudC1UeXBlOiBhcHBsaWNhdGlvbi94LXd3dy1mb3JtLXVybGVuY29kZWQNClVzZXItQWdlbnQ6IE1vemlsbGEvNS4wIChjb21wYXRpYmxlOyBCYWlkdXNwaWRlci8yLjA7ICtodHRwOi8vd3d3LmJhaWR1LmNvbS9zZWFyY2gvc3BpZGVyLmh0bWwpDQpIb3N0OiAxOTIuMTY4LjEwMC4xNzENCkNvbnRlbnQtTGVuZ3RoOiA3MTUNCkNhY2hlLUNvbnRyb2w6IG5vLWNhY2hlDQoNCmNhaWRhbz1ldmFsKGJhc2U2NF9kZWNvZGUoJ1FHbHVhVjl6WlhRb0ltUnBjM0JzWVhsZlpYSnliM0p6SWl3aU1DSXBPMEJ6WlhSZmRHbHRaVjlzYVcxcGRDZ3dLVHRwWmloUVNGQmZWa1ZTVTBsUFRqd25OUzR6TGpBbktYdEFjMlYwWDIxaFoybGpYM0YxYjNSbGMxOXlkVzUwYVcxbEtEQXBPMzA3WldOb2J5Z2lXRUJaSWlrN0pHMDlaMlYwWDIxaFoybGpYM0YxYjNSbGMxOW5jR01vS1Rza2NEMG5MMkpwYmk5emFDYzdKSE05SjJOa0lDOTFjM0l2YzJoaGNtVXZibWRwYm5ndmFIUnRiQzg3YkhNN1pXTm9ieUJiVTEwN2NIZGtPMlZqYUc4Z1cwVmRKenNrWkQxa2FYSnVZVzFsS0NSZlUwVlNWa1ZTV3lKVFExSkpVRlJmUmtsTVJVNUJUVVVpWFNrN0pHTTljM1ZpYzNSeUtDUmtMREFzTVNrOVBTSXZJajhpTFdNZ1hDSjdKSE45WENJaU9pSXZZeUJjSW5za2MzMWNJaUk3SkhJOUluc2tjSDBnZXlSamZTSTdKR0Z5Y21GNVBXRnljbUY1S0dGeWNtRjVLQ0p3YVhCbElpd2ljaUlwTEdGeWNtRjVLQ0p3YVhCbElpd2lkeUlwTEdGeWNtRjVLQ0p3YVhCbElpd2lkeUlwS1Rza1puQTljSEp2WTE5dmNHVnVLQ1J5TGlJZ01qNG1NU0lzSkdGeWNtRjVMQ1J3YVhCbGN5azdKSEpsZEQxemRISmxZVzFmWjJWMFgyTnZiblJsYm5SektDUndhWEJsYzFzeFhTazdjSEp2WTE5amJHOXpaU2drWm5BcE8zQnlhVzUwSUNSeVpYUTdPMlZqYUc4b0lsaEFXU0lwTzJScFpTZ3BPdyUzRCUzRCcpKTs=",
            "tag": [
              "扫描黑客后门"
            ],
            "is_apt": 0,
            "is_connected": 0,
            "status_desc": "未处理",
            "type_desc": "漏洞利用",
            "severity_desc": "中"
          },
          "assets": {
            "id": 80,
            "ip": "192.168.0.0/16",
            "name": "",
            "section": "终端",
            "location": "",
            "level": 0,
            "ext": "",
            "mac": "",
            "status": 1,
            "source": "manual",
            "sub_type": ""
          },
          "behave_uuid": "unix-socket-1693460780439527",
          "input_type": "unix_socket",
          "incident_id": "46e702b14138c70eb08b3ab7c333f4d8-1592299438",
          "machine_name": "",
          "machine_port": "80",
          "external_ip": "61.160.247.70",
          "external_port": "1114",
          "data_type": "url",
          "event_type": "net",
          "behave_source": "unix_socket-unix_socket_input-127.0.0.1",
          "geo_data": {
            "location": "中国-江苏-常州",
            "Country": "中国",
            "Province": "江苏",
            "City": "常州",
            "Org": "",
            "Isp": "电信",
            "Latitude": "31",
            "Longitude": "119",
            "TimeZone": "Asia/Shanghai",
            "UTC": "UTC+8",
            "ChinaCode": "320400",
            "PhoneCode": "86",
            "ISO2": "CN",
            "Continent": "AP"
          },
          "is_black_ip": False,
          "dest_assets": {
            "id": 0,
            "ip": "61.160.247.70",
            "name": "",
            "section": "",
            "location": "",
            "level": 0,
            "ext": "",
            "mac": "",
            "status": 0,
            "source": "",
            "sub_type": ""
          },
          "assets_machine": "__192.168.100.171",
          "dest_assets_machine": "__61.160.247.70",
          "alert_count": 14,
          "max_severity": 2,
          "last_occ_time":cur_time+290, 
          "first_occ_time":  cur_time,
          "device_id":device_id_n,
          "node_name": node_name,
          "src_ip": "127.0.0.1",
          "receive_time":cur_time+290, 
          "first_occ_time_desc": get_second_time(cur_time) ,
          "threat_name": "扫描黑客Webshell后门(base64传输)",
          "last_occ_time_desc": get_second_time(cur_time+290),
          "asset_name": "",
          "geo_str": "中国-江苏-常州",
          "time_desc": get_second_time(cur_time+290),
          "direction_desc": "外部攻击",
          "is_server": False
        },
        ],
            "incidentList": [                                               # 事件汇总列表
                {
                      "severity": 2,
                      "phase": [
                        "exploit"
                      ],
                      "direction": "in",
                      "incident_id": "2a622fbbd8f4e4245ad87c45d2cc191b-1587702077",
                      "incident_name": "来自美国攻击者的漏洞利用行为",
                      "first_time": cur_time ,
                      "last_time": cur_time ,
                      "attacker_ip": [
                        "192.168.217.130"
                      ],
                      "host_ip": [
                        "192.168.100.171"
                      ],
                      "host_name": [
                        "a.attack.com"
                      ],
                      "attack_name": [
                        "MySQL注入",
                        "测试SQL注入漏洞"
                      ],
                      "attack_tool": [],
                      "attack_result": "unknown",
                      "attack_type": "",
                      "attack_type_reason": "",
                      "is_proxy": False,
                      "geo_data": {
                        "location": "美国-美国",
                        "Country": "美国",
                        "Province": "美国",
                        "City": "",
                        "Org": "",
                        "Isp": "level3.com",
                        "Latitude": "37",
                        "Longitude": "-95",
                        "TimeZone": "America/Chicago",
                        "UTC": "UTC-5",
                        "ChinaCode": "",
                        "PhoneCode": "1",
                        "ISO2": "US",
                        "Continent": "NA"
                      },
                      "success_count": 1,
                      "unknown_count": 1,
                      "failed_count": 1,
                      "device_id": device_id_n,            # 节点device_id，和上面的nodeInfo中相同就可以
                      "node_name": node_name,
                      "src_ip": "192.168.100.175",
                      "receive_time": cur_time,
                      "result_count": [
                        1,
                        1,
                        1
                      ]
                  },
                {
                    "severity": 4,
                    "phase": [                                             
                        "recon",
                        "control"
                    ],
                    "direction": "in",
                    "incident_id": "46e702b14138c70eb08b3ab7c333f4d8-1592303160",   # 这个是事件id
                    "incident_name": "来自中国江苏常州攻击者的控制行为",
                    "first_time": cur_time ,
                    "last_time": cur_time ,
                    "attacker_ip": [
                        "6.160.247.70"
                    ],
                    "host_ip": [
                        "192.168.100.171",
                        "192.168.88.54"
                    ],
                    "host_name": [
                         
                    ],
                    "attack_name": [
                        "端口扫描",
                        "b374k Webshell连接成功"
                    ],
                    "attack_tool": [
                        "ScanPort",
                        "Nmap"
                    ],
                    "attack_result": "success",
                    "attack_type": "",
                    "attack_type_reason": "",
                    "is_proxy": False,
                    "geo_data": {
                        "location": "中国-江苏-常州",
                        "Country": "中国",
                        "Province": "江苏",
                        "City": "常州",
                        "Org": "",
                        "Isp": "电信",
                        "Latitude": "31",
                        "Longitude": "119",
                        "TimeZone": "Asia/Shanghai",
                        "UTC": "UTC+8",
                        "ChinaCode": "320400",
                        "PhoneCode": "86",
                        "ISO2": "CN",
                        "Continent": "AP"
                    },
                    "success_count": 0,
                    "unknown_count": 0,
                    "failed_count": 0,
                    "device_id": device_id_n,            # 节点device_id，和上面的nodeInfo中相同就可以
                    "node_name": node_name,
                    "result_count": [
                        0,
                        0,
                        0
                    ]
                }
            ]
        }
    }
    return data_mode
