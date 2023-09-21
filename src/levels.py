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

def win_cond3(level, settings):
    if settings.ent_list[0].rect.colliderect(settings.ent_list[1].rect):
        print("yes")
        return True
    return False
    
def win_cond4(level, settings):
    if settings.ent_list[0].rect.colliderect(settings.ent_list[2].rect):
        settings.FIRST_SHIP = True
        
    if settings.ent_list[1].rect.colliderect(settings.ent_list[2].rect):
        settings.SECOND_SHIP = True
    if settings.FIRST_SHIP == True and settings.SECOND_SHIP == True:
        print("dsafnugniu")
        return True
        
    return False

def win_cond5(level, settings):
    if settings.ent_list[0].rect.y <= 0 or settings.ent_list[0].rect.x <= 0:
        return True
    return False

def win_cond6(level, settings):
    if settings.ent_list[0].rect.colliderect(settings.ent_list[1].rect):
        return True
    return False

def win_cond7(level, settings):
    dead_list = []
    for i in range(len(settings.ent_list)):
        
        if settings.ent_list[i].is_alive == False:
            dead_list.append(1)
    
    if len(dead_list) >= 6:
        return True
    return False

def win_cond8(level, settings):
    pass






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