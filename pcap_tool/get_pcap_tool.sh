#!/bin/bash
#///////////////////////////////////////////////////
# bash get_pcap_tool ${ioc} #[test] 
# 此方法提供对ioc的pcap包，这里是以dig方式触发，但没有过滤请求的pcap存储，存储此时间的全部包
#///////////////////////////////////////////////////

# local dns_server 192.168.100.121
interface="ens192" #数据出口,此网卡要求是默认的访问使用端口,tcpdump 抓包使用的
dns_server="192.168.100.121" #ioc 查询的dns server 地址，此地址要作为pcap结果的检测使用
ioc=$1
pcap_name="test_${interface}_${ioc}.pcap"
echo "start get pcap*****************"
echo "interface:${interface}"
echo "dns_server:${dns_server}"
echo "ioc:${ioc}"
echo "target_pcap_name:${pcap_name}"
echo "*****************************"
tcpdump -i ${interface} -U -w test192.pcap&
tcpdump_pid=$!
echo "tcpdump_pid:${tcpdump_pid}"
ps -ef|grep ${tcpdump_pid}
echo "start:dig ${ioc} @${dns_server}"
dig ${ioc} @${dns_server}
echo "end:dig ${ioc} @${dns_server},waitting save pcap"
sleep 5
kill -9 ${tcpdump_pid}
ps -ef|grep ${tcpdump_pid}
cp test192.pcap ${pcap_name}
ls -all|grep pcap
echo "******************check pcap;grep ${dns_server}************ "
tcpdump -r ${pcap_name}|grep ${dns_server}

echo "******************end check pcap;grep ${dns_server}************ "
echo "use_pcap:${pcap_name}"
