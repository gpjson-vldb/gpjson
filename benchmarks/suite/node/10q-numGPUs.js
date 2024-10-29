const common = require("../../common/node.js");

async function main() {
    let datasets = []
    datasets.push("twitter_small_records_16x.json");
    datasets.push("twitter_small_records_32x.json");
    datasets.push("twitter_small_records_64x.json");
    datasets.push("twitter_small_records_128x.json");
    
    const params = common.parseParameters();
    const warmup = params["warmup"];
    const repeat = params["repeat"];
    const baseDir = params["datasets"];
    const engineName = params["engine"];
    const engine = require("../../engine/" + engineName + ".js");
    engine.init()

    for (var dataset of datasets) {
        engine.queryTT1_10qSetup(baseDir+dataset);
        await common.execute(engineName, warmup, repeat, baseDir+dataset, "TT1", engine.queryTT1_10q, engine.count);
        engine.queryTT1_10qFree();
    }
}

main()