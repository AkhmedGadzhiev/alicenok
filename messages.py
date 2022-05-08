# функция принимает и возвращает текст
def make_response(text):
	return {
	'response' : {
	'text' : text, 
	'tts' : text,
	'end_session' : False},
	'version' : '1.0'}


def make_response_error(text):
	return {
	'response' : {
	'text' : text, 
	'tts' : text,
	'end_session' : False,
	'buttons' : [
	{'title' : 'Назад',
	'hide' : True,
	'payload' : {'back' : 'games_back'}}]}, 
	'version' : '1.0'}

# функция выводит вводное сообщение
def wellcome_me_message():
	return {
	'response' : {
	'text' : 'Привет малыш! Я Алисёнок. Теперь я твой проводник в безграничном мире знаний. Чтобы узнать что я умею, спроси: "Что ты умеешь?"',
	'tts' : 'Привет малыш! Я Алисёнок. Теперь я твой проводник в безграничном мире знаний. Чтобы узнать что я умею, спроси: "Что ты умеешь?"',
	'end_session' : False,
	'buttons' : [
	{'title' : 'Что ты умеешь',
	'hide' : True,
	'payload' : {}}]},
	'user_state_update' : {
	'wellome_message' : 'was'},
	'version' : '1.0'}
	

# функция выводит приветственное сообщение
def hi_message(event):
	return {
	'response' : {
	'text' : 'Привет малыш! Ну что продолжим?',
	'tts' : 'Привет малыш! Ну что продолжим?',
	'end_session' : False,
	'buttons' : [
	{'title' : 'Да',
	'hide' : True,
	'payload' : {}}]},
	'version' : '1.0'}



# функция обрабатывает исключения
def fallback(event):
	return {
	'response' : {
	'text' : 'Малыш, повтори пожалуйста ещё раз',
	'tts' : 'Малыш, повтори пожалуйста ещё раз',
	'end_session' : False,  
	'card' : {
	'type' : 'BigImage',
	'image_id' : '1652229/5a40ea676c1c9795c917'},
	'buttons' : [
	{'title' : 'Назад',
	'payload' : {'back' : 'fallback_back'},
	'hide' : True}]},
	'version' : '1.0'}
