from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self):
        pass

class StudentReport(ReportGenerator):
    def generate_report(self):
        return "Generating Student Report"

class PlacementReport(ReportGenerator):
    def generate_report(self):
        return "Generating Placement Report"

class SimpleTextReporter:
    def __init__(self, title):
        self.title = title

    def generate_report(self):
        return f"Generating Text Report: {self.title}"

def run_reports(reports):
    for report in reports:
        print(report.generate_report())

if __name__ == "__main__":
    title = input().strip()
    
    student_report = StudentReport()
    placement_report = PlacementReport()
    text_reporter = SimpleTextReporter(title)
    
    reports = [student_report, placement_report, text_reporter]
    run_reports(reports)