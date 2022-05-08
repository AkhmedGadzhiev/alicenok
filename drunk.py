# функция выводит меню с напитками
def drunk():
	return {
	'response' : {
	'text' : 'Вот меню напитков', 
	'tts' : 'Вот меню напитков', 
	'end_session' : False,
	'card' : {
	'type' : 'BigImage',
	'image_id' : '937455/dc409d8246ba98c0713b'},
	'buttons' : [
	{'title' : 'Апельсиновый фреш',
	'payload' : {},
	'hide' : True},
	{'title' : 'Молоко',
	'payload' : {},
	'hide' : True},
	{'title' : 'Вода',
	'payload' : {},
	'hide' : True},
	{'title' : 'Смузи',
	'payload' : {},
	'hide' : True},
	{'title' : 'Назад',
	'payload' : {'back' : 'drunk_back'},
	'hide' : True}]},
	'version' : '1.0'}

# функция обрабатывает выбор напитка
def drink_handler(event):
	intent = event['request']['nlu']['intents']['drink']
	drink = intent['slots']['drinks']['value']

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

	dict = {
	'response' : {
	'text' : None,
	'tts' : None,
	'end_session' : False,
	'card' : {
	'type' : 'BigImage',
	'image_id' : '937455/dc409d8246ba98c0713b'},
	'buttons' : [
	{'title' : 'Апельсиновый фреш',
	'payload' : {},
	'hide' : True},
	{'title' : 'Молоко',
	'payload' : {},
	'hide' : True},
	{'title' : 'Вода',
	'payload' : {},
	'hide' : True},
	{'title' : 'Смузи',
	'payload' : {},
	'hide' : True},
	{'title' : 'Назад',
	'payload' : {'back' : 'drunk_back'},
	'hide' : True}]},
	'version' : '1.0'}

	try:
		if drink == 'fresh':
			dict['response']['text'] = 'Ммм, вкусно. Давай ещё!'
			dict['response']['tts'] = 'Вкусно! Давай ещё!'
			return dict
			

		elif drink == 'water':
			dict['response']['text'] = 'Вода - это источник жизни'
			dict['response']['tts'] = 'Вода - это источник жизни'
			return dict
			

		elif drink == 'milk':
			dict['response']['text'] = 'Люблю молоко!'
			dict['response']['tts'] = 'Люблю молоко!'
			return dict
			

		elif drink == 'smoothies':
			dict['response']['text'] = 'Фуу! Какая-то жижа'
			dict['response']['tts'] = 'Фуу! Какая-то жижа'
			return dict

	except KeyError:
		return ERROR_RESPONSE
