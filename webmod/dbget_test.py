# -*- coding:utf8 -*-
from dbget import db_mod
import time
import unittest

class TestDb_mod(unittest.TestCase):
    def test_get_report_data(self):
        """ 
        test get_report_data
        """
        x = db_mod("load_test", "192.168.1.41", "root", "password")
        res=x.get_report_data("test")
        #print res
        self.assertEqual(len(res), 119)
    def test_get_report_names(self):
        x = db_mod("load_test", "192.168.1.41", "root", "password")
        res = x.get_report_names()
        print res
        

if __name__=="__main__":
    unittest.main()
