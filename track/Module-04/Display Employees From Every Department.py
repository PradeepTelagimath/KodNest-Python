n = int(input())
departments = {}

for _ in range(n):
    data = input().split()
    department = data[0]
    employees = data[1:]
    departments[department] = employees

# Print department and employee pairs
for department, employees in departments.items():
    for employee in employees:
        print(f"{department}: {employee}")