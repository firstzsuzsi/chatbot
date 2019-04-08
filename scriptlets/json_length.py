import subprocess

counter = 1
filePath = "/home/zsuzsi/study/python/chatbot/results.json"

len = subprocess.Popen(["jq \"length\" /home/zsuzsi/study/python/chatbot/results.json"], stdout=subprocess.PIPE, shell = True)
out = len.stdout.read()

# print(out)

for i in len(out):
    counter += 1
print(counter)
