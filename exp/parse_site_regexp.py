import urllib.request
from inscriptis import get_text
import re

url = "https://en.wikipedia.org/wiki/La_traviata" 
# Get the site requested by the URL
response = urllib.request.urlopen(url)
content = response.read().decode("utf-8")
# Check if the site is downloaded
print("Length of content downloaded: " + str(len(content)) + " characters")

# tokens = [token for token in content.split()]
# print("Total number of tokens: " + str(len(tokens)))
# print("First 100 tokens:\n" + str(tokens[0:100])

# Strip down html fluff from the downloaded site
text = get_text(str(content))

# Split the text into tokens
tokens = re.split("\W+", text)
print("Number of tokens: " + str(len(tokens)))
print("First 10 tokens: " + str(tokens[0:10]))

# Store the frequency of the tokens in a dictionary
frequency = {}
# Count the frequency of the tokens
for words in tokens:
    if words in frequency:
        frequency[words] = frequency[words] + 1
    else:
        frequency[words] = 1
print(frequency)
# print("Top 10 tokens: " + str(frequency[0:10]))
