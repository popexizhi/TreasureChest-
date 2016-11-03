#!/bin/bash
echo "start get hostue list"
dir_path=$1
dirlist_f="dirlist.py"
sourcecode_dir="uecode"
ls -all ${dir_path}|grep boot|grep -v Ser|awk '{print $9}'|cut -c 4-|awk -F\. '{print $1}'>${dir_path}/${dirlist_f}
vim -S get_host.vi ${dir_path}/${dirlist_f}
cat ${dirlist_f}

echo "**********************************************************************"
echo "cp all code in db_dir"
cp ${sourcecode_dir}/* ${dir_path}
ls -all ${dir_path}|grep -v db

echo "**********************************************************************"
echo "start ue"
sta_str="python ClientMu.py"
cd ${dir_path}
nohup ${sta_str} &
ps -ef|grep ${sta_str}
