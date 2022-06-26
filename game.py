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


def retrieve_character(name, full_data=True):
    for character in characters:
        if character.name == name:
            print(character)
            if full_data:
                return character
            else:
                return {
                    "name": character.name,
                    "profession": character.profession,
                    "is_alive": character.is_alive,
                }
    raise Exception("Character not found")


def retrieve_all_characters():
    return [retrieve_character(character.name, False) for character in characters]


def battle(name1, name2):
    battle_log = []

    c = [retrieve_character(name1), retrieve_character(name2)]
    c1_attributes = Profession.get_battle_modifiers(c[0])
    c2_attributes = Profession.get_battle_modifiers(c[1])
    char_attributes = [
        {},
        {},
    ]

    (c1_speed, c2_speed) = calculate_random_speeds(
        c1_attributes["speed"], c2_attributes["speed"]
    )
    while c1_speed == c2_speed:
        (c1_speed, c2_speed) = calculate_random_speeds(
            c1_attributes["speed"], c2_attributes["speed"]
        )
    char_attributes[0]["attack"] = c1_attributes["attack"]
    char_attributes[1]["attack"] = c2_attributes["attack"]
    char_attributes[0]["speed"] = c1_speed
    char_attributes[1]["speed"] = c2_speed

    battle_log.append(
        f"{c[c1_speed < c2_speed].name} ({char_attributes[c1_speed < c2_speed]['speed']}) foi mais veloz que o {c[c1_speed > c2_speed].name} ({char_attributes[c1_speed > c2_speed]['speed']}) e irá começar!"
    )
    while c[0].life > 0 and c[1].life > 0:
        damage = calculate_atack(char_attributes[c1_speed < c2_speed]["attack"])

        is_c1_faster = c1_speed > c2_speed
        is_c2_faster = c1_speed < c2_speed
        c[is_c2_faster].life -= damage
        battle_log.append(
            f"{c[is_c2_faster].name} atacou {c[is_c1_faster].name} com {damage} de dano, {c[is_c1_faster].name} com {c[is_c1_faster].life if c[is_c1_faster] >=0 else 0} pontos de vida restantes;"
        )

        damage = calculate_atack(char_attributes[is_c1_faster]["attack"])
        c[is_c2_faster].life -= damage
        battle_log.append(
            f"{c[is_c1_faster].name} atacou {c[is_c2_faster].name} com {damage} de dano, {c[is_c2_faster].name} com {c[is_c2_faster].life if c[is_c2_faster] >=0 else 0} pontos de vida restantes;"
        )

    if c[0].life <= 0:
        c[0].life = 0
        c[0].is_alive = False
        battle_log.append(
            f"{c[1].name} venceu a batalha! {c[1].name} ainda tem {c[1].life} pontos de vida restantes!"
        )
    else:
        c[1].life = 0
        c[1].is_alive = False
        battle_log.append(
            f"{c[0].name} venceu a batalha! {c[0].name} ainda tem {c[0].life} pontos de vida restantes!"
        )

    return battle_log


def calculate_random_speeds(speed1, speed2):
    return (random.randint(0, speed1 + 1), random.randint(0, speed2 + 1))


def calculate_atack(attack):
    return random.randint(0, attack + 1)
