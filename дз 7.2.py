numbers = [13,24,38]

result = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))

print(result)
