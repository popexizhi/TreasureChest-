ls -all $1|grep boot|grep -v Ser|awk '{print $9}'|cut -c 4-|awk -F\. '{print $1}'>1.py
vim -S get_host.vi 1.py
