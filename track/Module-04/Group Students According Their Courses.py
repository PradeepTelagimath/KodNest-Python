def group_students(students):
    students_by_course = {}
    for name, course in students:
        if course not in students_by_course:
            students_by_course[course] = []
        students_by_course[course].append(name)
    return students_by_course

n = int(input())
students = []

for _ in range(n):
    name, course = input().split()
    students.append((name, course))

students_by_course = group_students(students)

for course, names in students_by_course.items():
    print(course + ": " + " ".join(names))