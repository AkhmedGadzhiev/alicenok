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
    wellcome_message = event['state']['user']['wellcome_message']

    response = {
        'session': request.json['session'],
        'version': request.json['version']
    }

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
            return {**response, **hi_message(event)}

        if event['session']['new']:
            return {**response, **wellcome_me_message()}

        if 'main_skills' in intents:
            return {**response, **main_skills()}
        
        if 'skills' in intents:
            return {**response, **skills(event)}

        if 'entertainments' in intents:
            return {**response, **entertainments(event)}

        if 'continue' in intents:
            return {**response, **alicenok()}
            
        if 'back' in intents:
            return {**response, **back(event)}

        if 'alicenok_actions' in intents:
            return {**response, **alicenok_actions(event)}

        if 'bath' in intents:
            return {**response, **bath_handler(event)}

        if 'drink' in intents:
            return {**response, **drink_handler(event)}

        if 'eat' in intents:
            return {**response, **feed_handler(event)}

        if 'walk' in intents:
            return {**response, **walk_handler(event)}

        if 'help' in intents:
            return {**response, **alicenok_help()}

        if 'games' in intents:
            return {**response, **make_response_error('Функция пока в стадии разработки')}

        if intents == {}: 
            return {**response, **fallback(event)}

    except KeyError:
        return ERROR_RESPONSE
