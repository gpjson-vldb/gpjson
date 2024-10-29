#!/bin/bash

DATASETS_SRC="/var/scratch/stalluri/gpjson/gitrepo/datasets"
DATASETS_DIR="/local/stalluri/gpjson_datasets"
OUTPUT_DIR="/var/scratch/stalluri/gpjson/rapids_vs_gpjson/results/a100"

create_dataset() {
    rm -f "$DATASETS_DIR/twitter_small_records_${1}x.json"
    echo $1
    for i in $( seq 1 $1 )
    do 
        cat "$DATASETS_DIR/twitter_small_records.json" >> "$DATASETS_DIR/twitter_small_records_${1}x.json"
    done
}

# Copy dataset to local
mkdir -p $DATASETS_DIR
rsync -a $DATASETS_SRC/ $DATASETS_DIR

# Create larger datasets
create_dataset 2
create_dataset 4
create_dataset 8

# mkdir -p $OUTPUT_DIR

# node --jvm --polyglot sizes.js warmup=5 repeat=10 datasets="$DATASETS_DIR" output="$OUTPUT_DIR"

OUTPUT_DIR2="/var/scratch/stalluri/gpjson/rapids_vs_gpjson/pyresults/a100"
mkdir -p $OUTPUT_DIR2

python cuSizes.py warmup=5 repeat=10 datasets="$DATASETS_DIR" output="$OUTPUT_DIR2"