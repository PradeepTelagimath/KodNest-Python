class StudentProfile:
    @staticmethod
    def is_valid_skill(skill_name):
        # Must contain at least one non-space character
        if not skill_name.strip():
            return False
        # Every character must be a letter or a space
        for char in skill_name:
            if not (char.isalpha() or char.isspace()):
                return False
        return True

    @staticmethod
    def normalize_skill(skill_name):
        # Split by any whitespace, lowercase each word, and join with single underscore
        words = skill_name.split()
        return "_".join(word.lower() for word in words)


# Read input
skill_name = input()

# Validate and process
if StudentProfile.is_valid_skill(skill_name):
    normalized = StudentProfile.normalize_skill(skill_name)
    print("Valid Skill")
    print(f"Normalized Skill: {normalized}")
else:
    print("Invalid Skill")