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
        student_skills = []
        for skill in self.student.skills:
            if skill.strip() != "":
                student_skills.append(skill.strip().lower())
                
        required_skills = []
        for skill in self.job.required_skills:
            if skill.strip() != "":
                required_skills.append(skill.strip().lower())

        if not required_skills:
            return 0.0

        match_count = 0
        for skill in required_skills:
            if skill in student_skills:
                match_count += 1

        return (match_count / len(required_skills)) * 100.0

class MissingSkillDetector(SkillAnalyzer):
    def analyze(self):
        student_skills = []
        for skill in self.student.skills:
            if skill.strip() != "":
                student_skills.append(skill.strip().lower())

        missing_skills = []
        for skill in self.job.required_skills:
            clean_skill = skill.strip()
            if clean_skill and clean_skill.lower() not in student_skills:
                missing_skills.append(clean_skill.lower())

        return missing_skills


student_skills = input().split(",")
required_skills = input().split(",")

student = StudentProfile(student_skills)
job = JobDescription(required_skills)

# Polymorphism implementation
match_calculator = MatchScoreCalculator(student, job)
missing_detector = MissingSkillDetector(student, job)

analyzers = [match_calculator, missing_detector]

for analyzer in analyzers:
    print(analyzer.analyze())