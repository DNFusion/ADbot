# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_check_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        mylist = []
        with open(file='data/entities.csv', mode='r') as f:
            myfile = csv.reader(f,delimiter=',')
            for row in myfile:
                for col in row:
                    mylist.append(col)
        print(tracker.latest_message)
        Tintent = tracker.latest_message['intent']
        intent = Tintent['name']
        if intent == "ask_location":
            for ent in tracker.latest_message['entities']:
                print(ent['entity'])
                if ent['entity'] in ["Department","Company"]:
                    dispatcher.utter_message(f"for {ent['value']} You will find it in {mylist[mylist.index(ent['value'])+1]}")
                elif ent['entity'] == "Person":
                    dispatcher.utter_message(f"You will find {ent['value']} in {mylist[mylist.index(ent['value'])+1]}")
        elif intent == "ask_info":
            for ent in tracker.latest_message['entities']:
                    dispatcher.utter_message(f"{mylist[mylist.index(ent['value'])+2]}\n")



        return []
