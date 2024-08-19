# Data and data manipulation functions

from character import Character
# from datetime import datetime

# List of characters for our initial table data
characters = [
  Character("Sandra", "Kami", 3, 35, "Warforged", "Druid", "Female", "No"),
  Character("Lukáš", "Snorri", 9, 21, "Fairy", "Bard", "Male", "No"),
  Character("Loki", "Connie Buřtušák", 3, 666, "High Elf", "Ranger", "Female", "Yes")
]
# Converts each character into a list of strings for our table data
def convert_characters_to_table_data():
  characters_data = []
  for character in characters:
    strings = character.convert_values_to_strings()
    characters_data.append(strings)
  return characters_data
  
# Validates the input and attemts to create a character, returns True if character created successfully and False otherwise
def try_to_create_character(user_name, character_name, level, age, race, character_class, is_male_or_female, newbie):
  if len(user_name) < 2 or len(character_name) < 2 or len(race) < 2 or len(character_class) < 2 or level == "" or age == "":
    return False

  try:
    # date_of_birth = datetime.strptime(date_of_birth, '%Y/%m/%d')
    # if date_of_birth > datetime.now():
      # return False

    level = int(level)
    age = int(age)
    if level <= 0 or age <= 0:
      return False
    if is_male_or_female == True:
      is_male_or_female = "Male"
    else:
      is_male_or_female = "Female"
    if newbie == True:
      newbie = "Yes"
    else:
      newbie = "No"

    character = Character(user_name, character_name, level, age, race, character_class, is_male_or_female, newbie)
    characters.append(character)
    return True
  except:
    return False