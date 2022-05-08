# функция выводит список банных пренадлежностей
def bath():
	return {
	'response' : {
	'text' : 'Ура! Люблю мыться',
	'tts' : 'Ура! Люблю мыться',
	'end_session' : 'false', 
	'card' : {
	'type' : 'BigImage',
	'image_id' : '937455/a689089e088a10118d39'},
	'buttons' : [
	{'title' : 'Шампунь',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Гель для душа',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Бальзам для шёрстки',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Смыть',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Назад',
	'payload' : {'back' : 'bathroom_back'},
	'hide' : 'true'}]},
	'version' : '1.0'}

# функция обрабатывает выбор банных пренадлежностей
def bath_handler(event):
	intent = event['request']['nlu']['intents']['bath']
	bath = intent['slots']['bath']['value']

	dict = {
	'response' : {
	'text' : None, 
	'tts' : None,
	'end_session' : 'false',
	'card' : {
	'type' : 'BigImage',
	'image_id' : '937455/a689089e088a10118d39'},
	'buttons' : [
	{'title' : 'Шампунь',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Гель для душа',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Бальзам для шёрстки',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Смыть',
	'payload' : {},
	'hide' : 'true'},
	{'title' : 'Назад',
	'payload' : {'back' : 'bathroom_back'},
	'hide' : 'true'}]},
	'version' : '1.0'}

	if bath == 'shampoo':
		dict['response']['text'] = 'Буль, буль'
		dict['response']['tts'] = 'Буль, буль'
		return dict

	elif bath == 'gel':
		dict['response']['text'] = 'Холодненький какой'
		dict['response']['tts'] = 'Холодненький какой'
		return dict

	elif bath == 'balm':
		dict['response']['text'] = 'Намыливай хорошенько'
		dict['response']['tts'] = 'Намыливай хорошенько'
		return dict

	elif bath == 'wash_off':
		dict['response']['text'] = 'Ой хорошо'
		dict['response']['tts'] = 'Ой хорошо'
		return dict