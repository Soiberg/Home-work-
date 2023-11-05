
def is_palindrome(s):
    # Удаляем пробелы и приводим строку к нижнему регистру
    s = s.replace(" ", "").lower()
    # Сравниваем строку с её обратной версией
    return s == s[::-1]
input_string = "Шалак"
result = is_palindrome(input_string)
print(result)