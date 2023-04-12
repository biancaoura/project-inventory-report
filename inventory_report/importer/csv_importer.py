import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path_to_csv: str):
        if not path_to_csv.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path_to_csv, "r") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')

            return list(reader)
