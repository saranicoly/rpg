import re

class Character:
  def __init__(self, name, profession):
    self.name = name
    self.profession = profession
  
  def validate_name(self):
    # the regex ensures that the name has only letters and underscores
    if re.match(r'^\w[^\d\W]+$', self.name) and len(self.name)<16:
      return True
    else:
      return False