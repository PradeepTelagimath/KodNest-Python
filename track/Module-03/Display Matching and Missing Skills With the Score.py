class StudentProfile:
    def __init__(self, raw_skills):
        self.skills = []
        for s in raw_skills:
            cleaned = s.strip().lower()
            if cleaned:
                self.skills.append(cleaned)

class JobDescription:
    def __init__(self, raw_skills):
        self.skills = []
        for s in raw_skills:
            cleaned = s.strip().lower()
            if cleaned:
                self.skills.append(cleaned)

class SkillAnalyzer:
    def __init__(self, student, job):
        self.student = student
        self.job = job

class MatchScoreCalculator(SkillAnalyzer):
    def analyze(self):
        if not self.job.skills:
            return 0.0, []

        matching_skills = []
        for req in self.job.skills:
            if req in self.student.skills and req not in matching_skills:
                matching_skills.append(req)

        score = (len(matching_skills) / len(self.job.skills)) * 100
        return score, matching_skills

class MissingSkillDetector(SkillAnalyzer):
    def analyze(self):
        missing_skills = []
        for req in self.job.skills:  # <--- FIXED HERE (changed from self.job.required_skills)
            if req not in self.student.skills and req not in missing_skills:
                missing_skills.append(req)
        return missing_skills

# Input Parsing & Execution
student_skills = input().split(",")
required_skills = input().split(",")

student = StudentProfile(student_skills)
job = JobDescription(required_skills)

score_calculator = MatchScoreCalculator(student, job)
missing_detector = MissingSkillDetector(student, job)

score, matching_skills = score_calculator.analyze()
missing_skills = missing_detector.analyze()

print("Match Score:", score)
print("Matching Skills:", matching_skills)
print("Missing Skills:", missing_skills)