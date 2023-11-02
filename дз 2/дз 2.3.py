coordinates = input("Введите координаты клетки (два числа, разделенных пробелом): ")
x, y = map(int, coordinates.split())
if (x + y) % 2 == 0:
    print("YES")
else:
    print("NO")
