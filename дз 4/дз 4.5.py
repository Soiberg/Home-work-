input_string = input()
input_string = input()
count_x = 0
count_y = 0
for char in input_string:
    if char == 'x':
        count_x += 1
    elif char == 'y':
        count_y += 1
print(f'x: {count_x}, y: {count_y}')
