#-*-coding:utf8-*-
import threading
import time,json,datetime
import websocket
from websocket import create_connection
import ssl
from data import *
import mapping_check 

class wss_client():
    def __init__(self):
        #self.wait_time = 10*2
        self.wait_time = 60*10

    def connet_server(self, id):
        self.id = id
        #self.device_id_n = "20CCDACF095494004E757C36DBDCA4%s" % str(self.id)
        self.device_id_n = mapping_check.device_id_list[id]
        self.log(self.device_id_n)
        #device_ip = "19.1.1%s.254" % str(self.id) 
        device_ip = mapping_check.node_name_list[id] 
        self.device_ip = device_ip
        data_connect = {"action":"reg_child","data":device_ip,"child_id": self.device_id_n}
        self.log(data_connect)
        url = 'wss://192.168.103.81:443/api/web/ws/cascade'
        header = {"cascade_call" :"true"}
        while True:  # 一直链接，直到连接上就退出循环
            time.sleep(1)
            try:
                self.ws = create_connection(url, sslopt={"check_hostname": False, "cert_reqs": ssl.CERT_NONE},header = {"cascade_call": "true"})
                self.log(self.ws)
                break
            except Exception as e:
                self.log('err:%s' % str(e))
                continue
            send = json.dumps(data_connect)
            self.log(send)
            self.log_in_file(send)
            self.ws.send(send)

    def log_in_file(self, msg, file="wss_send.log"):
        cur_time = time.time()
        cur_time_log = time.localtime(int(cur_time))
        cur_time_log = time.strftime("%Y-%m-%d %H:%M:%S", cur_time_log)
        msg = "[%s][%s]%s" % (str(cur_time_log),str(self.id), str(msg))
        print(msg)
        msg_in_file = "\n[%s][%s]send" % (str(cur_time_log),str(self.id))
        f = open(file, "a")
        f.writelines(msg_in_file)
        f.close()

    def log(self, msg):
        cur_time = time.time()
        print("[%s][%s]%s" % (str(cur_time),str(self.id), str(msg)))

    def doing(self):
        #self.log(self.ws)
        #判断是否是否为发送时间
        cur_second = datetime.datetime.now()
        self.log(cur_second.minute)
        while 1 != cur_second.minute % 10   : #只在[0-5]1分,11秒发送数据  
            time.sleep(1)
            cur_second = datetime.datetime.now()
        #发送数据
        cur_time = get_new_time() 
        alert_list_cur = "%s____%d" % (str(self.id), int(cur_time))
        data_c = get_data(self.device_id_n, cur_time,self.device_ip,str(cur_time))
        #data_c = get_data(self.device_id_n, cur_time,self.device_ip,alert_list_cur)
        data_cur = json.dumps(data_c)
        #self.log(data_cur)
        try:
            self.ws.send(data_cur)
            self.log_in_file(data_cur)
            time.sleep(60)
        except Exception as e:
            self.log_in_file("Closing socket because of error:" + str(e))
            self.ws.close()
            self.connet_server(self.id)

class timer(threading.Thread):
    def __init__(self, num, wss_client):
        threading.Thread.__init__(self)
        self.num = num
        self.wss_client = wss_client
        self.thread_stop = False

    def run(self):
        while True != self.thread_stop:
            self.wss_client.doing() 
     
        self.wss_client.log("stop")

    def stop(self):
        self.thread_stop = True

    
def test(num):
    all_client = []
    for i in xrange(num):
        print(i) 
        t = wss_client()
        t.connet_server(i)
        thread_n = timer(i, t)
        thread_n.start()
        all_client.append(thread_n)

    time.sleep(60*60 * 24*3)
    for i in all_client:
        i.stop()
         
if __name__=="__main__":
    
    #test(2)
    test(50)
