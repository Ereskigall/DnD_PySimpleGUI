# Form to create and save a new character

import PySimpleGUI as sg

import dataFunctions

import random

# Seznam ras k výběru
races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Human", "Tiefling"]

def race_choice():
  random_race = random.choice(races)
  return random_race

# Seznam povolání k výběru
character_classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

def class_choice():
  random_character_class = random.choice(character_classes)
  return random_character_class

levels = [i for i in range(1, 21)]

# Reads the 8 inputs and tries to create a character with them
def read_input_values(values):
  user_name = values["USER_NAME"]
  character_name = values["CHARACTER_NAME"]
  level = values["LEVEL"]
  age = values["AGE"]
  race = values["RACE"]
  character_class = values["CHARACTER_CLASS"]
  is_male_or_female = values["IS_MALE_OR_FEMALE"]
  newbie = values["NEWBIE"]
  could_create_character = dataFunctions.try_to_create_character(user_name, character_name, level, age, race, character_class, is_male_or_female, newbie)
  return could_create_character

# graph = sg.Graph(canvas_size=(10,10), graph_bottom_left=(0,0), graph_top_right=(10,10), key="GRAPH")
  
# Create the character sheet layout
def create_layout():
  return [
    [sg.Text("User name", size=(15,1)), sg.Input(size=25, tooltip="Write your name", key="USER_NAME")],
    [sg.Text("Character name", size=(15,1)), sg.Input(size=25, tooltip="Write your character's name", key="CHARACTER_NAME")],
    [sg.Text("Level", size=(15,1)), sg.Spin(levels, initial_value=1, size=3, readonly=True, tooltip="Select one of the offered options", key="LEVEL")],
    [sg.Text("Age", size=(15,1)), sg.Input(size=4, tooltip="Write your character's age", key="AGE")],
    [sg.Text("Race", size=(15,1)), sg.Combo(races, default_value="Dragonborn", readonly=True, tooltip="Select one of the offered options", key="RACE"), sg.Button("Random race", key="RACE"), sg.Text("And the winner is", size=(15,1)), sg.Text(key="OUT_RACE")],
    [sg.Text("Character class", size=(15,1)), sg.Combo(character_classes, default_value="Barbarian", readonly=True, tooltip="Select one of the offered options", key="CHARACTER_CLASS"), sg.Button("Random class", key="CLASS"), sg.Text("And the winner is", size=(15,1)), sg.Text(key="OUT_CHARACTER_CLASS")],
    [sg.Text("Is male or female?", size=(15,1)), sg.Radio("Male", "gen", key="IS_MALE_OR_FEMALE", default=True), sg.Radio("Female", "gen", key="IS_MALE_OR_FEMALE")],
    [sg.Text("Newbie?", size=(15,1)), sg.Checkbox("Yes", key="NEWBIE")],
    [sg.Cancel(), sg.Button("Save")],
    [sg.StatusBar("This is the statusbar")]
    # [sg.Text("Date of birth"), sg.Input(key="DATE_OF_BIRTH"), sg.CalendarButton("Select date", format='%Y/%m/%d')],
    # sg.Image(r'Warforge2.png', expand_x=True, expand_y=True)
  ]
  
# Nastavím si barevné téma všech oken, kromě té úplně horní lišty záhlaví, ta se nastavuje zvlášť.
sg.theme("DarkBrown5")
# Určím si, aby horní lišta (záhlaví) byla barevně sjednocená s nastaveným tématem oken - pro úplně všechna okna, která si vytvořím/nastavím.
sg.set_options(font=('Arial Bold', 12), use_custom_titlebar=True)
  
# Create character sheet window, display it, and capture user input
def display_sheet():
  character_sheet_layout = create_layout()
  # Mohu si nastavit takto i velikost okna.
  character_sheet_window = sg.Window("New Character Sheet", character_sheet_layout, size=(900, 350), enable_close_attempted_event=True)
  was_save_successful = False

  while True:
    event, values = character_sheet_window.read()
    if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and sg.popup_yes_no("Do you really want to exit?") == 'Yes':
      break
    elif event == sg.WIN_CLOSED or event == "Cancel":
      break
    elif event == "Random race":
      race = random.choice(races)
      character_sheet_window["RACE"].update(value=race)
    elif event == "Random class":
      character_class = random.choice(character_classes)
      character_sheet_window["CHARACTER CLASS"].update(value=character_class)
      # character_sheet_window.refresh()
    elif event == "Save":
      was_save_successful = read_input_values(values)
      if was_save_successful:
        # Nastavím si vyskakovací okno a určím, aby se mi zobrazovalo na topu všech otevřených oken.
        sg.popup_notify("Character saved!")
        break
      else:
        sg.Popup("Could not save character, invalid input(s). Please try again!", keep_on_top=True)
  character_sheet_window.close()
  return was_save_successful