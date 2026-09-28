n = int(input())
employees = []

for _ in range(n):
    name, salary = input().split()
    employees.append((name, int(salary)))

sorted_employees = sorted(employees, key=lambda x: x[1])

for name, salary in sorted_employees:
    print(name, salary)