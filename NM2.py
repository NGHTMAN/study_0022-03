print('Введите строку:')
Users_str = input()
# len - длина строки
k = len(Users_str)

# range для выполнения цикла в заданном диапазоне
for i in range(0, k - 1):

    if Users_str[i] == 'c' or Users_str[i] == 'C':
        print('Был введён символ c или C!')
        continue

    if i == 2:
        continue

    else:
        print(Users_str[i])

exit(0)
