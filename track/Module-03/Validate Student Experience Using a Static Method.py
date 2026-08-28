class StudentProfile:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    @staticmethod
    def is_valid_experience(experience):
        return 0 <= experience <= 40

# Read inputs
name = input().strip()
experience = int(input())

# Validate experience using the class name
if StudentProfile.is_valid_experience(experience):
    student = StudentProfile(name, experience)
    print("Profile Created")
    print(f"Name: {student.name}")
    print(f"Experience: {student.experience} years")
else:
    print("Invalid Experience")