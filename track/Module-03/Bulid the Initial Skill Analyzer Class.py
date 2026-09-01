class SkillAnalyzer:
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills

student_skills = input().split()
required_skills = input().split()

# Create the analyzer and display matched skills
analyzer = SkillAnalyzer(student_skills, required_skills)
matched = sorted(analyzer.get_matched_skills())

if matched:
    print(f"Matched Skills: {', '.join(matched)}")
else:
    print("Matched Skills: None")