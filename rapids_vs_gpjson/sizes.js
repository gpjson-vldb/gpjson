
const common = require("./common.js");

async function main() {
    const engine = Polyglot.eval('gpjson', "GJ");
    engine.buildKernels();

    let datasets = [
        "twitter_small_records.json",
        "twitter_small_records_0.125x.json",
        "twitter_small_records_0.25x.json",
        "twitter_small_records_0.5x.json",
        "twitter_small_records_2x.json",
        "twitter_small_records_4x.json",
        "twitter_small_records_8x.json"
    ]

    const params = common.parseParameters();
    const warmup = params["warmup"];
    const repeat = params["repeat"];
    const datasetDir = params["datasets"];
    const outputDir = params["output"];
    
    for (var dataset of datasets) {
        await common.execute(warmup, repeat, 
            `${datasetDir}/${dataset}`, 
            `${outputDir}/${dataset}`,
            async (ds) => {
                console.log(ds)
                engine.query(ds, ["$.user.lang"], true, true);
            }
        );
    }
}

main()