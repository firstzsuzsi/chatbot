from nltk.tokenize import sent_tokenize, regexp_tokenize, word_tokenize
import re

# Tokenizer that gets rid of punctuation, but keeps abbreviations intact (basically the best of sentence, regexp and word tokenization)
def smart_tokenize(request):
    # Parse the input into sentences the smart way
    sentences = sent_tokenize(request)
    sentences_nopunct = []

    # Get rid of punctuation, but not in abbreviations (not perfect, it slices off periods in abbreviations if they are at the end of a sentence...)
    for i in sentences:
        noend = re.sub("[\!\?\.\+]$", " ", i)
        nopunct = re.sub("[\,\;\:]", "", noend)
        sentences_nopunct.append(nopunct)

    # Finally, get those juicy word tokens you wanted all along
    string = "".join(sentences_nopunct)
    words = word_tokenize(string)
    return words

request = "Hi, Noam! Remind me to pick the strawberries at 12 p.m. tomorrow. Thank you. :D"
print(smart_tokenize(request))
