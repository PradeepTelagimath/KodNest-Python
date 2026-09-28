class StudentProfile:
    def __init__(self, raw_skills):
        self.skills = []
        for s in raw_skills:
            cleaned = s.strip().lower()
            if cleaned and cleaned not in self.skills:
                self.skills.append(cleaned)

class JobDescription:
    def __init__(self, raw_skills):
        self.required_skills = []
        for s in raw_skills:
            cleaned = s.strip().lower()
            if cleaned and cleaned not in self.required_skills:
                self.required_skills.append(cleaned)

class SkillAnalyzer:
    def __init__(self, student, job):
        self.student = student
        self.job = job

class MatchScoreCalculator(SkillAnalyzer):
    def analyze(self):
        if not self.job.required_skills:
            return 0.0

        matching_count = 0
        for req in self.job.required_skills:
            if req in self.student.skills:
                matching_count += 1

        return (matching_count / len(self.job.required_skills)) * 100.0

student = StudentProfile(input().split(","))
job = JobDescription(input().split(","))
calculator = MatchScoreCalculator(student, job)
print(calculator.analyze())