import csv
import math
import re
from collections import defaultdict
from string import punctuation
from nltk.stem.snowball import SnowballStemmer


def DocImport(r_file):
    commString = ''
    f = open(r_file)
    for line in f.readlines():
        commString += line
    documents = re.split(r'Документ\s+№\s*\d+[*]+', commString)
    return documents


def ToLowerCase(s):
    return s.lower()


def PunctuationReplace(s):
    return ''.join(c for c in s if c not in punctuation)


def ExportCsv(dict, counter):
    with open('model.csv', 'w+', encoding='utf-8') as file:
        a_pen = csv.writer(file)
        first_str = "Term "
        for i in range(1, counter):
            first_str += "Text:" + str(i) + " "
        first_str = first_str.split(" ")
        a_pen.writerow(first_str)
        for i, doc in dict.items():
            str_r = [i] + doc
            a_pen.writerow(str_r)


def TF(n, objs):
    dict = defaultdict(list)
    for word in n:
        for i, val in objs.items():
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
    print(newDict)
    itogDict = defaultdict(list)
    for word in n:
        for i, val in objs.items():
            itogDict[word].append(newDict[word][0] * val[0].count(word) / len(val[0]))
    print(itogDict)
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


stemmer = SnowballStemmer("russian")
documents = DocImport("dataset.txt")
print("Введите номера документов через enter. Для окончания ввода введите stop")
inputDocuments = []
while True:
    inp = str(input())
    if inp == "stop":
        break
    else:
        inputDocuments.append(documents[int(inp)])
objs = defaultdict(list)
counter = 1
doc = []
for inp in inputDocuments:
    inp = ToLowerCase(inp)
    inp = re.sub('[-«»—]', ' ', inp)
    inp = PunctuationReplace(inp)
    inp = re.sub('\n', '', inp)
    inp = re.sub(r'\s{2}', ' ', inp)
    inp = re.split('\s', inp)
    for i in range(len(inp)):
        inp[i] = stemmer.stem(inp[i])
    objs[counter].append(inp)
    doc += inp
    counter += 1
n = []
for i in doc:
    if i not in n:
        if i != "":
            n.append(i)
print("Выберите тип весов (1 - TF, 2 - Boolean, 3 - TF*IDF)")
typeInput = str(input())
if typeInput is "1":
    print("Индексирование завершено")
    ExportCsv(TF(n, objs), counter)
if typeInput is "2":
    print("Индексирование завершено")
    boolModel = Boolean(TF(n, objs))
    ExportCsv(boolModel, counter)
if typeInput is "3":
    print("Индексирование завершено")
    idfModel = TFIDF(TF(n, objs), counter - 1)
    ExportCsv(idfModel, counter)
