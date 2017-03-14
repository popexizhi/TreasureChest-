#!/bin/bash
hostip=$1
fp="."
command_str_fgw="${fp}/fgw_server -cfg=alone.cfg -relay"
command_str_bgw="${fp}/bgw_server -cfg=alone.cfg -relay"
command_str_app="${fp}/app_server -cfg=alone.cfg -alone"
command_str_ue="${fp}/slim_engine_test -cfg=alone.cfg -host=200"
command_str_ueII="${fp}/slim_engine_test -cfg=alone.cfg -host=201"
command_c2s_ue="${fp}/slim_engine_test -cfg=alone.cfg  -data_direction=c2s -host=300"
command_c2s_ueII="${fp}/slim_engine_test -cfg=alone.cfg  -data_direction=c2s -host=301"
command_udp_ue="${fp}/slim_engine_test -cfg=alone.cfg -host=1200 -udp"
command_udp_ueII="${fp}/slim_engine_test -cfg=alone.cfg -host=1201 -udp"
command_udp_c2s_ue="${fp}/slim_engine_test -cfg=alone.cfg  -data_direction=c2s -host=1300 -case=UdpThroughputTest.cfg"
command_udp_c2s_ueII="${fp}/slim_engine_test -cfg=alone.cfg  -data_direction=c2s -host=1301 -case=UdpThroughputTest.cfg"  

rm -rf *.db
rm -rf nohup.out
mv *.log.txt backup
mv -rf log backup

echo "download ... "
echo "sshpass -p'password' scp slim@192.168.1.99:/home/slim/jenkins/workspace/load_test/out/linux/*_server ."
sshpass -p'password' scp slim@192.168.1.99:/home/slim/jenkins/workspace/load_test/out/linux/*_server .
sshpass -p'password' scp slim@192.168.1.99:/home/slim/jenkins/workspace/load_test/out/linux/slim_engine_test .

nohup ${command_str_fgw} &
fgw_pid="$!"
echo "fgw pid: " $fgw_pid
sleep 6
nohup ${command_str_bgw} &
bgw_pid="$!"
echo "bgw pid: " $bgw_pid
sleep 3
nohup ${command_str_app} &
app_pid="$!"
echo "app pid: " $app_pid
sleep 3
echo "start tcp downlink test**********************************"
nohup ${command_str_ue} &
ue_pid="$!"
echo "ue pid: " $ue_pid
nohup ${command_str_ueII} &
ueII_pid="$!"
echo "ue pid: " $ueII_pid
sleep 120
echo "stop ue downlink test ********************************************"
kill -9 ${ue_pid} ${ueII_pid}

echo "start uplink test **********************************************"
nohup ${command_c2s_ue} &
ue_pid="$!"
echo "uplink ue pid: " $ue_pid
nohup ${command_c2s_ueII} &
ueII_pid="$!"
echo "uplink ue pid: " $ueII_pid
sleep 120
echo "stop uelink test**********************************************"
kill -9 ${ue_pid} ${ueII_pid}

echo "start udp downlink test**********************************"
nohup ${command_udp_ue} &
ue_pid="$!"
echo "ue pid: " $ue_pid
nohup ${command_udp_ueII} &
ueII_pid="$!"
echo "ue pid: " $ueII_pid
sleep 120
echo "stop udp ue downlink test ********************************************"
kill -9 ${ue_pid} ${ueII_pid}

echo "start udp uplink test **********************************************"
nohup ${command_udp_c2s_ue} &
ue_pid="$!"
echo "uplink ue pid: " $ue_pid
nohup ${command_udp_c2s_ueII} &
ueII_pid="$!"
echo "uplink ue pid: " $ueII_pid
sleep 120
echo "stop all test **********************************************"
kill -9 ${fgw_pid} ${bgw_pid} ${app_pid} ${ue_pid} ${ueII_pid}
echo "save log..."
cat app_server.log.txt |grep throughput|grep TCP|grep downlink>tcp_throughput_downlink.log
cat app_server.log.txt |grep throughput|grep TCP|grep uplink>tcp_throughput_uplink.log
cat app_server.log.txt |grep throughput|grep UDP|grep downlink>udp_throughput_downlink.log
cat app_server.log.txt |grep throughput|grep UDP|grep uplink>udp_throughput_uplink.log
cur_res=`cat tcp_throughput_downlink.log|grep "TCP"|sed 's/.*, //g'|sort|tail -n 1|sed 's/ Kbps//g'`
cur_res="thoughput downlink tcp : ${cur_res}"
echo "${cur_res}"
echo "${cur_res}">${hostip}.log
cur_res=`cat tcp_throughput_uplink.log|grep "TCP"|sed 's/.*, //g'|sort|tail -n 1|sed 's/ Kbps//g'`
cur_res="thoughput uplink tcp : ${cur_res}"
echo "${cur_res}"
echo "${cur_res}">>${hostip}.log
cur_res=`cat udp_throughput_downlink.log|grep "UDP"|sed 's/.*, //g'|sort|tail -n 1|sed 's/ Kbps//g'`
cur_res="thoughput downlink udp : ${cur_res}"
echo "${cur_res}"
echo "${cur_res}">>${hostip}.log
cur_res=`cat udp_throughput_uplink.log|grep "UDP"|sed 's/.*, //g'|sort|tail -n 1|sed 's/ Kbps//g'`
cur_res="thoughput uplink udp : ${cur_res}"
echo "${cur_res}"
echo "${cur_res}">>${hostip}.log
version=`cat *.log.txt|grep version=|sed 's/.*version=//g'|sed 's/:.*//g'|sort |uniq|xargs echo "version:"`
echo "version:${version}"
echo "${version}">>${hostip}.log
sshpass -p 'abc123,./' scp ${hostip}.log slim@192.168.1.216:/data/jenkins/workspace/dev88_thoughput_testcase/res
exit 0
