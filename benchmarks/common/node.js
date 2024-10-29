const { performance } = require('perf_hooks');

async function execute(engine, warmup, repeat, dataset, query, queryFunction, countFunction) {
    var result;
    for (let i = 0; i < warmup; i++)
        result = await queryFunction(dataset);
    var numResults = countFunction(result);
    var start = 0;
    var delays = [];
    for (let i = 0; i < repeat; i++) {
        start = performance.now();
        await queryFunction(dataset);
        delays.push(performance.now() - start);
    }
    average = delays.reduce((total, delay) => total + delay, 0) / repeat;
    std = Math.sqrt(delays.reduce((total, delay) => total + Math.pow((delay - average), 2), 0) / (repeat - 1));
    console.log(engine + "," + dataset + "," + query + "," + average + "," + std + "," + numResults + "," + warmup + "," + repeat);
}

function parseParameters() {
    const myArgs = process.argv.slice(2);
    var params = {};
    let idx = myArgs.findIndex(v => v.includes("warmup="));
    params['warmup'] = idx >= 0 ? parseInt(myArgs[idx].substring(7)) : 5;
    idx = myArgs.findIndex(v => v.includes("repeat="));
    params['repeat'] = idx >= 0 ? parseInt(myArgs[idx].substring(7)) : 10;
    idx = myArgs.findIndex(v => v.includes("engine="));
    params['engine'] = idx >= 0 ? myArgs[idx].substring(7) : "gpjson";
    idx = myArgs.findIndex(v => v.includes("datasets="));
    params['datasets'] = idx >= 0 ? myArgs[idx].substring(9) : "/home/ubuntu/datasets/";
    return params;
}

module.exports = { execute, parseParameters};