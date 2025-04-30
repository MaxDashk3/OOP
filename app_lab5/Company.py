import pandas as pd

from custom_types import *

@zope.interface.implementer(Serializable)
class Company:
    def __init__(self, title, company_type: CompanyType, creations: [int], revenue_per_month:{Month: {int: float}} = {}):
        self.title = title
        self.company_type = company_type
        self.creations = creations
        #revenue per month : {month: {creation id: revenue}}
        self.revenue_per_month = revenue_per_month

    def add_revenue(self, month: Month, revenue: {int: float}) -> None:
        self.revenue_per_month.add(month, revenue)

    def add_creation(self, creation_id: int):
        self.creations.append(creation_id)

    def to_dict(self) -> dict:
        revenue_per_month = {}
        for i in self.revenue_per_month.keys():
            revenue_per_month[str(i)] = self.revenue_per_month[i]
        return {"title": self.title, "company_type": self.company_type.value, "creations": self.creations, "revenue_per_month": revenue_per_month}

    @staticmethod
    def from_dict(data: dict):

        if type(data["revenue_per_month"]) != dict:
            data["revenue_per_month"] = ast.literal_eval(data["revenue_per_month"])
        if type(data["creations"]) != list:
            data["creations"] = ast.literal_eval(data["creations"])

        revenue_per_month = {}
        for i in data["revenue_per_month"].keys():
            revenue_per_month[Month.from_string(i)] = data["revenue_per_month"][i]

        return Company(data["title"], CompanyType(data["company_type"]), data["creations"], revenue_per_month)