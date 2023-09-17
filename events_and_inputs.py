import pygame
import sys
from levels import*
from characters_and_backgrounds import*
from ui import*
from pygame.locals import*
from settings import*


def Ready_Function():
    ###a function to start the game, after the pieces have been placed
    pass

def Restart_Function():
    ###a function to restart a level if your not liking how its looking
    pass
    
def Exit_Function(function_list, button_list, menu_level_select_list, Drawing, Actions, on_map_button_list):
    ###a function that allows you to exit the program, all these arguments i've fed in are pointless
    settings.Running = False
    sys.exit()

###a practice function to make sure the list reference thing is working
def printing(button_list):
    print("hello world")
    for i in button_list:
        i.Reset()

####a list of functions and buttons that act upon each other
###we can put all the ships and stuff in this character list and then act upon them
character_list = [practise_ship, enterprise]

entity_list = [practise_entity]

function_list = [printing, Level_Select, Level_One, Level_Two, Level_Three, Ready_Function, Restart_Function, Exit_Function]

button_list = [practise_button]

menu_button_list = [play_button, exit_button]

menu_level_select_list = [level_1_button, level_2_button, level_3_button]

###the buttons for when youre in the level
###right now the buttons dont do anything
on_map_button_list = [ready_button, restart_button]

###the all button list, used to reset the functionality of every button upon going to a new level or menu
all_button_list = [ready_button, restart_button , level_1_button, level_2_button, level_3_button, play_button, exit_button]

###a list for all the obstacles
obstacle_list = [planetx]

###list of texts
text_list = [text]



###a function to draw everything to the screen
def Drawing():
    ##temp until weve got an actual background image
    settings.screen.fill(settings.BLACK)
    pos = pygame.mouse.get_pos()
    
    for i in button_list:
        settings.screen.blit(i.animation_list[i.ind], i.rect)
        i.Pressed(function_list, button_list, menu_level_select_list, Drawing, Actions, on_map_button_list)
    
    if settings.level_or_menu == 1:  
        for i in text_list:
            i.Draw(f"Number of Kills: {0}", settings.RED, 30, 30)
        ###this draws what in the character list, probably best if this works on a timer
        ###that way one ship comes at a time
        for i in character_list:
            ####we should put this draw on a timer to allow ships to come out one at a time
            i.Draw(obstacle_list, character_list)
            i.Move()
            
        for i in entity_list:
            i.Draw()
            i.Move(pos)
            i.Gravity(character_list)
            
        for i in obstacle_list:
            i.Draw()



###gets the events like button presses
def Actions(button_list):
    pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            settings.Running = False
            sys.exit()
            
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                settings.Running = False
                sys.exit()
                
            if event.key == K_p:
                ###sets it to full screen, probably need to be able to undo that
                settings.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            
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