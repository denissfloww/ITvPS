import math
from collections import defaultdict


def TF(n, objs):
    dict = defaultdict(list)
    for word in n:
        for i, val in objs.items():
            val[0] = sorted(val[0])
            dict[word].append(val[0].count(word))
    return dict


def TFIDF(dict, counter):
    newDict = defaultdict(list)
    for i, doc in dict.items():
        count = 0
        for elem in doc:
            if elem > 0:
                count +=1
        newDict[i].append(math.log(counter/count))
    itogDict = defaultdict(list)
    for word in n:
        for i, val in objs.items():
            itogDict[word].append(newDict[word][0] * val[0].count(word) / len(val[0]))
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