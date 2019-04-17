from __future__ import absolute_import, division, unicode_literals
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import re
import datetime

class SetReminder(Action):
# Send the name of action
    def name(self):
        return "set_reminder"

    def run(self, dispatcher, tracker, domain):
# Get the entities.
        action = tracker.get_slot("action")
        datetime = tracker.get_slot("datetime")
# Tell the user what they will be reminded to do.
        response = "Sure thing! I will remind you to {} at {}".format(action, datetime)
        dispatcher.utter_message(response)
        results = [SlotSet("action", action)]
        return results

# class ResetSlot(Action):

#     def name(self):
#         return "reset_slot"

# # Reset action slot to default value after returning it
#     def run(self, dispatcher, tracker, domain):
#         return [SlotSet("action", None)]
