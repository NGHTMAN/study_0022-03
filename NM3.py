# Импорт встроенных математических функций
from math import factorial, acos
from random import randrange

# Просто красивое название
print('''

-    #Калькулятор 3000#    -

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
    
Чтобы прекратить использование калькулятора 3000, введите "done".
____________________________
''')


# Сложение
def plus(digit, digit2):
    print(float(digit + digit2))


# Вычитание
def minus(digit, digit2):
    print(float(digit - digit2))


# Умножение
def multiplication(digit, digit2):
    print(float(digit * digit2))


# Деление
def div(digit, digit2):
    print(float(digit / digit2))


# Возведение в степень
def exp(digit, digit2):
    print(float(digit ** digit2))


# Переменная для определения операции
Operation = input("Введите требуемую операцию: ")

# Цикл с условиями для выполнения необходимых операций (выход через "done")
while Operation != "done":

    # Сложение
    if Operation == "+":
        plus(float(input("Первое число: ")), float(input("Второе число: ")))

    # Вычитание
    elif Operation == "-":
        minus(float(input("Первое число: ")), float(input("Второе число: ")))

    # Умножение
    elif Operation == "*":
        multiplication(float(input("Первое число: ")), float(input("Второе число: ")))

    # Деление
    elif Operation == "/":
        div(float(input("Первое число: ")), float(input("Второе число: ")))

    # Возведение в степень
    elif Operation == "^":
        exp(float(input("Первое число: ")), float(input("Второе число: ")))

    # Модуль числа
    elif Operation == "abs":
        print(abs(float(input("Введите число: "))))

    # !roll 100 [команда в osu!, чтобы получить радомное число. Пасхалочка для себя самого ;)]
    elif Operation == "random":
        print(randrange(int(input("Введите верхнюю границу случайного числа: "))))

    # Факториал числа
    elif Operation == "factorial":
        print(factorial(float(input("Введите число: "))))

    # Арккосинус
    elif Operation == "acos":
        print(acos(float(input("Введите число от '-1' до '1': "))))

    Operation = input("Введите действие: ")
