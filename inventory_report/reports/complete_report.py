from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def get_stock_qty(report: list[dict]):
        companies = {}

        for company in report:
            if company not in companies:
                companies[company] = 1
            else:
                companies[company] += 1

        stock = ""
        for company_name, qty in companies.items():
            stock += f"- {company_name}: {qty}\n"

        return stock

    @staticmethod
    def generate(report: list[dict]):
        simple_report = SimpleReport.generate(report)
        companies = [product["nome_da_empresa"] for product in report]

        qty_stock = CompleteReport.get_stock_qty(companies)

        formatted_report = (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n{qty_stock}"
        )
        return formatted_report
