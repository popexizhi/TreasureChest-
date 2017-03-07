#!/bin/bash
ph="/home/slim/test/throught/"
logph="."
set_log(){
    echo "start set_log $1"
    logConfig="${ph}/logConfig.cfg"
    echo "">${logConfig}
	echo "set logConfig.cfg for testcase:$1**********************"
    case $1 in
    "L1UE2FGW" )
	    echo "param.test:test_service_mode = 4 //disable layer2 socket test">>${logConfig}
	    echo "param.Padding:Mode = 1 // enable stream test, layer 1, ue->fgw">>${logConfig}
        ;;
    "L1FGW2UE" )
	    echo "param.test:test_service_mode = 4 //disable layer2 socket test">>${logConfig}
        echo "param.Padding:Mode = 5  // enable stream test, layer 1, fgw->ue">>${logConfig}
        ;;
    "L1APP2BGW")
        echo "param.test:test_service_mode = 4   //disable layer2 socket test">>${logConfig}
        echo "param.Padding:Mode =3  // enable stream test, layer 1, app->bgw">>${logConfig}
        ;;
    "L1BGW2APP")
        echo "param.test:test_service_mode = 4   //disable layer2 socket test">>${logConfig}
        echo "param.Padding:Mode =6  // enable stream test, layer 1, bgw->app">>${logConfig}
        ;;
    "L2UE2APP")
        echo "param.test:test_service_mode = 4   //disable layer2 socket test">>${logConfig}
        echo "param.Padding:Mode = 2  // enable stream test, layer 2, ue->app">>${logConfig}
        ;;
    "L2APP2BGW")
        echo "param.test:test_service_mode = 4   //disable layer2 socket test">>${logConfig}
        echo "param.Padding:Mode = 4  // enable stream test, layer 2, app->ue">>${logConfig}
        ;;
    *)
        echo "no has this testcase name[$1]"
        ;;
    esac
	cat ${logConfig}
    return 0
}

get_log(){
	echo "testcase log check: $1****************************************"
    ph="res_`date '+%y%m%d'`"
    mkdir $ph
    echo "$ph"
    case $1 in
    "L1UE2FGW" )
    	echo "fgw get log **************************************************"
    	cat ${logph}/fgw.log.txt|grep "EpollLoop Throughput"
    	cat ${logph}/fgw.log.txt|grep "EpollLoop Throughput">$ph/$1_fgw.log
    	echo "ue get log **************************************************"
       	cat ${logph}/log/ue_client_200.log.txt|grep "EpollLoop Throughput"
       	cat ${logph}/log/ue_client_200.log.txt|grep "EpollLoop Throughput">$ph/$1_ue.log
        ;;
    "L1FGW2UE")
    	echo "fgw get log **************************************************"
    	cat ${logph}/fgw.log.txt|grep "EpollLoop Throughput"
    	cat ${logph}/fgw.log.txt|grep "EpollLoop Throughput">$ph/$1_fgw.log
    	echo "ue get log **************************************************"
       	cat ${logph}/log/ue_client_200.log.txt|grep "EpollLoop Throughput"
       	cat ${logph}/log/ue_client_200.log.txt|grep "EpollLoop Throughput">$ph/$1_ue.log
        ;;
    "L1APP2BGW")
        echo "bgw get log**************************************************"
        cat ${logph}/bgw.log.txt|grep "EpollLoop Throughput"
        cat ${logph}/bgw.log.txt|grep "EpollLoop Throughput">$ph/$1_bgw.log
        echo "app get log**************************************************"
        cat ${logph}/app_server.log.txt|grep "EpollLoop Throughput"
        cat ${logph}/app_server.log.txt|grep "EpollLoop Throughput">$ph/$1_app.log
        ;;
    "L1BGW2APP")
        echo "bgw get log**************************************************"
        cat ${logph}/bgw.log.txt|grep "EpollLoop Throughput"
        cat ${logph}/bgw.log.txt|grep "EpollLoop Throughput">$ph/$1_bgw.log
        echo "app get log**************************************************"
        cat ${logph}/app_server.log.txt|grep "EpollLoop Throughput"
        cat ${logph}/app_server.log.txt|grep "EpollLoop Throughput">$ph/$1_app.log
        ;;
    "L2UE2APP")
        echo "app get log**************************************************"
        cat ${logph}/app_server.log.txt|grep "EpollLoop Throughput"
        cat ${logph}/app_server.log.txt|grep "EpollLoop Throughput">$ph/$1_app.log
    	echo "ue get log **************************************************"
       	cat ${logph}/log/ue_client_200.log.txt|grep "EpollLoop Throughput"
       	cat ${logph}/log/ue_client_200.log.txt|grep "EpollLoop Throughput">$ph/$1_ue.log
        ;;
    "L2APP2UE")
        echo "app get log**************************************************"
        cat ${logph}/app_server.log.txt|grep "EpollLoop Throughput"
        cat ${logph}/app_server.log.txt|grep "EpollLoop Throughput">$ph/$1_app.log
    	echo "ue get log **************************************************"
       	cat $logph/log/ue_client_200.log.txt|grep "EpollLoop Throughput"
       	cat $logph/log/ue_client_200.log.txt|grep "EpollLoop Throughput">$ph/$1_ue.log
        ;;
    *)
        echo "no has this testcase name [$1]"
        ;;
    esac
    return 0

}

testcase_doing(){ 
    echo "testcase is $1"
	set_log $1
	./L12test.sh 
	get_log $1
}
#testcase_doing L1UE2FGW
