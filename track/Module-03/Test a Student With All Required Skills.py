class StudentProfile:
    def __init__(self, raw_skills):
        self.skills = []
        for s in raw_skills:
            cleaned = s.strip().lower()
            if cleaned:
                self.skills.append(cleaned)

class JobDescription:
    def __init__(self, raw_skills):
        self.required_skills = []
        for s in raw_skills:
            cleaned = s.strip().lower()
            if cleaned:
                self.required_skills.append(cleaned)

class SkillAnalyzer:
    def __init__(self, student, job):
        self.student = student
        self.job = job

    def analyze(self):
        pass

class MatchScoreCalculator(SkillAnalyzer):
    def analyze(self):
        if not self.job.required_skills:
            return 0.0

        matching_count = 0
        for req in self.job.required_skills:
            if req in self.student.skills:
                matching_count += 1

        return (matching_count / len(self.job.required_skills)) * 100.0

class MissingSkillDetector(SkillAnalyzer):
    def analyze(self):
        missing_skills = []
        for req in self.job.required_skills:
            if req not in self.student.skills and req not in missing_skills:
                missing_skills.append(req)
        return missing_skills

# Input parsing & Execution
student_skills = input().split(",")
required_skills = input().split(",")

student = StudentProfile(student_skills)
job = JobDescription(required_skills)

score_calculator = MatchScoreCalculator(student, job)
missing_detector = MissingSkillDetector(student, job)

print(score_calculator.analyze())
print(missing_detector.analyze())