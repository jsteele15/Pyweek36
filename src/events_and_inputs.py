import pygame
import sys
from pathlib import Path
from levels import*
from characters_and_backgrounds import*

from pygame.locals import*
from settings import Settings


def ready_func(button, settings):
    ###a function to start the game, after the pieces have been placed
    button.visible = False
    settings.PAUSED = False
    settings.started = True

def restart_func(button, settings):
    ###a function to restart a level if your not liking how its looking
    
    settings.load_level()
    
    
def exit_func(button, settings):
    ###a function that allows you to exit the program, all these arguments i've fed in are pointless
    settings.Running = False
    sys.exit()

def pickup_dm(button, settings):
    settings.mouse.has_dm = True
    button.visible = False

def start_game(button, settings):
    settings.PLAY = True
    settings.current_level += 1
    settings.load_level()

def skip(button, settings):
    settings.current_level += 1
    settings.load_level()

func_list = [ready_func, restart_func, exit_func, pickup_dm, start_game, skip]





###gets the events like button presses
def actions(ent_list, button_list, settings):
    pos = pygame.mouse.get_pos()

    settings.mouse.rect.x = pos[0]
    settings.mouse.rect.y = pos[1]
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            settings.Running = False
            sys.exit()
            
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                settings.Running = False
                sys.exit()
                
            if event.key == K_f:
                ###sets it to full screen, probably need to be able to undo that
                settings.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            
            if event.key == K_r:
                settings.current_level = 0
                settings.load_level()
            
        if event.type == KEYUP:
            pass
            
        if event.type == MOUSEBUTTONDOWN:
            for i in button_list:
                if i.rect.collidepoint(pos):
                    
                    i.Clicked_Once = True
                else:
                    if settings.mouse.has_dm == True:
                        ent_list.append(DarkMatter(Vec2(pos[0], pos[1])))
                        settings.mouse.has_dm = False
            
        if event.type == MOUSEBUTTONUP:
            for i in button_list:
                if i.rect.collidepoint(pos):
                    i.Clicked_Twice = True
                    i.pressed(func_list, settings)
                    i.Clicked_Once = False
                    i.Clicked_Twice = False
                    
      