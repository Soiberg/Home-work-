numbers = input("Введите список чисел через пробел: ").split()
n = int(input("Введите степень: "))
numbers = [int(num) for num in numbers]
result = [num ** n for num in numbers]
print(result)
