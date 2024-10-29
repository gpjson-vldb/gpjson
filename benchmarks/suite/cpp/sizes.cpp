#include "../../engine/engine.h"
#include "../../common/cpp.cpp"

int main(int argc, char *argv[]) {
    const char* datasets[9];
    datasets[0] = "twitter_small_records.json";
    datasets[1] = "twitter_small_records_0.125x.json";
    datasets[2] = "twitter_small_records_0.25x.json";
    datasets[3] = "twitter_small_records_0.5x.json";
    datasets[4] = "twitter_small_records_2x.json";
    datasets[5] = "twitter_small_records_4x.json";
    datasets[6] = "twitter_small_records_8x.json";
    datasets[7] = "twitter_small_records_12x.json";
    datasets[8] = "twitter_small_records_16x.json";

    const char* parameters[3];
    parseParameters(argc, argv, parameters);
    const char* engineName = engine;
    int warmup = atoi(parameters[0]);
    int repeat = atoi(parameters[1]);
    const char* baseDir = parameters[2];
    init();

    char path[strlen(baseDir) + 150];
    for (int i=0; i<9; i++) {
        execute(engineName, warmup, repeat, concat(baseDir, datasets[i], path), "TT4", queryTT4, count);
    }
    
    return 0;
}
