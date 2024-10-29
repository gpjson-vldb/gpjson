const common = require("../../common/node.js");

async function main() {
    let datasets = []
    datasets.push("twitter_small_records.json");
    datasets.push("twitter_small_records_0.125x.json");
    datasets.push("twitter_small_records_0.25x.json");
    datasets.push("twitter_small_records_0.5x.json");
    datasets.push("twitter_small_records_2x.json");
    datasets.push("twitter_small_records_4x.json");
    datasets.push("twitter_small_records_8x.json");
    datasets.push("twitter_small_records_12x.json");
    datasets.push("twitter_small_records_16x.json");

    const params = common.parseParameters();
    const warmup = params["warmup"];
    const repeat = params["repeat"];
    const engineName = params["engine"];
    const baseDir = params["datasets"];
    const engine = require("../../engine/" + engineName + ".js");
    engine.init()
    
    for (var dataset of datasets) {
        await common.execute(engineName, warmup, repeat, baseDir+dataset, "TT4", engine.queryTT4, engine.count);
    }
}

main()