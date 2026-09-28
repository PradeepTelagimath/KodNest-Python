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

class Manager:
    def analyze(self, student, job):
        # 1. Create a MatchScoreCalculator instance
        calculator = MatchScoreCalculator(student, job)
        
        # 2. Create a MissingSkillDetector instance
        detector = MissingSkillDetector(student, job)
        
        # 3. Call analyze() on both analyzer objects
        match_score = calculator.analyze()
        missing_skills = detector.analyze()
        
        # 4. Return both results
        return match_score, missing_skills


# Read input
student_skills = input().split(",")
required_skills = input().split(",")

# Create domain objects
student = StudentProfile(student_skills)
job = JobDescription(required_skills)

# Instantiate Manager and perform analysis
manager = Manager()
score, missing = manager.analyze(student, job)

# Print match score
print(score)

# Print missing skills formatted as expected
if missing:
    print(", ".join(missing))
else:
    print("None")