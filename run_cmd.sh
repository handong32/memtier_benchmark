#!/bin/bash

NUMREQ=4
NUMTHD=1
NUMC=1
RATIO='1:0'
DATA=~/data2.csv

./memtier_benchmark --server=10.10.1.2 --hide-histogram -c $NUMC -t $NUMTHD -n $NUMREQ --data-import $DATA --ratio=$RATIO -D -I
