from rasa_nlu.model import Metadata, Interpreter
import sys
import json

metadata = "/home/zsuzsi/study/chatbot/noam/models/nlu/default/noam_basic/"

def loader(metadata, message):
    interpreter = Interpreter.load(metadata)
    result = interpreter.parse(message)
    print(json.dumps(result, indent=2))

while True:
    line = sys.stdin.readline()
    line = line.replace("\n", " ")
    line = line.lower()
    if not line:
        break
    else:
        loader(metadata, line)
