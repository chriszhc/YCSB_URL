#!/bin/bash

#YCSB="~/Documents/Research/YCSB"
#YCSB_URL="~/Documents/Research/YCSB_URL"

cd ~/Documents/YCSB

./bin/ycsb load basic -P ./workloads/workloade -p recordcount=1000000 -s > ~/Documents/YCSB_URL/output_ycsb/loade_1M.dat

./bin/ycsb run basic -P ./workloads/workloade -p recordcount=1000000 -s > ~/Documents/YCSB_URL/output_ycsb/txnse_1M.dat

