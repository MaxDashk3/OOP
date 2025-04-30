import pandas as pd
import zope.interface
import json
from abc import ABC, abstractmethod

from Author import Author
from Company import Company
from Creation import Creation
from custom_types import CompanyType, Month


class Registry(ABC):
    def __init__(self, items: dict = None):
        if items is None:
            self._items = dict()
        else:
            self._items = dict(items)
            self.sort()
        self._max_id = 0

    @abstractmethod
    def sort(self) -> None:
        pass

    def __generate_id(self) -> int:
        self._max_id += 1
        return self._max_id

    def add(self, item):
        self._items[self.__generate_id()] = item
        self.sort()

    def add_many(self, items):
        for item in items:
            self.add(item)

    def remove(self, id: int):
        self._items.pop(id)

    def update(self, id: int, item):
        self._items[id] = item
        self.sort()

    def __getitem__(self, item):
        return self._items[item]

    def __setitem__(self, key, value):
        self._items[key] = value

    def __len__(self):
        return len(self._items)

    def __contains__(self, id):
        return id in self._items.keys()

    def __iter__(self):
        return iter(self._items.items())

    def to_csv(self, path) -> None:
        df = pd.DataFrame()
        for item in self._items.items():
            item_dict = {"id": item[0], **item[1].to_dict()}
            item_df = pd.DataFrame([item_dict])
            df = pd.concat([df, item_df])
        df.to_csv(path, index=False)

    def to_json(self, path) -> None:
        item_list = []
        for item in self._items.items():
            item_dict = {"id": item[0], **item[1].to_dict()}
            item_list.append(item_dict)
        json.dump(item_list, open(path, "w"), indent=4)

    def read_csv(self, path):
        df = pd.read_csv(path)
        items_dict = df.to_dict("records")
        for item in items_dict:
            self._items[item["id"]] = self._create_item_from_dict(item)
        self.sort()
        self._max_id = max(self._items.keys())

    def read_json(self, path):
        data = json.load(open(path))
        for item in data:
            self._items[item["id"]] = self._create_item_from_dict(item)
        self.sort()
        self._max_id = max(self._items.keys())

    @staticmethod
    @abstractmethod
    def _create_item_from_dict(item_dict: dict):
        pass

    @abstractmethod
    def show_data(self, *args, **kwargs) -> None:
        pass


class AuthorRegistry(Registry):
    def sort(self) -> None:
        sorted_items = dict(sorted(self._items.items(), key=lambda x: x[1].get_full_name()))
        self._items = sorted_items

    @staticmethod
    def _create_item_from_dict(item_dict: dict):
        return Author.from_dict(item_dict)

    def show_data(self):
        for id, item in self._items.items():
            print(f"id {id}:")
            print(f"surname: {item.surname}")
            print(f"name: {item.name}")
            print(f"patronymic: {item.patronymic}")
            print("a resident" if item.is_resident else "not a resident")
            print("----------------------")

class CreationRegistry(Registry):
    def sort(self) -> None:
        sorted_items = dict(sorted(self._items.items(), key=lambda x: x[1].title))
        self._items = sorted_items

    @staticmethod
    def _create_item_from_dict(item_dict: dict):
        return Creation.from_dict(item_dict)

    def show_data(self, authors: AuthorRegistry):
        for id, item in self._items.items():
            print(f"id {id}:")
            print(f"title: {item.title}")
            print(f"authors:")
            for auth_id, ownership in item.author_part_dict.items():
                try:
                    name = authors[auth_id].get_full_name()
                except KeyError:
                    name = f"[No author with id {auth_id}]"
                print(f"  {name} : {ownership}%")
            print("----------------------")

class CompanyRegistry(Registry):
    def sort(self) -> None:
        sorted_items = dict(sorted(self._items.items(), key=lambda x: x[1].title))
        self._items = sorted_items

    @staticmethod
    def _create_item_from_dict(item_dict: dict):
        return Company.from_dict(item_dict)

    def show_data(self, creations: CreationRegistry):
        for id, item in self._items.items():
            print(f"id {id}:")
            print(f"title: {item.title}")
            print(f"company_type: {item.company_type.value}")
            print("creations:")
            for i in item.creations:
                try:
                    title = creations[i].title
                except KeyError:
                    title =  f"[No creation with id {i}]"
                print(f"  {title}")
            print("revenue per month:")
            for month, val in item.revenue_per_month.items():
                print(f"  {str(month)}:")
                for creation, revenue in val.items():
                    try:
                        title = creations[creation].title
                    except KeyError:
                        title = f"[No creation with id {i}]"
                    print(f"    {title} : {revenue}")
            print("----------------------")