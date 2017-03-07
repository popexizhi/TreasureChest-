#!/bin/bash
hostip=$1
fp="/home/slim/test/throught/"
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


echo "starttest**********************"
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
sleep 2
nohup ${command_str_ue} &
ue_pid="$!"
echo "ue pid: "$ue_pid
sleep 300
echo "stop all test**********************"
kill -9 ${fgw_pid} ${bgw_pid} ${app_pid} ${ue_pid}
exit 0
