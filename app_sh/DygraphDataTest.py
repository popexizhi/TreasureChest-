#!/bin/python2.7
#-*-coding:utf8-*-
import unittest
from DygraphData import dygraph_data

class DygraphDataTest(unittest.TestCase):
    def xtest_check_line_source(self):
        x = dygraph_data()
        t_str= "[27928:1117/164406:280727675598:INFO:noc_quic_relay_ctrl.cc(527)]  NocRelayCtrl::KeepAliveTimerExpired relay_statics:  snd_data_indication_cnt= 1164428 send size = 82088544 rcv_data_indication_cnt= 1170225 rcv size = 871714478 tcp_tx size= 82088544 tcp_rx size= 876721808"
        res = x.check_line_source(t_str)
        self.assertEqual(res["time"], "1117/164406")
        self.assertEqual(res["snd_data_indication_cnt"], "1164428")
        self.assertEqual(res["rcv_data_indication_cnt"], "1170225")
    def xtest_chang_date(self):
        x = dygraph_data()
        self.assertEqual(x.chang_date("1117/164406"),"2016/11/17 16:44:06")

    def xtest_get_dir_file(self):
        x = dygraph_data()
        print x.get_dir_file(dir_p="monitor_data", file_format="log")
    
    def xtest_check_line_source_for_app(self):
        x = dygraph_data()
        t_str= "[2016-12-07-10-57-22-874:889]  app server[46324] :total online client count: 880"
        app_reg = {"app hostid":u"(?<=app server\[)\d\d*"}
        res = x.check_line_source(t_str, app_reg, 0)
        print res
        
    def xtest_check_line_source_for_app_err_line(self):
        x = dygraph_data()
        t_str= "[2016-12-07-12-12-50-87:823]  app server[34251[2016-12-07-12-12-50-73:445]  app server[32239] :total online client count: 999"
        app_reg = {"app hostid":u"(?<=app server\[)\d\d*","time":u"\d\d*-\d\d*-\d\d*-\d\d*-\d\d*-\d\d*","total online client count":u"\d\d*(?=$)"}
        res = x.check_line_source(t_str, app_reg, 0)
        print res

    def test_check_line_source_for_app_line(self):
        x = dygraph_data()
        t_str= """
[288218:1229/122639:3193572652584:INFO:noc_quic_appserver.cc(446)] HandleL2AuthReq, host_id: 84913, version: 1, begin
[288218:1229/122639:3193572652591:INFO:noc_quic_appserver.cc(454)] HandleL2AuthReq, host_id: 84913, version: 1, QueryL2Pincode
[288218:1229/122639:3193572764405:INFO:noc_quic_appserver.cc(462)] HandleL2AuthReq, host_id: 84913, version: 1, pincode: 65ea4561c3b4
[288218:1229/122639:3193572793092:INFO:noc_quic_appserver.cc(473)] HandleL2AuthReq, host_id: 84913, version: 1, CreateAndSendL2AuthSuccessResp
[288218:1229/122639:3193572816919:INFO:noc_quic_appserver.cc(475)] HandleL2AuthReq, host_id: 84913, version: 1, end
        """
        HandleL2AuthReq_B = {\
                    "HandleL2AuthReq":u"HandleL2AuthReq.*",
                    "time":u"\d\d*/\d\d*"
                    }
        for i in t_str.split("\n"):
            res = x.check_line_source(i, HandleL2AuthReq_B)
            print res

if __name__=="__main__":
    unittest.main()
        
