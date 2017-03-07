#!/bin/bash
source setlogconfig.bash
for i in L1UE2FGW L1FGW2UE L1APP2BGW L1BGW2APP L2UE2APP L2APP2UE
do
    echo "[$i]start:`date '+%y_%m_%d %H:%M'`****************************************************"
    set_log $i 
    testcase_doing "$i"
    echo "[$i]stop: `date '+%y_%m_%d %H:%M'`***************************************************"
done
