from __future__ import absolute_import, division, unicode_literals
import logging
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

logging.basicConfig(level = "INFO")

training_data = "/home/zsuzsi/study/chatbot/noam/data/stories.md"
policy_config = "/home/zsuzsi/study/chatbot/noam/policy_config.yml"
model_path = "/home/zsuzsi/study/chatbot/noam/models/dialogue"
domain = "/home/zsuzsi/study/chatbot/noam/domain.yml"

agent = Agent(domain, policies = [MemoizationPolicy(), KerasPolicy()])
data = agent.load_data(training_data, augmentation_factor = 50)

agent.train(data)

agent.persist(model_path)
