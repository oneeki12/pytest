import random
import math

v = "выбери Камень (k), ножницы (n), бумага (b)"
a = input(v)

s_comp = 0
s_pl = 0

print("Очки компьютера: 0 ")
print("Очки игрока: 0 ")

if v == "k":
    print("comp: b")
    print("Я выиграл")
    s_comp = s_comp + 1
    print("Я: " + s_comp + "Ты: " + s_pl)
if v == "n":
    print("comp: k")
    print("Я выиграл")
    s_comp = s_comp + 1
    print("Я: " + s_comp + "Ты: " + s_pl)
if v == "b":
    print("comp: n")
    print("Я выиграл")
    s_comp = s_comp + 1
    print("Я: " + s_comp + "Ты: " + s_pl)
else:
    print(0)
