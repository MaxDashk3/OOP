import zope.interface

from Registries import *

class CompanyCalculator:
    __royalties_by_type = {CompanyType.MEDIA: 0.8, CompanyType.ENTERTAINMENT: 0.5, CompanyType.OTHER: 0.2}

    @staticmethod
    def calculate_royalties(company: Company, creations: CreationRegistry):
        auth_revenue_dict = {}
        for month, earnings in company.revenue_per_month.items():
            for creat_id, revenue in earnings.items():
                for auth_id, part in creations[creat_id].author_part_dict.items():
                    auth_revenue_dict.setdefault(auth_id, {})
                    auth_revenue_dict[auth_id].setdefault(month, 0.0)
                    auth_revenue_dict[auth_id][month] += revenue*(part/100) * CompanyCalculator.__royalties_by_type[company.company_type]
        return auth_revenue_dict

class IAuthorTaxCalculator(zope.interface.Interface):
    def calculate_with_tax(earnings_dict: dict) -> dict:
        pass

@zope.interface.implementer(IAuthorTaxCalculator)
class ResidentTaxCalculator:
    @staticmethod
    def calculate_with_tax(earnings_dict: dict) -> dict:
        total_tax = 0.0
        for i in earnings_dict.keys():
            total_tax += earnings_dict[i] * 0.2
            earnings_dict[i] *= 0.8
        return {"tax": total_tax, "earnings": earnings_dict}


@zope.interface.implementer(IAuthorTaxCalculator)
class NonResidentTaxCalculator:
    @staticmethod
    def calculate_with_tax(earnings_dict: dict) -> dict:
        total_tax = 0.0
        for i in earnings_dict.keys():
            if 0 <= earnings_dict[i] <= 1000:
                tax_rate = 0.02
            elif earnings_dict[i] <= 5000:
                tax_rate = 0.05
            elif earnings_dict[i] <= 10000:
                tax_rate = 0.10
            elif earnings_dict[i] <= 20000:
                tax_rate = 0.15
            elif earnings_dict[i] <= 50000:
                tax_rate = 0.20
            else: tax_rate = 0.25

            total_tax += earnings_dict[i] * tax_rate
            earnings_dict[i] *= (1 - tax_rate)

        return {"tax": total_tax, "earnings": earnings_dict}


class EarningsTaxCalculator:
    @staticmethod
    def before_tax_earnings(companies: CompanyRegistry, creations: CreationRegistry) -> dict:
        auth_earnings_dict = {}
        for id, company in companies:
            for auth_id, earnings in CompanyCalculator.calculate_royalties(company, creations).items():
                for month, pay in earnings.items():
                    auth_earnings_dict.setdefault(auth_id, {})
                    auth_earnings_dict[auth_id].setdefault(str(month), 0.0)
                    auth_earnings_dict[auth_id][str(month)] += pay
        return auth_earnings_dict


    @staticmethod
    def total_tax(companies: CompanyRegistry, creations: CreationRegistry, authors: AuthorRegistry):
        auth_earnings_dict = EarningsTaxCalculator.before_tax_earnings(companies, creations)
        total_tax = 0.0
        for id, earnings in auth_earnings_dict.items():
            if authors[id].is_resident:
                earnings_with_tax = ResidentTaxCalculator.calculate_with_tax(earnings)
            else:
                earnings_with_tax = NonResidentTaxCalculator.calculate_with_tax(earnings)
            total_tax += earnings_with_tax["tax"]

        return total_tax

    @staticmethod
    def after_tax_earnings(companies: CompanyRegistry, creations: CreationRegistry, authors: AuthorRegistry):
        auth_earnings_dict = EarningsTaxCalculator.before_tax_earnings(companies, creations)
        for id, earnings in auth_earnings_dict.items():
            if authors[id].is_resident:
                earnings_with_tax = ResidentTaxCalculator.calculate_with_tax(earnings)
            else:
                earnings_with_tax = NonResidentTaxCalculator.calculate_with_tax(earnings)
            auth_earnings_dict[id] = earnings_with_tax["earnings"]

        return auth_earnings_dict

