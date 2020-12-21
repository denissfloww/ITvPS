from collections import defaultdict


def DictFiller(count):
    infoClasses = defaultdict(list)
    for i in range(1, count + 1):
        infoClasses[i].append(0)
        infoClasses[i].append(0)
        infoClasses[i].append(0)
    return infoClasses


def Count(sourceClasses, resultClasses, infoClasses):
    for i in range(len(sourceClasses)):
        if sourceClasses[i] == resultClasses[i]:
            infoClasses[sourceClasses[i]][0] += 1
        else:
            infoClasses[sourceClasses[i]][1] += 1
            infoClasses[resultClasses[i]][2] += 1
    return infoClasses


def Calculate(count, infoClasses):
    resultDict = DictFiller(count)
    for i in range(1, count + 1):
        TP = infoClasses[i][0]
        FP = infoClasses[i][1]
        FN = infoClasses[i][2]
        P = TP / (FP + TP if FP + TP != 0 else 1)
        R = TP / (FN + TP if FN + TP != 0 else 1)
        F = 2 * P * R / (P + R if P + R != 0 else 1)
        resultDict[i][0] = P
        resultDict[i][1] = R
        resultDict[i][2] = F
    return resultDict