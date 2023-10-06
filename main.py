n = float(input("Введите число 1: "))
y = float(input("Введите число 2: "))
print("Сколько знаков после запятой вы хотите оставить?")
count = int(input())
s = (n + y) / 2
number = round(s, count)
print(number)