# Create the StudentProfile class
class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


# Create the PlacementManager class
class PlacementManager:
    def __init__(self):
        self.student_profiles = []

    def add_student_profile(self, student_profile):
        self.student_profiles.append(student_profile)

    def filter_students_by_course(self, course):
        matching_students = []
        for student in self.student_profiles:
            if student.course.lower() == course.lower():
                matching_students.append(student)
        return matching_students


# Read the student details
manager = PlacementManager()

n = int(input())

for _ in range(n):
    student_id = int(input())
    name = input().strip()
    course = input().strip()
    
    student = StudentProfile(student_id, name, course)
    manager.add_student_profile(student)

filter_course = input().strip()

# Filter and display the matching students
results = manager.filter_students_by_course(filter_course)

if results:
    for student in results:
        print(student)
else:
    print(f"No students found for course: {filter_course}")