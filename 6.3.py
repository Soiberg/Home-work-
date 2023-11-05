def find_maximum(a, b, c=None):
    if c is None:
        return max(a, b)
    return max(a, b, c)

result2 = find_maximum(20, 13, 9)

print("Максимум из чисел:", result2)
