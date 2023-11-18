def find_max(lst):
    if not lst:
        return None


    current_max = lst[0]
    rest_max = find_max(lst[1:])


    if rest_max is not None and rest_max > current_max:
        return rest_max
    else:
        return current_max


# Пример использования
my_list = [61,26,53,31,75,76,45,91]
result = find_max(my_list)
print("число", result)
