import os
import io
import sys

counter = 0
length = input()
filePath = "/home/zsuzsi/study/python/chatbot/results.json"

while counter < int(length):
    os.system("< " + filePath + " jq -s '.[" + str(counter) + "].intent | \"\(.name), \(.confidence)\"' && < " + filePath + " jq -s '.[" + str(counter) + "].entities[] | \"\(.value), \(.entity)\"'")
    counter += 1

