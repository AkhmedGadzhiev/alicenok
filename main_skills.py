# import
from skills.alicenok.entertainments_skills import *
from skills.alicenok.games_list import *
from skills.alicenok.alicenok import *
from skills.alicenok.messages import *
from skills.alicenok.alicenok_help import *


# функция возвращает основной раздел с возможностями
def main_skills():
	return {
	'response' : {
	'text' : 'Вот что я умею',
	'tts' : 'Вот что я умею',
	'end_session' : False,
	'card' : {
	'type' : 'BigImage',
	'image_id' : '1521359/46c76afdc205da46b21a'},
	'buttons' : [
	{'title' : 'Развлечения',
	'payload' : {'entertainments' : 'entertainments'},
	'hide' : True},
	{'title' : 'Мини-игры',
	'payload' : {'games' : 'games'},
	'hide' : True},
	{'title' : 'Алисёнок',
	'payload' : {'alicenok' : 'alicenok'},
	'hide' : True},
	{'title' : 'Тестировщикам',
	'payload' : {'back' : 'testers_back'},
	'url' : 'https://www.youtube.com/watch?v=UmS-uFOoyA0',
	'hide' : True},
	{'title' : 'Помощь',
	'payload' : {},
	'hide' : True}]},
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
		if payload == entertainments:
			return entertainments_skills(event)

		if payload == games:
			return games_list()

		if payload == alicenok and alicenok_wellcome_message != 'was':
			return alicenok_wellcome_message(event)

		if payload == alicenok and alicenok_wellcome_message == 'was':
			return alicenok_hi_message()

		if skill == 'testers':
			return {
			'response' : {
			'text' : 'Перенаправляю на страницу YouTube',
			'end_session' : False,
			'buttons' : [
			{'title' : 'Назад',
			'hide' : True,
			'payload' : {'back' : 'testers_back'}}]},
			'version' : '1.0'}

		if payload == info_alicenok or info_entertainments or info_games:
			return alicenok_help_handler(event)

	except KeyError:
		return ERROR_RESPONSE
