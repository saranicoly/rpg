class Profession:
    professions = {
        "warrior": {
            "life": 20,
            "strength": 10,
            "agility": 5,
            "intelligence": 5,
            "battle_modifiers": {
                "attack": "80% da Força + 20% da Destreza",
                "speed": "60% da Destreza + 20% da Inteligência",
            },
        },
        "thief": {
            "life": 15,
            "strength": 4,
            "agility": 10,
            "intelligence": 4,
            "battle_modifiers": {
                "attack": "25% da Força + 100% da Destreza + 25% da Inteligência",
                "speed": "80% da Destreza",
            },
        },
        "mage": {
            "life": 12,
            "strength": 5,
            "agility": 6,
            "intelligence": 10,
            "battle_modifiers": {
                "attack": "20% da Força + 50% da Destreza + 150% da Inteligência",
                "speed": "20% da Força + 50% da Destreza",
            },
        },
    }

    @staticmethod
    def validate_profession(profession):
        if profession in Profession.professions:
            return True
        else:
            return False

    @staticmethod
    def get_battle_modifiers(character):
        return {
            "warrior": {
                "attack": character.strength * 0.8 + character.agility * 0.2,
                "speed": character.agility * 0.6 + character.intelligence * 0.2,
            },
            "thief": {
                "attack": character.strength * 0.25
                + character.agility
                + character.intelligence * 0.25,
                "speed": character.agility * 0.8,
            },
            "mage": {
                "attack": character.strength * 0.2
                + character.agility * 0.5
                + character.intelligence * 1.5,
                "speed": character.strength * 0.2 + character.agility * 0.5,
            },
        }[character.profession]
