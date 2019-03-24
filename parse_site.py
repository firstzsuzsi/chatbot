import urllib.request
from inscriptis import get_text
import os

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
