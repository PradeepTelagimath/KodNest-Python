class Course:
    def __init__(self, course_name):
        self.course_name = course_name

    def display_course(self):
        print(f"Course: {self.course_name}")

class CodingCourse(Course):
    pass

# Read input
course_name = input().strip()

# Create a CodingCourse object and call the inherited method
course_obj = CodingCourse(course_name)
course_obj.display_course()