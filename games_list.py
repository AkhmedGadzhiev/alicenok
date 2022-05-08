# функция возвращает список мини-игр
def games_list():
	return {
	'response' : {
	'text' : 'Вот список мини-игр', 
	'tts' : 'Раздел в стадии разработки - кнопки неактивны', 
	'end_session' : 'false', 
	'card' : {
	'type' : 'BigImage', 
	'image_id' : '1521359/2e2d66f08a0f16ff8317'}, 
	'buttons' : [
	{'title' : 'Попугай', 
	'payload' : {}, 
	'hide' : 'true'}, 
	{'title' : 'Угадай животное', 
	'payload' : {}, 
	'hide' : 'true'}, 
	{'title' : 'Азбука', 
	'payload' : {}, 
	'hide' : 'true'}, 
	{'title' : 'Цифры', 
	'payload' : {'game_func' : 'numbers'}, 
	'hide' : 'true'},
	{'title' : 'Назад', 
	'payload' : {'back' : 'games_list_back'}, 
	'hide' : 'true'}]}, 
	'version' : '1.0'}