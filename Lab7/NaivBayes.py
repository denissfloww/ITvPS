from collections import defaultdict
import math


def CountWordInEachClasses(values):
    commcountDict = defaultdict(int)
    for key, val in values.items():
        commcountDict[int(key)] = len(val[0])
    return commcountDict


def Pwc(tfdict, commcountDict, universum):
    pwcdict = defaultdict(list)
    for key, val in tfdict.items():
        count = 1
        for i in val:
            countWC = int(i) + 1
            countC = commcountDict[count]
            V = int(len(universum))
            pwcdict[key].append((countWC + 1) / (countC + V))
            count += 1
    return pwcdict


def Pc(countClasses):
    summ = 0
    for key, val in countClasses.items():
        summ += val
    print(summ)
    pcDict = defaultdict(list)
    for key, val in countClasses.items():
        pcDict[key].append(val / summ)

    return pcDict


def Pcd(testValues, pwcValues, pcCounts):
    resDict = defaultdict(list)
    counter = 1
    for key, val in testValues.items():
        res = [0 for i in range(len(pcCounts.keys()))]
        for i in range(len(pcCounts.keys())):
            for word in val[0]:
                if word in pwcValues.keys():
                    res[i] += math.log(float(pwcValues[word][i]))
        for key in range(len(res)):
            res[key] = res[key] + math.log(float(pcCounts[str(key + 1)][0]))
        resDict[counter].append(res)
        counter += 1
    return resDict
