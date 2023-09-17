import pygame
from settings import*

def Level_Select(button_list, menu_level_select_list, Drawing, Actions):
    #tells the game its a menu
    settings.level_or_menu = 1
    
    button_list.clear()
    for i in menu_level_select_list:
        button_list.append(i)
    
    while settings.Running:
        Drawing()
        Actions(Drawing)

def Level_One(button_list, menu_level_select_list, Drawing, Actions):
    settings.level_or_menu = 1
    while settings.Running:
        Drawing()
        Actions(Drawing)
    
def Level_Two():
    settings.level_or_menu = 1
    while settings.Running:
        Drawing()
        Actions(Drawing)
    
def Level_Three():
    settings.level_or_menu = 1
    while settings.Running:
        Drawing()
        Actions(Drawing)