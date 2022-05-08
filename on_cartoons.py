# функция выводит список мультиков
def on_cartoons():
	return {
	'response' : {
	'text' : 'Вот список моих мультиков',
	'tts' : 'Вот список моих мультиков',
	'end_session' : 'false',
	'card' : {
	'type' : 'ItemsList',
	'header' : {
	'text' : 'Вот список моих мультиков:'},
	'items' : [
	{'image_id' : '1540737/4704710b7c5bc2367d41',
	'title' : 'Синий трактор',
	'button' : {
	'text' : 'Синий трактор',
	'url' : 'https://www.youtube.com/watch?v=QD6H0W0HQG4',
	'payload' : {}}},
	{'image_id' : '937455/90e2a94ff33943d50466',
	'title' : 'Тиг и Лео',
	'button' : {
	'text':'Тиг и Лео',
	'url' : 'https://www.youtube.com/watch?v=hM8Z2lGy0wk',
	'payload' : {}}},
	{'image_id' : '1030494/7eccc1a32766ab1db4db',
	'title' : 'Фиксики',
	'button' : {
	'text' : 'Фиксики',
	'url' : 'https://www.youtube.com/watch?v=ZvBW4UKn6e8',
	'payload' : {}}},
	{'image_id' : '965417/38b464529d7168f72446',
	'title' : 'Ми-ми-мишки',
	'button' : {
	'text' : 'Ми-ми-мишки',
	'url' : 'https://www.youtube.com/watch?v=2DyONLKB0F8',
	'payload' : {}}},
	{'image_id' : '937455/0f658036f6273bc592d4',
	'title' : 'Назад',
	'button' : {
	'text' : 'Назад',
	'payload' : {'back' : 'on_cartoons_back'}}}]}},
	'version' : '1.0'}