import json
import random
import os, sys


class Play:

    def __init__(self, word):
        self.word = [elem for elem in word] # преобразуем в список
        self.guessing = ["?" for elem in word] # заполняем на вывод
        self.count_answer = 5
        self.list_symbols = []

    def print_table(self): # выводим в табличном виде слово
        os.system('cls') # очищаем консоль
        print(f"Осталось попыток: {self.count_answer}")
        print(f"Введенные значения: {self.list_symbols}")
        print("+---" * len(self.guessing) + "+")
        s = "|"
        for elem in self.guessing:
            s += f" {elem} |"
        print(s, "+---" * len(self.guessing) + "+", sep="\n")

    def input_symbol(self): # вводим символ
        answer = input("Введите значение: ") 
        self.list_symbols.append(answer) 

    def check_input(self): # проверяет введенное значение
        value = False
        if self.list_symbols[-1] in self.word: # если введенный символ есть в слове
            for i in range(len(self.guessing)):
                if self.word[i] == self.list_symbols[-1]: 
                    self.guessing[i] = self.list_symbols[-1]
                    value = True
        
        if value == False:
            self.count_answer -= 1

    def start_play(self):
        self.print_table() # вывод в консоль таблицы со словом
        if "?" not in self.guessing:
            print("Победа. Вы угадали слово!")
            return None
        self.input_symbol()
        self.check_input()
        if self.count_answer != 0:
            return self.start_play()
        else:
            print("Попытки закончились. Вы проиграли!")

def open_json(filename): # функция для чтения json-файла
    with open(filename, encoding='utf-8') as f:
        return json.load(f) 

def main():
    words = open_json("words.json") # считываем список слов
    while True:
        word = random.sample(words["list_words"], 1) # получаем случайный элемент из списка
        play = Play(word[0])
        play.start_play()

        if input("Продолжим играть? (любой ввод/n)\nввод: ") == "n":
            sys.exit() # выход из программы

if __name__ == "__main__":
    main()