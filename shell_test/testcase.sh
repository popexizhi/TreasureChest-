#!/bin/bash
source setlogconfig.bash
init(){
    #准备testcase条件
    local resdir=$1
    if [[ ! -d ${resdir} ]];
    then 
        mkdir ${resdir}
    else
        rm -rf ${resdir}/* #清空文件夹中全部内容
    fi
    echo "${resdir} ls -all"
    ls -all ${resdir}
}

./download.sh #下载新版本load_test指定版本
all_test="L1UE2FGW L1FGW2UE L1APP2BGW L1BGW2APP L2UE2APP L2APP2UE"
#all_test="L1UE2FGW L1FGW2UE"
#init
init $1

for i in ${all_test}
do
    echo "[$i]start:`date '+%y_%m_%d %H:%M'`****************************************************"
    set_log $i 
    testcase_doing "$i" $1
    echo "[$i]stop: `date '+%y_%m_%d %H:%M'`***************************************************"
done

