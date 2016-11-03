#-*-coding:utf8-*-
import re
import subprocess

class monlog():
    def sh_grep(self, str_, filep = "pp.log"):
        com_str = """cat %s|grep '%s'""" % (str(filep), str(str_))
        return self._com(com_str)
    def _com(self, cmd):
         getchar = "a"
         self.log(cmd)
         self.app_log_b = subprocess.Popen([cmd], shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE)
         # Send the data and get the output
         stdout, stderr = self.app_log_b.communicate(getchar)
         return stdout

    def log(self, mess):
        #print "[monlog] %s" % str(mess)
        mes = "[monlog]%s %s \n" % (str() ,str(mess))
        f = open("mon.log", "wb")
        f.write(mes)
        f.close()

if __name__=="__main__":
    x = monlog()
    x.sh_grep("SlimSocketAgent::SocketManagerRegister start, host_id=")
