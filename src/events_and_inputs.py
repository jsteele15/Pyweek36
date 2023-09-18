import pygame
import sys
from pathlib import Path
from levels import*
from characters_and_backgrounds import*

from pygame.locals import*
from settings import Settings


def ready_func(settings):
    ###a function to start the game, after the pieces have been placed
    settings.PAUSED = False
    settings.started = True

def restart_func(settings):
    ###a function to restart a level if your not liking how its looking
    settings.level_started = False
    pass
    
    
def exit_func(settings):
    ###a function that allows you to exit the program, all these arguments i've fed in are pointless
    settings.Running = False
    sys.exit()

func_list = [ready_func, restart_func, exit_func]


###a practice function to make sure the list reference thing is working
def printing(button_list):
    print("hello world")
    for i in button_list:
        i.Reset()

####a list of functions and buttons that act upon each other
###we can put all the ships and stuff in this character list and then act upon them
#character_list = [practise_ship, enterprise]


button_list = []

#menu_button_list = [play_button, exit_button]

#menu_level_select_list = [level_1_button, level_2_button, level_3_button]

###the buttons for when youre in the level
###right now the buttons dont do anything
#on_map_button_list = [ready_button, restart_button]

###the all button list, used to reset the functionality of every button upon going to a new level or menu
#all_button_list = [ready_button, restart_button , level_1_button, level_2_button, level_3_button, play_button, exit_button]

###a list for all the obstacles
#obstacle_list = [planetx]

###list of texts
#text_list = [text]

###a function to draw everything to the screen
def Drawing():
    ##temp until weve got an actual background image
    settings.screen.fill(settings.BLACK)
    pos = pygame.mouse.get_pos()
    
    #for i in button_list:
     #   settings.screen.blit(i.animation_list[i.ind], i.rect)
      #  i.Pressed(function_list, button_list, menu_level_select_list, Drawing, Actions, on_map_button_list)
    
    if settings.level_or_menu == 1:  
        for i in text_list:
            #supposed to be a list of tupples
            ##proof of concept
            #not actually drawing right now for some reason
            i.Draw((f"Number of Kills: 0", settings.RED, 500, 500))
            
        ###this draws what in the character list, probably best if this works on a timer
        ###that way one ship comes at a time
        
        for ent in ent_list:
            i.draw()



###gets the events like button presses
def actions(button_list, settings):
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
                    """
            for i in entity_list:
                if i.rect.collidepoint(pos):
                    i.Clicked = True
                    print(f"clicked {i.Clicked}")
            """
        if event.type == MOUSEBUTTONUP:
            for i in button_list:
                if i.rect.collidepoint(pos):
                    i.Clicked_Twice = True
                    i.pressed(func_list, settings)
                    i.Clicked_Once = False
                    i.Clicked_Twice = False
                    
    
    ###the actions function goes into every menu loop
    ###the two functions below need to be in every loop
    ###ergo, i've placed them in this function even though 
    ###it doesnt make a huge amount of sense based on what they do
    ###move them if you want
    
    #pygame.display.update()
    #settings.clock.tick(60)        