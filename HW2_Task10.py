# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть

from random import randint
num = int(input("Сколько монет бросаем на стол? "))
coins = []
for i in range(num):
    coins.append(randint(0,1))
    print(coins[i], end=" ")
if coins.count(1) >= coins.count(0):
    print(f" -> {coins.count(0)}")
else: print(f" -> {coins.count(1)}")