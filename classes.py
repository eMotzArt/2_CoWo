class BasicWord:

    def __init__(self, word, subwords_list):
        self.word = word
        self.subwords_list = subwords_list

    def __repr__(self):
        return self.word

    # проверка на совпадение
    def is_match(self, word):
        if word in self.subwords_list:
            return True
        return False

    # возвращает количество "подслов"
    def subwords_count(self):
        return len(self.subwords_list)


class Player:

    # инициализируется по имени
    def __init__(self, name):
        self.name = name
        self.accepted_words = []

    def __repr__(self):
        return self.name

    # вернет количество угаданых слов
    def accepted_words_count(self):
        return len(self.accepted_words)

    # добавит угаданное слово в список угаданных слов
    def add_accepted_word(self, word):
        self.accepted_words.append(word)

    # вернет true если пользователь уже угадал это слово
    def is_already_use(self, word):
        if word in self.accepted_words:
            return True
        return False
