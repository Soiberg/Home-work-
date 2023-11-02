
algebra_students = input("алгебре ").split()
geometry_students = input("геометрии").split()

trigonometry_students = input("тригонометрии").split()
algebra_set = set(algebra_students)
geometry_set = set(geometry_students)
trigonometry_set = set(trigonometry_students)
common_students = algebra_set & geometry_set & trigonometry_set

if common_students:
    common_students = sorted(common_students)
    print(" ".join(common_students))
else:
    print("Все три задачи никто не решил")

