import random
print("Введите число, на которое вы хотите сделать ставку от 1 до 9")
s = int(input())
a = random.randint(1, 9)
b = random.randint(1, 9)
c = random.randint(1, 9)
if s == a and s == b:
    print("ВЫ ВЫИГРАЛИ")
else:
    if s == a and s == c:
        print("ВЫ ВЫИГРАЛИ")
    else:
        if s == b and s == c:
            print("ВЫ ВЫИГРАЛИ")
        else:
            print("ПРОИГРАЛ")
print(a)
print(b)
print(c)