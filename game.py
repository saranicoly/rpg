from character import Character
from profession import Profession
import random

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

def battle(name1, name2):
    battle_log = []
    c1, c2 = retrieve_character(name1), retrieve_character(name2)
    c1_attributes = Profession.get_battle_modifiers(c1["attributes"], c1["profession"])
    c2_attributes = Profession.get_battle_modifiers(c2["attributes"], c2["profession"])

    (c1_speed, c2_speed) = calculate_random_speeds(c1_attributes["speed"], c2_attributes["speed"])
    while(c1_speed == c2_speed):
        battle_log.append(f"{name1} e {name2} tiveram a mesma velocidade calculada ({c1_speed})!")
        (c1_speed, c2_speed) = calculate_random_speeds(c1_attributes["speed"], c2_attributes["speed"])
    if c1_speed > c2_speed:
        battle_log.append(f"{name1} ({c1_speed}) foi mais veloz que o {name2} ({c2_speed}) e irá começar!")
        atack = calculate_atack(c1_attributes["attack"])
        c2["life"] -= atack
        f"{name1} atacou {name2} com {atack} de dano, {name2} com {c2['life']} pontos de vida restantes;"
    else:
        battle_log.append(f"{name2} ({c2_speed}) foi mais veloz que o {name1} ({c1_speed}) e irá começar!")
        atack = calculate_atack(c2_attributes["attack"])
        c1["life"] -= atack
        f"{name2} atacou {name1} com {atack} de dano, {name1} com {c1['life']} pontos de vida restantes;"

def calculate_random_speeds(speed1, speed2):
    return (random.randint(0, speed1), random.randint(0, speed2))

def calculate_atack(atack):
    return random.randint(0, atack)