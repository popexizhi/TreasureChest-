#!/bin/bash

for dirname in $(ls -all |grep "^d"|grep -v "uecode\|\."|awk '{print $9}');do
    echo ${dirname}
    sh get_host.sh ${dirname} 
done 
