class SkillAnalyzer:
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills

class MatchScoreCalculator(SkillAnalyzer):
    def calculate_match_score(self):
        matched = self.get_matched_skills()
        if not self.required_skills:
            return 0.0
        return (len(matched) / len(self.required_skills)) * 100

student_skills = input().split()
required_skills = input().split()

calculator = MatchScoreCalculator(student_skills, required_skills)
score = calculator.calculate_match_score()
print(f"Match Score: {score:.2f}%")