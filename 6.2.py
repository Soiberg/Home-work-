def registr_1(name, last_name,patronymic,age):
    return (name , last_name , patronymic , age , 'зарегистрирован')
name =(input())
last_name =(input())
patronymic =(input())
age =int(input())
reg = registr_1(name, last_name,patronymic,age)
print(reg)

