numbers = input("Введите два числа, разделенных пробелом: ")

num1, num2 = map(int, numbers.split())

if num1 > num2:
    print(num1)
else:
    print(num2)