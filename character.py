import re
from profession import Profession


class Character:
    def __init__(self, name: str, profession: str) -> None:
        self.name = name
        self.is_alive = True
        self.profession = profession
        for key in Profession.professions[profession]:
            setattr(self, key, Profession.professions[profession][key])

    @staticmethod
    def validate_name(name: str) -> bool:
        # the regex ensures that the name has only letters and underscores
        if re.match(r"^\w[^\d\W]+$", name) and len(name) < 16:
            return True
        else:
            return False
