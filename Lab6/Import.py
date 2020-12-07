from collections import defaultdict
import csv
from collections import Counter

def ImportTrainDocumets(file):
    dict = defaultdict(list)
    with open(file, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        classArray = []
        for row in file_reader:
            if row[3] == "class":
                continue
            dict[row[3]].append(row[1] + " " + row[2])
            classArray.append(row[3])
        newDict = defaultdict(list)
        for key, val in dict.items():
            newDict[key].append(' '.join(val))
        countClass = Counter(classArray)
    return countClass, newDict

def ImportTestDocuments(file):
    dict = defaultdict(list)
    with open(file, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        count = 0
        for row in file_reader:
            if row[3] == "class":
                continue
            dict[count].append(row[1] + " " + row[2])
            count += 1
    return dict


def Import(file = "pwc.csv"):
    dict = defaultdict(list)
    with open(file, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            if len(row) == 0:
                continue
            for i in range(1, len(row)):
                dict[row[0]].append(row[i])
    return dict
