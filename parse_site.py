import urllib.request
from inscriptis import get_text
import re
import os

#Add url to the site to be crawled and file path to write into
url = "https://en.wikipedia.org/wiki/The_Marriage_of_Figaro_(play)"
filePath = "/home/zsuzsi/study/python/chatbot/web_page.txt"

#Get the site requested by the URL
response = urllib.request.urlopen(url)
content = response.read().decode("utf-8")
#Get only the text from the requested site
text = get_text(str(content))
#Get rid of unnecessary line breaks
# textNobreak = re.sub("\n", "", text)

#Write site content into file
with open(filePath, "w") as file:
    file.write(str(text))

file.close()

