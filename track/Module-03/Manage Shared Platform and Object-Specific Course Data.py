class Course:
    # Shared platform variable
    platform_name = "KodNest Learning"

    def __init__(self, course_name, duration_days, fee):
        # Store object-specific course data
        self.course_name = course_name
        self.duration_days = duration_days
        self.fee = fee


# Read input details for Course 1
course1_name = input().strip()
course1_duration = int(input())
course1_fee = int(input())

# Read input details for Course 2
course2_name = input().strip()
course2_duration = int(input())
course2_fee = int(input())

# Create two Course objects
c1 = Course(course1_name, course1_duration, course1_fee)
c2 = Course(course2_name, course2_duration, course2_fee)

# Print the shared platform name
print(f"Platform: {Course.platform_name}")

# Print both course records
print(f"Course 1: {c1.course_name}")
print(f"Duration: {c1.duration_days} days")
print(f"Fee: {c1.fee}")

print(f"Course 2: {c2.course_name}")
print(f"Duration: {c2.duration_days} days")
print(f"Fee: {c2.fee}")