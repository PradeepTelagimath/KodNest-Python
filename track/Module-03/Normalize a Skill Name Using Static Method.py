class StudentProfile:
    @staticmethod
    def normalize_skill(skill_name):
        return "_".join(skill_name.strip().lower().split())

# Read input
skill_name = input()

# Normalize the skill using the class name
normalized = StudentProfile.normalize_skill(skill_name)

# Print the normalized skill
print(f"Normalized Skill: {normalized}")