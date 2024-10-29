#!/bin/bash

SUITE=batch1
DATASETS="/home/ubuntu/datasets-ext/"

source common.sh

# gpjson
if [ "$noGPU" = false ]
then
    gpjson $GRAAL_PATH $WARMUP $REPEAT $DATASETS
fi

# nodejsonpath
nodejsonpath $NODE_PATH $WARMUP $REPEAT $DATASETS

# nodejsonpathplus
nodejsonpathplus $NODE_PATH $WARMUP $REPEAT $DATASETS

# nodemanual
nodemanual $NODE_PATH $WARMUP $REPEAT $DATASETS

# nodesimdjson
nodesimdjson $NODE_PATH $WARMUP $REPEAT $DATASETS

# javajsonpath
javajsonpath Batch1 $WARMUP $REPEAT $THREADS $DATASETS

binCompile

# pison
pison $SUITE $WARMUP $REPEAT $DATASETS

# rapidjson
rapidjson $SUITE $WARMUP $REPEAT $DATASETS

# simdjson
simdjson $SUITE $WARMUP $REPEAT $DATASETS

echo "Benchmarks done"