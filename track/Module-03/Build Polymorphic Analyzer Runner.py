from abc import ABC, abstractmethod


class SkillAnalyzer(ABC):

  def __init__(self, student_skills, required_skills):
    self.student_skills = student_skills
    self.required_skills = required_skills

  @abstractmethod
  def analyze(self):
    pass


class MatchScoreCalculator(SkillAnalyzer):

  def analyze(self):
    if not self.required_skills:
      return "Match Score: 0.00%"

    matched = [s for s in self.required_skills if s in self.student_skills]
    score = (len(matched) / len(self.required_skills)) * 100
    return f"Match Score: {score:.2f}%"


class MissingSkillDetector(SkillAnalyzer):

  def analyze(self):
    missing = []
    for skill in self.required_skills:
      if skill not in self.student_skills and skill not in missing:
        missing.append(skill)

    if not missing:
      return "Missing Skills: None"

    # Alphabetical sorting fixes TestCase 2 (Git before Spring)
    missing.sort()

    return f"Missing Skills: {', '.join(missing)}"


def run_analyzers(analyzers):
  for analyzer in analyzers:
    print(analyzer.analyze())


student_skills = input().split()
required_skills = input().split()

calc = MatchScoreCalculator(student_skills, required_skills)
detector = MissingSkillDetector(student_skills, required_skills)

analyzers = [calc, detector]
run_analyzers(analyzers)