#программа для расчёта оценок
#Сделал Никита Коваль 05.04.2023 19:23
a = int(input("Введи количество вопросов\n>"))    #Количество вопросов к примеру: 24
b = int(input("Введи количество правильных ответов\n>")) #Количество правильных ответов к примеру: 13 из 24
ball = int(input("Какая у вас система оценивания вводите цифрой(5, 12)\n>")) #Какая система оценивания Пятибальная или Двенадцатибальная
c = int(((b/a)*100)) #формула для расчёта оценок в процентах к примеру: 6 из 12 это 50 процентов
if ball == 12: #Если система двенадцатибальная обрабатывается данный кусок кода
    if 100 >= c >= 92: #Если процент равен диапазону от 100 до 92, то выводится оценка которая была предварительно рассчитана на калькуляторе.
        print("Ваша оценка: 12") #Следующие условия делают тоже самое: Диапазон, оценка
    elif 92 >= c >= 84:
        print("Ваша оценка: 11")
    elif 84 >= c >= 79:
        print("Ваша оценка: 10")
    elif 79 >= c >= 67:
        print("Ваша оценка: 9")
    elif 67 >= c >= 62:
        print("Ваша оценка: 8")
    elif 62 >= c >= 58:
        print("Ваша оценка: 7")
    elif 58 >= c >= 46:
        print("Ваша оценка: 6")
    elif 46 >= c >= 41:
        print("Ваша оценка: 5")
    elif 41 >= c >= 33:
        print("Ваша оценка: 4")
    elif 33 >= c >= 25:
        print("Ваша оценка: 3")
    elif 25 >= c >= 16:
        print("Ваша оценка: 2")
    elif c < 16:
        print("Ваша оценка: 1")
elif ball == 5: #Если пятибальная система, то производится всё тоже самое: Диапазон, оценка
    if 100 >= c >= 84:
        print("Ваша оценка: 5")
    elif 84 >= c >= 67:
        print("Ваша оценка: 4")
    elif 67 >= c >= 50:
        print("Ваша оценка: 3")
    elif 50 >= c >= 0:
        print("Ваша оценка: 2")
pl = input()