# Наша функция
def create_dict():

    # Первый список слов
    first_words = input("Введи первый список слов через запятую: ")

    # split - разбиение строки на части
    # В нашем случае разделитель - запятая
    first_list = first_words.split(',')

    # Вывод количества слов с помощью поиска пробелов + 1, так как в конце строки пробел не ставится
    word_count = first_words.count(" ") + 1
    print("Вы ввели количество слов в первом списке:", word_count)

    # Благодаря F-strings подставляем в {} необходимые нам переменные
    second_words = input(f"Введи второй список из {word_count} слов через запятую: ")
    second_list = second_words.split(',')

    # dict - словарь (ключ: значение); zip - "цикл" прохождения по массиву из слов
    final_dict = dict(zip(first_list, second_list))
    print(final_dict)

    # Конструкция для открытия и закрытия файла
    # 'w' - открытие на запись, содержимое файла удаляется; если файла не существует, то создается новый
    # key - ключи словаря, val - значения словаря
    # write - запись в файл
    with open('secret.txt', 'w', encoding='utf-8') as f:
        for key, val in final_dict.items():
            f.write(f'{key}:{val}\n')
    return 0


# Просто красивое название
print("\n\n<-------------------------------| Добро пожаловать в программу-словарик! |------------------------------->")
print("\n\n")
print("Введи 1, чтобы создать словарь\nВведи 0, чтобы завершить работу\n")

operation = input("Answer: ")
while operation != "0":
    # Вызов функции
    create_dict()
    print("\n\n")
    print("Введи 1, чтобы создать словарь\nВведи 0, чтобы завершить работу\n")

    operation = input("Answer: ")