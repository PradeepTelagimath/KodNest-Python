class StudentProfile:

    def __init__(self, student_id, name, score, skills):
        self.__student_id = student_id
        
        # Validate name
        if name and name.strip():
            self.__name = name.strip()
        else:
            self.__name = "Unknown"
            
        # Validate score
        if 0 <= score <= 100:
            self.__score = score
        else:
            self.__score = 0
            
        # Initialize skills list
        if isinstance(skills, str):
            self.__skills = [s.strip() for s in skills.split(",") if s.strip()]
        else:
            self.__skills = list(skills)

    # Read-only property for student_id
    @property
    def student_id(self):
        return self.__student_id

    # Getter and setter for name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name and new_name.strip():
            self.__name = new_name.strip()

    # Getter and setter for score
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        if 0 <= new_score <= 100:
            self.__score = new_score

    # Read-only property returning skills as a tuple
    @property
    def skills(self):
        return tuple(self.__skills)

    # Method to add a new unique, non-empty skill
    def add_skill(self, new_skill):
        cleaned_skill = new_skill.strip()
        if cleaned_skill and cleaned_skill not in self.__skills:
            self.__skills.append(cleaned_skill)

    # String representation
    def __str__(self):
        skills_str = ", ".join(self.__skills)
        return (
            f"STUDENT PROFILE\n"
            f"Student ID: {self.__student_id}\n"
            f"Name: {self.__name}\n"
            f"Score: {self.__score}\n"
            f"Skills: {skills_str}"
        )


# Input Reading
student_id = int(input())
name = input().strip()
initial_score = int(input())
skills_input = input().strip()
new_score = int(input())
new_skill = input().strip()

initial_skills = [
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()
]

# Create one StudentProfile object
student = StudentProfile(student_id, name, initial_score, initial_skills)

# Update the score through the property
student.score = new_score

# Add the skill through the method
student.add_skill(new_skill)

# Print the final object
print(student)