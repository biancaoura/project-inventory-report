import json
from inventory_report.importer.importer import Importer


class JSONImporter(Importer):
    @staticmethod
    def import_data(path_to_json: str):
        with open(path_to_json, "r") as file:
            return json.load(file)
