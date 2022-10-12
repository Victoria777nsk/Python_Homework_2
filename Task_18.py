# 18. *Реализуйте алгоритм перемешивания списка.

n = int(input('Введите количество элементов: '))
numbers = []
for i in range(n):
    from random import randint      # Импортируем модуль random, чтобы использовать метод randint
    numbers.append(randint(0, 9))   # Возвращаем случайное целое число от 0 до 9 и добавл. его в конец списка
print(numbers)

list = numbers[:]                   # Копируем последовательность с помощью среза [:]
numbers_length = len(list)

for i in range(numbers_length):
    index = randint(0, numbers_length - 1)  # Берем элемент списка со случайным индексом
    temp = list[i]                          # Вводим переменную temp для временного хранения элемента списка
    list[i] = list[index]
    list[index] = temp
print(list)