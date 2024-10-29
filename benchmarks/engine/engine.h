#include <bits/stdc++.h>
using namespace std;

#ifndef ENGINE
#define ENGINE

extern char const *engine;

class Result {};
class StringResult : public Result {
    public:
    string res;

    StringResult(string str) {
        res = str;
    }
};
class CharPtResult : public Result {
    public:
    char* res;

    CharPtResult(char* str) {
        res = str;
    }
};

void init();
int count(vector<Result> result);

vector<Result> queryTT1(char* file);
vector<Result> queryTT2(char* file);
vector<Result> queryTT3(char* file);
vector<Result> queryTT4(char* file);
vector<Result> queryWM(char* file);
vector<Result> queryBB(char* file);

#endif