import math
import re
from collections import defaultdict
from nltk.stem.snowball import SnowballStemmer
import spacy
from spacy_russian_tokenizer import RussianTokenizer, MERGE_PATTERNS
from spacy.lang.ru import Russian
import Measures
import Export


def ToLowerCase(s):
    return s.lower()


def PunctuationReplace(inp):
    inp = re.sub('[-«»—,.()\[\]"%:;?]', ' ', inp)
    inp = re.sub('\\n', '', inp)
    inp = inp.replace('\\', '')
    inp = inp.replace('n', '')
    inp = inp.replace("'", '')
    inp = inp.replace('ufeff', '')
    inp = inp.replace('xa0', ' ')
    inp = re.sub(r'\s{2,3}', ' ', inp)
    inp = re.sub(r'\s{2}', ' ', inp)
    return inp


def Tokenizer(inp):
    nlp = Russian()
    russian_tokenizer = RussianTokenizer(nlp, MERGE_PATTERNS)
    nlp.add_pipe(russian_tokenizer, name='russian_tokenizer')
    return nlp(inp)


def LemmAndStem(inp):
    doc = []
    stemmer = SnowballStemmer("russian")
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
