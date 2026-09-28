class StudentProfile:
    def __init__(self, skills):
        self.skills = skills

class JobDescription:
    def __init__(self, required_skills):
        self.required_skills = required_skills

class SkillAnalyzer:
    def __init__(self, student, job):
        self.student = student
        self.job = job

class MatchScoreCalculator(SkillAnalyzer):
    def analyze(self):
        student_skills = [s.strip().lower() for s in self.student.skills if s.strip()]
        required_skills = [s.strip().lower() for s in self.job.required_skills if s.strip()]

        if not required_skills:
            return 0.0

        matches = 0
        for skill in required_skills:
            if skill in student_skills:
                matches += 1

        return round(matches / len(required_skills), 1)

class MissingSkillDetector(SkillAnalyzer):
    def analyze(self):
        student_skills = [s.strip().lower() for s in self.student.skills if s.strip()]
        missing_skills = []

        for skill in self.job.required_skills:
            normalized_skill = skill.strip().lower()
            if normalized_skill and normalized_skill not in student_skills:
                missing_skills.append(normalized_skill)

        return missing_skills

# Input parsing
student_skills = input().split(",")
required_skills = input().split(",")

student = StudentProfile(student_skills)
job = JobDescription(required_skills)

# Analyzers instantiation and execution
score_calculator = MatchScoreCalculator(student, job)
missing_detector = MissingSkillDetector(student, job)

print(f"Match Score: {score_calculator.analyze()}")
print(f"Missing Skills: {missing_detector.analyze()}")