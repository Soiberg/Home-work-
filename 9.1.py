def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

a = int(input("первое число "))
b = int(input("второе число: "))

result_lcm = lcm(a, b)
print(f"Наименьшее общее кратное чисел {a} и {b}: {result_lcm}")
