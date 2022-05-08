# import
from skills.alicenok.on_cartoons import *
from skills.alicenok.messages import *


# функция возвращает список развлечений
def entertainments_skills(event):
	return {
	'response' : {
	'text' : 'Вот список развлечений',
	'tts' : 'Вот список развлечений. Обрати внимание что некоторые функции пока ещё в стадии разработки.',
	'end_session' : False, 
	'card' : {
	'type' : 'BigImage', 
	'image_id' : '1030494/7bf1cf374ceb4edf93f7'},
	'buttons' : [
	{'title' : 'Включи мультик', 
	'payload' : {}, 
	'hide' : True}, 
	{'title' : 'Расскажи сказку', 
	'payload' : {}, 
	'url' : 'https://music.yandex.ru/users/yamusic-podcast/playlists/1039/?from=alice&mob=0&play=1', 
	'hide' : True},
	{'title' : 'Спой песенку', 
	'payload' : {}, 
	'hide' : True},
	{'title' : 'Назад', 
	'payload' : {'back' : 'entertainments_back'}, 
	'hide' : True}]}, 
	'version' : '1.0'}  


# функция обрабатывает запросы при нажатии кнопок в разделе развлечений
def entertainments(event):
	intent = event['request']['nlu']['intents']['entertainments']
	entertainment = intent['slots']['entertainments']['value']

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
		if entertainment == 'cartoon':
			return on_cartoons()

		if entertainment == 'story':
			return {
			'response' : {
			'text' : 'Включаю сказку',
			'tts' : 'Включаю сказку',
			'end_session' : False,
			'buttons' : [
			{'title' : 'Назад',
			'hide' : True,
			'payload' : {'back' : 'on_cartoons_back'}}]},
			'version' : '1.0'}

		if entertainment == 'song':
			return {
			'response' : {
			'text' : 'Функция пока в стадии разработки',
			'tts' : 'Функция пока в стадии разработки',
			'end_session' : False,
			'buttons' : [
			{'title' : 'Назад',
			'hide' : True,
			'payload' : {'back' : 'song_back'}}]},
			'version' : '1.0'}

	except KeyError:
		return ERROR_RESPONSEs
