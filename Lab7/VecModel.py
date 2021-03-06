import math
from collections import defaultdict
import Export
import Import


def MakeUniversum(dosc):
    n = []
    for i, val in dosc.items():
        [n.append(item) for item in val[0] if item not in n]
    return n

def TF(n, objs):
    dict = defaultdict(list)
    for word in n:
        for i, val in objs.items():
            val[0] = sorted(val[0])
            dict[word].append(val[0].count(word))
    return dict


def TFIDF(dict, counter, n, objs, export = 0, idfBool = 0):
    newDict = defaultdict(list)
    if idfBool == 1:
        newDict = Import.Import("idf.csv")
    else:
        for i, doc in dict.items():
            count = 0
            for elem in doc:
                if elem > 0:
                    count +=1
            newDict[i].append(math.log(counter/count))
    if export == 1:
        Export.Export("idf.csv",newDict)
    itogDict = defaultdict(list)
    for word in n:
        for i, val in objs.items():
            itogDict[word].append(float(newDict[word][0]) * val[0].count(word) / len(val[0]))
    return itogDict


def Boolean(dict):
    boolDict = defaultdict(list)
    for i, count in dict.items():
        for con in count:
            if con > 0:
                boolDict[i].append(1)
            else:
                boolDict[i].append(0)
    return boolDict