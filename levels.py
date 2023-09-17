import pygame
from settings import*

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