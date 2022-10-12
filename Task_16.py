# 16. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример для n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}

n = int(input('Введите количество чисел n: '))
dictionary = {}
sum = 0

if n > 0:
    for i in range(1, n + 1):
        dictionary[i] = round(((1 + 1 / i) ** i), 2)
        sum = sum + dictionary[i]
    print(dictionary)
    print('Сумма чисел =', round((sum), 2))

else:
    print('Ошибка! Введите число > 0.')