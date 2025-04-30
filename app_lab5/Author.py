from custom_types import Serializable, zope

@zope.interface.implementer(Serializable)
class Author:

    def __init__(self, name, surname, patronymic, is_resident):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.is_resident = is_resident

    def get_full_name(self) -> str:
        return " ".join([self.surname, self.name, self.patronymic])

    @staticmethod
    def from_dict(data: dict):
        return Author(data["name"], data["surname"], data["patronymic"], bool(data["is_resident"]))

    def to_dict(self) -> dict:
        return {"name": self.name, "surname": self.surname, "patronymic": self.patronymic, "is_resident": self.is_resident}
