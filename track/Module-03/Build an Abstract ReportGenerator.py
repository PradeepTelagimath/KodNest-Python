from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self):
        pass

class StudentReport(ReportGenerator):
    def __init__(self, name):
        self.name = name

    def generate_report(self):
        print(f"Generating student report for {self.name}")

name = input()
report = StudentReport(name)
report.generate_report()