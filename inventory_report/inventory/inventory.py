import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path_to_csv: str, report_type: str):
        with open(path_to_csv, "r") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            data = list(reader)

        if report_type.lower() == "simples":
            return SimpleReport.generate(data)
        elif report_type.lower() == "completo":
            return CompleteReport.generate(data)
