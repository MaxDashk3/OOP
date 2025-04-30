from enum import Enum
import zope.interface
from abc import ABC, abstractmethod
import json, ast
import pandas as pd


class CompanyType(Enum):
    MEDIA = "media"
    ENTERTAINMENT = "entertainment"
    OTHER = "other"

class Month:
    def __init__(self, month:int, year:int):
        self.year = year
        self.month = month

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month:int):
        if 1 <= month <=12:
            self.__month = month
        else:
            raise ValueError("Month should be an number from 1 to 12")

    def __str__(self):
        return f"{self.month}.{self.year}"

    @staticmethod
    def from_string(string: str):
        split_str = string.split(".")
        if len(split_str) == 2:
            return Month(int(split_str[0]), int(split_str[1]))
        else:
            raise ValueError("Incorrect format")

class Serializable(zope.interface.Interface):
    def to_dict(self) -> dict:
        pass

    def from_dict(data: dict):
        pass
