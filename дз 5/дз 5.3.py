str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

set1 = set(str1)
set2 = set(str2)

if set1 == set2:
    print("Эти строки являются анаграммами.")
else:
    print("Эти строки не являются анаграммами.")


