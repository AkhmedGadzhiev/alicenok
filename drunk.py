# функция выводит меню с напитками
def drunk():
	return {
	'response' : {
	'text' : 'Вот меню напитков', 
	'tts' : 'Вот меню напитков', 
	'end_session' : 'false',
	'card' : {
	'type' : 'BigImage',
	'image_id' : '937455/dc409d8246ba98c0713b'},
	'buttons' : [
	{'title' : 'Апельсиновый фреш',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Молоко',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Вода',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Смузи',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Назад',
	'payload' : {'back' : 'drunk_back'},
	'hide' : 'true'}]},
	'version' : '1.0'}

# функция обрабатывает выбор напитка
def drink_handler(event):
	intent = event['request']['nlu']['intents']['drink']
	drink = intent['slots']['drinks']['value']

	dict = {
	'response' : {
	'text' : None,
	'tts' : None,
	'end_session' : 'false',
	'card' : {
	'type' : 'BigImage',
	'image_id' : '937455/dc409d8246ba98c0713b'},
	'buttons' : [
	{'title' : 'Апельсиновый фреш',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Молоко',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Вода',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Смузи',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Назад',
	'payload' : {'back' : 'drunk_back'},
	'hide' : 'true'}]},
	'version' : '1.0'}

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
		

