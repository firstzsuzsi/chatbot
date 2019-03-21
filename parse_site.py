import urllib.request
from inscriptis import get_text
import re

#Add url to the site to be crawled and file path to write into
url = "https://en.wikipedia.org/wiki/The_Marriage_of_Figaro_(play)"
filePath = "/home/zsuzsi/study/python/web_page.txt"

#Get the site noted by the URL
response = urllib.request.urlopen(url)
content = response.read()

#Write site content into file
with open("/home/zsuzsi/study/python/web_page.txt", "w") as file:
    file.write(str(content))

file.close()

