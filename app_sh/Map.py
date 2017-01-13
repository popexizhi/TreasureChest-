#-*-coding:utf8-*
HandleL2AuthReq = {\
            "1HandleL2AuthReq":u"HandleL2AuthReq.*",
            "time":u"\d\d*/\d\d*:\d{6}"
            }
HandleDeviceInfoIndication = {\
            "2HandleDeviceInfoIndication":u"HandleDeviceInfoIndication.*",
            "time":u"\d\d*/\d\d*:\d{6}"
            }
EAPServiceWorker_DoConfirmPolicyVersion = {\
#            "3EAPServiceWorker::DoConfirmPolicyVersion":u"EAPServiceWorker::DoConfirmPolicyVersion.*version: 0,",
            "3EAPServiceWorker::DoConfirmPolicyVersion":u"EAPServiceWorker::DoConfirmPolicyVersion.*",
            "time":u"\d\d*/\d\d*:\d{6}"
            }
EAPRpcService_OnDevicePolicyUpdated = {\
#            "4EAPRpcService::OnDevicePolicyUpdated":u"EAPServiceWorker::DoSendConfirmResponse.*",
            "4EAPRpcService::OnDevicePolicyUpdated":u"EAPRpcService::OnDevicePolicyUpdated.*",
            "time":u"\d\d*/\d\d*:\d{6}"
            }
Key_list = ["1HandleL2AuthReq", \
            "2HandleDeviceInfoIndication",\
            "3EAPServiceWorker::DoConfirmPolicyVersion",\
            "4EAPRpcService::OnDevicePolicyUpdated"
            ]
