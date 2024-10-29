# exit when any command fails
set -e

# keep track of the last executed command
trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
# echo an error message before exiting
trap 'echo "\"${last_command}\" command exited with exit code $?."' EXIT

# Default values
NODE_PATH="$NODE_DIR/bin"
GRAAL_PATH="$GRAAL_DIR/bin"
WARMUP=5
REPEAT=10
THREADS=11 #12-1 (java default for a 12 core machine)
noGPU=false

# Read command parameters - usage: -g -w {number} -r {number} -t {number}
while getopts gw:r:t:d: OPT
do
    case "$OPT" in
        g) noGPU=true ;;
        w) WARMUP=${OPTARG} ;;
        r) REPEAT=${OPTARG} ;;
        t) THREADS=${OPTARG} ;;
        d) DATASETS=${OPTARG} ;;
    esac
done

echo "Starting benchmarks. skip GPU: $noGPU, warmup: $WARMUP, repeat: $REPEAT, threads: $THREADS, datasets: $DATASETS"
echo "engine,dataset,query,time,stddev,results,warmup,repeat,options" > $SUITE.csv

nodejsonpath() {
    node nodejsonpath $1 $2 $3 $4 $5
}

nodejsonpathplus() {
    node nodejsonpathplus $1 $2 $3 $4 $5
}

nodemanual() {
    node nodemanual $1 $2 $3 $4 $5
}

nodesimdjson() {
    node nodesimdjson $1 $2 $3 $4 $5
}

pison() {
    bin pison $1 $2 $3 $4
}

rapidjson() {
    bin rapidjson $1 $2 $3 $4
}

simdjson() {
    bin simdjson $1 $2 $3 $4
}

gpjson() {
    echo "running gpjson"
    execute "$1/node --jvm --polyglot suite/node/$SUITE.js warmup=$2 repeat=$3 engine=gpjson datasets=$4" "none"
}

gpjsonWithOptions() {
    echo "running gpjson with $2"
    execute "$1/node --jvm --polyglot --experimental-options $2 suite/node/$SUITE.js warmup=$3 repeat=$4 engine=gpjson datasets=$5" "$2"
}

javajsonpath() {
    cd suite/javajsonpath
    echo "running javajsonpath"
    mvn package > /dev/null 2>&1
    cd ../..
    execute "java -cp suite/javajsonpath/target/javajsonpath-1.0-SNAPSHOT-jar-with-dependencies.jar it.polimi.$1 warmup=$2 repeat=$3 threads=$4 datasets=$5" "none"
}

node() {
    echo "running $1"
    execute "$2/node suite/node/$SUITE.js warmup=$3 repeat=$4 engine=$1 datasets=$5" "none"
}

bin() {
    echo "running $1"
    execute "suite/cpp/bin/$1/$2 warmup=$3 repeat=$4 datasets=$5" "none"
}

binCompile() {
    cd suite/cpp
    make $SUITE > /dev/null 2>&1
    cd ../..
}

execute() {
    $1 | while read line; do echo ${line},$2; done >> $SUITE.csv
}