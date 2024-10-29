#include "../../engine/engine.h"
#include "../../common/cpp.cpp"

int main(int argc, char *argv[]) {
    const char* datasets[15];
    datasets[0] = "twitter_small_records_changeUserLang0.json";
    datasets[1] = "twitter_small_records_deleteUser0.json";
    datasets[2] = "twitter_small_records_deleteUserLang0.json";
    datasets[3] = "twitter_small_records_changeUserLang25.json";
    datasets[4] = "twitter_small_records_deleteUser25.json";
    datasets[5] = "twitter_small_records_deleteUserLang25.json";
    datasets[6] = "twitter_small_records_changeUserLang50.json";
    datasets[7] = "twitter_small_records_deleteUser50.json";
    datasets[8] = "twitter_small_records_deleteUserLang50.json";
    datasets[9] = "twitter_small_records_changeUserLang75.json";
    datasets[10] = "twitter_small_records_deleteUser75.json";
    datasets[11] = "twitter_small_records_deleteUserLang75.json";
    datasets[12] = "twitter_small_records_changeUserLang100.json";
    datasets[13] = "twitter_small_records_deleteUser100.json";
    datasets[14] = "twitter_small_records_deleteUserLang100.json";

    const char* parameters[3];
    parseParameters(argc, argv, parameters);
    const char* engineName = engine;
    int warmup = atoi(parameters[0]);
    int repeat = atoi(parameters[1]);
    const char* baseDir = parameters[2];
    init();

    char path[strlen(baseDir) + 150];
    for (int i=0; i<15; i++) {
        execute(engineName, warmup, repeat, concat(baseDir, datasets[i], path), "TT4", queryTT4, count);
    }
    
    return 0;
}