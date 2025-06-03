import random
import time
txt = "Приветсвуем Вас в нашей игре - Рулетка! Правила игры - С помощью рулетки мы выберем 3 случайных цифры.Вам будет предложен выбор цифры и режима.Если цифра совпадет с выбранными с помощью рулетки цифрами, то приз ваш"
for i in txt:
    time.sleep(0.011)
    print(i, end="", flush=True)
d = 100000
while d > 0:
    print()
    print()
    time.sleep(2)
    print("Выберите режим рулетки")
    print("1-Обычный(Для выигрыша нужно совпадение хотя бы одного числа.Коэффицент - х5)")
    time.sleep(1)
    print("2-Азартный(Для выигрыша нужно совпадение хотя бы двух чисел.Коэффицент - х50)")
    time.sleep(1)
    print("3-Супер азартный(Для выигрыша нужно совпадение трех чисел.Коэффицент - х500)")
    r = int(input())
    if r == 2:
        print("Ваш выбор - Азартный")
    if r == 1:
        print("Ваш выбор - Обычный")
    if r == 3:
        print("Ваш выбор - Супер азартный")
    time.sleep(1)
    print("Ваш баланс" ,d)
    print("Введите сумму ставки")
    p = int(input())
    if p > d:
        print("Вы не можете поставить сумму, которая превышает ваш баланс, повторите попытку")
        p = int(input())
    if p > d:
        print("Вы не можете поставить сумму, которая превышает ваш баланс, повторите попытку")
        p = int(input())
    if p > d:
        print("Вы не можете поставить сумму, которая превышает ваш баланс, повторите попытку")
        p = int(input())
    d = d - p
    print("Введите цифру, на которое вы хотите сделать ставку от 1 до 9")
    s = int(input())
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    if r == 1:
        time.sleep(1)
        print("Раскручиваем посильнее...Подождите")
        time.sleep(1)
        print(a)
        time.sleep(2)
        print(b)
        time.sleep(2)
        print(c)
        time.sleep(2)
        if s == a or s == b or s == c:
            d = d + p * 5
            print("Поздравляем!Выигрыш")
        else:
            print("Cожалаеем, это поражение")
    if r == 2:
        time.sleep(1)
        print("Раскручиваем посильнее...Подождите")
        time.sleep(2)
        print(a)
        time.sleep(2)
        print(b)
        time.sleep(2)
        print(c)
        if s == a and s == b:
            print("Поздравляем!Выигрыш")
            d = d + p*50
            time.sleep(2)
    else:
        if s == a and s == c:
            print("Поздравляем!Выигрыш")
            d = d + p * 50
            time.sleep(2)
    if s == b and s == c:
        print("Поздравляем!Выигрыш")
        d = d + p*50
        time.sleep(2)
    if r == 3:
        print("Раскручиваем посильнее...Подождите")
        time.sleep(1)
        print(a)
        time.sleep(2)
        print(b)
        time.sleep(2)
        print(c)
        time.sleep(2)
        if s == a and s == b and s == c:
            print("Поздраляем!Выигрыш")
            d = d + p * 500
        else:
            print("Cожалаеем, это поражение")
            time.sleep(2)
    if d <= 0:
        print("Спасибо за игру!Ваш баланс - 0")
        time.sleep(2)

