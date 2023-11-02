# Введите текст с балансированными скобками
input_text = input("Введите текст с балансированными скобками: ")

# Инициализируйте переменные для поиска начальной и конечной скобок
start = input_text.find('(')
end = input_text.find(')')

# Пока найдены пары скобок, извлеките их содержимое и выведите
while start != -1 and end != -1:
    content = input_text[start + 1:end]
    print(content)

    # Удалите скобки и их содержимое из исходного текста
    input_text = input_text[:start] + input_text[end + 1:]

    # Поиск следующей пары скобок
    start = input_text.find('(')
    end = input_text.find(')')

