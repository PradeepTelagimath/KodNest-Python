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
        student_skills = self.student.skills
        required_skills = self.job.required_skills

        normalized_required = [s.strip().lower() for s in required_skills if s.strip()]

        if not normalized_required:
            return 0.0

        normalized_student = [s.strip().lower() for s in student_skills if s.strip()]

        match_count = 0
        for skill in normalized_required:
            if skill in normalized_student:
                match_count += 1

        return (match_count / len(normalized_required)) * 100.0


student_skills = input().split(",")
required_skills = input().split(",")

student = StudentProfile(student_skills)
job = JobDescription(required_skills)
calculator = MatchScoreCalculator(student, job)

print(calculator.analyze())