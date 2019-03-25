from nltk.tokenize import sent_tokenize, regexp_tokenize, word_tokenize
import re
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import WordNetLemmatizer

# request = "Hi, Noam! Remind me to pick the strawberries at 12 p.m. tomorrow. Thank you. :D"


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

# Now stem the heck out of those tokens
# Wrangle any string with your nifty smart tokenizer
# request2 = "Noam, I already ate breakfast, please, stop nagging me."

# Initialize stemmer object
# lst = LancasterStemmer()
# stemmed = []

# Stem the token list and append the values to a new list
# for i in smart_tokenize(request2):
#     stems = lst.stem(i)
#     stemmed.append(stems)
# print(stemmed)

# Lemmatize as well, while you are at it

request3 = "I got quite tired, Noam. Please, set me an alarm for 7 a.m."
lem = WordNetLemmatizer()
lemmas = []

for l in smart_tokenize(request3):
    lemma = lem.lemmatize(l)
    lemmas.append(lemma)
print(lemmas)

