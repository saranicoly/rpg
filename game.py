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
                "speed": details["battle_modifiers"]["speed"],
            }
    raise Exception("Character not found")


def battle(name1, name2):
    battle_log = []

    c = [retrieve_character(name1), retrieve_character(name2)]
    c1_attributes = Profession.get_battle_modifiers(
        c[0]["attributes"], c[0]["profession"]
    )
    c2_attributes = Profession.get_battle_modifiers(
        c[1]["attributes"], c[1]["profession"]
    )
    c[0]["attack"],c[1]["attack"] = c1_attributes["attack"], c2_attributes["attack"]

    (c1_speed, c2_speed) = calculate_random_speeds(
        c1_attributes["speed"], c2_attributes["speed"]
    )
    while c1_speed == c2_speed:
        (c1_speed, c2_speed) = calculate_random_speeds(
            c1_attributes["speed"], c2_attributes["speed"]
        )
    c[0]["speed"], c[1]["speed"] = c1_speed, c2_speed
    battle_log.append(
        f"{c[c1_speed < c2_speed]['name']} ({c[c1_speed < c2_speed]['speed']}) foi mais \
            veloz que o {c[c1_speed > c2_speed]['name']} ({c[c1_speed > c2_speed]['speed']}) e irá começar!"
    )
    while c[0]["attributes"]["life"] > 0 and c[1]["attributes"]["life"] > 0:
        damage = calculate_atack(c[c1_speed < c2_speed]["attack"])

        is_c1_faster = c1_speed > c2_speed
        is_c2_faster = c1_speed < c2_speed
        c[is_c2_faster]["attributes"]["life"] -= damage
        battle_log.append(
            f"{c[is_c2_faster]['name']} atacou {c[is_c1_faster]['name']} com {damage} de dano, \
            {c[is_c1_faster]['name']} com {c[is_c1_faster]['attributes']['life']} pontos de vida restantes;"
        )

        damage = calculate_atack(c[is_c1_faster]["attack"])
        c[is_c2_faster]["attributes"]["life"] -= damage
        battle_log.append(
            f"{c[is_c1_faster]['name']} atacou {c[is_c2_faster]['name']} com {damage} de dano, \
            {c[is_c2_faster]['name']} com {c[is_c2_faster]['attributes']['life']} pontos de vida restantes;"
        )

    if c[0]["attributes"]["life"] <= 0:
        c[0]["attributes"]["life"] = 0
        battle_log.append(
            f"{c[1]['name']} venceu a batalha! {c[1]['name']} ainda tem {c[1]['attributes']['life']} pontos de vida restantes!"
        )
    else:
        c[1]["attributes"]["life"] = 0
        battle_log.append(
            f"{c[0]['name']} venceu a batalha! {c[0]['name']} ainda tem {c[0]['attributes']['life']} pontos de vida restantes!"
        )

    return battle_log


def calculate_random_speeds(speed1, speed2):
    return (random.randint(0, speed1), random.randint(0, speed2))


def calculate_atack(atack):
    return random.randint(0, atack)
