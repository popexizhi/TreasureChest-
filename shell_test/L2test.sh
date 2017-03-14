#!/bin/bash
hostip=$1
fp="."
command_str_fgw="${fp}/fgw_server -cfg=alone_other.cfg -relay"
command_str_bgw="${fp}/bgw_server -cfg=alone_other.cfg -relay"
command_str_ue="${fp}/slim_engine_test -cfg=alone_other.cfg -host=200"
command_str_ueII="${fp}/slim_engine_test -cfg=alone_other.cfg -host=201"

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
nohup ${command_str_ue} &
ue_pid="$!"
echo "ue pid: "$ue_pid
sleep 600
echo "stop all test**********************"
kill -9 ${fgw_pid} ${bgw_pid} ${ue_pid}
exit 0
