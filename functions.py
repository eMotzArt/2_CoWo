import requests
import json
from random import choice
from classes import BasicWord


def get_random_word() -> BasicWord:
    link = "https://jsonkeeper.com/b/CF86"

    response = requests.get(link).text
    response_to_json = json.loads(response)
    random_word = choice(response_to_json)

    word = BasicWord(random_word['word'], random_word['subwords'])

    return word
