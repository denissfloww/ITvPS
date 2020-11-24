from collections import defaultdict
import math


def Pcd(UdocForClasses, pwcdict):
    Pc = math.log(3 / 9)
    dict = defaultdict(list)
    counter = 1
    for key, val in UdocForClasses.items():
        res = defaultdict(int)
        for i in range(3):
            for word in val[0]:
                if word in pwcdict.keys():
                    res[i] += math.log(pwcdict[word][i])
        for i in res:
            i = Pc + i
        dict[counter].append(res)
        counter += 1
    return dict
