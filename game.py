from character import Character
from profession import Profession

characters = []

def create_character(name, profession):
    if Character.validate_name(name) and Profession.validate_profession(profession):
        # TODO: deixar as validacoes de cada classe separadas e adicionar validacao para nome unico
        characters.append(Character(name, profession))
    else:
        raise Exception("Invalid name or profession")


def retrieve_character(name):
    for character in characters:
        if character.name == name:
            details = Profession.professions[character.profession]
            return {
                "name": character.name,
                "profession": character.profession,
                "life": details["attributes"]["life"],
                "strength": details["attributes"]["strength"],
                "agility": details["attributes"]["agility"],
                "intelligence": details["attributes"]["intelligence"],
                "attack": details["battle_modifiers"]["attack"],
                "speed": details["battle_modifiers"]["speed"]
            }
    raise Exception("Character not found")
