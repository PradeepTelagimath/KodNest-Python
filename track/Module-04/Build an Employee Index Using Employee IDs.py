def build_employee_index(employees):
    employee_by_id = {}
    for emp in employees:
        employee_by_id[emp["employee_id"]] = emp
    return employee_by_id

n = int(input())
employees = []

for _ in range(n):
    employee_id, name, department = input().split()
    employees.append({
        "employee_id": employee_id,
        "name": name,
        "department": department
    })

required_id = input()

employee_by_id = build_employee_index(employees)
employee = employee_by_id.get(required_id)

if employee is None:
    print("Employee not found")
else:
    print(employee["name"])
    print(employee["department"])