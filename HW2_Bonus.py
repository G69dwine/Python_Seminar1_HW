'''
Даны положительные числа A, B, C. На прямоугольнике размера A x B размещено максимально возможное количество квадратов со стороной C (без наложений).
Найти количество квадратов, размещенных на прямоугольнике. Операции умножения и деления не использовать.
'''

# width = int(input("Длина прямоугольника: "))
# height = int(input("Ширина прямоугольника: "))
# square = int(input("Величина стороны квадрата: "))
# count = 0
# for i in range(1, width, square):
#     for i in range(1, height, square):
#         count += 1
# print(count)

'''
Спортсмен-лыжник начал тренировки, пробежав в первый день 10 км. 
Каждый следующий день он увеличивал длину пробега на P процентов от пробега предыдущего дня (P — вещественное, 0 < P < 50).
По данному P определить, после какого дня суммарный пробег лыжника за все дни превысит 200 км, 
и вывести найденное количество дней K (целое) и суммарный пробег S (вещественное число).
'''
# firstDistance = 10
# procent = int(input("Процент от пробега: "))/100
# i = firstDistance
# count = 1
# while i <= 200:
#     i += i*procent
#     count += 1
# print(f"{i} км за {count} дней")


'''
5. Сумма дробей (часть первая)
Пользователь вводит число N. Найдите сумму чисел: 1 + 1.1 + 1.2 + 1.3 + ... + (1 + N / 10).
'''
# num = int(input("Введите число: "))
# sum = 0
# for i in range(num + 1):
#     sum += 1+i/10
# print(sum)

'''
6. Сумма дробей (часть вторая)
Пользователь вводит число N. Найдите сумму чисел: 1 + 1/2 + 1/3 + ... + 1/N
'''
# num = int(input("Введите число: "))
# sum = 0
# for i in range(1, num + 1):
#     sum += 1/i
# print(round(sum,2))

