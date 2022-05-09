# import
from skills.alicenok.messages import *
from skills.alicenok.main_skills import *
from skills.alicenok.on_cartoons import *
from skills.alicenok.entertainments_skills import *
from skills.alicenok.games_list import *
from skills.alicenok.alicenok import *
from skills.alicenok.feed import *
from skills.alicenok.drunk import *
from skills.alicenok.bathroom import *
from skills.alicenok.walk import *
from skills.alicenok.alicenok_help import *
from skills.alicenok.back import *
from flask import Blueprint, request

alicenok_app = Blueprint('alicenok_app', __name__)

# main function
@alicenok_app.route('/', methods=["POST"])
def handler(): 
    event = request.json
    intents = event['request']['nlu']['intents']
    if 'state' in event and 'user' in event['state'] and 'wellcome_message' in event['state']['user']:
        wellcome_message = event['state']['user']['wellcome_message']

    ERROR_RESPONSE = {
        'response' : {
        'text' : 'Малыш, повтори пожалуйста ещё раз',
        'tts' : 'Малыш, повтори пожалуйста ещё раз',
        'end_session' : False,
        'buttons' : [
        {'title' : 'Назад',
        'payload' : {},
        'hide' : True}]},
        'version' : '1.0',
        'session' : request.json['session']}

    try:
        if wellcome_message == 'was' and event['session']['new']:
            return hi_message(event)

        if event['session']['new']:
            return wellcome_me_message()

        if 'main_skills' in intents:
            return main_skills()
        
        if 'skills' in intents:
            return skills(event)

        if 'entertainments' in intents:
            return entertainments(event)

        if 'continue' in intents:
            return alicenok()
            
        if 'back' in intents:
            return back(event)

        if 'alicenok_actions' in intents:
            return alicenok_actions(event)

        if 'bath' in intents:
            return bath_handler(event)

        if 'drink' in intents:
            return drink_handler(event)

        if 'eat' in intents:
            return feed_handler(event)

        if 'walk' in intents:
            return walk_handler(event)

        if 'help' in intents:
            return alicenok_help()

        if 'games' in intents:
            return make_response_error('Функция пока в стадии разработки')

        if intents == {}: 
            return fallback(event)

    except KeyError:
        return ERROR_RESPONSE 
    
