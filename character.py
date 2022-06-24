import re

class Character:
  def __init__(self, name, profession):
    self.name = name
    self.profession = profession
  
  def validate_name(self):
    if re.match(r'^\w[^\d\W]+$', self.name):
      return True
    else:
      return False