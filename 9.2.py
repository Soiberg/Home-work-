def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(n):
    primes = [num for num in range(2, n+1) if is_prime(num)]
    return primes

# Ввод числа n
n = int(input("Введите число"))

result_primes = find_primes(n)
print(f" числа от 1 до {n}: {result_primes}")
