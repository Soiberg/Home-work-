row = int(input("Введите номер строки (1-8): "))
column = int(input("Введите номер столбца (1-8): "))

# Проверка на цвет клетки
if (row + column) % 2 == 0:
    print("NO")  # Черная клетка
else:
    print("YES")