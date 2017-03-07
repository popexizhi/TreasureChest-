#!/usr/bin/env bats
load setlogconfig

@test "addition using bc" {
    result="$(echo 2+2 | bc)"
    [ "$result" -eq 4 ]
}
@test "setlog use testcase" {
    run set_log L1UE2FGW
    [ "$status" -eq 0 ]
    echo $output
    #[ "$output" = "param.Padding:Mode = 1 // enable stream test, layer 1, ue->fgw" ]
    #result=`cat ${cfp}`
    #[ "${result[0]}" = "param.test:test_service_mode = 4 //disable layer2 socket test"  ]
}
@test "get log testcase" {
    run get_log L1UE2FGW  
    [ "$status" -eq 0 ]
    echo $output
}
