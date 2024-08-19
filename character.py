# Character model

# from datetime import datetime

class Character:
  # Initialize a Character and set the values for the fields
  def __init__(self, user_name, character_name, level, age, race, character_class, is_male_or_female, newbie):
    self.user_name = user_name
    self.character_name = character_name
    self.level = level
    self.age = age
    self.race = race
    self.character_class = character_class
    self.is_male_or_female = is_male_or_female
    self.newbie = newbie
    
  # Convert each of the fields to a string, bundle them into a list, and return it
  def convert_values_to_strings(self):
    # date_of_birth = datetime.strftime(self.date_of_birth, '%Y/%m/%d') # YYYY/MM/DD
    level = str(self.level)
    age = str(self.age)
    is_male_or_female = str(self.is_male_or_female)
    newbie = str(self.newbie)
    return [self.user_name, self.character_name, level, age, self.race, self.character_class, is_male_or_female, newbie]