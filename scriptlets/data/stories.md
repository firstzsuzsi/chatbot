## story 01
* greet
    - utter_greet
    - action_restart

## story 02
* ask_reminder{"action": "go to the dentist"}
    - utter_summary
    - set_reminder
    - slot{"action": "go to the dentist"}

## story 04
* delete_reminder
    - utter_summary

## story 05
* goodbye
    - utter_goodbye

## story 05
* insult
    - utter_sorry

## story 06
* fallback
    - utter_fallback

## story 07
* how_are_you
    - utter_state

## story 08
* escalate
    - utter_escalate

## story 09
* affirmation
    - utter_affirm

## story 10
* negation
    - utter_negated

## story 11
* ask_reminder{"action": "take down the trash"}
    - utter_summary
    - set_reminder
    - slot{"action": "take down the trash"}

## story 12
* thanks
    - utter_welcome
