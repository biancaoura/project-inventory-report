import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path_to_json: str):
        if not path_to_json.endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(path_to_json, "r") as file:
            return json.load(file)
