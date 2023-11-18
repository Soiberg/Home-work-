from functools import reduce

def find_max(x, y):
    return x if x > y else y

numbers = [59,34,64,468]

max_number = reduce(find_max, numbers)

print("Наибольший элемент", max_number)
