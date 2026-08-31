class Employee:
    def __init__(self, name):
        self.name = name
        print("Employee constructor")

class Developer(Employee):
    def __init__(self, name):
        print("Developer constructor started")
        super().__init__(name)
        print("Developer constructor completed")

name = input().strip()

# Create the object and display the name
display = Developer(name)
print(f"Developer: {display.name}")