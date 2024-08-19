# Characters table, program entry point

import PySimpleGUI as sg

import dataFunctions

import characterSheet

# Characters table column titles
table_headings = [
  "User name", "Character name", "Level", "Age", "Race", "Character class", "Is male or female?", "Newbie?"
]

# Characters table data
table_data = dataFunctions.convert_characters_to_table_data()
# Add new character button pressed, display character sheet
def press_add_character_button(characters_window):
  was_save_successful = characterSheet.display_sheet()
  if was_save_successful:
    table_data = dataFunctions.convert_characters_to_table_data()
    characters_window["CHARACTERS_TABLE"].update(values=table_data)
    
# Characters window stuff
characters_window_layout = [
  [sg.Text("All Character Data"), sg.Button("Add new character")],
  [sg.Table(headings=table_headings, values=table_data, auto_size_columns=True, key="CHARACTERS_TABLE")]
]

characters_window = sg.Window("Characters List", characters_window_layout, size=(900,300), enable_close_attempted_event=True)
# Display character window
while True:
  event, values = characters_window.read()
  if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and sg.popup_yes_no("Do you really want to exit?") == 'Yes':
    break
  elif event == sg.WIN_CLOSED:
    break
  elif event == "Add new character":
    press_add_character_button(characters_window)
characters_window.close()