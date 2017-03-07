#!/bin/bash
set_log(){
    logConfig="logConfig.cfg"
    echo "">${logConfig}
	echo "set logConfig.cfg for testcase:$0**********************"
    case $0 in
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
        echo "no has this testcase name"
        ;;
    esac
	cat ${logConfig}
}

get_log(){
	echo "testcase log check: $0****************************************"
	echo "fgw get log **************************************************"
	cat fgw.log.txt|grep "EpollLoop Throughput"
	echo "ue get log **************************************************"
	cat log/ue_client_200.log.txt|grep "EpollLoop Throughput"
}

testcase_doing(){ 
    echo "testcase is $0"
	set_log $0
	./L12test.sh 
	get_log $0
}

testcase_doing L1UE2FGW
