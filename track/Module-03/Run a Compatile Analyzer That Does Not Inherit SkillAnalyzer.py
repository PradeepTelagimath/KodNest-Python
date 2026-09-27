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
    if required == 0:
      return 0.0
    return (matched / required) * 100

  def analyze(self):
    score = self.calculate_match_score()
    return f"Match Score: {score:.2f}%"


class MissingSkillDetector(SkillAnalyzer):

  def analyze(self):
    missing = self.required_skills - self.student_skills
    if not missing:
      return "Missing Skills: None"
    # Convert to list and sort to ensure consistent output order
    missing_list = sorted(list(missing))
    return f"Missing Skills: {', '.join(missing_list)}"


# Duck typing class - does not inherit from SkillAnalyzer
class RequiredSkillCountAnalyzer:

  def __init__(self, required_skills):
    self.required_skills = required_skills

  def analyze(self):
    return f"Required Skill Count: {len(self.required_skills)}"


def run_analyzers(analyzers):
  for analyzer in analyzers:
    print(analyzer.analyze())


# Input processing
student_skills = input().split()
required_skills = input().split()

# Instantiate analyzer objects
calc = MatchScoreCalculator(student_skills, required_skills)
detector = MissingSkillDetector(student_skills, required_skills)
count_analyzer = RequiredSkillCountAnalyzer(required_skills)

# Store all three objects in one list
analyzers = [calc, detector, count_analyzer]

# Polymorphic / Duck-typed runner execution
run_analyzers(analyzers)