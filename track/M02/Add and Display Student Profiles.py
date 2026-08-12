class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


class PlacementManager:
    def __init__(self):
        self.student_profiles = []

    def add_student_profile(self, student_profile):
        # Add the received student object to the list
        self.student_profiles.append(student_profile)

    def display_student_profiles(self):
        # Handle an empty collection
        if not self.student_profiles:
            print("No student profiles available")
            return

        # Display all student profiles
        print("STUDENT PROFILES")
        for profile in self.student_profiles:
            print(profile)


# Main Execution
manager = PlacementManager()

n = int(input())
for _ in range(n):
    student_id = input()
    name = input()
    course = input()
    profile = StudentProfile(student_id, name, course)
    manager.add_student_profile(profile)

manager.display_student_profiles()