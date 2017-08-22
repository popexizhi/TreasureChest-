#-*-coding:utf8-*-
import MySQLdb
import time


class db_mod():

    def __init__(self, db_name, ip, user, pd):
        self.ip = ip
        self.user = user
        self.pd = pd
        self.db_name = db_name
        self.port = 3306
        self.charset = "utf8"

        #self.db = MySQLdb.connect(ip ,user, pd, db_name, port=3306, charset="utf8")
        # self.db = MySQLdb.connect(self.ip ,self.user, self.pd, self.db_name, port=self.port3306, charset=self.charset"utf8")
        #self.cursor = self.db.cursor()

#    def __del__(self):
#        self.db.close()

    def log(self, message):
        print "*" * 20
        print message

    def get_dev_pin(self, user_mail):
        sql = "select pincode from nx_pin where principal=%s order by id desc limit 1;" % user_mail
        return self.select(sql)
    
    def get_report_data(self, report_name):
        sql = "SELECT testcase_item, testcase_value from cluster_fun where report_name='%s';" % str(report_name) 
        #self.log(sql)
        res=self.select(sql, num="all")
        return res

    def get_report_names(self):
        sql= "select DISTINCT report_name from cluster_fun where report_name not like '%testreport%' ORDER BY report_name DESC;" #不显示测试数据
        return self.select(sql, num="all")

    def select(self, sql, num="one" , sql_debug=None):
        self.db = MySQLdb.connect(self.ip, self.user, self.pd, self.db_name, port=self.port, charset=self.charset)
        self.cursor = self.db.cursor()
        self.log(sql)
        # Fetch a single row using fetchone() method.

        # debug doing
        if (None != sql_debug):
            self.log("[debug for sql] sql is %s" % str(sql_debug))
            res = self.cursor.execute(sql)
            num = self.cursor.fetchall()
            self.log("[debug for sql ]num is %d; \n\t\t all is %s " % (len(num), str(num)))
            t_sql = """select app_server_id from eap_user_app_servers where user_id = (select id from eap_user where email="1475901005.52");"""
            r = self.cursor.execute(t_sql)
            n = self.cursor.fetchall()
            self.log("[debug]num is %d; \n\t\t all is %s " % (len(n), str(n)))
            #assert len(self.cursor.fetchall()) > 1
            # disconnect from server
        res = self.cursor.execute(sql)
        if "one" == num:
            data = self.cursor.fetchone()
        if "all" == num:
            data = self.cursor.fetchall()
        self.db.close()
        return data

    def update_app_ip(self, host_ip="192.168.1.25", target_host_ip="0.0.0.1"):
        """change eap db 中激活状态app 的ip 防止注册端口冲突临时使用 """
        update_sql = 'UPDATE  nx_app_server  set host_ip = "%s" where app_server_status != "LOADING" and host_ip ="%s" ;' % (target_host_ip, host_ip)
        # self.log(update_sql)
        #self.cursor = self.db.cursor()
        return self.update(update_sql)



    def update(self, u_sql):
        self.log(u_sql)
        self.db = MySQLdb.connect(self.ip, self.user, self.pd, self.db_name, port=self.port, charset=self.charset)
        self.cursor = self.db.cursor()
        res = self.cursor.execute(u_sql)
        self.db.commit()
        self.db.close()

        return res

if __name__ == "__main__":
    db_name = "load_test"
    ip  = "192.168.1.41"
    user = "root"
    passwd = "password"
    x = db_mod(db_name, ip, user, passwd)
    x.get_report_data("test")
    print res


