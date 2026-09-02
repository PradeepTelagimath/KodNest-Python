class StudentProfile:
    def show_profile(self):
        pass

class FresherStudent(StudentProfile):
    def __init__(self, name, graduation_year):
        self.name = name
        self.graduation_year = graduation_year

    def show_profile(self):
        print(f"{self.name} - Fresher - Graduation Year: {self.graduation_year}")

class ExperiencedStudent(StudentProfile):
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    def show_profile(self):
        print(f"{self.name} - Experienced - Experience: {self.experience} years")

fresher_name = input()
graduation_year = int(input())
experienced_name = input()
experience = int(input())

fresher = FresherStudent(fresher_name, graduation_year)
experienced = ExperiencedStudent(experienced_name, experience)

employees = [fresher, experienced]

for emp in employees:
    emp.show_profile()