import pygame
from settings import*

class Level:
    def __init__(self, button_list, ent_list, win_cond) -> None:
        self.button_list = button_list
        self.ent_list = ent_list
        self.win_cond = win_cond

def win_cond1(level, settings):
    if settings.ent_list[0].is_alive == False:
        return True
    return False

def win_cond2(level, settings):
    if settings.ent_list[0].rect.x >= (settings.ent_list[1].rect.x + 200):
        if settings.ent_list[0].is_alive == True:
            return True
    return False



def Level_Select(function_list, button_list, menu_level_select_list, Drawing, Actions, on_map_button_list):
    #tells the game its a menu
    settings.level_or_menu = 0
    
    button_list.clear()
    for i in menu_level_select_list:
        button_list.append(i)
    
    while settings.Running:
        Drawing()
        Actions(button_list)


def Level_One(function_list, button_list, menu_level_select_list, Drawing, Actions, on_map_button_list):
    settings.level_or_menu = 1
    
    button_list.clear()
    for i in on_map_button_list:
        button_list.append(i)
        
    while settings.Running:
        Drawing()
        Actions(button_list)

    
def Level_Two(function_list, button_list, menu_level_select_list, Drawing, Actions, on_map_button_list):
    settings.level_or_menu = 1
    
    button_list.clear()
    for i in on_map_button_list:
        button_list.append(i)
        
    while settings.Running:
        Drawing()
        Actions(button_list)
   
   
def Level_Three(function_list, button_list, menu_level_select_list, Drawing, Actions, on_map_button_list):
    settings.level_or_menu = 1
    
    button_list.clear()
    for i in on_map_button_list:
        button_list.append(i)
        
    while settings.Running:
        Drawing()
        Actions(button_list)