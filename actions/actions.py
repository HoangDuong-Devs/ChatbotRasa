from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
# class ActionCustomFallback(Action):
#     def name(self) -> str:
#         return "action_custom_fallback"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: dict) -> list:
#         dispatcher.utter_message(text="I'm sorry, I didn't understand that. Could you please clarify?")
#         return []
