# import
from entertainments_skills import *
from games_list import *
from alicenok import *
from messages import *
from alicenok_help import *


# функция возвращает основной раздел с возможностями
def main_skills():
	return {
	'response' : {
	'text' : 'Вот что я умею',
	'tts' : 'Вот что я умею',
	'end_session' : 'false',
	'card' : {
	'type' : 'BigImage',
	'image_id' : '1521359/46c76afdc205da46b21a'},
	'buttons' : [
	{'title' : 'Развлечения',
	'payload' : {'entertainments' : 'entertainments'},
	'hide' : 'true'},
	{'title' : 'Мини-игры',
	'payload' : {'games' : 'games'},
	'hide' : 'true'},
	{'title' : 'Алисёнок',
	'payload' : {'alicenok' : 'alicenok'},
	'hide' : 'true'},
	{'title' : 'Тестировщикам',
	'payload' : {'back' : 'testers_back'},
	'url' : 'https://www.youtube.com/watch?v=UmS-uFOoyA0',
	'hide' : 'true'},
	{'title' : 'Помощь',
	'payload' : {},
	'hide' : 'true'}]},
	'version' : '1.0'}


# функция обрабатывает выбор основных возможностей
def skills(event):
    payload = event['request']['payload']
    skill = event['request']['nlu']['intents']['skills']['slots']['skills']['value']
    entertainments = {'entertainments' : 'entertainments'}
    games = {'games' : 'games'}
    alicenok = {'alicenok' : 'alicenok'}
    info_games = {'info' : 'info_games'}
    info_entertainments = {'info' : 'info_entertainments'}
    info_alicenok = {'info' : 'info_alicenok'}
    alicenok_wellcome_message = event['state']['user']['alicenok_wellcome_message']

    if payload == entertainments:
        return entertainments_skills(event)
  
    elif payload == games:
        return games_list()

    elif payload == alicenok and alicenok_wellcome_message != 'was':
        return alicenok_wellcome_message(event)

    elif payload == alicenok and alicenok_wellcome_message == 'was':
    	return alicenok_hi_message()

    elif skill == 'testers':
    	return {
		'response' : {
		'text' : 'Перенаправляю на страницу YouTube',
		'end_session' : 'false',
		'buttons' : [
		{'title' : 'Назад',
		'hide' : 'true',
		'payload' : {'back' : 'testers_back'}}]},
		'version' : '1.0'}

    elif payload == info_alicenok or info_entertainments or info_games:
    	return alicenok_help_handler(event)