import math
import re
from collections import defaultdict
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
    # inp = ''.join(c for c in inp if c not in punctuation)
    inp = re.sub('[-«»—,.()\[\]"%:;?]', ' ', inp)
    inp = re.sub('\n', '', inp)
    inp = re.sub(r'\s{2,3}', ' ', inp)
    inp = re.sub(r'\s{2}', ' ', inp)
    return inp


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

def ObjsCleaner(objs):
    for key, val in objs.items():
        for i in val[0]:
            if i is ' ' or i is '  ':
                val[0].remove(i)
    return objs

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
docs = []
for inp in inputDocuments:
    inp = ToLowerCase(inp)
    inp = PunctuationReplace(inp)
    inp = Tokenizer(inp)
    doc = LemmAndStem(inp)
    objs[counter].append(doc)
    docs += doc
    counter += 1
n = []
[n.append(item) for item in docs if item not in n]
objs = ObjsCleaner(objs)
TFModelDoc = TF(n, objs)
Export.ExportCsv(TFModelDoc, counter)
print("Введите запрос")
query = str(input())
query = ToLowerCase(query)
query = PunctuationReplace(query)
query = Tokenizer(query)
docs2 = LemmAndStem(query)
n2 = []
[n2.append(item) for item in docs2 if item not in n2]
objs2 = defaultdict(list)
objs2[1].append(docs2)
query = TF(n2, objs2)
cos = Measures.Cos(query, TFModelDoc, counter - 1)
jacc = Measures.Jaccarda(query, TFModelDoc, counter - 1)
dice = Measures.Dice(query, TFModelDoc, counter - 1)
Export.ExportCsvMeasures(cos, jacc, dice, inpNumber)
print("Индексирование завершено")