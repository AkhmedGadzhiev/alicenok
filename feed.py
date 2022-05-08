# функция выводит основное меню
def feed():
	return {
	'response' : {
	'text' : 'Вот моё меню', 
	'tts' : 'Вот моё меню',
	'end_session' : 'false', 
	'card' : {
	'type' : 'BigImage',
	'image_id' : '937455/dc409d8246ba98c0713b'},
	'buttons' : [
	{'title' : 'Крекер',
	'payload' : {},
	'hide' : True},
	{'title' : 'Рыба',
	'payload' : {},
	'hide' : True},
	{'title' : 'Салат',
	'payload' : {},
	'hide' : True},
	{'title' : 'Острый перец',
	'payload' : {},
	'hide' : True},
	{'title' : 'Назад',
	'payload' : {'back' : 'feed_back'},
	'hide' : True}]},
	'version' : '1.0'}

# функция обрабатывает выбор еды
def feed_handler(event):
	intent = event['request']['nlu']['intents']['eat']
	eat = intent['slots']['eats']['value']

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

	dict =  {
	'response' : {
	'text' : None,
	'tts' : None,
	'end_session' : 'false',
	'card' : {
	'type' : 'BigImage',
	'image_id' : '937455/dc409d8246ba98c0713b'},
	'buttons' : [
	{'title' : 'Крекер',
	'payload' : {},
	'hide' : True},
	{'title' : 'Рыба',
	'payload' : {},
	'hide' : True},
	{'title' : 'Салат',
	'payload' : {},
	'hide' : True},
	{'title' : 'Острый перец',
	'payload' : {},
	'hide' : True},
	{'title' : 'Назад',
	'payload' : {'back' : 'feed_back'},
	'hide' : True}]},
	'version' : '1.0'}

	try:
		if eat == 'cracker':
			dict['response']['text'] = 'Ммм, вкусно. Давай ещё!'
			dict['response']['tts'] = 'Вкусно! Давай ещё!'
			return dict

		elif eat == 'fish':
			dict['response']['text'] = 'Ещё, ещё!'
			dict['response']['tts'] = 'Ещё, ещё!'
			return dict

		elif eat == 'salad':
			dict['response']['text'] = 'По-моему ты меня перекармливаешь'
			dict['response']['tts'] = 'По-моему ты меня перекармливаешь'
			return dict
			

		elif eat == 'pepper':
			dict['response']['text'] = 'Аааа! Почему так остро?'
			dict['response']['tts'] = 'А+а+а! Почему так остро?'
			return dict
	except KeyError:
		return ERROR_RESPONSE
