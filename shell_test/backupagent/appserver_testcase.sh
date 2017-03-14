#!/bin/bash
start_test(){
    hostip=$1
    fp="."
    command_str_app="${fp}/app_server -cfg=alone.cfg -alone"
    ph="resapp_`date '+%y%m%d'`"
    
    rm -rf *.db
    rm -rf nohup.out
    mv *.log.txt backup
    mv app_server_log_backup/* backup
    mv -rf log backup
    
    echo "download ... "
    echo "sshpass -p'password' scp slim@192.168.1.99:/home/slim/jenkins/workspace/load_test/out/linux/*_server ."
    sshpass -p'password' scp slim@192.168.1.99:/home/slim/jenkins/workspace/load_test/out/linux/app_server .
    
    nohup ${command_str_app} &
    app_pid="$!"
    echo "app pid: " $app_pid
    echo "start 99 gw_* and ue**********************************************"
    sshpass -p'password' ssh slim@192.168.1.99 "cd ~/test/socketthought&&./throughout_testcase.sh"
    echo "stop appserver test **********************************************"
    kill -9 ${app_pid}
}
get_csv(){
    resfp=$1
    fp_list=`ls -all $1|grep log$|awk '{print $9}'`
    for i in $fp_list
    do
        #echo "time,throughput(KiB/s)">${resfp}/$i.csv
        #cat ${resfp}/$i|sed 's/^\[[0-9]\+://g'|sed 's/:.*throughput = /,/g'|sed 's/KiB.*//g'>>${resfp}/$i.csv #KiB/s
        echo "time,throughput(Kbps)">${resfp}/$i.csv
        cat ${resfp}/$i|sed 's/^\[[0-9]\+://g'|sed 's/:.* KiB \/ s//g'|sed 's/Kbps//g'|sed 's/ //g'>>${resfp}/$i.csv #Kbps

        echo ${resfp}/$i.csv
    done 
}
save_log(){
    echo "save log..."
    ph="resapp_`date '+%y%m%d'`"
    hostip=$1
    mkdir ${ph}
    cat app_server.log.txt |grep throughput|grep TCP|grep downlink>${ph}/tcp_throughput_downlink.log
    cat app_server.log.txt |grep throughput|grep TCP|grep uplink>>${ph}/tcp_throughput_uplink.log
    cat app_server.log.txt |grep throughput|grep UDP|grep downlink>>${ph}/udp_throughput_downlink.log
    cat app_server.log.txt |grep throughput|grep UDP|grep uplink>>${ph}/udp_throughput_uplink.log
    get_csv ${ph}
    version=`cat *.log.txt|grep version=|sed 's/.*version=//g'|sed 's/:.*//g'|sort |uniq|xargs echo "version:"`
    echo "version:${version}"
    echo "${version}">${hostip}.log
    cur_res=`cat ${ph}/tcp_throughput_downlink.log|grep "TCP"|sed 's/.*, //g'|sort|tail -n 1|sed 's/ Kbps//g'`
    cur_res="thoughput downlink tcp max(Kbps) : ${cur_res}"
    echo "${cur_res}"
    echo "${cur_res}">>${hostip}.log
    cur_res=`cat ${ph}/tcp_throughput_uplink.log|grep "TCP"|sed 's/.*, //g'|sort|tail -n 1|sed 's/ Kbps//g'`
    cur_res="thoughput uplink tcp max(Kbps) : ${cur_res}"
    echo "${cur_res}"
    echo "${cur_res}">>${hostip}.log
    cur_res=`cat ${ph}/udp_throughput_downlink.log|grep "UDP"|sed 's/.*, //g'|sort|tail -n 1|sed 's/ Kbps//g'`
    cur_res="thoughput downlink udp max(Kbps) : ${cur_res}"
    echo "${cur_res}"
    echo "${cur_res}">>${hostip}.log
    cur_res=`cat ${ph}/udp_throughput_uplink.log|grep "UDP"|sed 's/.*, //g'|sort|tail -n 1|sed 's/ Kbps//g'`
    cur_res="thoughput uplink udp max(Kbps) : ${cur_res}"
    echo "${cur_res}"
    echo "${cur_res}">>${hostip}.log
#    sshpass -p'password' scp ${hostip}.log slim@192.168.1.25:/home/slim/jenkins_test/jenkins_test/workspace/TC_loadtest_app/load_L2/monitor
#    sshpass -p'password' scp -r ${ph} slim@192.168.1.25:/home/slim/jenkins_test/jenkins_test/workspace/TC_loadtest_app/load_L2/monitor/socket_th
#    sshpass -p'password' ssh slim@192.168.1.25 "cd /home/slim/jenkins_test/jenkins_test/workspace/TC_loadtest_app/load_L2/monitor&&./getdata_socket.sh socket_th/${ph} ${hostip}.log"
    ./appserver_testcase_odds.sh ${hostip}.log ${ph}
    
}
start_test $1 #启动测试
save_log $1 #收集结果并处理
exit 0
