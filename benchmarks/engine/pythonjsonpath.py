from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse
import json

def init():
    pass

def queryTT1(path):
    jsonpath_expr = parse('user.lang')
    return do(path, [jsonpath_expr])

def queryTT2(path):
    jsonpath_expr1 = parse('user.lang')
    jsonpath_expr2 = parse('lang')
    return do(path, [jsonpath_expr1, jsonpath_expr2])

def queryTT3(path):
    jsonpath_expr = parse('user[?(@lang = "nl")].lang')
    return do(path, [jsonpath_expr])

def queryTT4(path):
    jsonpath_expr = parse('user[?(@lang = "en")].lang')
    return do(path, [jsonpath_expr])

def queryWM(path):
    jsonpath_expr1 = parse('bestMarketplacePrice.price')
    jsonpath_expr2 = parse('name')
    return do(path, [jsonpath_expr1, jsonpath_expr2])

def queryBB(path):
    jsonpath_expr = parse('categoryPath[1:3].id')
    return do(path, [jsonpath_expr])

def do(path, exprs):
    file = open(path, 'r')

    result = []
    while line := file.readline():
        json_obj = json.loads(line)
        for expr in exprs:
            item = expr.find(json_obj)
            result.append([x.value for x in item])

    file.close()

    return result

def count(result):
    count = 0
    for line in result:
        count += len(line)
    return count