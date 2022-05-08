# import
from on_cartoons import *
from messages import *


# функция возвращает список развлечений
def entertainments_skills(event):
	return {
	'response' : {
	'text' : 'Вот список развлечений',
	'tts' : 'Вот список развлечений. Обрати внимание что некоторые функции пока ещё в стадии разработки.',
	'end_session' : 'false', 
	'card' : {
	'type' : 'BigImage', 
	'image_id' : '1030494/7bf1cf374ceb4edf93f7'},
	'buttons' : [
	{'title' : 'Включи мультик', 
	'payload' : {}, 
	'hide' : 'true'}, 
	{'title' : 'Расскажи сказку', 
	'payload' : {}, 
	'url' : 'https://music.yandex.ru/users/yamusic-podcast/playlists/1039/?from=alice&mob=0&play=1', 
	'hide' : 'true'},
	{'title' : 'Спой песенку', 
	'payload' : {}, 
	'hide' : 'true'},
	{'title' : 'Назад', 
	'payload' : {'back' : 'entertainments_back'}, 
	'hide' : 'true'}]}, 
	'version' : '1.0'}  


# функция обрабатывает запросы при нажатии кнопок в разделе развлечений
def entertainments(event):
	intent = event['request']['nlu']['intents']['entertainments']
	entertainment = intent['slots']['entertainments']['value']

	if entertainment == 'cartoon':
		return on_cartoons()

	elif entertainment == 'story':
		return {
		'response' : {
		'text' : 'Включаю сказку',
		'tts' : 'Включаю сказку',
		'end_session' : 'false',
		'buttons' : [
		{'title' : 'Назад',
		'hide' : 'true',
		'payload' : {'back' : 'on_cartoons_back'}}]},
		'version' : '1.0'}

	elif entertainment == 'song':
		return {
		'response' : {
		'text' : 'Функция пока в стадии разработки',
		'tts' : 'Функция пока в стадии разработки',
		'end_session' : 'false',
		'buttons' : [
		{'title' : 'Назад',
		'hide' : 'true',
		'payload' : {'back' : 'song_back'}}]},
		'version' : '1.0'}