class BasicWord:

    def __init__(self, word: str, subwords_list: list):
        self.word = word
        self.subwords_list = subwords_list

    def __repr__(self) -> str:
        return self.word

    # проверка на совпадение
    def is_match(self, word: str) -> bool:
        if word in self.subwords_list:
            return True
        return False

    # возвращает количество "подслов"
    def subwords_count(self) -> int:
        return len(self.subwords_list)


class Player:

    # инициализируется по имени
    def __init__(self, name: str):
        self.name = name
        self.accepted_words = []

    def __repr__(self) -> str:
        return self.name

    # вернет количество угаданых слов
    def accepted_words_count(self) -> int:
        return len(self.accepted_words)

    # добавит угаданное слово в список угаданных слов
    def add_accepted_word(self, word: str):
        self.accepted_words.append(word)

    # вернет true если пользователь уже угадал это слово
    def is_already_use(self, word: str) -> bool:
        if word in self.accepted_words:
            return True
        return False
