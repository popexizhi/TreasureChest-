#!/bin/bash
source setlogconfig.bash #logConfig file
start_test(){
    hostip=$1
    testcase=$2
    res_fp=$3
    fp="."
    echo "[testcase ${testcase}]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
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
    echo "start 99 gw_* and ue******************"
    cmd_doing="cd /home/slim/test/TreasureChest-/shell_test&&./testcase_other.sh ${testcase} ${res_fp}"
    echo $cmd_doing
    echo `sshpass -p'password' ssh slim@192.168.1.99 "${cmd_doing}" `
    echo "stop appserver test **********************************************"
    kill -9 ${app_pid}
    mv logConfig.cfg logConfig_back #清理logConfig.cfg现场
}
get_csv(){
    resfp=$1
    fp_list=`ls -all $1|grep log$|awk '{print $9}'`
    for i in $fp_list
    do
        echo "time,throughput(KiB/s)">${resfp}/$i.csv
        cat ${resfp}/$i|sed 's/^\[[0-9]\+://g'|sed 's/:.*throughput = /,/g'|sed 's/KiB.*//g'>>${resfp}/$i.csv
        echo ${resfp}/$i.csv
    done 
}
save_log(){
    echo "save log..."
    hostip=$1
    ph=$2
    cur_res=`cat ${ph}/L2UE2APP_app.log.csv|grep -v time|sed 's/.*,//g'|sort -n|tail -n1`
    cur_res="L2ue2app app read max: ${cur_res}"
    echo "${cur_res}"
    echo "${cur_res}">>${hostip}.log
    cur_res=`cat ${ph}/L2APP2UE_app.log.csv|grep -v time|sed 's/,[0-9]*$//g'|sed 's/.*,//g'|sort -n|tail -n1`
    cur_res="L2ue2app app sent max: ${cur_res}"
    echo "${cur_res}"
    echo "${cur_res}">>${hostip}.log
    sshpass -p'password' scp ${hostip}.log slim@192.168.1.25:/home/slim/jenkins_test/jenkins_test/workspace/TC_loadtest_app/load_L2/monitor
    sshpass -p'password' scp -r ${ph} slim@192.168.1.25:/home/slim/jenkins_test/jenkins_test/workspace/TC_loadtest_app/load_L2/monitor/socket_th
    sshpass -p'password' ssh slim@192.168.1.25 "cd /home/slim/jenkins_test/jenkins_test/workspace/TC_loadtest_app/load_L2/monitor&&./getdata_socket.sh socket_th/${ph} ${hostip}.log"
    ./appserver
    
}
save_csv_log(){
    dir_fp=$1 
    list_fp=`ls -all ${dir_fp}|grep log$|sed 's/.* //g'|sed ':a;N;$!ba;s/\n/ /g'`
    echo ${list_fp}
    for i in $list_fp
    do
        echo "time,sent(kb),read(kb)">${dir_fp}/$i.csv
        cat ${dir_fp}/$i|sed 's/^\[[0-9]\+://g'|sed 's/:.*sent=/,/g'|sed 's/(kb.*=/,/g'|sed 's/(kb)//g'>>${dir_fp}/$i.csv
    done

}
get_testcase_logConfig(){
    testcase=$1
    echo "testcase name is ${testcase}"
    set_log ${testcase}
}
res_dir=$2
des_log=$1
for i in L2UE2APP L2APP2UE
do
    testcase=$i
    get_testcase_logConfig ${testcase}
    start_test ${des_log} ${testcase} ${res_dir} #启动测试
    get_log ${testcase} ${res_dir} #收集结果并处理
    save_csv_log ${res_dir} #收集结果并处理
done
save_log ${des_log} ${res_dir}
exit 0
