# import
from main_skills import *
from entertainments_skills import *
from on_cartoons import *
from games_list import *
from alicenok import *


# функция отправляет назад
def back(event):
	payload = event['request']['payload']['back']

	if payload == 'alicenok_help_back':
		return main_skills()

	elif payload == 'entertainments_back':
		return main_skills()

	elif payload == 'on_cartoons_back':
		return entertainments_skills(event)

	elif payload == 'games_list_back':
		return main_skills()

	elif payload == 'alicenok_wellcome_message_back':
		return main_skills()

	elif payload == 'testers_back':
		return main_skills()

	elif payload == 'song_back':
		return entertainments_skills(event)

	elif payload == 'fallback_back':
		return main_skills()

	elif payload == 'alicenok_back':
		return main_skills()

	elif payload == 'feed_back':
		return alicenok()

	elif payload == 'drunk_back':
		return alicenok()

	elif payload == 'walk_back':
		return alicenok()

	elif payload == 'bathroom_back':
		return alicenok()

	elif payload == 'games_back':
		return games_list()