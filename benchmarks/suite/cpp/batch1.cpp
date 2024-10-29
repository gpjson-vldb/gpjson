#include "../../engine/engine.h"
#include "../../common/cpp.cpp"

int main(int argc, char *argv[]) {
    const char* datasets[3];
    datasets[0] = "twitter_small_records.json";
    datasets[1] = "walmart_small_records.json";
    datasets[2] = "bestbuy_small_records.json";

    const char* parameters[3];
    parseParameters(argc, argv, parameters);
    const char* engineName = engine;
    int warmup = atoi(parameters[0]);
    int repeat = atoi(parameters[1]);
    const char* baseDir = parameters[2];
    init();

    char path[strlen(baseDir) + 150];
    execute(engineName, warmup, repeat, concat(baseDir, datasets[0], path), "TT1", queryTT1, count);
    execute(engineName, warmup, repeat, concat(baseDir, datasets[0], path), "TT2", queryTT2, count);
    execute(engineName, warmup, repeat, concat(baseDir, datasets[0], path), "TT3", queryTT3, count);
    execute(engineName, warmup, repeat, concat(baseDir, datasets[0], path), "TT4", queryTT4, count);

    execute(engineName, warmup, repeat, concat(baseDir, datasets[1], path), "WM", queryWM, count);

    execute(engineName, warmup, repeat, concat(baseDir, datasets[2], path), "BB", queryBB, count);
    
    return 0;
}