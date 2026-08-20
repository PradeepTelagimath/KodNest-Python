class StudentProfile:
    def __init__(self, student_id, name, course, experience, skills):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills = skills

    def __str__(self):
        # Format skills as a comma-separated string
        skills_str = ", ".join(self.skills)
        
        return (
            f"STUDENT PROFILE\n"
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Experience in Years: {self.experience}\n"
            f"Skills: {skills_str}"
        )

# Reading inputs
student_id = int(input().strip())
name = input().strip()
course = input().strip()
experience = int(input().strip())
skills = input().strip().split()

# Creating exactly one StudentProfile object
student = StudentProfile(student_id, name, course, experience, skills)

# Displaying the object
print(student)