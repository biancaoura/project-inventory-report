from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(path: str, report_type: str):
        if path.endswith(".csv"):
            data = CsvImporter.import_data(path)
        elif path.endswith(".json"):
            data = JsonImporter.import_data(path)
        else:
            data = XmlImporter.import_data(path)

        if report_type.lower() == "simples":
            print(SimpleReport.generate(data))
            return SimpleReport.generate(data)
        elif report_type.lower() == "completo":
            print(CompleteReport.generate(data))
            return CompleteReport.generate(data)
