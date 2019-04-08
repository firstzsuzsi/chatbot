from parse_site import parse

# Tokenize text from an html written in a file
url = "https://en.wikipedia.org/wiki/Necronomicon"
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
