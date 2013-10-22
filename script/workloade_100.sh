#!/bin/bash

#YCSB="~/Documents/Research/YCSB"
#YCSB_URL="~/Documents/Research/YCSB_URL"

cd ~/Documents/Research/YCSB

./bin/ycsb load basic -P ./workloads/workloade -s > ~/Documents/Research/YCSB_URL/output_ycsb/loade_1000.dat

./bin/ycsb run basic -P ./workloads/workloade -s > ~/Documents/Research/YCSB_URL/output_ycsb/txnse_1000.dat

