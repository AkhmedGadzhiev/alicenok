# import
from skills.alicenok.feed import *
from skills.alicenok.drunk import *
from skills.alicenok.walk import *
from skills.alicenok.bathroom import *


# функция выводит вступительное сообщение
def alicenok_wellcome_message(event):
	return {
	'response' : {
	'text' : 'Привет! Теперь ты мой хозяин. Меня можно накормить, напоить, выгулять, помыть. Только не забывай пожалуйста обо мне',
	'tts' : 'Привет! Теперь ты мой хозяин. Меня можно накормить, напоить, выгулять, помыть. Только не забывай пожалуйста обо мне',
	'end_session' : False,
	'card' : {
	'type' : 'BigImage',
	'image_id' : '1540737/721d93d5c6a17a965325'},
	'buttons' : [
	{'title' : 'Далее',
	'payload' : {'continue' : 'continue'},
	'hide' : True},
	{'title' : 'Назад',
	'payload' : {'back' : 'alicenok_wellcome_message_back'},
	'hide' : True}]},
	'user_state_update' : {'alicenok_wellcome_message' : 'was'},
	'version' : '1.0'}

# функция выводит приветственное сообщение
def alicenok_hi_message():
	return {
	'response' : {
	'text' : 'Привет хозяин! Я проголодался, а ещё хочу пить и мне не помешал бы лёгкий душ после прогулки',
	'tts' : 'Привет хозяин! Я проголодался, а ещё хочу пить и мне не помешал бы лёгкий душ после прогулки',
	'end_session' : False,
	'buttons' : [
	{'title' : 'Далее',
	'hide' : True,
	'payload' : {'continue' : 'alicenok_continue'}},
	{'title' : 'Назад',
	'hide' : True,
	'payload' : {'back' : 'alicenok_back'}}]},
	'version' : '1.0'}


# функция выводит список возможностей для Алисёнка
def alicenok():
	return {
	'response' : {
	'text' : 'Вот что ты можешь',
	'tts' : 'Вот что ты можешь',
	'end_session' : False, 
	'card' : {
	'type' : 'BigImage',
	'image_id' : '1521359/46c76afdc205da46b21a'},
	'buttons' : [
	{'title' : 'Покормить',
	'payload' : {},
	'hide' : True},
	{'title' : 'Напоить',
	'payload' : {},
	'hide' : True},
	{'title' : 'Выгулять',
	'payload' : {},
	'hide' : True},
	{'title' : 'Помыть',
	'payload' : {},
	'hide' : True},
	{'title' : 'Назад',
	'payload' : {'back' : 'alicenok_back'},
	'hide' : True}]},
	'version' : '1.0'}


# функция обрабатывает выбор действий для Алисёнка
def alicenok_actions(event):
	intent = event['request']['nlu']['intents']['alicenok_actions']
	action = intent['slots']['actions']['value']

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
		if action == 'feed':
			return feed()

		elif action == 'drunk':
			return drunk()

		elif action == 'walk':
			return walk()

		elif action == 'wash':
			return bath()

	except KeyError:
		return ERROR_RESPONSE
