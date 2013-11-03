#!/bin/bash

cd ~/Documents/YCSB

./bin/ycsb load basic -P ./workloads/workloade -P ../YCSB_URL/script/small_1K.dat -s > ~/Documents/Research/YCSB_URL/output_ycsb/loade_1K.dat

./bin/ycsb run basic -P ./workloads/workloade -P ../YCSB_URL/script/small_1K.dat -s > ~/Documents/Research/YCSB_URL/output_ycsb/txnse_1K.dat


