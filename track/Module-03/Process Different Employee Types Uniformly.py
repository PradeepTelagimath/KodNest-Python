class Employee:
    def show_details(self):
        pass

class PermanentEmployee(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"{self.name} - Permanent - Salary: {self.salary}")

class ContractEmployee(Employee):
    def __init__(self, name, contract_months):
        self.name = name
        self.contract_months = contract_months

    def show_details(self):
        print(f"{self.name} - Contract - Duration: {self.contract_months} months")

# Input reading
permanent_name = input()
salary = input()
contract_name = input()
contract_months = input()

# Object creation and storage in a single list
employees = [
    PermanentEmployee(permanent_name, salary),
    ContractEmployee(contract_name, contract_months)
]

# Processing objects with a single loop
for emp in employees:
    emp.show_details()