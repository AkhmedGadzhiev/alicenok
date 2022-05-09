# import
from skills.alicenok.main_skills import *
from skills.alicenok.entertainments_skills import *
from skills.alicenok.on_cartoons import *
from skills.alicenok.games_list import *
from skills.alicenok.alicenok import *


# функция отправляет назад
def back(event):
  payload = event['request']['payload']['back']

  ERROR_RESPONSE = {
    'response' : {
    'text' : 'Малыш, повтори пожалуйста ещё раз',
    'tts' : 'Малыш, повтори пожалуйста ещё раз',
    'end_session' : False,
    'buttons' : [
    {'title' : 'Назад',
    'payload' : {},
    'hide' : True}]},
    'version' : '1.0'}

  try:
    if payload == 'alicenok_help_back':
      return main_skills()

    if payload == 'entertainments_back':
      return main_skills()

    if payload == 'on_cartoons_back':
      return entertainments_skills(event)

    if payload == 'games_list_back':
      return main_skills()

    if payload == 'alicenok_wellcome_message_back':
      return main_skills()

    if payload == 'testers_back':
      return main_skills()

    if payload == 'song_back':
      return entertainments_skills(event)

    if payload == 'fallback_back':
      return main_skills()

    if payload == 'alicenok_back':
      return main_skills()

    if payload == 'feed_back':
      return alicenok()

    if payload == 'drunk_back':
      return alicenok()

    if payload == 'walk_back':
      return alicenok()

    if payload == 'bathroom_back':
      return alicenok()

    if payload == 'games_back':
      return games_list()
      
  except KeyError:
    return ERROR_RESPONSE
