from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CSVImporter
from inventory_report.importer.json_importer import JSONImporter


class Inventory:
    @staticmethod
    def import_data(path: str, report_type: str):
        if path.endswith(".csv"):
            data = CSVImporter.import_data(path)
        elif path.endswith(".json"):
            data = JSONImporter.import_data(path)

        if report_type.lower() == "simples":
            return SimpleReport.generate(data)
        elif report_type.lower() == "completo":
            return CompleteReport.generate(data)
