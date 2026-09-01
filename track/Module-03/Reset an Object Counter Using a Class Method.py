class StudentProfile:
    student_count = 0

    def __init__(self):
        StudentProfile.student_count += 1

    @classmethod
    def reset_count(cls):
        # Reset the shared counter using cls
        cls.student_count = 0


n = int(input())
m = int(input())

for _ in range(n):
    StudentProfile()

print(f"Before Reset: {StudentProfile.student_count}")

StudentProfile.reset_count()

for _ in range(m):
    StudentProfile()

print(f"After Reset: {StudentProfile.student_count}")