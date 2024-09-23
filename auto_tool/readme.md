#下面脚本都使用sshpass,要求确保ssh首次登录过再使用如下脚本
#批量添加key到指定主机ip,backup_authorized_keys为key的批量文件
bash add_key ${ip}
#批量处理主机内容
bash batch_do
#批量处理主机执行脚本, hots_list为主机列表
bash hosts_do hosts_list 
#github backup
bash git_backup "${git add message}"
#github add file||dir
bash git_add {${file}|${dir}} "{git add message}"
