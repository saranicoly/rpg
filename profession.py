class Profession:
  def __init__(self, name, job):
    self.name = name
    self.job = self.professions[job]

  professions = {
    "warrior": {
      "attributes": {"life": 20, "strength": 10, "agility": 5, "intelligence": 5},
      "battle_modifiers": {"attack": 9, "speed": 4}
    },
    "thief": {
      "attributes": {"life": 15, "strength": 4, "agility": 10, "intelligence": 4},
      "battle_modifiers": {"attack": 12, "speed": 8}
    },
    "mage": {
      "attributes": {"life": 12, "strength": 5, "agility": 6, "intelligence": 10},
      "battle_modifiers": {"attack": 19, "speed": 4}
    }
  }

  @staticmethod
  def validate_profession(profession):
    if profession in Profession.professions:
      return True
    else:
      return False
