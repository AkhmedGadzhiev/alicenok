# функция выводит список мест для прогулки
def walk():
	return {
	'response' : {
	'text' : 'Пошли гулять! Куда пойдём?',
	'tts' : 'Пошли гулять! Куда пойдём?', 
	'end_session' : 'false', 
	'card' : {
	'type' : 'BigImage',
	'image_id' : '937455/a6e48cbda4c8b165f016'},
	'buttons' : [
	{'title' : 'В парк',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'В сад',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'На улицу',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Назад',
	'payload' : {'back' : 'walk_back'},
	'hide' : 'true'}]},
	'version' : '1.0'}

# функция обрабатывает выбор места для прогулки
def walk_handler(event):
	intent = event['request']['nlu']['intents']['walk']
	place = intent['slots']['walk']['value']

	dict = {
	'response' : {
	'text' : None,
	'tts' : None, 
	'end_session' : 'false', 
	'card' : {
	'type' : 'BigImage',
	'image_id' : None},
	'buttons' : [
	{'title' : 'В парк',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'В сад',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'На улицу',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Домой',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Назад',
	'payload' : {'back' : 'walk_back'},
	'hide' : 'true'},]},
	'version' : '1.0'}

	if place == 'park':
		del dict['response']['buttons'][0]
		dict['response']['text'] = 'Как здесь красиво!'
		dict['response']['tts'] = 'Как здесь красиво!'
		dict['response']['card']['image_id'] = '1533899/1064c48a5d0fd36a946e'
		return dict


	elif place == 'garden':
		del dict['response']['buttons'][1]
		dict['response']['text'] = 'Какой же здесь всё-таки чистый воздух'
		dict['response']['tts'] = 'Какой же здесь всё-таки чистый воздух'
		dict['response']['card']['image_id'] = '1533899/3eab7c0af24b90d57a4b'
		return dict

	elif place == 'street':
		del dict['response']['buttons'][2]
		dict['response']['text'] = 'Опять плитку переложили'
		dict['response']['tts'] = 'Опять плитку переложили'
		dict['response']['card']['image_id'] = '1533899/787f214a838f26865241'
		return dict

	elif place == 'home':
		del dict['response']['buttons'][3]
		dict['response']['text'] = 'Вот мы и дома. Спасибо что погулял со мной'
		dict['response']['tts'] = 'Вот мы и дома. Спасибо что погулял со мной'
		dict['response']['card']['image_id'] = '937455/a6e48cbda4c8b165f016'
		return dict