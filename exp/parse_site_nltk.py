from urllib import request
from bs4 import BeautifulSoup as BS
import nltk
import re

# Get site
url = "https://en.wikipedia.org/wiki/Madama_Butterfly"
content = request.urlopen(url).read().decode("utf-8")
# Recognize elements with BS, isolate paragraphs
soup = BS(content, "lxml")
paragraphs = soup.find_all("p")
# Get text only
text = [t.text for t in paragraphs]

# Tokenize text, get rid of special characters
tokens = re.split("\W+", str(text))

# Create a frequency distribution using NLTK
freq_dist = nltk.FreqDist(tokens)

# Print the whole thing in a key-value format (not actual dictionary)
for key, value in freq_dist.items():
    print(str(key) + ":" + str(value))

# file = "/home/zsuzsi/study/python/chatbot/tokens.csv"
# with open(file, "w") as csv:
#     csv.write(str(tokens_clean))


# Make a plot based on the gathered data
# freq_dist.plot(50, cumulative = False)

# Find all links in site (adds links that are only useful for the server the site is on i.e. images)
# for links in soup.find_all("a"):
    # print(links.get("href"))

