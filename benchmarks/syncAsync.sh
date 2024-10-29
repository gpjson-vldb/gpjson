#!/bin/bash

SUITE=syncAsync
DATASETS="/home/ubuntu/datasets-ext/"

source common.sh

# gpjson
if [ "$noGPU" = false ]
then
    OPTIONS="--gpjson.grcuda.ExecutionPolicy=async"
    gpjsonWithOptions $GRAAL_PATH $OPTIONS $WARMUP $REPEAT $DATASETS

    OPTIONS="--gpjson.grcuda.ExecutionPolicy=sync"
    gpjsonWithOptions $GRAAL_PATH $OPTIONS $WARMUP $REPEAT $DATASETS
fi

echo "Benchmarks done"