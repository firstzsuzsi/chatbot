#! /bin/bash

python3 -m rasa_core.train \
        interactive -o /home/zsuzsi/study/chatbot/noam/models/dialogue \
        -d /home/zsuzsi/study/chatbot/noam/domain.yml \
        -c /home/zsuzsi/study/chatbot/noam/policy_config.yml \
        -s /home/zsuzsi/study/chatbot/noam/data/stories.md \
        --nlu /home/zsuzsi/study/chatbot/noam/models/nlu/default/noam_basic \
        --endpoints /home/zsuzsi/study/chatbot/noam/endpoints.yml
