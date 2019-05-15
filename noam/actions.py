from __future__ import absolute_import, division, unicode_literals
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, ReminderScheduled
import datetime
from datetime import timedelta
import re

class SetReminder(Action):
    def name(self):
        return "ask_reminder"

    def run(self, dispatcher, tracker, domain):
        response = "Let's pretend I have set a reminder, shall we?"
        dispatcher.utter_message(response)

class SummarizeReminder(Action):
    def name(self):
        return "summarize_reminder"

    def run(self, dispatcher, tracker, domain):
        action = tracker.get_slot("action")
        datetime = tracker.get_slot("datetime")
        response = "So you want me to remind you to {} at {}. Is that true?".format(action, datetime)
        dispatcher.utter_message(response)
        return [SlotSet("action", action)]

class ReassureReminder(Action):
# Send the name of action
    def name(self):
        return "reassure_reminder"

    def run(self, dispatcher, tracker, domain):
# Get the entities.
        datetime = tracker.get_slot("datetime")
# Tell the user what they will be reminded to do.
        response = "Sure thing! Reminder set for the following time: {} ".format(datetime)
        dispatcher.utter_message(response)
        return [SlotSet("datetime", datetime)]

class ReminderAlarm(Action):
    def name(self):
        return "reminder_alarm"
    def run(self, dispatcher, tracker, domain):
        action = tracker.get_slot("action")
        response = "Hey, I am reminding you! Do this: {}!".format(action)
        dispatcher.utter_message(response)
        return [SlotSet("action", action)]

class DeleteReminder(Action):
    def name(self):
        return "delete_reminder"
    def run(self, dispatcher, tracker, domain):
        response = "Reminders are still imaginary. So let's imagine I've just deleted this one.".format(action)
        dispatcher.utter_message(response)

class SummarizeDeleteReminder(Action):
    def name(self):
        return "summarize_delete_reminder"
    def run(self, dispatcher, tracker, domain):
        action = tracker.get_slot("action")
        datetime = tracker.get_slot("datetime")
        response = "You want me to delete the reminder for {} that was set for {}. Is that true?".format(action, datetime)
        dispatcher.utter_message(response)
        return [SlotSet("action", action)]

class ReassureDeleteReminder(Action):
    def name(self):
        return "reassure_delete_reminder"
    def run(self, dispatcher, tracker, domain):
        action = tracker.get_slot("action")
        datetime = tracker.get_slot("datetime")
        response = "I will delete the reminder for {}.".format(datetime)
        dispatcher.utter_message(response)
        return [SlotSet("datetime", datetime)]

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
