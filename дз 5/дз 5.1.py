
n = int(input())
city_count = {}
for _ in range(n):
    city = input()
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

duplicate_count = 0


for city, count in city_count.items():
    if count > 1:
        duplicate_count += 1


print( duplicate_count)


