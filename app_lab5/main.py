import ast
import os
from Calculators import *

def to_csv_all(path_to_folder: str, creations: CreationRegistry, authors: AuthorRegistry, companies: CompanyRegistry) -> None:
    os.makedirs(path_to_folder, exist_ok=True)
    creations.to_csv(os.path.join(path_to_folder, "creations.csv"))
    authors.to_csv(os.path.join(path_to_folder, "authors.csv"))
    companies.to_csv(os.path.join(path_to_folder, "companies.csv"))

def to_json_all(path_to_folder: str, creations: CreationRegistry, authors: AuthorRegistry, companies: CompanyRegistry) -> None:
    os.makedirs(path_to_folder, exist_ok=True)
    creations.to_json(os.path.join(path_to_folder, "creations.csv"))
    authors.to_json(os.path.join(path_to_folder, "authors.csv"))
    companies.to_json(os.path.join(path_to_folder, "companies.csv"))

def from_csv_all(path_to_folder: str):
    #returns list of 3 registries in the following order: creations, authors, companies
    creations = CreationRegistry()
    creations.read_csv(os.path.join(path_to_folder, "creations.csv")),
    authors = AuthorRegistry()
    authors.read_csv(os.path.join(path_to_folder, "authors.csv")),
    companies = CompanyRegistry()
    companies.read_csv(os.path.join(path_to_folder, "companies.csv"))
    return[creations, authors, companies]

def from_json_all(path_to_folder: str):
    #returns list of 3 registries in the following order: creations, authors, companies
    creations = CreationRegistry()
    creations.read_json(os.path.join(path_to_folder, "creations.json")),
    authors = AuthorRegistry()
    authors.read_json(os.path.join(path_to_folder, "authors.json")),
    companies = CompanyRegistry()
    companies.read_json(os.path.join(path_to_folder, "companies.json"))
    return[creations, authors, companies]


creations = CreationRegistry()
authors = AuthorRegistry()
companies = CompanyRegistry()

while True:
    print("Choose a command:\n"
          "read [csv/json] [all/cr/auth/comp] [path/folder_path(for all)] - reads data from file(s) (path should not contain spaces)\n"
          "write [csv/json] [all/cr/auth/comp] [path/folder_path(for all)] - writes data to file(s) (path should not contain spaces)\n"
          "add [cr/auth/comp] - adds a new entry\n"
          "upd [cr/auth/comp] [id] - updates an entry\n"
          "rm [cr/auth/comp] [id] - removes an entry\n"
          "clear [all/cr/auth/comp] - removes all entries from registry(ies)\n"
          "show [all/cr/auth/comp] - displays data from registry(ies)\n"
          "tax - shows total tax paid to the country\n"
          "earn - shows authors' earnings with tax applied\n"
          "exit - exits the program\n")

    user_input = input()
    user_input = user_input.lower().split(" ")
    command = user_input[0]
    args = user_input[1:]
    match command:
        case "read":
            match args[0]:
                case "csv":
                    match args[1]:
                        case "all":
                            creations, authors, companies = from_csv_all(args[2])
                        case "cr":
                            creations.read_csv(args[2])
                        case "auth":
                            authors.read_csv(args[2])
                        case "comp":
                            companies.read_csv(args[2])
                        case _ :
                            print("Invalid command")
                case "json":
                    match args[1]:
                        case "all":
                            creations, authors, companies = from_json_all(args[2])
                        case "cr":
                            creations.read_json(args[2])
                        case "auth":
                            authors.read_json(args[2])
                        case "comp":
                            companies.read_json(args[2])
                        case _:
                            print("Invalid command")
                case _:
                    print("Invalid command")

        case "write":
            match args[0]:
                case "csv":
                    match args[1]:
                        case "all":
                            to_csv_all(args[2], creations, authors, companies)
                        case "cr":
                            creations.to_csv(args[2])
                        case "auth":
                            authors.to_csv(args[2])
                        case "comp":
                            companies.to_csv(args[2])
                        case _ :
                            print("Invalid command")
                case "json":
                    match args[1]:
                        case "all":
                            to_json_all(args[2], creations, authors, companies)
                        case "cr":
                            creations.to_json(args[2])
                        case "auth":
                            authors.to_json(args[2])
                        case "comp":
                            companies.to_json(args[2])
                        case _:
                            print("Invalid command")
                case _:
                    print("Invalid command")

        case "add": #add [cr/auth/comp] - adds a new entry
            match args[0]:
                case "cr":
                    title = input("Enter title: ")
                    author_part_dict = ast.literal_eval("{"+input("Enter author ownership (auth_id1: ownership, auth_id2: ownership ...): ")+"}")
                    creations.add(Creation(title, author_part_dict))

                case "auth":
                    name = input("Enter name: ")
                    surname = input("Enter surname: ")
                    patronymic = input("Enter patronymic: ")
                    is_resident = input("Is the author a resident? y/n: ")
                    is_resident = True if is_resident.lower() == "y" else False
                    authors.add(Author(name, surname, patronymic, is_resident))

                case "comp":
                    title = input("Enter title: ")
                    company_types_dict = {"1": CompanyType.MEDIA, "2": CompanyType.ENTERTAINMENT, "3": CompanyType.OTHER}
                    company_type = company_types_dict[input("Choose company type (media: 1, entertainment: 2, other: 3): ")]
                    company_creations = ast.literal_eval("["+input("Enter id's for creations owned by company (id1, id2, ...: ): ")+"]")
                    revenue_per_month_str = input("Enter revenue per month (month.year: {creation_id: revenue, ...}, ... ; leave empty if unknown): ")
                    if revenue_per_month_str.strip() == "":
                        companies.add(Company(title, company_type, company_creations))
                    else:
                        revenue_per_month_str = "{"+revenue_per_month_str+"}"
                        revenue_per_month = {}
                        for month, val in ast.literal_eval(revenue_per_month_str).items():
                            revenue_per_month[Month.from_string(str(month))] = val
                        companies.add(Company(title, company_type, company_creations, revenue_per_month))

                case _:
                    print("Invalid command")

        case "upd": #upd [cr/auth/comp] [id] - updates an entry
            obj_dict = None
            match args[0]:
                case "cr":
                    obj_dict = creations[int(args[1])].to_dict()
                case "auth":
                    obj_dict = authors[int(args[1])].to_dict()
                case "comp":
                    obj_dict = companies[int(args[1])].to_dict()
                case _:
                    print("Invalid command")
                    continue

            upd_dict = {}
            for attr, val in obj_dict.items():
                user_val = input(f"{attr}: {val} \nEnter new value or leave empty to skip: ")
                if user_val == "":
                    continue

                upd_dict[attr] = user_val

            for attr, val in upd_dict.items():
                obj_dict[attr] = val

            match args[0]:
                case "cr":
                    creations[int(args[1])] = Creation.from_dict(obj_dict)
                case "auth":
                    authors[int(args[1])] = Author.from_dict(obj_dict)
                case "comp":
                    companies[int(args[1])] = Company.from_dict(obj_dict)

        case "rm":  # rm [cr/auth/comp] [id] - removes an entry
            match args[0]:
                case "cr":
                    creations.remove(int(args[1]))
                case "auth":
                    authors.remove(int(args[1]))
                case "comp":
                    companies.remove(int(args[1]))
                case _:
                    print("Invalid command")

        case "clear":
            creations = CreationRegistry()
            authors = AuthorRegistry()
            companies = CompanyRegistry()

        case "show":
            match args[0]:
                case "all":
                    print("----------Authors-----------")
                    authors.show_data()
                    print("----------Creations-----------")
                    creations.show_data(authors)
                    print("----------Companies-----------")
                    companies.show_data(creations)
                    print()

                case "cr":
                    print("----------Creations-----------")
                    creations.show_data(authors)
                case "auth":
                    print("----------Authors-----------")
                    authors.show_data()
                case "comp":
                    print("----------Companies-----------")
                    companies.show_data(creations)

        case "tax":
            print(f"Total paid tax: {round(EarningsTaxCalculator.total_tax(companies, creations, authors),2)}")

        case "earn":
            earnings_dict = EarningsTaxCalculator.after_tax_earnings(companies, creations, authors)
            for auth_id, earnings in earnings_dict.items():
                try:
                    name = authors[auth_id].get_full_name()
                except KeyError:
                    name = f"[No author with id {auth_id}]"
                print(f"{name}:")
                for month, revenue in earnings.items():
                    print(f"  {month}: {round(revenue,2)}")

                print("-----------------")

        case "exit":
            break