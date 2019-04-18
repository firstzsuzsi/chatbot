from __future__ import absolute_import, division, unicode_literals
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, ReminderScheduled
import datetime
from datetime import timedelta
import re

class SummarizeReminder(Action):
    def name(self):
        return "summarize_reminder"

    def run(self, dispatcher, tracker, domain):
        action = tracker.get_slot("action")
        datetime = tracker.get_slot("datetime")
        response = "So you want me to remind you to {} at {}. Is that true?".format(action, datetime)
        dispatcher.utter_message(response)
        return [SlotSet("action", action)]

class SetReminder(Action):
    def name(self):
        return "set_reminder"

    def run(self, dispatcher, tracker, domain):
        return [ReminderScheduled("reminder_alarm", datetime.datetime.now() + timedelta(seconds=10))]

class ReminderAlarm(Action):
    def name(self):
        return "reminder_alarm"
    def run(self, dispatcher, tracker, domain):
        action = tracker.get_slot("action")
        response = "Hey, I am reminding you! Do this: {}!".format(action)
        dispatcher.utter_message(response)
        return [SlotSet("action", action)]

class ReassureReminder(Action):
# Send the name of action
    def name(self):
        return "reassure_reminder"

    def run(self, dispatcher, tracker, domain):
# Get the entities.
        action = tracker.get_slot("action")
# Tell the user what they will be reminded to do.
        response = "Sure thing! I will remind you to {} in 10 seconds".format(action)
        dispatcher.utter_message(response)
        return [SlotSet("action", action)]

# class Fallback(Action):
#     def name(self):
#         return "fallback"

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_message("I do not know what is going on.")


# class ResetSlot(Action):

#     def name(self):
#         return "reset_slot"

# # Reset action slot to default value after returning it
#     def run(self, dispatcher, tracker, domain):
#         return [SlotSet("action", None)]
