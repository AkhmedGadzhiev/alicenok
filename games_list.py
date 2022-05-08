# функция возвращает список мини-игр
def games_list():
	return {
	'response' : {
	'text' : 'Вот список мини-игр', 
	'tts' : 'Раздел в стадии разработки - кнопки неактивны', 
	'end_session' : False, 
	'card' : {
	'type' : 'BigImage', 
	'image_id' : '1521359/2e2d66f08a0f16ff8317'}, 
	'buttons' : [
	{'title' : 'Попугай', 
	'payload' : {}, 
	'hide' : True}, 
	{'title' : 'Угадай животное', 
	'payload' : {}, 
	'hide' : True}, 
	{'title' : 'Азбука', 
	'payload' : {}, 
	'hide' : True}, 
	{'title' : 'Цифры', 
	'payload' : {'game_func' : 'numbers'}, 
	'hide' : True},
	{'title' : 'Назад', 
	'payload' : {'back' : 'games_list_back'}, 
	'hide' : True}]}, 
	'version' : '1.0'}
