import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Patch
from plot_utils import *
import math

sns.set_style("whitegrid", {"ytick.left": True})
plt.rcParams["font.family"] = ["serif"]
plt.rcParams["font.size"] = 12
plt.rcParams['hatch.linewidth'] = 0.6
plt.rcParams['axes.labelpad'] = 5 
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

colors = sns.color_palette('husl', n_colors=11)
dir = "/Users/lucadanelutti/repo/gpjson/benchmarks/result/thesis/"

def GPUsBatch1(filename):
    frame = pd.DataFrame()
    temp = pd.read_csv(dir+"batch1/"+filename)
    temp['machine'] = filename[:-4].upper()
    frame = pd.concat([frame, temp])
    frame['time'] = frame['time'] / 1000
    frame['stddev'] = frame['stddev'] / 1000
    tempColors = [colors[i] for i in [3, 4, 5, 6, 7, 8, 9, 10]]
    tempColors.insert(0, colors[0])
    return {"name": "GPUOverview-"+filename[:-4].upper(),
        "data": frame,
        "ratio": "gpjson", 
        "bar_label": "edge",
        "bar_label_padding": 3,
        "ncols": 5,
        "bbox_to_anchor": 0.8,
        "bottomPadding": 0.15,
        "topPadding": 0.9,
        "xlabel": "Engine", 
        "ylabel": "Execution Time [s]",
        "engine_order": ['gpjson', 'nodejsonpath', 'nodejsonpathplus', 'nodemanual', 'nodesimdjson', 'javajsonpath', 'pison', 'rapidjson', 'simdjson'],
        "col": 'query',
        "col_order": ['TT1', 'TT2', "TT3", "TT4", "WM", "BB"],
        "col_labels": ['TT1', 'TT2', "TT3", "TT4", "WM", "BB"],
        "col_wrap": 3,
        "labels": ['GpJSON', 'Node jsonpath', 'Node jsonpath-plus', 'Node manual', 'Node simdjson', 'Java JSONPath', 'Pison', 'RapidJSON', 'simdjson'],
        "colors": tempColors
        }

def HPCBatch1():
    frame = pd.DataFrame()
    for filename in ['gpu4.8.csv', 'gpu3.1.csv', 'gpu2.1.csv']:
        temp = pd.read_csv(dir+"batch1/"+filename)
        temp = temp.loc[temp['engine'] == "gpjson"]
        temp['machine'] = "OPTIMIZED3-12c"
        temp['engine'] = "gpjson" + "-" + filename[:-4].upper()
        frame = pd.concat([frame, temp])
    temp = pd.read_csv(dir+"batch1/optimized3-12c.csv")
    temp['machine'] = "OPTIMIZED3-12c"
    frame = pd.concat([frame, temp])
    frame['time'] = frame['time'] / 1000
    frame['stddev'] = frame['stddev'] / 1000
    return {"name": "HPCBatch1",
        "data": frame,
        "ratio": "gpjson-GPU4.8", 
        "bar_label": "edge",
        "bar_label_padding": 3, 
        # "limit": [[0, 8],[0, 10],[0, 10],[0, 10],[0, 10],[0, 20]],   
        "xlabel": "Engine", 
        "ylabel": "Execution Time [s]",
        "ncols": 4,
        "bbox_to_anchor": 0.6,
        "bottomPadding": 0.18,
        "topPadding": 0.9,
        "engine_order": ['gpjson-GPU4.8', 'gpjson-GPU3.1', 'gpjson-GPU2.1', 'nodejsonpath', 'nodejsonpathplus', 'nodemanual', 'nodesimdjson', 'javajsonpath', 'pison', 'rapidjson', 'simdjson'],
        "col": 'query',
        "col_order": ['TT1', 'TT2', "TT3", "TT4", "WM", "BB"],
        "col_labels": ['TT1', 'TT2', "TT3", "TT4", "WM", "BB"],
        "col_wrap": 3,
        "labels": ['GpJSON-GPU4.8', 'GpJSON-GPU3.1', 'GpJSON-GPU2.1', 'Node jsonpath', 'Node jsonpath-plus', 'Node manual', 'Node simdjson', 'Java JSONPath', 'Pison', 'RapidJSON', 'simdjson'],
        "colors": colors
        }

def HPCBatch1Summary():
    frame = pd.DataFrame()
    for filename in ['gpu4.8.csv', 'gpu3.1.csv', 'gpu2.1.csv']:
        temp = pd.read_csv(dir+"batch1/"+filename)
        temp = temp.loc[temp['engine'] == "gpjson"]
        temp['machine'] = "OPTIMIZED3-12c"
        temp['engine'] = "gpjson" + "-" + filename[:-4].upper()
        frame = pd.concat([frame, temp])
    temp = pd.read_csv(dir+"batch1/optimized3-12c.csv")
    temp['machine'] = "OPTIMIZED3-12c"
    frame = pd.concat([frame, temp])
    frame['time'] = frame['time'] / 1000
    frame['stddev'] = frame['stddev'] / 1000
    return {"name": "HPCBatch1Summary",
        "data": frame,
        "ratio": "gpjson-GPU4.8", 
        "bar_label": "edge",
        "bar_label_padding": 3, 
        # "limit": [[0, 8],[0, 10],[0, 10],[0, 10],[0, 10],[0, 20]],   
        "xlabel": "Engine", 
        "ylabel": "Execution Time [s]",
        "ncols": 6,
        "bbox_to_anchor": 0.78,
        "bottomPadding": 0.15,
        "topPadding": 0.9,
        "aspect": 1.2,
        "engine_order": ['gpjson-GPU4.8', 'gpjson-GPU3.1', 'gpjson-GPU2.1', 'nodejsonpath', 'nodejsonpathplus', 'nodemanual', 'nodesimdjson', 'javajsonpath', 'pison', 'rapidjson', 'simdjson'],
        "col": 'query',
        "col_order": ['TT1', 'TT2', "TT3", "TT4", "WM", "BB"],
        "col_labels": ['TT1', 'TT2', "TT3", "TT4", "WM", "BB"],
        "col_wrap": 3,
        "labels": ['GpJSON-GPU4.8', 'GpJSON-GPU3.1', 'GpJSON-GPU2.1', 'Node jsonpath', 'Node jsonpath-plus', 'Node manual', 'Node simdjson', 'Java JSONPath', 'Pison', 'RapidJSON', 'simdjson'],
        "colors": colors
        }

def sizes():
    frame = pd.DataFrame()
    for filename in ['gpu4.8.csv', 'gpu3.1.csv', 'gpu2.1.csv']:
        temp = pd.read_csv(dir+"sizes/"+filename)
        temp = temp.loc[temp['engine'] == "gpjson"]
        temp['machine'] = "OPTIMIZED3-12c"
        temp['engine'] = "gpjson" + "-" + filename[:-4].upper()
        frame = pd.concat([frame, temp])
    temp = pd.read_csv(dir+"sizes/optimized3-12c.csv")
    temp['machine'] = "OPTIMIZED3-12c"
    frame = pd.concat([frame, temp])
    frame['stddev'] = frame['stddev'] / 1000
    frame['time'] = frame['time'] / 1000
    frame['dataset'] = frame['dataset'].apply(lambda x: x.split("/")[-1])
    baseSize = 0.807
    for engine in frame['engine'].unique():
        for machine in frame['machine'].unique():
            for dataset in ['twitter_small_records.json', 'twitter_small_records_0.125x.json', 'twitter_small_records_0.25x.json', 'twitter_small_records_0.5x.json', 'twitter_small_records_2x.json', 'twitter_small_records_4x.json', 'twitter_small_records_8x.json', 'twitter_small_records_12x.json', 'twitter_small_records_16x.json']:
                multiplier = 1 if (dataset == 'twitter_small_records.json') else float(dataset.split("_")[3].split("x")[0])
                time = frame.loc[(frame['machine'] == machine) & (frame['engine'] == engine) & (frame['dataset'] == dataset), 'time'].iloc[0]
                frame.loc[(frame['machine'] == machine) & (frame['engine'] == engine) & (frame['dataset'] == dataset), 'time'] = baseSize * multiplier / frame.loc[(frame['machine'] == machine) & (frame['engine'] == engine) & (frame['dataset'] == dataset), 'time'].iloc[0]
                frame.loc[(frame['machine'] == machine) & (frame['engine'] == engine) & (frame['dataset'] == dataset), 'stddev'] = baseSize * multiplier * frame.loc[(frame['machine'] == machine) & (frame['engine'] == engine) & (frame['dataset'] == dataset), 'stddev'].iloc[0] / (time*time)
    return {"name": "HPCSizes",
        "data": frame,
        "ratio": "gpjson-GPU4.8", 
        "bar_label": "edge",
        "bar_label_padding": 10,
        "xlabel": "Engine", 
        "ylabel": "Speed [GB/s]",
        "limit": [[0, 5] for _ in range(9)],
        "ncols": 4,
        "bbox_to_anchor": 0.45,
        "bottomPadding": 0.10,
        "topPadding": 0.95,
        "title_y": 1.05,
        "hspace": 0.3,
        "row": 'machine',
        "row_order": ['OPTIMIZED3-12c'],
        "engine_order": ['gpjson-GPU4.8', 'gpjson-GPU3.1', 'gpjson-GPU2.1', 'javajsonpath', 'pison', 'rapidjson', 'simdjson'],
        "col": 'dataset',
        "col_order": ["twitter_small_records_0.125x.json", "twitter_small_records_0.25x.json", "twitter_small_records_0.5x.json", "twitter_small_records.json", "twitter_small_records_2x.json", "twitter_small_records_4x.json", "twitter_small_records_8x.json", "twitter_small_records_12x.json", "twitter_small_records_16x.json"],
        "col_labels": ["0.125x", "0.25x", "0.5x", "1x", "2x", "4x", "8x", "12x", "16x"],
        "col_wrap": 3,
        "labels": ['GpJSON-GPU4.8', 'GpJSON-GPU3.1', 'GpJSON-GPU2.1' ,'Java JSONPath', 'Pison', 'RapidJSON', 'simdjson'],
        "colors": colors
        }

def sizesPresentation():
    frame = pd.DataFrame()
    for filename in ['gpu4.8.csv', 'gpu3.1.csv', 'gpu2.1.csv']:
        temp = pd.read_csv(dir+"sizes/"+filename)
        temp = temp.loc[temp['engine'] == "gpjson"]
        temp['machine'] = "OPTIMIZED3-12c"
        temp['engine'] = "gpjson" + "-" + filename[:-4].upper()
        frame = pd.concat([frame, temp])
    temp = pd.read_csv(dir+"sizes/optimized3-12c.csv")
    temp['machine'] = "OPTIMIZED3-12c"
    frame = pd.concat([frame, temp])
    frame['stddev'] = frame['stddev'] / 1000
    frame['time'] = frame['time'] / 1000
    frame['dataset'] = frame['dataset'].apply(lambda x: x.split("/")[-1])
    baseSize = 0.807
    for engine in frame['engine'].unique():
        for machine in frame['machine'].unique():
            for dataset in ['twitter_small_records.json', 'twitter_small_records_0.125x.json', 'twitter_small_records_0.25x.json', 'twitter_small_records_0.5x.json', 'twitter_small_records_2x.json', 'twitter_small_records_4x.json', 'twitter_small_records_8x.json', 'twitter_small_records_12x.json', 'twitter_small_records_16x.json']:
                multiplier = 1 if (dataset == 'twitter_small_records.json') else float(dataset.split("_")[3].split("x")[0])
                time = frame.loc[(frame['machine'] == machine) & (frame['engine'] == engine) & (frame['dataset'] == dataset), 'time'].iloc[0]
                frame.loc[(frame['machine'] == machine) & (frame['engine'] == engine) & (frame['dataset'] == dataset), 'time'] = baseSize * multiplier / frame.loc[(frame['machine'] == machine) & (frame['engine'] == engine) & (frame['dataset'] == dataset), 'time'].iloc[0]
                frame.loc[(frame['machine'] == machine) & (frame['engine'] == engine) & (frame['dataset'] == dataset), 'stddev'] = baseSize * multiplier * frame.loc[(frame['machine'] == machine) & (frame['engine'] == engine) & (frame['dataset'] == dataset), 'stddev'].iloc[0] / (time*time)
    return {"name": "HPCSizesPresentation",
        "data": frame,
        "ratio": "gpjson-GPU4.8", 
        "bar_label": "edge",
        "bar_label_padding": 10,
        "xlabel": "Engine", 
        "ylabel": "Speed [GB/s]",
        "limit": [[0, 4] for _ in range(9)],
        "ncols": 4,
        "bbox_to_anchor": 0.45,
        "bottomPadding": 0.2,
        "topPadding": 0.90,
        "title_y": 1.05,
        "hspace": 0.3,
        "row": 'machine',
        "row_order": ['OPTIMIZED3-12c'],
        "engine_order": ['gpjson-GPU4.8', 'gpjson-GPU3.1', 'gpjson-GPU2.1', 'javajsonpath', 'pison', 'rapidjson', 'simdjson'],
        "col": 'dataset',
        "col_order": ["twitter_small_records_0.125x.json", "twitter_small_records_0.25x.json", "twitter_small_records_0.5x.json", "twitter_small_records.json", "twitter_small_records_2x.json", "twitter_small_records_4x.json", "twitter_small_records_8x.json", "twitter_small_records_12x.json", "twitter_small_records_16x.json"],
        "col_labels": ["0.125x", "0.25x", "0.5x", "1x", "2x", "4x - in memory", "8x", "12x", "16x - out of memory"],
        "col_wrap": 3,
        "labels": ['GpJSON-GPU4.8', 'GpJSON-GPU3.1', 'GpJSON-GPU2.1' ,'Java JSONPath', 'Pison', 'RapidJSON', 'simdjson'],
        "colors": colors
        }

def selectivity():
    frame = pd.DataFrame()
    for filename in ['gpu4.8.csv', 'gpu3.1.csv', 'gpu2.1.csv']:
        temp = pd.read_csv(dir+"selectivity/"+filename)
        temp = temp.loc[temp['engine'] == "gpjson"]
        temp['machine'] = "OPTIMIZED3-12c"
        temp['engine'] = "gpjson" + "-" + filename[:-4].upper()
        frame = pd.concat([frame, temp])
    temp = pd.read_csv(dir+"selectivity/optimized3-12c.csv")
    temp['machine'] = "OPTIMIZED3-12c"
    frame = pd.concat([frame, temp])
    for engine in frame['engine'].unique():
        for dataset in frame['dataset'].unique():
            temp = dataset.split("_")[3].split(".")[0]
            i = 0
            while (temp[len(temp) - 1 - i] >= '0' and temp[len(temp) - 1 - i] <= '9'):
                i += 1
            frame.loc[(frame['engine'] == engine) & (frame['dataset'] == dataset), 'edit'] = dataset.split("_")[3].split(".")[0][:-i]
            frame.loc[(frame['engine'] == engine) & (frame['dataset'] == dataset), 'percentage'] = dataset.split("_")[3].split(".")[0][-i:]
    frame['time'] = frame['time'] / 1000
    frame['stddev'] = frame['stddev'] / 1000
    return {"name": "HPCSelectivity",
        "data": frame,
        "ratio": "gpjson-GPU4.8", 
        "bar_label": "edge",
        "bar_label_padding": 10,
        "xlabel": "Engine", 
        "ylabel": "Execution Time [s]",
        "limit": [[0, 7] for _ in range(3)],
        "ncols": 6,
        "bbox_to_anchor": 0,
        "bottomPadding": 0.12,
        "topPadding": 0.95,
        "aspect": 1,
        "title_y": 1.05,
        "row": 'edit',
        "row_order": ['changeUserLang', 'deleteUser', 'deleteUserLang'],
        "row_labels": ['Change $.user.lang', 'Delete $.user key', 'Delete $.user.lang key'],
        "engine_order": ['gpjson-GPU4.8', 'gpjson-GPU3.1', 'gpjson-GPU2.1', 'nodejsonpath', 'nodejsonpathplus', 'nodemanual', 'nodesimdjson', 'javajsonpath', 'pison', 'rapidjson', 'simdjson'],
        "col": 'percentage',
        "col_order": ["0", "25", "50", "75", "100"],
        "col_labels": ["0%", "25%", "50%", "75%", "100%"],
        "labels": ['GpJSON-GPU4.8', 'GpJSON-GPU3.1', 'GpJSON-GPU2.1', 'Node jsonpath', 'Node jsonpath-plus', 'Node manual', 'Node simdjson', 'Java JSONPath', 'Pison', 'RapidJSON', 'simdjson'],
        "colors": colors
        }

def syncVSAsync():
    frame = pd.DataFrame()
    maxVal = list()
    for filename in ['gpu4.8.csv', 'gpu3.1.csv', 'gpu2.1.csv']:
        temp = pd.read_csv(dir+"syncAsync/"+filename)
        temp['machine'] = filename[:-4]
        for executionPolicy in temp['options'].unique():
            temp.loc[(temp['options'] == executionPolicy), 'engine'] = "gpjson" + "-" + executionPolicy.split("=")[1]
        frame = pd.concat([frame, temp])
        max = temp['time'].max() / 1000
        max = math.ceil(max * 10) / 10
        maxVal.append(max)
    frame['time'] = frame['time'] / 1000
    frame['stddev'] = frame['stddev'] / 1000
    maxVal[1] += 0.1
    maxVal[2] += 0.1
    return {"name": "syncVSAsync",
        "data": frame,
        "ratio": "gpjson-async", 
        "bar_label": "edge",
        "bar_label_padding": 10, 
        "limit": [[0, max] for max in maxVal],
        "xlabel": "Execution Policy", 
        "ylabel": "Execution Time [s]",
        "ncols": 3,
        "bbox_to_anchor": -3.0,
        "bottomPadding": 0.10,
        "topPadding": 0.95,
        "aspect": 0.6,
        "wspace": 0.8,
        "hspace": 0.3,
        "title_y": 1.05,
        "engine_order": ['gpjson-async', 'gpjson-sync'],
        "row": 'machine',
        "row_order": ['gpu4.8', 'gpu3.1', 'gpu2.1'],
        "col": 'query',
        "col_order": ['TT1', 'TT2', "TT3", "TT4", "WM", "BB"],
        "col_labels": ['TT1', 'TT2', "TT3", "TT4", "WM", "BB"],
        "col_wrap": 6,
        "labels": ['Async', 'Sync'],
        "colors": colors
        }

def numGPUs():
    frame = pd.DataFrame()
    maxVal = list()
    for filename in ['gpu4.8.csv', 'gpu3.8.csv']:
        temp = pd.read_csv(dir+"numGPUs/"+filename)
        temp['machine'] = filename[:-4]
        for numGPUs in temp['options'].unique():
            temp.loc[(temp['options'] == numGPUs), 'engine'] = "gpjson" + "-" + numGPUs.split("=")[1]
        frame = pd.concat([frame, temp])
        max = temp['time'].max() / 1000
        max = math.ceil(max * 10) / 10
        maxVal.append(max)
    frame['time'] = frame['time'] / 1000
    frame['stddev'] = frame['stddev'] / 1000
    frame['dataset'] = frame['dataset'].apply(lambda x: x.split("/")[-1])
    maxVal[0] += 3
    maxVal[1] += 3
    return {"name": "numGPUs",
        "data": frame,
        "ratio": "gpjson-1", 
        "bar_label": "edge",
        "bar_label_padding": 8, 
        "limit": [[0, max] for max in maxVal],
        "xlabel": "GPU Count", 
        "ylabel": "Execution Time [s]",
        "ncols": 4,
        "bbox_to_anchor": -0.5,
        "bottomPadding": 0.15,
        "topPadding": 0.90,
        "aspect": 0.6,
        "wspace": 0.25,
        "title_y": 1.05,
        "engine_order": ['gpjson-1', 'gpjson-2', 'gpjson-4', 'gpjson-8'],
        "row": 'machine',
        "row_order": ['gpu4.8', 'gpu3.8'],
        "col": 'dataset',
        "col_order": ["twitter_small_records_8x.json", "twitter_small_records_12x.json", "twitter_small_records_16x.json", "twitter_small_records_32x.json", "twitter_small_records_64x.json"],
        "col_labels": ["8x", "12x", "16x", "32x", "64x"],
        "col_wrap": 5,
        "labels": ['1 GPU', '2 GPUs', '4 GPUs', '8 GPUs'],
        "colors": colors
        }

def numGPUs_10q():
    frame = pd.DataFrame()
    maxVal = list()
    for filename in ['gpu4.8.csv', 'gpu3.8.csv']:
        temp = pd.read_csv(dir+"10q-numGPUs/"+filename)
        temp['machine'] = filename[:-4]
        for numGPUs in temp['options'].unique():
            temp.loc[(temp['options'] == numGPUs), 'engine'] = "gpjson" + "-" + numGPUs.split("=")[1]
            frame = pd.concat([frame, temp])
    frame['time'] = frame['time'] / 1000
    frame['stddev'] = frame['stddev'] / 1000
    frame['dataset'] = frame['dataset'].apply(lambda x: x.split("/")[-1])
    baseSize = 0.807
    for machine in frame['machine'].unique():
        for engine in frame['engine'].unique():
            for dataset in frame['dataset'].unique():
                multiplier = 1 if (dataset == 'twitter_small_records.json') else float(dataset.split("_")[3].split("x")[0])
                time = frame.loc[(frame['machine'] == machine) & (frame['engine'] == engine) & (frame['dataset'] == dataset), 'time'].iloc[0]
                frame.loc[(frame['machine'] == machine) & (frame['engine'] == engine) & (frame['dataset'] == dataset), 'time'] = 10 / frame.loc[(frame['machine'] == machine) & (frame['engine'] == engine) & (frame['dataset'] == dataset), 'time'].iloc[0] / baseSize * multiplier
                frame.loc[(frame['machine'] == machine) & (frame['engine'] == engine) & (frame['dataset'] == dataset), 'stddev'] = 10 / baseSize * multiplier * frame.loc[(frame['machine'] == machine) & (frame['engine'] == engine) & (frame['dataset'] == dataset), 'stddev'].iloc[0] / (time*time)
    for machine in frame['machine'].unique():
        max = frame.loc[(frame['machine'] == machine), 'time'].max()
        max = math.ceil(max * 10) / 10
        maxVal.append(max)
    maxVal[0] += 10
    maxVal[1] += 10
    return {"name": "10q-numGPUs",
        "data": frame,
        "ratio": "gpjson-8", 
        "bar_label": "edge",
        "bar_label_padding": 8, 
        "limit": [[0, max] for max in maxVal],
        "xlabel": "GPU Count", 
        "ylabel": "Speed [query / (s * GB)]",
        "ncols": 4,
        "bbox_to_anchor": 0.1,
        "bottomPadding": 0.13,
        "topPadding": 0.91,
        "aspect": 0.6,
        "wspace": 0.25,
        "hspace": 0.3,
        "title_y": 1.12,
        "engine_order": ['gpjson-1', 'gpjson-2', 'gpjson-4', 'gpjson-8'],
        "col": 'dataset',
        "row": 'machine',
        "row_order": ['gpu4.8', 'gpu3.8'],
        "col_order": ["twitter_small_records_16x.json", "twitter_small_records_32x.json", "twitter_small_records_64x.json", "twitter_small_records_128x.json"],
        "col_labels": ["16x", "32x", "64x", "128x"],
        "col_wrap": 4,
        "labels": ['1 GPU', '2 GPUs', '4 GPUs', '8 GPUs'],
        "colors": colors
        }

def batching():
    frame = pd.DataFrame()
    for filename in ['gpu4.8.csv', 'gpu3.1.csv', 'gpu2.1.csv']:
        temp = pd.read_csv(dir+"2x-batching/"+filename)
        temp['machine'] = filename[:-4]
        for partitionInfo in temp['options'].unique():
            if (len(partitionInfo.split(" ")) > 1):
                temp.loc[(temp['options'] == partitionInfo), 'gridSize'] = "adjusted"
            else:
                temp.loc[(temp['options'] == partitionInfo), 'gridSize'] = "default"
            temp.loc[(temp['options'] == partitionInfo), 'engine'] = "gpjson" + "-" + partitionInfo.split(" ")[0].split("=")[1]
        temp.loc[(temp['query'] == "TT1-noBatching") & (temp['engine'] == "gpjson-1073741824"), 'engine'] = "gpjson-0"
        temp.loc[temp['engine'] == "gpjson-0", 'query'] = "TT1"
        temp = temp.loc[temp['query'] == "TT1"]
        frame = pd.concat([frame, temp])
    frame['time'] = frame['time'] / 1000
    frame['stddev'] = frame['stddev'] / 1000
    frame['dataset'] = frame['dataset'].apply(lambda x: x.split("/")[-1])
    baseSize = 0.807
    for engine in frame['engine'].unique():
            for machine in frame['machine'].unique():
                for gridSize in frame['gridSize'].unique():
                    multiplier = 2
                    time = frame.loc[(frame['engine'] == engine) & (frame['gridSize'] == gridSize) & (frame['machine'] == machine), 'time'].iloc[0]
                    frame.loc[(frame['engine'] == engine) & (frame['gridSize'] == gridSize) & (frame['machine'] == machine), 'time'] = baseSize * multiplier / frame.loc[(frame['engine'] == engine) & (frame['gridSize'] == gridSize) & (frame['machine'] == machine), 'time'].iloc[0]
                    frame.loc[(frame['engine'] == engine) & (frame['gridSize'] == gridSize) & (frame['machine'] == machine), 'stddev'] = baseSize * multiplier * frame.loc[(frame['engine'] == engine) & (frame['gridSize'] == gridSize) & (frame['machine'] == machine), 'stddev'].iloc[0] / (time*time)
    maxVal = frame['time'].max()
    maxVal = math.ceil(maxVal)
    return {"name": "batching",
        "data": frame,
        "ratio": "gpjson-0", 
        "bar_label": "edge",
        "bar_label_padding": 15, 
        "limit": [[0, maxVal], [0, maxVal], [0, maxVal]],
        "xlabel": "Partition Size", 
        "ylabel": "Speed [GB/s]",
        "ncols": 3,
        "bbox_to_anchor": 0.10,
        "bottomPadding": 0.15,
        "topPadding": 0.9,
        "aspect": 1,
        "wspace": 0.25,
        "hspace": 0.3,
        "title_y": 1.05,
        "engine_order": ["gpjson-0", "gpjson-1073741824", "gpjson-536870912", "gpjson-268435456", "gpjson-134217728"],
        "col": 'machine',
        "col_order": ["gpu4.8", "gpu3.1", "gpu2.1"],
        "col_labels": ["GPU4.8", "GPU3.1", "GPU2.1"],
        "row": "gridSize",
        "row_order": ["default", "adjusted"],
        "labels": ["0 (no batching)", "1GB", "512MB", "256MB", "128MB"],
        "colors": colors
        }

def prototype():
    frame = pd.DataFrame()
    maxVal = list()
    for filename in ['gpu3.1.csv']:
        temp = pd.read_csv(dir+"syncAsync/"+filename)
        temp['machine'] = filename[:-4]
        temp = temp.loc[temp['engine'] == "gpjson"]
        temp['engine'] = "gpjson"
        frame = pd.concat([frame, temp])
        max = temp['time'].max() / 1000
        max = math.ceil(max * 10) / 10
        maxVal.append(max)
    for filename in ['gpu3.1-uptodate.csv']:
        temp = pd.read_csv("/Users/lucadanelutti/repo/gpjson/benchmarks/result/old/batch1/"+filename)
        temp['machine'] = filename[:-4]
        temp = temp.loc[temp['engine'] == "gpjson"]
        temp['engine'] = "gpjson-prototype"
        frame = pd.concat([frame, temp])
        max = temp['time'].max() / 1000
        max = math.ceil(max * 10) / 10
        maxVal.append(max)
    frame['time'] = frame['time'] / 1000
    frame['stddev'] = frame['stddev'] / 1000
    return {"name": "prototype",
        "data": frame,
        "ratio": "gpjson", 
        "bar_label": "edge",
        "bar_label_padding": 10, 
        "limit": [[0, max] for _ in range(6)],
        "xlabel": "Execution Policy", 
        "ylabel": "Execution Time [s]",
        "ncols": 3,
        "bbox_to_anchor": -3.0,
        "bottomPadding": 0.25,
        "topPadding": 0.85,
        "aspect": 0.6,
        "wspace": 0.8,
        "hspace": 0.3,
        "title_y": 1.05,
        "engine_order": ['gpjson', 'gpjson-prototype'],
        "col": 'query',
        "col_order": ['TT1', 'TT2', "TT3", "TT4", "WM", "BB"],
        "col_labels": ['TT1', 'TT2', "TT3", "TT4", "WM", "BB"],
        "col_wrap": 6,
        "labels": ['GpJSON', 'GpJSON-prototype'],
        "colors": colors
        }

def doPlot(plot):
    data = plot['data']
    g = sns.catplot(data=data, kind='bar', x="engine",
                    order=plot['engine_order'],
                    y="time", alpha=1, palette=plot['colors'],
                    col=plot['col'], col_order=plot['col_order'],
                    row=plot['row'], row_order=plot['row_order'],
                    height=4, aspect=plot['aspect'],
                    sharey=False, sharex=False, margin_titles=True)

    g.set_axis_labels(plot['xlabel'], plot['ylabel'])

    cmap = dict(zip(plot['labels'], plot['colors']))
    patches = [Patch(color=v, label=k) for k, v in cmap.items()]
    plt.legend(handles=patches, bbox_to_anchor=(plot['bbox_to_anchor'], -0.2), loc='best', borderaxespad=0, ncols=plot['ncols'])

    for i,axes in enumerate(g.axes):  
        for ii,ax in enumerate(axes):
            if 'limit' in plot:
                ax.set(ylim=plot['limit'][i])
            ax.set(xticklabels=[])
            tempdata = data.loc[(data[plot['row']] == plot["row_order"][i]) & (data[plot['col']] == plot['col_order'][ii]) & (data['engine'].isin(plot['engine_order']))]
            ax.errorbar(data=tempdata, x="engine", y="time", yerr="stddev", fmt="none", c="k")
            labels = []
            for e in plot['engine_order']:
                ratio = tempdata.loc[tempdata['engine'] == e]['time'].values[0] / tempdata.loc[tempdata['engine'] == plot['ratio']]['time'].values[0]
                if ratio != 1:
                    labels.append(f"{ratio:.1f}x")
                else:
                    labels.append("")
            ax.bar_label(ax.containers[0], labels=labels, label_type=plot['bar_label'], padding=plot['bar_label_padding'], rotation=90)
            ax.set_title(plot['col_labels'][ii], y= (plot['title_y'] if ('title_y' in plot) else 1.15))

    plt.tight_layout()
    plt.subplots_adjust(hspace=plot['hspace'] if ('hspace' in plot) else 0.4, wspace=plot['wspace'] if ('wspace' in plot) else 0.2, bottom=plot['bottomPadding'], top=plot['topPadding'])

    plt.savefig(f"{plot['name']}.pdf")
    plt.show()

def doPlotOneRow(plot):
    data = plot['data']
    g = sns.catplot(data=data, kind='bar', x="engine",
                    order=plot['engine_order'],
                    y="time", alpha=1, palette=plot['colors'],
                    col=plot['col'], col_order=plot['col_order'],
                    col_wrap=plot['col_wrap'],
                    height=4, aspect=plot['aspect'] if ('aspect' in plot) else 1,
                    sharey=False, sharex=False, margin_titles=True)

    g.set_axis_labels(plot['xlabel'], plot['ylabel'])

    cmap = dict(zip(plot['labels'], plot['colors']))
    patches = [Patch(color=v, label=k) for k, v in cmap.items()]
    plt.legend(handles=patches, bbox_to_anchor=(plot['bbox_to_anchor'], -0.2), loc='best', borderaxespad=0, ncols=plot['ncols'])

    for i,a in enumerate(g.axes):  
        if 'limit' in plot:
            a.set(ylim=plot['limit'][i])
        a.set(xticklabels=[])
        tempdata = data.loc[(data[plot['col']] == plot['col_order'][i]) & (data['engine'].isin(plot['engine_order']))]
        a.errorbar(data=tempdata, x="engine", y="time", yerr="stddev", fmt="none", c="k")
        labels = []
        for e in plot['engine_order']:
            ratio = tempdata.loc[tempdata['engine'] == e]['time'].values[0] / tempdata.loc[tempdata['engine'] == plot['ratio']]['time'].values[0]
            if ratio != 1:
                labels.append(f"{ratio:.1f}x")
            else:
                labels.append("")
        a.bar_label(a.containers[0], labels=labels, label_type=plot['bar_label'], padding=plot['bar_label_padding'], rotation=90)
        a.set_title(plot['col_labels'][i], y= (plot['title_y'] if ('title_y' in plot) else 1.15))

    plt.tight_layout()
    plt.subplots_adjust(hspace=plot['hspace'] if ('hspace' in plot) else 0.4, wspace=plot['wspace'] if ('wspace' in plot) else 0.2, bottom=plot['bottomPadding'], top=plot['topPadding'])

    plt.savefig(f"{plot['name']}.pdf", dpi=1200)
    plt.show()
    

for filename in ['gpu4.8.csv', 'gpu3.1.csv', 'gpu2.1.csv']:
    doPlotOneRow(GPUsBatch1(filename))

doPlotOneRow(HPCBatch1())

doPlotOneRow(sizes())

doPlotOneRow(sizesPresentation())

doPlot(selectivity())

doPlot(syncVSAsync())

doPlot(numGPUs())

doPlot(numGPUs_10q())

doPlot(batching())

doPlotOneRow(HPCBatch1Summary())

doPlotOneRow(prototype())