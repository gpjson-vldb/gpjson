#!/bin/bash

SUITE=numGPUs
DATASETS="/home/ubuntu/datasets-ext/"

source common.sh

# gpjson
if [ "$noGPU" = false ]
then
    OPTIONS="--gpjson.grcuda.NumberOfGPUs=1"
    gpjsonWithOptions $GRAAL_PATH $OPTIONS $WARMUP $REPEAT $DATASETS

    OPTIONS="--gpjson.grcuda.NumberOfGPUs=2"
    gpjsonWithOptions $GRAAL_PATH $OPTIONS $WARMUP $REPEAT $DATASETS

    OPTIONS="--gpjson.grcuda.NumberOfGPUs=4"
    gpjsonWithOptions $GRAAL_PATH $OPTIONS $WARMUP $REPEAT $DATASETS

    OPTIONS="--gpjson.grcuda.NumberOfGPUs=8"
    gpjsonWithOptions $GRAAL_PATH $OPTIONS $WARMUP $REPEAT $DATASETS
fi

echo "Benchmarks done"