class SkillAnalyzer:
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills


class MatchScoreCalculator(SkillAnalyzer):
    def calculate_match_score(self):
        # Calculate percentage of required skills matched
        if not self.required_skills:
            return 0.0
        matched = self.get_matched_skills()
        return (len(matched) / len(self.required_skills)) * 100


class MissingSkillDetector(SkillAnalyzer):
    def get_missing_skills(self):
        # Return set difference of required skills and student skills
        return self.required_skills - self.student_skills


# Read input
student_skills = [skill.strip() for skill in input().split(",")]
required_skills = [skill.strip() for skill in input().split(",")]

# Instantiate objects
calculator = MatchScoreCalculator(student_skills, required_skills)
detector = MissingSkillDetector(student_skills, required_skills)

# Output match score formatted to 1 decimal place
score = calculator.calculate_match_score()
print(f"Match Score: {score:.1f}%")

# Output missing skills in alphabetical order
missing = sorted(list(detector.get_missing_skills()))
if missing:
    print(f"Missing Skills: {', '.join(missing)}")
else:
    print("Missing Skills: None")