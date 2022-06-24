from character import Character
from profession import Profession

personagens = []
def create_character(name, profession):
  if(Character.validate_name(name) and Profession.validate_profession(profession)):
    personagens.append(Character(name, profession))
  else:
    raise Exception("Invalid name or profession")