const common = require("../../common/node.js");

async function main() {
    const twitter = "twitter_small_records.json";
    const walmart = "walmart_small_records.json";
    const bestbuy = "bestbuy_small_records.json";
    
    const params = common.parseParameters();
    const warmup = params["warmup"];
    const repeat = params["repeat"];
    const baseDir = params["datasets"];
    const engineName = params["engine"];
    const engine = require("../../engine/" + engineName + ".js");
    engine.init()

    await common.execute(engineName, warmup, repeat, baseDir+twitter, "TT1", engine.queryTT1, engine.count);
    await common.execute(engineName, warmup, repeat, baseDir+twitter, "TT2", engine.queryTT2, engine.count);
    await common.execute(engineName, warmup, repeat, baseDir+twitter, "TT3", engine.queryTT3, engine.count);
    await common.execute(engineName, warmup, repeat, baseDir+twitter, "TT4", engine.queryTT4, engine.count);

    await common.execute(engineName, warmup, repeat, baseDir+walmart, "WM", engine.queryWM, engine.count);

    await common.execute(engineName, warmup, repeat, baseDir+bestbuy, "BB", engine.queryBB, engine.count);
}

main()