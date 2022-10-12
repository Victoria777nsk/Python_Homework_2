# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на введенных пользователем позициях.

n = int(input('Введите количество элементов: '))
numbers = []
for i in range(n):
    from random import randint      # Импортируем модуль random, чтобы использовать метод randint
    numbers.append(randint(-n,n))   # Возвращаем случайное целочисл. значение между нижним и верхним пределами
print(numbers)

x = int(input('Введите позицию первого элемента умножения: '))
y = int(input('Введите позицию второго элемента умножения: '))

for i in range(len(numbers)):
    mult = numbers[x - 1] * numbers[y - 1]

print(f'{numbers[x - 1]} * {numbers[y - 1]} = {mult}')