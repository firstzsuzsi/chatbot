## story 01
* greet
    - utter_greet
    - action_restart

## story 02
* ask_reminder{"action": "go to the dentist", "datetime": "8 o'clock"}
  - summarize_reminder
    - slot{"action": "go to the dentist"}
    - slot{"datetime": "8 o'clock"}
  - action_listen
* affirmation
  - utter_affirm
  - reassure_reminder
    - slot{"action": "go to the dentist"}
  - set_reminder
  - reminder{"action": "reminder_alarm", "date_time": "2019-04-18T15:45:29.585788", "name": "34ade0ce-61e0-11e9-88ea-3859f9489455", "kill_on_user_msg": true}
  - reminder_alarm
   - slot{"action": "go to the dentist"}

## story 04
* delete_reminder
    - utter_delete

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
* ask_reminder{"action": "eat your veggies", "datetime": "7am tomorrow"}
 - summarize_reminder
   - slot{"action": "eat your veggies"}
   - slot{"datetime": "7am tomorrow"}
 - action_listen
* affirmation
  - utter_affirm
  - reassure_reminder
    - slot{"action": "eat your veggies"}
  - set_reminder
 - reminder{"action": "reminder_alarm", "date_time": "2019-04-18T15:45:29.585788", "name": "34ade0ce-61e0-11e9-88ea-3859f9489455", "kill_on_user_msg": true}
 - reminder_alarm
   - slot{"action": "eat your veggies"}

## story 10
* negation
    - utter_negated

## story 11
* ask_reminder{"action": "take down the trash", "datetime": "5:30"}
  - summarize_reminder
    - slot{"action": "take down the trash"}
    - slot{"datetime": "5:30"}
  - action_listen
* affirmation
  - utter_affirm
  - reassure_reminder
    - slot{"action": "take down the trash"}
  - set_reminder
  - reminder{"action": "reminder_alarm", "date_time": "2019-04-18T15:45:29.585788", "name": "34ade0ce-61e0-11e9-88ea-3859f9489455", "kill_on_user_msg": true}
  - reminder_alarm
    - slot{"action": "take down the trash"}
   
## story 12
* thanks
    - utter_welcome

## story 13
* ask_reminder{"action": "brush your teeth", "datetime": "7am"}
 - summarize_reminder
   - slot{"action": "brush your teeth"}
   - slot{"datetime": "7am"}
 - action_listen
* negation
  - utter_negated

## story 14
* ask_reminder{"action": "go to cookery school", "datetime": "8 pm Tuesday"}
 - summarize_reminder
   - slot{"action": "go to cookery school"}
   - slot{"datetime": "8 pm Tuesday"}
 - action_listen
* negation
  - utter_negated
    
## Generated Story 2224379513271223494
* ask_reminder{"action": "eat cupcakes", "datetime": " 9am tomorrow"}
    - slot{"action": "eat cupcakes"}
    - slot{"datetime": " 9am tomorrow"}
    - summarize_reminder
    - slot{"action": "eat cupcakes"}
* affirmation
    - utter_affirm
    - reassure_reminder
    - slot{"action": "eat cupcakes"}
    - set_reminder
    - reminder{"action": "reminder_alarm", "date_time": "2019-04-18T15:45:29.585788", "name": "34ade0ce-61e0-11e9-88ea-3859f9489455", "kill_on_user_msg": true}
    - reminder_alarm
    - slot{"action": "eat cupcakes"}

