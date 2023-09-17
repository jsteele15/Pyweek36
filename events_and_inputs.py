import pygame
import sys
from levels import*
from characters_and_backgrounds import*
from ui import*
from pygame.locals import*
from settings import*


###a practice function to make sure the list reference thing is working
def printing(button_list):
    print("hello world")
    for i in button_list:
        i.Reset()

####a list of functions and buttons that act upon each other
###we can put all the ships and stuff in this character list and then act upon them
character_list = [practise_ship]

entity_list = [practise_entity]

function_list = [printing, Level_Select, Level_One, Level_Two, Level_Three]

button_list = [practise_button]

menu_button_list = [play_button, exit_button]

menu_level_select_list = [level_1_button, level_2_button, level_3_button]



###a function to draw everything to the screen
def Drawing():
    settings.screen.fill(settings.RED)
    pos = pygame.mouse.get_pos()
    for i in button_list:
        settings.screen.blit(i.animation_list[i.ind], i.rect)
        i.Pressed(function_list, button_list, menu_level_select_list, Drawing, Actions)
    
    if settings.level_or_menu == 1:    
        ###this draws what in the character list, probably best if this works on a timer
        ###that way one ship comes at a time
        for i in character_list:
            i.Draw()
            i.Move()
            
        for i in entity_list:
            i.Draw()
            i.Move(pos)
            i.Gravity(character_list)



###gets the events like button presses
def Actions(button_list):
    pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            settings.Running = False
            sys.exit()
            
        if event.type == KEYDOWN:
            pass
            
        if event.type == KEYUP:
            pass
            
        if event.type == MOUSEBUTTONDOWN:
            for i in button_list:
                if i.rect.collidepoint(pos):
                    i.Clicked_Once = True
                    
            for i in entity_list:
                if i.rect.collidepoint(pos):
                    i.Clicked = True
                    print(f"clicked {i.Clicked}")
            
        if event.type == MOUSEBUTTONUP:
            for i in button_list:
                if i.rect.collidepoint(pos):
                    i.Clicked_Twice = True
                else:
                    i.Clicked_Once = False
                    
            for i in entity_list:
                i.Clicked = False
    
    ###the actions function goes into every menu loop
    ###the two functions below need to be in every loop
    ###ergo, i've placed them in this function even though 
    ###it doesnt make a huge amount of sense based on what they do
    ###move them if you want
    pygame.display.update()
    settings.clock.tick(60)        