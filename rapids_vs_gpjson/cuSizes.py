# %%
import cudf
import sys
import time
import json

def execute(warmup, repeat, dataset, output, queryFunction):
    try:
        for _ in range(warmup):
            queryFunction(dataset)
    except Exception as e:
        print(dataset)
        print(e)
        return
    
    start = 0
    delays = []
    for _ in range(repeat):
        start = time.perf_counter()
        queryFunction(dataset)
        end = time.perf_counter()
        delays.append(end - start)
    
    with open(output, "w") as f:
        json.dump(delays, f)


def parse_args():
    params = {}
    args = sys.argv[1:]

    arg = next((x for x in args if "warmup=" in x), "")
    params["warmup"] = int(arg[7:]) if arg != "" else 5
    arg = next((x for x in args if "repeat=" in x), -1)
    params["repeat"] = int(arg[7:]) if arg != "" else 10
    arg = next((x for x in args if "datasets=" in x), -1)
    params["datasets"] = arg[9:] if arg != "" else "/local/stalluri/gpjson_datasets"
    arg = next((x for x in args if "output=" in x), -1)
    params["output"] = arg[7:] if arg != "" else "/var/scratch/stalluri/gpjson/rapids_vs_gpjson/results"
    print(params)
    return params

# dtypes = {
#     "created_at":                   str,
#     "id":                            int,
#     "id_str":                       str,
#     "text":                         str,
#     "source":                       str,
#     "truncated":                      bool,
#     "in_reply_to_status_id":         int,
#     "in_reply_to_status_id_str":    str,
#     "in_reply_to_user_id":           int,
#     "in_reply_to_user_id_str":      str,
#     "in_reply_to_screen_name":      str,
#     "user":                         dict,
#     "geo":                          dict,
#     "coordinates":                  dict,
#     "place":                        dict,
#     "contributors":                   int,
#     "retweeted_status":             dict,
#     "is_quote_status":                bool,
#     "retweet_count":                 int,
#     "favorite_count":                int,
#     "entities":                     dict,
#     "favorited":                      bool,
#     "retweeted":                      bool,
#     "possibly_sensitive":             bool,
#     "filter_level":                 str,
#     "lang":                         str,
#     "timestamp_ms":                 str,
#     "quoted_status_id":              int,
#     "quoted_status_id_str":         str,
#     "quoted_status":                dict,
#     "extended_entities":            dict,
#     "display_text_range":             list,
#     "extended_tweet":               dict,
#     "limit":                        dict,
# }
# %%
def main():
    datasets = [
        "twitter_small_records.json",
        "twitter_small_records_0.125x.json",
        "twitter_small_records_0.25x.json",
        "twitter_small_records_0.5x.json",
        "twitter_small_records_2x.json",
        "twitter_small_records_4x.json",
        "twitter_small_records_8x.json"
    ]

    params = parse_args()
    warmup = params["warmup"]
    repeat = params["repeat"]
    datasetDir = params["datasets"]
    outputDir = params["output"]

    def query(ds):
        df = cudf.read_json(ds, lines=True)
        del df

    for dataset in datasets:
        execute(warmup, repeat, 
            f"{datasetDir}/{dataset}", 
            f"{outputDir}/{dataset}",
            query
        )

if __name__=="__main__":
    main()
