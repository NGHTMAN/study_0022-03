# Импорт встроенных математических функций
from math import factorial, acos
from random import randrange
import os


class Calculator3100:

    # Сложение
    @staticmethod
    def plus(digit, digit2):
        print(float(digit + digit2))

    # Вычитание
    @staticmethod
    def minus(digit, digit2):
        print(float(digit - digit2))

    # Умножение
    @staticmethod
    def multiplication(digit, digit2):
        print(float(digit * digit2))

    # Деление
    @staticmethod
    def div(digit, digit2):
        print(float(digit / digit2))

    # Возведение в степень
    @staticmethod
    def exp(digit, digit2):
        print(float(digit ** digit2))

    # Цикл с условиями для выполнения необходимых операций (выход через "done")
    def do_math(self, operation):
        while operation != "done":

            # Сложение
            if operation == "+":
                self.plus(float(input("Первое число: ")), float(input("Второе число: ")))

            # Вычитание
            elif operation == "-":
                self.minus(float(input("Первое число: ")), float(input("Второе число: ")))

            # Умножение
            elif operation == "*":
                self.multiplication(float(input("Первое число: ")), float(input("Второе число: ")))

            # Деление
            elif operation == "/":
                self.div(float(input("Первое число: ")), float(input("Второе число: ")))

            # Возведение в степень
            elif operation == "^":
                self.exp(float(input("Первое число: ")), float(input("Второе число: ")))

            # Модуль числа
            elif operation == "abs":
                print(abs(float(input("Введите число: "))))

            # !roll 100 [команда в osu!, чтобы получить радомное число. Пасхалочка для себя самого ;)]
            elif operation == "random":
                print(randrange(int(input("Введите верхнюю границу случайного числа: "))))

            # Факториал числа
            elif operation == "factorial":
                print(factorial(float(input("Введите число: "))))

            # Арккосинус
            elif operation == "acos":
                print(acos(float(input("Введите число от '-1' до '1': "))))

            operation = input("Введите требуемую операцию: ")


run_3100 = Calculator3100()

input("Press enter to continue...")
os.system('cls')

# Просто красивое название
print('''

-    #Калькулятор 3100#    -

____________________________  
Список доступных операций:

    "+" - сложение
    "-" - вычитание
    "*" - умножение
    "/" - деление
    "^" - возведение в степень
    "abs" - модуль числа
    "random" - случайное число
    "factorial" - факториал числа
    "acos" - арккосинус

Чтобы прекратить использование калькулятора 3100, введите "done".
____________________________
''')

do = input("Введите действие: ")
run_3100.do_math(do)
