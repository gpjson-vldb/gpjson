#include "../src/pison/RecordLoader.h"
#include "../src/pison/BitmapIterator.h"
#include "../src/pison/BitmapConstructor.h"

#include <math.h>
#include <chrono>
#include <iostream>
#include <fstream>
#include <bits/stdc++.h>

#include "engine.h"

char const *engine = "pison";

void init() {}

int count(vector<Result> result) {
    return result.size();
}

Record* getRecord(char* path) {
    Record* rec = RecordLoader::loadSingleRecord(path);
    if (rec == NULL) {
        cout<<"record loading fails."<<endl;
        exit(-1);
    }
    return rec;
}

RecordSet* getRecordSet(char* path) {
    RecordSet* rec_set = RecordLoader::loadRecords(path);
    if (rec_set->size() == 0) {
        cout<<"record loading fails."<<endl;
        exit(-1);
    }
    return rec_set;
}

// $.user.lang
vector<Result> queryTT1(char* file) {
    RecordSet* record_set = getRecordSet(file);

    // set the number of threads for parallel bitmap construction
    int thread_num = 1;
    /* set the number of levels of bitmaps to create, either based on the
     * query or the JSON records. E.g., query $[*].user.id needs three levels
     * (level 0, 1, 2), but the record may be of more than three levels
     */
    int level_num = 3;

    /* process the records one by one: for each one, first build bitmap, then perform
     * the query with a bitmap iterator
     */
    int num_recs = record_set->size();
    Bitmap* bm = NULL;

    vector<Result> result;
    for (int i = 0; i < num_recs; i++) {
        bm = BitmapConstructor::construct((*record_set)[i], thread_num, level_num);
        BitmapIterator* iter = BitmapConstructor::getIterator(bm);
        if (iter->isObject() && iter->moveToKey("user")) {
            if (iter->down() == false) continue;
            if (iter->isObject() && iter->moveToKey("lang")) {
                char* value = iter->getValue();
                result.push_back(CharPtResult(value));
                if (value) free(value);
            }
            iter->up();
        }
        delete iter;
        delete bm;
    }
    delete record_set;

    return result;
}

// {$.user.lang, $.lang}
vector<Result> queryTT2(char* file) {
    RecordSet* record_set = getRecordSet(file);

    // set the number of threads for parallel bitmap construction
    int thread_num = 1;
    /* set the number of levels of bitmaps to create, either based on the
     * query or the JSON records. E.g., query $[*].user.id needs three levels
     * (level 0, 1, 2), but the record may be of more than three levels
     */
    int level_num = 3;

    /* process the records one by one: for each one, first build bitmap, then perform
     * the query with a bitmap iterator
     */
    int num_recs = record_set->size();
    Bitmap* bm = NULL;

    vector<Result> result;
    unordered_set<char*> set;
    char* key = NULL;
    for (int i = 0; i < num_recs; i++) {
        bm = BitmapConstructor::construct((*record_set)[i], thread_num, level_num);
        BitmapIterator* iter = BitmapConstructor::getIterator(bm);
        set.insert("lang");
        set.insert("user");
        while (iter->isObject() && (key = iter->moveToKey(set)) != NULL) {
            if (strcmp(key, "lang") == 0) {
                char* value = iter->getValue();
                result.push_back(CharPtResult(value));
                if (value) free(value);
            } else {
                if (iter->down() == false) continue;  /* value of "user" */
                if (iter->isObject() && iter->moveToKey("lang")) {
                    // value of "lang"
                    char* value = iter->getValue();
                    result.push_back(CharPtResult(value));
                    if (value) free(value);
                }
                iter->up();
            }
        }
        delete iter;
        delete bm;
    }
    delete record_set;
    
    return result;
}

// $.user.lang[?(@ == 'nl')]"
vector<Result> queryTT3(char* file) {
    RecordSet* record_set = getRecordSet(file);

    // set the number of threads for parallel bitmap construction
    int thread_num = 1;
    /* set the number of levels of bitmaps to create, either based on the
     * query or the JSON records. E.g., query $[*].user.id needs three levels
     * (level 0, 1, 2), but the record may be of more than three levels
     */
    int level_num = 3;

    /* process the records one by one: for each one, first build bitmap, then perform
     * the query with a bitmap iterator
     */
    int num_recs = record_set->size();
    Bitmap* bm = NULL;

    vector<Result> result;
    for (int i = 0; i < num_recs; i++) {
        bm = BitmapConstructor::construct((*record_set)[i], thread_num, level_num);
        BitmapIterator* iter = BitmapConstructor::getIterator(bm);
        if (iter->isObject() && iter->moveToKey("user")) {
            if (iter->down() == false) continue;
            if (iter->isObject() && iter->moveToKey("lang")) {
                char* value = iter->getValue();
                if (strcmp(value, "\"nl\",") == 0 || strcmp(value, " \"nl\", ") == 0) {
                    result.push_back(CharPtResult(value));
                }
                if (value) free(value);
            }
            iter->up();
        }
        delete iter;
        delete bm;
    }
    delete record_set;
    
    return result;
}

// $.user.lang[?(@ == 'en')]"
vector<Result> queryTT4(char* file) {
    RecordSet* record_set = getRecordSet(file);

    // set the number of threads for parallel bitmap construction
    int thread_num = 1;
    /* set the number of levels of bitmaps to create, either based on the
     * query or the JSON records. E.g., query $[*].user.id needs three levels
     * (level 0, 1, 2), but the record may be of more than three levels
     */
    int level_num = 3;

    /* process the records one by one: for each one, first build bitmap, then perform
     * the query with a bitmap iterator
     */
    int num_recs = record_set->size();
    Bitmap* bm = NULL;

    vector<Result> result;
    for (int i = 0; i < num_recs; i++) {
        bm = BitmapConstructor::construct((*record_set)[i], thread_num, level_num);
        BitmapIterator* iter = BitmapConstructor::getIterator(bm);
        if (iter->isObject() && iter->moveToKey("user")) {
            if (iter->down() == false) continue;
            if (iter->isObject() && iter->moveToKey("lang")) {
                char* value = iter->getValue();
                if (strcmp(value, "\"en\",") == 0 || strcmp(value, " \"en\", ") == 0) {
                    result.push_back(CharPtResult(value));
                }
                if (value) free(value);
            }
            iter->up();
        }
        delete iter;
        delete bm;
    }
    delete record_set;
    
    return result;
}

// {$.bestMarketplacePrice.price, $.name}
vector<Result> queryWM(char* file) {
    RecordSet* record_set = getRecordSet(file);

    // set the number of threads for parallel bitmap construction
    int thread_num = 1;
    /* set the number of levels of bitmaps to create, either based on the
     * query or the JSON records. E.g., query $[*].user.id needs three levels
     * (level 0, 1, 2), but the record may be of more than three levels
     */
    int level_num = 3;

    /* process the records one by one: for each one, first build bitmap, then perform
     * the query with a bitmap iterator
     */
    int num_recs = record_set->size();
    Bitmap* bm = NULL;

    vector<Result> result;
    unordered_set<char*> set;
    char* key = NULL;
    for (int i = 0; i < num_recs; i++) {
        bm = BitmapConstructor::construct((*record_set)[i], thread_num, level_num);
        BitmapIterator* iter = BitmapConstructor::getIterator(bm);
        set.insert("bestMarketplacePrice");
        set.insert("name");
        while (iter->isObject() && (key = iter->moveToKey(set)) != NULL) {
            if (strcmp(key, "bestMarketplacePrice") == 0) {
                if (iter->down() == false) continue;
                if (iter->isObject() && iter->moveToKey("price")) {
                    char* value = iter->getValue();
                    result.push_back(CharPtResult(value));
                    if (value) free(value);
                }
                iter->up();
            } else {
                char* value = iter->getValue();
                result.push_back(CharPtResult(value));
                if (value) free(value);
            }
        }
        delete iter;
        delete bm;
    }
    delete record_set;

    return result;
}

// $.categoryPath[1:3].id
vector<Result> queryBB(char* file) {
    RecordSet* record_set = getRecordSet(file);

    // set the number of threads for parallel bitmap construction
    int thread_num = 1;
    /* set the number of levels of bitmaps to create, either based on the
     * query or the JSON records. E.g., query $[*].user.id needs three levels
     * (level 0, 1, 2), but the record may be of more than three levels
     */
    int level_num = 3;

    /* process the records one by one: for each one, first build bitmap, then perform
     * the query with a bitmap iterator
     */
    int num_recs = record_set->size();
    Bitmap* bm = NULL;

    vector<Result> result;
    for (int i = 0; i < num_recs; i++) {
        bm = BitmapConstructor::construct((*record_set)[i], thread_num, level_num);
        BitmapIterator* iter = BitmapConstructor::getIterator(bm);
        if (iter->isObject() && iter->moveToKey("categoryPath")) {
            if (iter->down() == false) continue;
            if (iter->isArray()) {
                for (int idx = 1; idx <= 2; ++idx) {
                    if (iter->moveToIndex(idx)) {
                        if (iter->down() == false) continue;
                        if (iter->isObject() && iter->moveToKey("id")) {
                            // value of "id"
                            char* value = iter->getValue();
                            result.push_back(CharPtResult(value));
                            if (value) free(value);
                        }
                        iter->up();
                    }
                }
            }
            iter->up();
        }
        delete iter;
        delete bm;
    }
    delete record_set;

    return result;
}