class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def display_profile(self):
        print(f"Employee: {self.name}")
        print(f"Language: {self.language}")

name = input().strip()
language = input().strip()

dev = Developer(name, language)
dev.display_profile()