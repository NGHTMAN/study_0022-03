# Наша функция
def vegetables():

    # Просто красивое название
    print("\n#--------<|Добро пожаловать в магазинчик Тамако!|>--------#\n")

    # Введение названия овощей
    veg1 = input("Введите название первого овоща: ")
    veg2 = input("Введите название второго овоща: ")
    veg3 = input("Введите название третьего овоща: ")

    # Перенос строки
    print("\n")

    # Функции перевода в нижний регистр, верхний регистр, стиль заголовка
    print(veg1.lower(), veg2.lower(), veg3.lower())
    print(veg1.upper(), veg2.upper(), veg3.upper())
    print(veg1.title(), veg2.title(), veg3.title())

    print("\n")

    # Количество овощей
    сount_veg1 = input("Сколько овощей '" + veg1 + "' вы хотите? ")
    сount_veg2 = input("Сколько овощей '" + veg2 + "' вы хотите? ")
    сount_veg3 = input("Сколько овощей '" + veg3 + "' вы хотите? ")

    print("\nОтлично! Что ж, держите:\n")

    # Все овощи с их количеством в "format" режиме
    print(veg1.title() + " в количестве {} шт.".format(сount_veg1))
    print(veg2.title() + " в количестве {} шт.".format(сount_veg2))
    print(veg3.title() + " в количестве {} шт.".format(сount_veg3))
    return 0


# Вызов функции
vegetables()
