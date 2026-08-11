def add_student(name, students=None):
    if students is None:
        students = []
    students.append(name)
    print(students)

first_name = input()
second_name = input()
third_name = input()

add_student(first_name)
add_student(second_name)
add_student(third_name)