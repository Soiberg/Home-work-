number = float(input("Введите число: "))
n = int(input("Введите количество знаков после запятой: "))
rounded_number = round(number, n)
print(f"Результат округления: {rounded_number}")