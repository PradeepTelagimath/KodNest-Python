n = int(input())
departments = {}

for _ in range(n):
    data = input().split()
    department = data[0]
    salaries = list(map(int, data[1:]))
    departments[department] = salaries

# Calculate and print total salary for each department
for department, salaries in departments.items():
    total_salary = sum(salaries)
    print(f"{department}: {total_salary}")