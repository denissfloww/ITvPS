import math
from collections import defaultdict


def Cos(query, TFModel, counter):
    res = defaultdict(list)
    for i in range(counter):
        cur = defaultdict(list)
        for key, value in TFModel.items():
            cur[key].append(value[i])
        res[i].append(CalcCos(query, cur))
    return res


def CalcCos(query, cur):
    summ = 0
    sumsqrt1 = 0
    sumsqrt2 = 0
    cur = DictAdd(query, cur)
    query = DictAdd(cur, query)
    for key,val in query.items():
        summ += cur[key][0] * query[key][0]
        sumsqrt1 += cur[key][0] ** 2
        sumsqrt2 += query[key][0] ** 2
    sumsqrt1 = math.sqrt(sumsqrt1)
    sumsqrt2 = math.sqrt(sumsqrt2)
    res = summ / (sumsqrt1 * sumsqrt2)
    return res

def Jaccarda(query, TFModel, counter):
    res = defaultdict(list)
    for i in range(counter):
        cur = defaultdict(list)
        for key, value in TFModel.items():
            cur[key].append(value[i])
        res[i].append(CalcJacc(query, cur))
    return res

def CalcJacc(query, cur):
    numerator = 0
    denumerator = 0
    cur = DictAdd(query, cur)
    query = DictAdd(cur, query)
    for key, val in query.items():
        numerator += min(query[key][0], cur[key][0])
        denumerator += max(query[key][0], cur[key][0])
    res = numerator / denumerator
    return res

def Dice(query, TFModel, counter):
    res = defaultdict(list)
    for i in range(counter):
        cur = defaultdict(list)
        for key, value in TFModel.items():
            cur[key].append(value[i])
        res[i].append(CalcDice(query, cur))
    return res

def CalcDice(query, cur):
    numerator = 0
    denumerator = 0
    cur = DictAdd(query, cur)
    query = DictAdd(cur, query)
    for key, val in query.items():
        numerator += min(query[key][0], cur[key][0])
        denumerator += query[key][0] + cur[key][0]
    res = (2 * numerator) / denumerator
    return res

def DictAdd(query, cur):
    for key, val in query.items():
        if key not in cur:
            cur[key].append(0)
    return cur