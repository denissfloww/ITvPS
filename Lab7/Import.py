import os
from collections import defaultdict
import csv
from collections import Counter
import re


def ImportTrainDocumets(docName):
    dict = defaultdict(list)
    countDocInClass = defaultdict(list)
    docClass = defaultdict(list)
    count = 1
    countForClasses = 1
    for file in docName:
        commString = ''
        f = open(file, encoding='utf-8')
        for line in f.readlines():
            commString += line
        documents = re.split(r'[*]+', commString)
        countDocInClass[countForClasses].append(0)
        for i in documents:
            countDocInClass[countForClasses][0] += 1
            docClass[count].append(countForClasses)
            dict[count].append(i)
            count += 1
        countForClasses += 1
    return dict, countDocInClass, docClass


def ImportTestDocuments(file):
    dict = defaultdict(list)
    with open(file, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        classArray = []
        count = 0
        for row in file_reader:
            if row[1] == "class":
                continue
            dict[count].append(row[0])
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
