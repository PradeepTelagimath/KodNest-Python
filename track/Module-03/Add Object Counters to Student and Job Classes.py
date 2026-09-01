class StudentProfile:
    student_count = 0

    def __init__(self):
        StudentProfile.student_count += 1


class JobDescription:
    job_count = 0

    def __init__(self):
        JobDescription.job_count += 1


n = int(input())
m = int(input())

for _ in range(n):
    StudentProfile()

for _ in range(m):
    JobDescription()

print(f"Students Created: {StudentProfile.student_count}")
print(f"Jobs Created: {JobDescription.job_count}")