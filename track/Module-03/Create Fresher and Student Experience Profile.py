class StudentProfile:
    def __init__(self, name):
        self.name = name

    def display_profile(self, category):
        print(f"{category} Student: {self.name}")

class FresherStudent(StudentProfile):
    pass

class ExperiencedStudent(StudentProfile):
    pass


fresher_name = input().strip()
experienced_name = input().strip()

# Create both objects and display their profiles using inherited methods
fresher_profile = FresherStudent(fresher_name)
experienced_profile = ExperiencedStudent(experienced_name)

fresher_profile.display_profile("Fresher")
experienced_profile.display_profile("Experienced")