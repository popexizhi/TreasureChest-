#!/bin/bash
source download.sh
source setlogconfig.bash
testcase=$1
echo "[${testcase}]start:`date '+%y_%m_%d %H:%M'`****************************************************"
set_log ${testcase} 
set_log_res="$!"
echo "set_log_res $set_log_res"
testcase_for_other "${testcase}"
echo "[${testcase}]stop: `date '+%y_%m_%d %H:%M'`***************************************************"
