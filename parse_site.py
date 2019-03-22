import urllib.request
from inscriptis import get_text
import os


# Add url to the site to be crawled and file path to write into
# url = "https://en.wikipedia.org/wiki/The_Marriage_of_Figaro_(play)"
# filePath = "/home/zsuzsi/study/python/chatbot/web_page.txt"

def parse(url, filePath):
    # Get the site requested by the URL
    response = urllib.request.urlopen(url)
    content = response.read().decode("utf-8")
    # Get only the text from the requested site
    text = get_text(str(content))

    # Write site content into file
    with open(filePath, "w") as file:
        file.write(str(text))

    file.close()

urlTest = "https://en.wikipedia.org/wiki/The_Marriage_of_Figaro_(play)"
filePathTest = "/home/zsuzsi/study/python/chatbot/web_page.txt"
parse(urlTest, filePathTest)

# This part is to go into the word_frequency.py file, once I have figured out how to run the parser function in there.

# Get text from a website written in a file
url = "https://en.wikipedia.org/wiki/The_Marriage_of_Figaro_(play)"
filePath = "/home/zsuzsi/study/python/chatbot/web_page.txt"
parse(url, filePath)

# Store the frequency of words in a dictionary
frequency = {}

# Open the file with the website content
filePath = "/home/zsuzsi/study/python/chatbot/web_page.txt"
with open(filePath, "r") as text:
    words = text.read()
    # Tokenize the text
    for tokens in words.split():
        # Count the frequency of the tokens
        if tokens in frequency:
            frequency[tokens] = frequency[tokens] + 1
        else:
            frequency[tokens] = 1
print(frequency)
