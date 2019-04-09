from __future__ import absolute_import, division, unicode_literals
from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import datetime

class setReminder(action):
    def action_remind(self):
        return "set_reminder"

    def set_reminder(self):
        print("Lets pretend I have set a reminder, okay?")
