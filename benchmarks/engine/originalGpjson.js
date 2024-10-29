const { count } = require('console');
const fs = require('fs');
const { performance } = require('perf_hooks');

var baseDir;
var gpjson;
var DEBUG;

// https://stackoverflow.com/a/18650828
function formatBytes(bytes, decimals = 2) {
    if (bytes === 0) return '0 bytes';
    const k = 1000;
    const dm = decimals < 0 ? 0 : decimals;
    const sizes = ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
}

function init(dir) {
    baseDir = dir;
    gpjson = Polyglot.eval('gpjson', 'jsonpath');
    const myArgs = process.argv.slice(2);
    DEBUG = myArgs.includes("DEBUG") ? true : false;
    let idx = myArgs.findIndex(v => v.includes("warmup="));
    const warmup_query = idx >= 0 ? parseInt(myArgs[idx].substring(7)) : 5;
    idx = myArgs.findIndex(v => v.includes("repeat="));
    const repeat_query = idx >= 0 ? parseInt(myArgs[idx].substring(7)) : 10;
    return [warmup_query, repeat_query];
}

function countResults(result) {
    var count = 0;
    for (let q = 0; q < result.length; q++) {
        for (let i = 0; i < result[q].length; i++) {
            for (let j = 0; j < result[q][i].length; j++) {
                if (result[q][i][j] != null)
                    count += 1;
            }
        }
    }
    return count;
}

// $.user.lang
function query_TT1(dataset) {
    result = gpjson.query(baseDir + dataset, "$.user.lang");
    return result;
}

// {$.user.lang, $.lang}
function query_TT2(dataset) {
    result = gpjson.query(baseDir + dataset, ["$.user.lang", "$.lang"]);
    return result;
}

// $.user.lang[?(@ == 'nl')]
function query_TT3(dataset) {
    result = gpjson.query(baseDir + dataset, "$.user.lang[?(@ == 'nl')]");
    return result;
}

// $.user.lang[?(@ == 'en')]
function query_TT4(dataset) {
    result = gpjson.query(baseDir + dataset, "$.user.lang[?(@ == 'en')]");
    return result;
}

// {$.bestMarketplacePrice.price, $.name}
function query_WM(dataset) {
    result = gpjson.query(baseDir + dataset, ["$.bestMarketplacePrice.price", "$.name"]);
    return result;
}

// $.categoryPath[1:3].id
function query_BB(dataset) {
    result = gpjson.query(baseDir + dataset, "$.categoryPath[1:3].id");
    return result;
}

function execute(warmup_query, repeat_query, dataset, func, query) {
    if (DEBUG) console.log("Starting warmup queries on dataset " + dataset);
    var result;
    for (let i = 0; i < warmup_query; i++)
        result = func(dataset);
    var numResults = countResults(result);
    var start = 0;
    var delays = [];
    for (let i = 0; i < repeat_query; i++) {
        start = performance.now();
        func(dataset);
        delays.push(performance.now() - start);
    }
    average = delays.reduce((total, delay) => total + delay, 0) / repeat_query;
    std = Math.sqrt(delays.reduce((total, delay) => total + Math.pow((delay - average), 2), 0) / (repeat_query - 1));
    const speed = fs.statSync(baseDir + dataset).size / average * 1000;
    if (DEBUG) console.log("Executed query " + query + " on dataset " + dataset + " in " + average + "ms | " + formatBytes(speed) + "/s; results: " + numResults);
    console.log("gpjson," + dataset + "," + query + "," + average + "," + std + "," + numResults + "," + warmup_query + "," + repeat_query);
}

module.exports = function() {
    this.init = init;
    this.execute = execute;
    this.query_TT1 = query_TT1;
    this.query_TT2 = query_TT2;
    this.query_TT3 = query_TT3;
    this.query_TT4 = query_TT4;
    this.query_WM = query_WM;
    this.query_BB = query_BB;
}
