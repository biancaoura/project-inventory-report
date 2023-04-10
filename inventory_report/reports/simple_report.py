from datetime import datetime


class SimpleReport:
    @staticmethod
    def get_oldest_manufacture_date(report: list[dict]):
        manufacture_dates = [date["data_de_fabricacao"] for date in report]
        oldest_manufacture_date = min(manufacture_dates)

        return oldest_manufacture_date

    @staticmethod
    def get_closest_expiry_date(report: list[dict]):
        curr_date = datetime.today().isoformat()
        expiry_dates = [
            date["data_de_validade"]
            for date in report
            if date["data_de_validade"] >= curr_date
        ]

        return min(expiry_dates)

    @staticmethod
    def get_company_most_products(report: list[dict]):
        companies = {company["nome_da_empresa"]: 0 for company in report}

        for company in report:
            companies[company["nome_da_empresa"]] += 1

        return max(companies, key=companies.get)

    @staticmethod
    def generate(products: list[dict]):
        oldest_manufacture_date = SimpleReport.get_oldest_manufacture_date(
            products
        )
        closest_date = SimpleReport.get_closest_expiry_date(products)
        most_product_company = SimpleReport.get_company_most_products(products)
        return (
            f"Data de fabricação mais antiga: {oldest_manufacture_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {most_product_company}"
        )
