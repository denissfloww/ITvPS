import os
from collections import defaultdict

def ImportDocumets(path):
    dict = defaultdict(list)
    directory = os.getcwd() + "\\" + path
    files = os.listdir(directory)
    for doc in files:
        f = open(os.path.join(directory, doc), encoding='utf-8')
        commString = ''
        for line in f.readlines():
            commString += " " + line
        dict[doc].append(commString)
    return dict