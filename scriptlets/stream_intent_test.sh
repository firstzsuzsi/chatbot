#! /bin/bash

pdftotext ~/study/tools/ted-chiang-story-of-your-life-2000.pdf - \
    |python3 ~/study/chatbot/scriptlets/stream_sentence_tokenize.py \
    | python3 ~/study/chatbot/noam/noam_nlu_interpreter.py \
    >> ~/study/chatbot/test_short_story.txt
