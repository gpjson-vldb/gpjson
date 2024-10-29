import sys
sys.path.append('../../common')
sys.path.append('../../engine')
from python import execute, parseParameters
import pythonjsonpath

def main():
    twitter = "test_small_records.json"
    walmart = "walmart_small_records.json"
    bestbuy = "bestbuy_small_records.json"
    
    params = parseParameters(sys.argv)
    warmup = params["warmup"]
    repeat = params["repeat"]
    baseDir = params["datasets"]
    engineName = "pythonjsonpath"
    engine = pythonjsonpath
    engine.init()

    execute(engineName, warmup, repeat, baseDir+twitter, "TT1", engine.queryTT1, engine.count)
    execute(engineName, warmup, repeat, baseDir+twitter, "TT2", engine.queryTT2, engine.count)
    execute(engineName, warmup, repeat, baseDir+twitter, "TT3", engine.queryTT3, engine.count)
    execute(engineName, warmup, repeat, baseDir+twitter, "TT4", engine.queryTT4, engine.count)

    execute(engineName, warmup, repeat, baseDir+walmart, "WM", engine.queryWM, engine.count)

    execute(engineName, warmup, repeat, baseDir+bestbuy, "BB", engine.queryBB, engine.count)

main()