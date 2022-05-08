# функция выводит список разделов для получения информации о них
def alicenok_help():
	return {
	'response' : {
	'text' : 'Список разделов',
	'end_session' : 'false',	
	'card' : {
	'type' : 'ItemsList',
	'header' : {
	'text' : 'Список разделов'},
	'items' : [
	{'image_id' : '1030494/1419ffbf1834325866ac',
	'title' : 'Разработчики',
	'button' : {
	'text' : 'Разработчики',
	'url' : 'https://lowly-sprite-a0a.notion.site/INFO-Developers-29bf4f77f6b840b2b015ca16675888da',
	'payload' : {'info' : 'info_developers'}}},
	{'image_id' : '1030494/1419ffbf1834325866ac',
	'title' : 'Развлечения',
	'button' : {
	'text':'Развлечения',
	'payload' : {'info' : 'info_entertainments'}}},
	{'image_id' : '1030494/1419ffbf1834325866ac',
	'title' : 'Мини-игры',
	'button' : {
	'text' : 'Мини-игры',
	'payload' : {'info' : 'info_games'}}},
	{'image_id' : '1030494/1419ffbf1834325866ac',
	'title' : 'Алисёнок',
	'button' : {
	'text' : 'Алисёнок',
	'payload' : {'info' : 'info_alicenok'}}},
	{'image_id' : '937455/0f658036f6273bc592d4',
	'title' : 'Назад',
	'button' : {
	'text' : 'Назад',
	'payload' : {'back' : 'alicenok_help_back'}}}]}},
	'version' : '1.0'}

# функция обрабатывает выбор раздела, и предоставляет информацию о нём
def alicenok_help_handler(event):
	payload = event['request']['payload']['info']

	if payload == 'info_developers':
		return {
		'response' : 
		{'text' : 'Вы были перенаправлены на страницу Notion',
		'end_session' : 'false'}, 
		'version' : '1.0'}

	elif payload == 'info_entertainments':
		return {
		'response' : 
		{'text' : 'Раздел "Развлечения" предоставляет всякого рода медиаконтент, например: мультики, сказки, песенки',
		'tts' : 'Раздел "Развлечения" предоставляет всякого рода медиаконтент, например: мультики, сказки, песенки',
		'end_session' : 'false'},
		'version' : '1.0'}

	elif payload == 'info_games':
		return {
		'response' : 
		{'text' : 'Раздел "Мини-игры" позволяет обучаться в игровой форме. Раздел находится в стадии разработки'}, 
		'version' : '1.0'}

	elif payload == 'info_alicenok':
		return {
		'response' : 
		{'text' : 'Раздел "Алисёнок" представляет из себя виртуального питомца, которого можно покормить, напоить, выгулять, помыть',
		'end_session' : 'false'},
		'version' : '1.0'}