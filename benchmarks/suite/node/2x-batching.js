const common = require("../../common/node.js");

async function main() {
    let datasets = []
    datasets.push("twitter_small_records_2x.json");
    
    const params = common.parseParameters();
    const warmup = params["warmup"];
    const repeat = params["repeat"];
    const baseDir = params["datasets"];
    const engineName = params["engine"];
    const engine = require("../../engine/" + engineName + ".js");
    engine.init()

    for (var dataset of datasets) {
        await common.execute(engineName, warmup, repeat, baseDir+dataset, "TT1-noBatching", engine.queryTT1_noBatching, engine.count);
        await common.execute(engineName, warmup, repeat, baseDir+dataset, "TT1", engine.queryTT1, engine.count);
    }
}

main()