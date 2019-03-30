from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter
import json

data = "./data/noam_training_data.md"
configure = "./data/nlu_config.yml"
modelExp = "./models/nlu"
metadata = "./models/nlu/default/noam_basic"

def trainer(data, configure, modelExp):
    training_data = load_data(data)
    trainer = Trainer(config.load(configure))
    trainer.train(training_data)
    model_directory = trainer.persist(modelExp, fixed_model_name = "noam_basic")

def loader(metadata, message):
    interpreter = Interpreter.load(metadata)
    result = interpreter.parse(message)
    print(json.dumps(result, indent=2))

# trainer(data, configure, modelExp)
message = input()
loader(metadata, message)
