# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

origamies = int(input("Сколько журавликов всего собрали ребята? "))
if origamies%6 != 0: print("С таким кол-вом задача не решается!")
else:
    petros = int(origamies/6)
    sergios = petros
    kates = 2*(petros + sergios)
    print(f"Из {origamies} журавликов Петя собрал {petros}, Катя - {kates}, Сережа - {sergios}")