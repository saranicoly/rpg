
import random
from typing import Union

from character import Character
from profession import Profession

characters = []


def create_character(name: str, profession: str) -> None:
    if not Character.validate_name(name):
        raise Exception("Invalid name")
    if not Profession.validate_profession(profession):
        raise Exception("Invalid profession")
    for character in characters:
        if character.name == name:
            raise Exception(f"Character {name} already exists")

    characters.append(Character(name, profession))


def retrieve_character(name: str, full_data: bool=True) -> Union[Character,dict]:
    for character in characters:
        if character.name == name:
            print(character)
            if full_data:
                return character
            else: # short form for all chars view
                return {
                    "name": character.name,
                    "profession": character.profession,
                    "is_alive": character.is_alive,
                }
    raise Exception("Character not found")


def retrieve_all_characters() -> list:
    return [retrieve_character(character.name, False) for character in characters]


def battle(name1: str, name2: str) -> list:
    battle_log = []

    char = [retrieve_character(name1), retrieve_character(name2)]
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

    # those variables are going to help us with a python trick that easily allows
    # us to select the faster character without needing to use a conditional statement
    # every time, since if c1_speed > c2_speed, c1_speed will be the faster one, thus
    # returning True, which evaluates to 1, selecting our second character, and vice versa
    is_c1_faster = c1_speed > c2_speed
    is_c2_faster = c1_speed < c2_speed
    battle_log.append(
        log_messages["speed_winner"].format(
            char1=char[is_c2_faster].name,
            char2=char[is_c1_faster].name,
            speed1=char_attributes[is_c2_faster]["speed"],
            speed2=char_attributes[is_c1_faster]["speed"],
        )
    )
    while char[0].life > 0 and char[1].life > 0:
        damage = calculate_atack(char_attributes[is_c2_faster]["attack"])

        char[is_c1_faster].life -= damage
        battle_log.append(
            log_messages["attack"].format(
                char1=char[is_c2_faster].name,
                char2=char[is_c1_faster].name,
                damage=damage,
                life=(char[is_c1_faster].life if char[is_c1_faster].life >= 0 else 0),
            )
        )

        damage = calculate_atack(char_attributes[is_c1_faster]["attack"])
        char[is_c2_faster].life -= damage
        battle_log.append(
            log_messages["attack"].format(
                char1=char[is_c1_faster].name,
                char2=char[is_c2_faster].name,
                damage=damage,
                life=(char[is_c2_faster].life if char[is_c2_faster].life >= 0 else 0),
            )
        )

    if char[0].life <= 0:
        char[0].life = 0
        char[0].is_alive = False
        battle_log.append(
            log_messages["winner"].format(char1=char[1].name, life=char[1].life)
        )
    else:
        char[1].life = 0
        char[1].is_alive = False
        battle_log.append(
            log_messages["winner"].format(char1=char[0].name, life=char[0].life)
        )

    return battle_log


def calculate_random_speeds(speed1: int, speed2: int) -> tuple:
    return (random.randint(0, speed1), random.randint(0, speed2))


def calculate_atack(attack: int) -> int:
    return random.randint(0, attack)


log_messages = {
    "speed_winner": "O {char1} ({speed1}) foi mais veloz que o {char2} ({speed2}) e irá começar!",
    "attack": "{char1} atacou o {char2} com {damage} de dano, {char2} com {life} pontos de vida restantes!",
    "winner": "{char1} venceu a batalha! {char1} ainda tem {life} pontos de vida restantes!",
}
