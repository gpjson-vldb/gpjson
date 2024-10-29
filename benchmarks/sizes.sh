#!/bin/bash

SUITE=sizes
DATASETS="/home/ubuntu/datasets-ext/"

source common.sh

# gpjson
if [ "$noGPU" = false ]
then
    gpjson $GRAAL_PATH $WARMUP $REPEAT $DATASETS
fi

# javajsonpath
javajsonpath Sizes $WARMUP $REPEAT $THREADS $DATASETS

binCompile

# pison
pison $SUITE $WARMUP $REPEAT $DATASETS

# rapidjson
rapidjson $SUITE $WARMUP $REPEAT $DATASETS

# simdjson
simdjson $SUITE $WARMUP $REPEAT $DATASETS

echo "Benchmarks done"