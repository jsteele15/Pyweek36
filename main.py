import pygame
from events_and_inputs import*

def Start_Menu():
    while settings.Running:
        Drawing(button_list, function_list)
        Actions(button_list)
    
def Level_One():
    while settings.Running:
        Actions()
    
def Level_Two():
    while settings.Running:
        Actions()
    
def Level_Three():
    while settings.Running:
        Actions()
    
if __name__ == "__main__":
    Start_Menu()