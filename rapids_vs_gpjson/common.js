const { performance } = require('perf_hooks');
const fs = require('node:fs');

async function execute(warmup, repeat, dataset, output, queryFunction) {
    var result;
    for (let i = 0; i < warmup; i++)
        result = await queryFunction(dataset);
    var start = 0;
    var delays = [];
    for (let i = 0; i < repeat; i++) {
        start = performance.now();
        await queryFunction(dataset);
        delays.push(performance.now() - start);
    }
    fs.writeFileSync(output, JSON.stringify(delays));
}

function parseParameters() {
    const myArgs = process.argv.slice(2);
    var params = {};
    let idx = myArgs.findIndex(v => v.includes("warmup="));
    params['warmup'] = idx >= 0 ? parseInt(myArgs[idx].substring(7)) : 5;
    idx = myArgs.findIndex(v => v.includes("repeat="));
    params['repeat'] = idx >= 0 ? parseInt(myArgs[idx].substring(7)) : 10;
    idx = myArgs.findIndex(v => v.includes("datasets="));
    params['datasets'] = idx >= 0 ? myArgs[idx].substring(9) : "/local/stalluri/gpjson_datasets";
    idx = myArgs.findIndex(v => v.includes("output="));
    params['output'] = idx >= 0 ? myArgs[idx].substring(7) : "/var/scratch/stalluri/gpjson/rapids_vs_gpjson/results";
    return params;
}

module.exports = { execute, parseParameters};