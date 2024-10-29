const common = require("../../common/node.js");

async function main() {
    let datasets = []
    datasets.push("twitter_small_records_changeUserLang0.json");
    datasets.push("twitter_small_records_deleteUser0.json");
    datasets.push("twitter_small_records_deleteUserLang0.json");
    datasets.push("twitter_small_records_changeUserLang25.json");
    datasets.push("twitter_small_records_deleteUser25.json");
    datasets.push("twitter_small_records_deleteUserLang25.json");
    datasets.push("twitter_small_records_changeUserLang50.json");
    datasets.push("twitter_small_records_deleteUser50.json");
    datasets.push("twitter_small_records_deleteUserLang50.json");
    datasets.push("twitter_small_records_changeUserLang75.json");
    datasets.push("twitter_small_records_deleteUser75.json");
    datasets.push("twitter_small_records_deleteUserLang75.json");
    datasets.push("twitter_small_records_changeUserLang100.json");
    datasets.push("twitter_small_records_deleteUser100.json");
    datasets.push("twitter_small_records_deleteUserLang100.json");

    const params = common.parseParameters();
    const warmup = params["warmup"];
    const repeat = params["repeat"];
    const baseDir = params["datasets"];
    const engineName = params["engine"];
    const engine = require("../../engine/" + engineName + ".js");
    engine.init()

    for (var dataset of datasets) {
        await common.execute(engineName, warmup, repeat, baseDir+dataset, "TT4", engine.queryTT4, engine.count);
    }
}

main()