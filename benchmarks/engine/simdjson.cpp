#include <iostream>
#include "../src/simdjson/simdjson.h"

#include <math.h>
#include <chrono>
#include <string>
#include <vector>

#include "engine.h"

using namespace std;

char const *engine = "simdjson";

class StringViewResult : public Result {
    public:
    string_view res;

    StringViewResult(string_view str) {
        res = str;
    }
};

void init() {}

int count(vector<Result> result) {
    return result.size();
}

// $.user.lang
vector<Result> queryTT1(char* path) {
    simdjson::dom::parser parser;
    simdjson::dom::document_stream stream = parser.load_many(path);

    vector<Result> result;
    for (simdjson::dom::element doc : stream) {
        auto elem = doc["user"]["lang"];
        simdjson::error_code error = elem.error();
        if (error == simdjson::error_code::SUCCESS) {
            string_view value = elem.get_string();
            result.push_back(StringViewResult(value));
        }
    }
    return result;
}

// {$.user.lang, $.lang}
vector<Result> queryTT2(char* path) {
    simdjson::dom::parser parser;
    simdjson::dom::document_stream stream = parser.load_many(path);

    vector<Result> result;
    for (simdjson::dom::element doc : stream) {
        auto elem = doc["user"]["lang"];
        simdjson::error_code error = elem.error();
        if (error == simdjson::error_code::SUCCESS) {
            string_view value = elem.get_string();
            result.push_back(StringViewResult(value));
        }

        elem = doc["lang"];
        error = elem.error();
        if (error == simdjson::error_code::SUCCESS) {
            string_view value = elem.get_string();
            result.push_back(StringViewResult(value));
        }
    }
    return result;
}

// $.user.lang[?(@ == 'nl')]"
vector<Result> queryTT3(char* path) {
    simdjson::dom::parser parser;
    simdjson::dom::document_stream stream = parser.load_many(path);

    vector<Result> result;
    for (simdjson::dom::element doc : stream) {
        auto elem = doc["user"]["lang"];
        simdjson::error_code error = elem.error();
        if (error == simdjson::error_code::SUCCESS) {
            string_view value = elem.get_string();
            if ((string_view) value == "nl") {
                result.push_back(StringViewResult(value));
            }
        }
    }
    return result;
}

// $.user.lang[?(@ == 'en')]"
vector<Result> queryTT4(char* path) {
    simdjson::dom::parser parser;
    simdjson::dom::document_stream stream = parser.load_many(path);

    vector<Result> result;
    for (simdjson::dom::element doc : stream) {
        auto elem = doc["user"]["lang"];
        simdjson::error_code error = elem.error();
        if (error == simdjson::error_code::SUCCESS) {
            string_view value = elem.get_string();
            if ((string_view) value == "en") {
                result.push_back(StringViewResult(value));
            }
        }
    }
    return result;
}

// {$.bestMarketplacePrice.price, $.name}
vector<Result> queryWM(char* path) {
    simdjson::dom::parser parser;
    simdjson::dom::document_stream stream = parser.load_many(path);

    vector<Result> result;
    for (simdjson::dom::element doc : stream) {
        auto elem = doc["bestMarketplacePrice"]["price"];
        simdjson::error_code error = elem.error();
        if (error == simdjson::error_code::SUCCESS) {
            if (elem.is_double()) {
                double d = elem.get_double();
                string_view value = string_view(to_string(d));
                result.push_back(StringViewResult(value));
            }  
        }

        elem = doc["name"];
        error = elem.error();
        if (error == simdjson::error_code::SUCCESS) {
            string_view value = elem.get_string();
            result.push_back(StringViewResult(value));
        }
    }
    return result;
}

// $.categoryPath[1:3].id
vector<Result> queryBB(char* path) {
    simdjson::dom::parser parser;
    simdjson::dom::document_stream stream = parser.load_many(path);

    vector<Result> result;
    for (simdjson::dom::element doc : stream) {
        int idx = 0;
        auto arr = doc["categoryPath"];
        for (auto value : arr) {
            if (idx >= 3) break;
            if (idx >= 1) {
                auto elem = value["id"];
                simdjson::error_code error = elem.error();
                if (error == simdjson::error_code::SUCCESS) {
                    string_view value = elem.get_string();
                    result.push_back(StringViewResult(value));
                } 
            }
            idx++;
        }
    }
    return result;
}