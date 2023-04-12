import csv
from inventory_report.importer.importer import Importer


class CSVImporter(Importer):
    @staticmethod
    def import_data(path_to_csv: str):
        with open(path_to_csv, "r") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')

            return list(reader)
