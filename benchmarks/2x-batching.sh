#!/bin/bash

SUITE=2x-batching
DATASETS="/home/ubuntu/datasets-ext/"

source common.sh

# gpjson
if [ "$noGPU" = false ]
then
    OPTIONS="--gpjson.PartitionSize=1073741824"
    gpjsonWithOptions $GRAAL_PATH "$OPTIONS" $WARMUP $REPEAT $DATASETS
    OPTIONS="--gpjson.PartitionSize=536870912"
    gpjsonWithOptions $GRAAL_PATH "$OPTIONS" $WARMUP $REPEAT $DATASETS
    OPTIONS="--gpjson.PartitionSize=268435456"
    gpjsonWithOptions $GRAAL_PATH "$OPTIONS" $WARMUP $REPEAT $DATASETS
    OPTIONS="--gpjson.PartitionSize=134217728"
    gpjsonWithOptions $GRAAL_PATH "$OPTIONS" $WARMUP $REPEAT $DATASETS
    ###
    OPTIONS="--gpjson.PartitionSize=1073741824 --gpjson.IndexBuilderGridSize=16384"
    gpjsonWithOptions $GRAAL_PATH "$OPTIONS" $WARMUP $REPEAT $DATASETS
    OPTIONS="--gpjson.PartitionSize=536870912 --gpjson.IndexBuilderGridSize=8192"
    gpjsonWithOptions $GRAAL_PATH "$OPTIONS" $WARMUP $REPEAT $DATASETS
    OPTIONS="--gpjson.PartitionSize=268435456 --gpjson.IndexBuilderGridSize=4096"
    gpjsonWithOptions $GRAAL_PATH "$OPTIONS" $WARMUP $REPEAT $DATASETS
    OPTIONS="--gpjson.PartitionSize=134217728 --gpjson.IndexBuilderGridSize=2048"
    gpjsonWithOptions $GRAAL_PATH "$OPTIONS" $WARMUP $REPEAT $DATASETS
fi

echo "Benchmarks done"