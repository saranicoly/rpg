class Profession:
  professions = {
    "warrior": {
      "attributes": {"life": 20, "strength": 10, "agility": 5, "intelligence": 5},
      "battle_modifiers": {"attack": '80% da Força + 20% da Destreza', "speed": "60% da Destreza + 20% da Inteligência"}
      # "battle_modifiers": {"attack": 9, "speed": 4}
    },
    "thief": {
      "attributes": {"life": 15, "strength": 4, "agility": 10, "intelligence": 4},
      "battle_modifiers": {"attack": "25% da Força + 100% da Destreza + 25% da Inteligência", "speed": "80% da Destreza"}
      # "battle_modifiers": {"attack": 12, "speed": 8}
    },
    "mage": {
      "attributes": {"life": 12, "strength": 5, "agility": 6, "intelligence": 10},
      "battle_modifiers": {"attack": "20% da Força + 50% da Destreza + 150% da Inteligência", "speed": "20% da Força + 50% da Destreza"}
      # "battle_modifiers": {"attack": 19, "speed": 4}
    }
  }

  @staticmethod
  def validate_profession(profession):
    if profession in Profession.professions:
      return True
    else:
      return False
