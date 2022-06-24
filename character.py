import re

class Character:
  def __init__(self, name, profession):
    self.name = name
    self.profession = profession
  
  @staticmethod
  def validate_name(name):
    # the regex ensures that the name has only letters and underscores
    if re.match(r'^\w[^\d\W]+$', name) and len(name)<16:
      return True
    else:
      return False