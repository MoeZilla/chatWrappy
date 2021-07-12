import requests

from src import base


message = ""
name = "chatbot"
owner = "moezilla"
userid = "1"

def chat(msg):
    message = msg
    body = {
        'message': message,
        'name': botname,
        'onwer': onwername,
        'userid': user
    }
    response = requests.get(url=base, params=body).json()['message']
    
    return response




                                                                                                                                                                                                                                                               
