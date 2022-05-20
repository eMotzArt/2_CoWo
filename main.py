from classes import Player
from functions import get_random_word


def main():
    user_name = input('Добро пожаловать, игрок. Представься.\n')
    player = Player(user_name)

    print(f"Привет, {player}")

    word = get_random_word()
    print(f'Составьте {word.subwords_count()} слов из слова "{word}"\n'
          f"Слова должны быть не короче {len(min(word.subwords_list, key=lambda word_: len(word_)))} букв\n"
          f"Вы всегда можете ввести stop для завершения игры\n"
          f"Поехали. Ваше первое слово?")

    for try_ in range(word.subwords_count()):
        user_word = input().strip().lower()

        if user_word == 'stop':
            print("Вы остановили игру")
            break

        #не стал делать if в if'e, воспользовался continue
        if not word.is_match(user_word):
            print("Неверно")
            continue

        #знаю, что использую инверсию условий, много not (
        if not player.is_already_use(user_word):
            player.add_accepted_word(user_word)
            print("Верно, такой вариант есть")
        else:
            print("Слово верное, но Вы уже называли его")


    print(f"Игра завершена.\n"
          f"Количество угаданых слов: {player.accepted_words_count()}")


if __name__ == '__main__':
    main()
