from abc import ABC, abstractmethod

class SkillAnalyzer(ABC):
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills

    @abstractmethod
    def analyze(self):
        pass

class MatchScoreCalculator(SkillAnalyzer):
    def calculate_match_score(self):
        matched = len(self.get_matched_skills())
        required = len(self.required_skills)
        return (matched / required) * 100 if required > 0 else 0.0

    def analyze(self):
        score = self.calculate_match_score()
        print(f"Match Score: {score:.2f}%")

class MissingSkillDetector(SkillAnalyzer):
    def get_missing_skills(self):
        return self.required_skills - self.student_skills

    def analyze(self):
        missing = sorted(list(self.get_missing_skills()))
        if missing:
            print(f"Missing Skills: {', '.join(missing)}")
        else:
            print("Missing Skills: None")

# Main execution logic
if __name__ == "__main__":
    student_skills = input().split()
    required_skills = input().split()

    calculator = MatchScoreCalculator(student_skills, required_skills)
    detector = MissingSkillDetector(student_skills, required_skills)

    calculator.analyze()
    detector.analyze()