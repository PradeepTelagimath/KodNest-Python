class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        course,
        score=0.0,
        is_placed=False
    ):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.is_placed = is_placed

    def __str__(self):
        placement_status = (
            "Placed" if self.is_placed
            else "Not Placed"
        )

        return (
            f"{self.student_id} | "
            f"{self.name} | "
            f"{self.course} | "
            f"{self.score:.1f} | "
            f"{placement_status}"
        )


student_one = StudentProfile(
    course="Python",
    student_id=101,
    is_placed=False,
    name="Asha",
    score=85.0
)

student_two = StudentProfile(
    course="Java",
    name="Rahul",
    student_id=102
)

print(student_one)
print(student_two)