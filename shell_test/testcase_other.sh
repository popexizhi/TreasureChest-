#!/bin/bash
source download.sh
source setlogconfig.bash
#ph="res_`date '+%y%m%d%H%M'`"
testcase=$1
res_dir=$2
echo "[ ${testcase} ]start:`date '+%y_%m_%d %H:%M'`****************************************************"
set_log ${testcase} 
set_log_res="$!"
echo "set_log_res $set_log_res"
testcase_for_other "${testcase}" $res_dir
echo "[${testcase}]stop: `date '+%y_%m_%d %H:%M'`***************************************************"
