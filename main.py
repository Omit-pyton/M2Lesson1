import random

all_words = ["пермутирование", "гидроавиация", "дифторпропан", "микрокалория", "дезсредство", "газопоглощение",
             "полузакрытость", "упадочничество", "предосенье", "эксповилка", "опытность", "тонкопряд",
             "филантроп", "замполит", "морны", "сеноуборка", ]
word_id = int(random.randint(0, len(all_words) - 1))
word = all_words[word_id]
word_exp = ['*'] * len(word)

play = input("Со скольки попыток вы угадаете слово " + "".join(word_exp) + ": ")
play = int(play)
k = 0

while k < play or word_exp != word:
    letter = input("Назовите вашу букву: ")
    letter = letter.lower()
    for num in range(len(word)):
        if word[num] == letter:
            word_exp[num] = letter
    s = "".join(word_exp)
    print("".join(word_exp))
    if s == word:
        print("Поздравляю! Вы угадали слово!")
        break
    k += 1
