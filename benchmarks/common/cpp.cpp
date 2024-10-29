using namespace std;

uint64_t timeSinceEpochMillisec() {
  using namespace std::chrono;
  return duration_cast<milliseconds>(system_clock::now().time_since_epoch()).count();
}

double avg(uint64_t *delays, int n) {
    uint64_t sum = 0;
    for (int i=0; i<n; i++) {
        sum += delays[i];
    }
    return (double)sum/n;
}

double stdDev(uint64_t *delays, int n, int average) {
    int sum = 0;
    for (int i=0; i<n; i++) {
        sum += (delays[i]-average)*(delays[i]-average);
    }
    return sqrt((float)sum/(n-1));
}

void execute(const char* engine, int warmup, int repeat, char* dataset, const char* query, vector<Result> (*queryFunction)(char*), int (*countFunction)(vector<Result>)) {
    vector<Result> result;
    for (int i=0; i < warmup; i++) 
        result = queryFunction(dataset);
    int numResults = countFunction(result);
    uint64_t delays[repeat];
    uint64_t beginTime;
    for (int i=0; i < repeat; i++) {
        beginTime = timeSinceEpochMillisec();
        queryFunction(dataset);
        delays[i] = timeSinceEpochMillisec() - beginTime;
    }
    double average = avg(delays, repeat);
    double std = stdDev(delays, repeat, average);
    cout << engine<<","<<dataset<<","<<query<<","<<average<<","<<std<<","<<numResults<<","<<warmup<<","<<repeat << endl;
}

char const **parseParameters(int argc, char *argv[], char const **parameters) { 
    parameters[0] = "5";
    parameters[1] = "10";
    parameters[2] = "/home/ubuntu/datasets/";
    for(int i = 1; i < argc; i++) {
        if(!strncmp(argv[i], "warmup=", 7)) {
            parameters[0] = &argv[i][7];
        }
        else if(!strncmp(argv[i], "repeat=", 7)) {
            parameters[1] = &argv[i][7];
        }
        else if(!strncmp(argv[i], "datasets=", 9)) {
            parameters[2] = &argv[i][9];
        }
    }
    return parameters;
}

char* concat(const char* baseDir, const char* fileName, char* path) {
    strcpy(path, baseDir);
    strcat(path, fileName);
    return path;
}