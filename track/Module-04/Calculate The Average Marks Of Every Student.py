n = int(input())
students = []

for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(int, data[1:]))
    students.append({
        "name": name,
        "marks": marks
    })

# Iterate over each student dictionary to calculate and print average
for student in students:
    name = student["name"]
    marks = student["marks"]
    average = sum(marks) / len(marks)
    print(f"{name}: {average:.2f}")