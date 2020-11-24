import math
import re
from collections import defaultdict
from nltk.stem.snowball import SnowballStemmer
import spacy
from spacy_russian_tokenizer import RussianTokenizer, MERGE_PATTERNS
from spacy.lang.ru import Russian
import Measures
import Export
import Import
import NaivBayes
import PreProcessing
import VecModel

test = Import.ImportDocumets("train")
dosc = defaultdict(list)
docForClasses = defaultdict(list)
classes = ['1', '1', '1', '2', '2', '2', '3', '3', '3']
counter = 0
for key, value in test.items():
    value = PreProcessing.ToLowerCase(str(value))
    value = PreProcessing.PunctuationReplace(str(value))
    value = PreProcessing.Tokenizer(value)
    value = PreProcessing.LemmAndStem(value)
    del value[0]
    docForClasses[classes[counter]].append(value)
    dosc[classes[counter]].append(value)
    counter += 1

n = []
for i, val in dosc.items():
    [n.append(item) for item in val[0] if item not in n]
tfdict = VecModel.TF(n, docForClasses)

pwcdict = defaultdict(list)
commcountDict = defaultdict(int)
for key, val in docForClasses.items():
    commcountDict[int(key)] = len(val[0])

for key, val in tfdict.items():
    count = 1
    for i in val:
        countWC = int(i) + 1
        countC = commcountDict[count]
        V = int(len(n))
        pwcdict[key].append((countWC + 1) / (countC + V))
        count += 1

test = Import.ImportDocumets("test")
Udocs = defaultdict(list)
UdocForClasses = defaultdict(list)
counter = 1
UcountDocsInClass = defaultdict(list)
for key, value in test.items():
    value = PreProcessing.ToLowerCase(str(value))
    value = PreProcessing.PunctuationReplace(str(value))
    value = PreProcessing.Tokenizer(value)
    value = PreProcessing.LemmAndStem(value)
    del value[0]
    UdocForClasses[counter].append(value)
    UcountDocsInClass[counter].append(1)
    Udocs[counter].append(value)
    counter += 1

res = NaivBayes.Pcd(UdocForClasses, pwcdict)
