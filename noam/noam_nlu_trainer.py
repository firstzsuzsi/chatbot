from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config

data = "./data/noam_training_data.md"
configure = "./data/nlu_config.yml"
modelExp = "./models/nlu"

def trainer(data, configure, modelExp):
    training_data = load_data(data)
    trainer = Trainer(config.load(configure))
    trainer.train(training_data)
    model_directory = trainer.persist(modelExp, fixed_model_name = "noam_basic")


trainer(data, configure, modelExp)
