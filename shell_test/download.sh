#!/bin/bash

#备份旧的应用程序
if [[ ! -d old_back ]];
then
    mkdir old_back
fi
mv *_server old_back
mv slim_engine_test old_back

#下载新版应用程序
sshpass -p'password' scp slim@192.168.1.99:/home/slim/jenkins/workspace/load_test/out/linux/*_server .
sshpass -p'password' scp slim@192.168.1.99:/home/slim/jenkins/workspace/load_test/out/linux/slim_engine_test .

