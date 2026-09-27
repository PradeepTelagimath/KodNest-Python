class CSVExporter:

  def __init__(self, file_name):
    self.file_name = file_name

  def export(self):
    return f"CSV Export: {self.file_name}.csv"


class JSONExporter:

  def __init__(self, file_name):
    self.file_name = file_name

  def export(self):
    return f"JSON Export: {self.file_name}.json"


class PDFExporter:

  def __init__(self, file_name):
    self.file_name = file_name

  def export(self):
    return f"PDF Export: {self.file_name}.pdf"


def run_exporters(exporters):
  for exporter in exporters:
    print(exporter.export())


# Driver Code
file_name = input()

csv_exporter = CSVExporter(file_name)
json_exporter = JSONExporter(file_name)
pdf_exporter = PDFExporter(file_name)

exporters = [csv_exporter, json_exporter, pdf_exporter]
run_exporters(exporters)