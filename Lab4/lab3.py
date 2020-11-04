import csv
import math
import re
from collections import defaultdict
from string import punctuation
from nltk.stem.snowball import SnowballStemmer
import spacy
from spacy_russian_tokenizer import RussianTokenizer, MERGE_PATTERNS
from spacy.lang.ru import Russian
import Measures
import Export


def DocImport(r_file):
    commString = ''
    f = open(r_file)
    for line in f.readlines():
        commString += line
    documents = re.split(r'Документ\s+№\s*\d+[*]+', commString)
    return documents


def ToLowerCase(s):
    return s.lower()


def PunctuationReplace(inp):
    inp = ''.join(c for c in inp if c not in punctuation)
    inp = re.sub('[-«»—]', ' ', inp)
    inp = re.sub('\n', '', inp)
    inp = re.sub(r'\s{2}', ' ', inp)
    return inp


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

def Tokenizer(inp):
    nlp = Russian()
    russian_tokenizer = RussianTokenizer(nlp, MERGE_PATTERNS)
    nlp.add_pipe(russian_tokenizer, name='russian_tokenizer')
    return nlp(inp)

def LemmAndStem(inp):
    doc = []
    for token in list(inp):
        token = token.lemma_
        token = stemmer.stem(token)
        doc.append(token)
    return doc

stemmer = SnowballStemmer("russian")
documents = DocImport("dataset.txt")
print("Введите номера документов через enter. Для окончания ввода введите stop")
inputDocuments = []
inpNumber = []
while True:
    inp = str(input())
    if inp == "stop":
        break
    else:
        inpNumber.append(int(inp))
        inputDocuments.append(documents[int(inp)])
objs = defaultdict(list)
counter = 1
doc = []
for inp in inputDocuments:
    inp = ToLowerCase(inp)
    inp = PunctuationReplace(inp)
    inp = Tokenizer(inp)
    doc = LemmAndStem(inp)
    objs[counter].append(doc)
    doc += doc
    counter += 1
n = []
for i in doc:
    if i not in n:
        if i != "":
            n.append(i)
TFModelDoc = TF(n, objs)
Export.ExportCsv(TFModelDoc, counter)
query = u"Веб Всемирно известный физик-теоретик Стивен Хокинг уверен, что Марс будет колонизирован людьми в ближайшее столетие, сообщает Rusargument."
query = ToLowerCase(query)
query = PunctuationReplace(query)
query = Tokenizer(query)
doc = LemmAndStem(query)
n = []
for i in doc:
    if i not in n:
        if i != "":
            n.append(i)
objs = defaultdict(list)
objs[1].append(doc)
query = TF(n, objs)
cos = Measures.Cos(query, TFModelDoc, counter - 1)
jacc = Measures.Jaccarda(query, TFModelDoc, counter - 1)
dice = Measures.Dice(query, TFModelDoc, counter - 1)
Export.ExportCsvMeasures(cos, jacc, dice, inpNumber)
print("Индексирование завершено")