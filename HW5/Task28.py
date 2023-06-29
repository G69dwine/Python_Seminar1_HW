'''
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
2 2 -> 4
'''

a = int(input("Число a: "))
b = int(input("Число b: "))

def simpleSum(num1, num2):
    if num2 == 0: 
        return num1
    return 1+simpleSum(num1, num2-1)

print(f"{a} + {b} = {simpleSum(a,b)}")