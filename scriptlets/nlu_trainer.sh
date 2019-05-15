#! /bin/bash

python3 -m rasa_nlu.train \
        -c /home/zsuzsi/study/chatbot/noam/data/nlu_config.yml \
        --data /home/zsuzsi/study/chatbot/noam/data/nlu.md\
        -o /home/zsuzsi/study/chatbot/noam/models \
        --fixed_model_name noam_basic \
        --project current \
        --verbose
