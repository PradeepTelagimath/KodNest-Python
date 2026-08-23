class StudentProfile:
    def __init__(self, student_id, name, course, score, is_placed):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.is_placed = is_placed

    def __str__(self):
        status = "Placed" if self.is_placed else "Not Placed"
        return (
            "STUDENT PROFILE\n"
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Score: {self.score:.1f}\n"
            f"Placement Status: {status}"
        )


student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
placement_input = input().strip()

# Convert placement_input into a Boolean value
is_placed = placement_input.lower() == "yes"

# Create a StudentProfile object using keyword arguments
student = StudentProfile(
    student_id=student_id,
    name=name,
    course=course,
    score=score,
    is_placed=is_placed
)

print(student)