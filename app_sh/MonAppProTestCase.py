#-*-coding:utf8 -*-
import unittest
from MonAppPro import mon_app

class test_mon_app(unittest.TestCase):
    def test_save_b_e_one_file(self):
        x = mon_app()
        td_list_b = [[1,12],[2,14]]
        td_list_e = [[1,20],[4,21]]
        pre_list = [[1,12,20],\
                    [2,26,20],\
                    [4,26,41],\
                    ]
        res = x.save_b_e_one_file(td_list_b, td_list_e)
        print res
        print "~" * 20
        self.assertEqual(res[1], pre_list)

    def test_save_b_e_one_file_oneline(self):
        """无叠加line """
        x = mon_app()
        td_list_b = [[1,12]]
        td_list_e = [[4,21]]
        pre_list = [[1,12,0],\
                    [4,12,21],\
                    ]
        res = x.save_b_e_one_file(td_list_b, td_list_e)
        print res
        print "~" * 20
        self.assertEqual(res[1], pre_list)
    
    def test_save_all_num(self):
        x = mon_app()
        td_list_1 = [[1,1,2],[5,2,4]]
        td_list_2 = [[1,2,2],[4,3,2]]
        td_list_3 = [[3,2,2],[4,3,2]]
        td_list_4 = [[4,2,2],[5,2,4]]
        pre_list = [[1, 2, 2, 2, 2, 0, 0, 0, 0],\
                    [2, 1, 2, 2, 2, 0, 0, 0, 0],\
                    [3, 1, 2, 2, 2, 2, 2, 0, 0],\
                    [4, 1, 2, 3, 2, 3, 2, 2, 2],\
                    [5, 2, 4, 3, 4, 3, 2, 2, 4],\
                    ]
        key_res = {"1HandleL2AuthReq":td_list_1,\
        "2HandleDeviceInfoIndication":td_list_2,\
        "3EAPServiceWorker::DoConfirmPolicyVersion":td_list_3,\
        "4EAPRpcService::OnDevicePolicyUpdated":td_list_4\
        }
        res = x.save_all_num(key_res)
        print res
        print "~" * 20
        self.assertEqual(res[1], pre_list)
if __name__ == "__main__":
    unittest.main()

