def find_divisors(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors

n = int(input("Введите число"))

# Находим все делители числа n и выводим результат
result_divisors = find_divisors(n)
print(f"Делители {n}: {result_divisors}")
