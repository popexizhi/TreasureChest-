#!/bin/bash
source setlogconfig.bash
./download.sh #下载新版本load_test指定版本
all_test="L1UE2FGW L1FGW2UE L1APP2BGW L1BGW2APP L2UE2APP L2APP2UE"
#all_test="L1UE2FGW L1FGW2UE"
for i in ${all_test}
do
    echo "[$i]start:`date '+%y_%m_%d %H:%M'`****************************************************"
    set_log $i 
    testcase_doing "$i" $1
    echo "[$i]stop: `date '+%y_%m_%d %H:%M'`***************************************************"
done
