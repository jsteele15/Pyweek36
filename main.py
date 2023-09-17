import pygame
from events_and_inputs import*

def Start_Menu():
    #tells the game its a menu
    settings.level_or_menu = 0
    #removes any previous buttons and puts the start buttons in
    button_list.clear()
    for i in menu_button_list:
        button_list.append(i)
    
    print(settings.S_WIDTH)
    while settings.Running:
        Drawing()
        Actions(button_list)

    
if __name__ == "__main__":
    Start_Menu()