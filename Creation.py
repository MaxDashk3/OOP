import ast

from custom_types import Serializable, zope

@zope.interface.implementer(Serializable)
class Creation:
    def __init__(self, title, author_part_dict: {int: float}):
        self.title = title
        self.author_part_dict = author_part_dict

    @property
    def author_part_dict(self):
        return self._author_part_dict

    @author_part_dict.setter
    def author_part_dict(self, author_part_dict):
        if sum(author_part_dict.values()) != 100:
            raise ValueError("Sum of ownership has to be 100!")
        else:
            self._author_part_dict = author_part_dict

    def to_dict(self) -> dict:
        return {"title": self.title, "author_part_dict": self.author_part_dict}

    @staticmethod
    def from_dict(data: dict):
        if type(data["author_part_dict"]) is not dict:
            author_part_dict = ast.literal_eval(data["author_part_dict"])
        else: author_part_dict = data["author_part_dict"]
        return Creation(data["title"], author_part_dict)