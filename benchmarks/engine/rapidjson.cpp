#include <cstdio>
#include <iostream>
#include <chrono>
#include <string>
#include <vector>
#include <math.h>

#include "../src/rapidjson/document.h"
#include "../src/rapidjson/filereadstream.h"

#include "engine.h"

using namespace std;

char const *engine = "rapidjson";

void init() {}

int count(vector<Result> result) {
    return result.size();
}

// $.user.lang
vector<Result> queryTT1(char* path) {
    FILE* fp = fopen(path, "r");
    char readBuffer[65536];
    rapidjson::FileReadStream is(fp, readBuffer, sizeof(readBuffer));
    rapidjson::Document d;
    d.ParseStream<rapidjson::kParseStopWhenDoneFlag>(is);

    vector<Result> result;
    while(!d.HasParseError()) {
        if (d.IsObject() && d.HasMember("user") && d["user"].IsObject()) {
            if (d["user"].HasMember("lang") && d["user"]["lang"].IsString()) {
                string value = d["user"]["lang"].GetString();
                result.push_back(StringResult(value));
            }
        }
        d.ParseStream<rapidjson::kParseStopWhenDoneFlag>(is);
    }
    
    fclose(fp);
    return result;
}

// {$.user.lang, $.lang}
vector<Result> queryTT2(char* path) {
    FILE* fp = fopen(path, "r");
    char readBuffer[65536];
    rapidjson::FileReadStream is(fp, readBuffer, sizeof(readBuffer));
    rapidjson::Document d;
    d.ParseStream<rapidjson::kParseStopWhenDoneFlag>(is);

    vector<Result> result;
    while(!d.HasParseError()) {
        if (d.IsObject() && d.HasMember("user") && d["user"].IsObject()) {
            if (d["user"].HasMember("lang") && d["user"]["lang"].IsString()) {
                string value = d["user"]["lang"].GetString();
                result.push_back(StringResult(value));
            }
        }
        if (d.IsObject() && d.HasMember("lang") && d["lang"].IsString()) {
            string value = d["lang"].GetString();
            result.push_back(StringResult(value));
        }
        d.ParseStream<rapidjson::kParseStopWhenDoneFlag>(is);
    }
    
    fclose(fp);
    return result;
}

// $.user.lang[?(@ == 'nl')]"
vector<Result> queryTT3(char* path) {
    FILE* fp = fopen(path, "r");
    char readBuffer[65536];
    rapidjson::FileReadStream is(fp, readBuffer, sizeof(readBuffer));
    rapidjson::Document d;
    d.ParseStream<rapidjson::kParseStopWhenDoneFlag>(is);

    vector<Result> result;
    while(!d.HasParseError()) {
        if (d.IsObject() && d.HasMember("user") && d["user"].IsObject()) {
            if (d["user"].HasMember("lang") && d["user"]["lang"].IsString() && d["user"]["lang"] == "nl") {
                string value = d["user"]["lang"].GetString();
                result.push_back(StringResult(value));
            }
        }
        d.ParseStream<rapidjson::kParseStopWhenDoneFlag>(is);
    }
    
    fclose(fp);
    return result;
}

// $.user.lang[?(@ == 'en')]"
vector<Result> queryTT4(char* path) {
    FILE* fp = fopen(path, "r");
    char readBuffer[65536];
    rapidjson::FileReadStream is(fp, readBuffer, sizeof(readBuffer));
    rapidjson::Document d;
    d.ParseStream<rapidjson::kParseStopWhenDoneFlag>(is);

    vector<Result> result;
    while(!d.HasParseError()) {
        if (d.IsObject() && d.HasMember("user") && d["user"].IsObject()) {
            if (d["user"].HasMember("lang") && d["user"]["lang"].IsString() && d["user"]["lang"] == "en") {
                string value = d["user"]["lang"].GetString();
                result.push_back(StringResult(value));
            }
        }
        d.ParseStream<rapidjson::kParseStopWhenDoneFlag>(is);
    }
    
    fclose(fp);
    return result;
}

// {$.bestMarketplacePrice.price, $.name}
vector<Result> queryWM(char* path) {
    FILE* fp = fopen(path, "r");
    char readBuffer[65536];
    rapidjson::FileReadStream is(fp, readBuffer, sizeof(readBuffer));
    rapidjson::Document d;
    d.ParseStream<rapidjson::kParseStopWhenDoneFlag>(is);

    vector<Result> result;
    while(!d.HasParseError()) {
        if (d.IsObject() && d.HasMember("bestMarketplacePrice") && d["bestMarketplacePrice"].IsObject()) {
            if (d["bestMarketplacePrice"].HasMember("price") && d["bestMarketplacePrice"]["price"].IsNumber()) {
                string value = to_string(d["bestMarketplacePrice"]["price"].GetDouble());
                result.push_back(StringResult(value));
            }
        }
        if (d.IsObject() && d.HasMember("name") && d["name"].IsString()) {
            string value = d["name"].GetString();
            result.push_back(StringResult(value));
        }
        d.ParseStream<rapidjson::kParseStopWhenDoneFlag>(is);
    }
    
    fclose(fp);
    return result;
}

// $.categoryPath[1:3].id
vector<Result> queryBB(char* path) {
    FILE* fp = fopen(path, "r");
    char readBuffer[65536];
    rapidjson::FileReadStream is(fp, readBuffer, sizeof(readBuffer));
    rapidjson::Document d;
    d.ParseStream<rapidjson::kParseStopWhenDoneFlag>(is);

    vector<Result> result;
    while(!d.HasParseError()) {
        if (d.IsObject() && d.HasMember("categoryPath") && d["categoryPath"].IsArray()) {
            for (int i=1; i<3 && i<d["categoryPath"].Size(); i++) {
                if (d["categoryPath"][i].IsObject() && d["categoryPath"][i].HasMember("id") && d["categoryPath"][i]["id"].IsString()) {
                    string value = d["categoryPath"][i]["id"].GetString();
                    result.push_back(StringResult(value));
                }
            }
        }
        d.ParseStream<rapidjson::kParseStopWhenDoneFlag>(is);
    }
    
    fclose(fp);
    return result;
}