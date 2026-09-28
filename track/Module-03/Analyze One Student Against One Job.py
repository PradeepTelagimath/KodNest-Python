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

    def analyze(self):
        pass

class MatchScoreCalculator(SkillAnalyzer):
    def analyze(self):
        student_skills = [s.strip().lower() for s in self.student.skills if s.strip()]
        required_skills = [s.strip().lower() for s in self.job.required_skills if s.strip()]

        if not required_skills:
            return 0.0

        match_count = 0
        for skill in required_skills:
            if skill in student_skills:
                match_count += 1

        return (match_count / len(required_skills)) * 100.0

class MissingSkillDetector(SkillAnalyzer):
    def analyze(self):
        student_skills = [s.strip().lower() for s in self.student.skills if s.strip()]
        
        missing_skills = []
        for s in self.job.required_skills:
            clean_skill = s.strip()
            if clean_skill and clean_skill.lower() not in student_skills:
                # Keep original skill casing from job required skills
                missing_skills.append(clean_skill)

        return missing_skills


# Read input lines
student_skills = input().split(",")
required_skills = input().split(",")

# Instantiate profile and job objects
student = StudentProfile(student_skills)
job = JobDescription(required_skills)

# Instantiate analyzer objects
score_calculator = MatchScoreCalculator(student, job)
missing_detector = MissingSkillDetector(student, job)

# Calculate and print match score
match_score = score_calculator.analyze()
print(match_score)

# Identify and print missing skills
missing = missing_detector.analyze()
if missing:
    print(", ".join(missing))
else:
    print("None")
    