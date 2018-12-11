#-*-coding:utf8-*-
import urllib2, json, urllib
import sys, datetime, time
class Sender():
    def __init__(self, url):
        self._url = url

    def doing(self):
        self.log("[send machine:%s]************************" % self.machine)
        kind_list = ["get_header_data", "Ramnit", "BlackTech"]
        for msg_kind in kind_list:
            data = self.get_data(msg_kind)  
            self.log("[%s]res:%s" % (msg_kind,self.poster(data)))

    def poster(self, data):
        data_jsondumps = json.dumps(data)
        self.log(self._url)
        self.log(data_jsondumps)
        try:
            #req = urllib2.Request(self._url, data_jsondumps, {'Content-Type': 'application/json'})
            req = urllib2.Request(self._url)
            req.add_data(urllib.urlencode(data)) #, {'Content-Type': 'application/json'})
            f = urllib2.urlopen(req)
            get_data = f.read()
            f.close()
            respone_json = json.loads(get_data) 
            self.log(respone_json)
            print respone_json["verbose_msg"]
            return respone_json
        except urllib2.HTTPError as e:
            self.log("The server could not fulfill the request.Error code: %s" % str(e.code))

        except urllib2.URLError as e:
            self.log("Failed to reach a server. Reson:%s" % str(e.reason))

        else:
            return {}

    def log(self, mes):
        print "[sender]%s" % str(mes)

if __name__ == "__main__":
    t = Sender("http://10.9.147.243/intra/public/sendEmail")
    filepath = "mail.txt"
    f=open(filepath)
    con = f.readlines()
    conx= ""
    f.close()
    for i in con:
        conx = conx + str(i)
    print conx
    data = {
            "recipients":"test@mail.cn",
            "subject":"dump-mail",
            "cc":"test@mail.cn",
            "content":conx,
            "contentType":"html"
        }
    t.poster(data)
