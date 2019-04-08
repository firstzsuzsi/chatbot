#!/usr/bin/env python3

import sys
import re
from nltk.tokenize import sent_tokenize

lineList= []
while True:
    line = sys.stdin.readline()
    if not line:
        break
    line = line.replace("\n", " ")
    line = re.sub("^[\s+]" , "", line)
    lineList.append(line)

sentenceList = sent_tokenize("".join(lineList))

for sentence in sentenceList:
    print(sentence)
