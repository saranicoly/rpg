import re
from profession import Profession

class Character:
  def __init__(self, name, profession: Profession):
    self.name = name
    self.profession = profession
    self.is_alive = True
  
  @staticmethod
  def validate_name(name):
    # the regex ensures that the name has only letters and underscores
    if re.match(r'^\w[^\d\W]+$', name) and len(name)<16:
      return True
    else:
      return False