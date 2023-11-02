num_str = input("Введите число: ")
sum_of_digits = 0
for digit in num_str:
    if digit.isdigit():
        sum_of_digits += int(digit)
print("Сумма цифр числа:", sum_of_digits)
