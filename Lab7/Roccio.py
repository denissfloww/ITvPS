import math
from collections import defaultdict


def RoccioTrain(countClasses, tfidf, docClass):
    resDict = defaultdict(list)
    for key, val in countClasses.items():
        for key2, val2 in tfidf.items():
            M = 0
            count = 0
            for i in val2:
                if docClass[count + 1][0] == key:
                    M += i
                count += 1
            resDict[key2].append(M / val[0])
    return resDict


def RoccioCalc(tfidf, roccioVal, testDocCount, roccioClassCount):
    resDict = defaultdict(list)
    for i in range(testDocCount):
        tokenAndMdict = defaultdict(list)
        for key , val in tfidf.items():
            for j in range(roccioClassCount):
                if key in roccioVal.keys():
                    MD = (float(roccioVal[key][j]) - float(val[i])) ** 2
                    tokenAndMdict[key].append(MD)
        for k in range(roccioClassCount):
            U = 0
            for key2 , val2 in tokenAndMdict.items():
                U += float(val2[k])
            U = math.sqrt(U)
            resDict[k].append(U)
    return  resDict




