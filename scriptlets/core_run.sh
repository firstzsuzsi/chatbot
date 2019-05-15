#!/bin/bash

python3 -m rasa_core.run \
       --enable_api \
       -d /home/zsuzsi/study/chatbot/noam/models/dialogue \
       -u /home/zsuzsi/study/chatbot/noam/models/nlu/default/noam_basic \
       --endpoints /home/zsuzsi/study/chatbot/noam/endpoints.yml
