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

class MissingSkillDetector(SkillAnalyzer):
    def analyze(self):
        # Normalize student skills
        normalized_student = [s.strip().lower() for s in self.student.skills if s.strip()]
        
        missing_skills = []
        for s in self.job.required_skills:
            clean_skill = s.strip()
            # Check if skill is non-empty and missing from student's skills
            if clean_skill and clean_skill.lower() not in normalized_student:
                missing_skills.append(clean_skill.lower())
                
        return missing_skills


student_skills = input().split(",")
required_skills = input().split(",")

student = StudentProfile(student_skills)
job = JobDescription(required_skills)
detector = MissingSkillDetector(student, job)

print(detector.analyze())