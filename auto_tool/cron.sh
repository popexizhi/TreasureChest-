#!/bin/bash
find /root/use_pcap -name \*.\*cap\* -exec  tcpreplay -i tap0 -M 100 -l 1 {} \;
