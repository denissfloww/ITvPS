import spacy
from string import punctuation
from collections import defaultdict
import pymorphy2
from spacy.lang.ru import Russian
from spacy_russian_tokenizer import RussianTokenizer, MERGE_PATTERNS
from prettytable import PrettyTable
import re


def FillDict():
    dict = defaultdict(list)
    dict["N"].append("NOUN")
    dict["A"].append("ADJF")
    dict["A"].append("ADJS")
    dict["A"].append("PRTF")
    dict["A"].append("PRTS")
    dict["A"].append("NUMR")
    dict["A"].append("NPRO")
    dict["V"].append("VERB")
    dict["V"].append("INFN")
    dict["V"].append("GRND")
    dict["D"].append("ADVB")
    dict["P"].append("PREP")
    dict["P"].append("PRCL")
    return dict


def UtfCod(s):
    return s


def ToLowerCase(s):
    return s.lower()


def PunctuationReplace(s):
    return ''.join(c for c in s if c not in punctuation)


def Tokenizer(inp):
    nlp = Russian()
    russian_tokenizer = RussianTokenizer(nlp, MERGE_PATTERNS)
    nlp.add_pipe(russian_tokenizer, name='russian_tokenizer')
    return nlp(inp)


dict = FillDict()


def PosChanger(inp):
    res = ""
    for i in dict.items():
        if inp in i[1]:
            res = i[0]
    if res == "":
        res = inp
    return res


def TableFiller(objs):
    x = PrettyTable()
    x.field_names = ["ID", "Token", "No. of document", "Count", "POS"]
    for i in objs.items():
        Token = i[0]
        ID = i[1][0]
        POS = i[1][1]
        Count = i[1][2]
        NumbDoc = i[1][3]
        x.add_row([ID, Token, NumbDoc, Count, POS])
    return x


inputDocuments = []
while True:
    inp = str(input())
    if inp == "stop":
        break
    else:
        inputDocuments.append(inp)
docCounter = 1
objs = defaultdict(list)
counter = 1
for inp in inputDocuments:
    inp = UtfCod(inp)
    inp = ToLowerCase(inp)
    inp = PunctuationReplace(inp)
    inp = re.sub('[-«»—]', '', inp)
    doc = Tokenizer(inp)
    morph = pymorphy2.MorphAnalyzer()
    for token in list(doc):
        token = token.lemma_
        if token not in objs.keys():
            p = morph.parse(token)[0]
            objs[token].append(counter)
            objs[token].append(PosChanger(p.tag.POS))
            objs[token].append(1)
            objs[token].append(docCounter)
            counter += 1
        else:
            objs[token][2] += 1
    for i in list(objs):
        if re.match('\s', i[0]) is not None:
            rep = ""
            objs.pop(i[0])

    docCounter += 1
print(TableFiller(objs))
