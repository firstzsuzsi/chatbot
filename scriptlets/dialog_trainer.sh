#! /bin/bash

python3 -m rasa_core.train \
-d /home/zsuzsi/study/chatbot/noam/domain.yml \
-s /home/zsuzsi/study/chatbot/noam/data/stories.md \
-o /home/zsuzsi/study/chatbot/noam/models/current/dialogue \
-c /home/zsuzsi/study/chatbot/noam/policy_config.yml
