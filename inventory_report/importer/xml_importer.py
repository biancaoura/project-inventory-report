import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path_to_xml: str):
        if not path_to_xml.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(path_to_xml, "r") as file:
            reader = xmltodict.parse(file.read())
            return reader["dataset"]["record"]
