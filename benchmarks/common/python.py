import time
import sys
import math
from functools import reduce

def execute(engine, warmup, repeat, dataset, query, queryFunction, countFunction):
    for i in range(warmup):
        result = queryFunction(dataset)
    numResults = countFunction(result)
    start = 0
    delays = []
    for i in range(repeat):
        start = time.perf_counter()
        queryFunction(dataset)
        delays.append((time.perf_counter() - start) * 1000)
    average = reduce(lambda total, delay: total+delay, delays) / repeat
    std = math.sqrt(reduce(lambda total, delay: total+math.pow((delay-average), 2), delays) / (repeat - 1))
    print(engine + "," + dataset + "," + query + "," + str(average) + "," + str(std) + "," + str(numResults) + "," + str(warmup) + "," + str(repeat))

def parseParameters(argv):
    params = dict()
    params['warmup'] = 5
    params['repeat'] = 10
    params['datasets'] = "/home/ubuntu/datasets/"

    for par in argv:
        if (par[:7] == "warmup"):
            params['warmup'] = int(par[7:])
        elif (par[:7] == "repeat"):
            params['repeat'] = int(par[7:])
        elif (par[:9] == "datasets"):
            params['datasets'] = par[9:]
    return params
    