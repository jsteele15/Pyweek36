import pygame
import sys
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
character_list = []
entity_list = []
function_list = [printing]
button_list = [practise_button]




###a function to draw everything to the screen
def Drawing(button_list, function_list):
    
    for i in button_list:
        settings.screen.blit(i.animation_list[i.ind], i.rect)
        i.Pressed(function_list, button_list)


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
            
        if event.type == MOUSEBUTTONUP:
            for i in button_list:
                if i.rect.collidepoint(pos):
                    i.Clicked_Twice = True
    
    ###the actions function goes into every menu loop
    ###the two functions below need to be in every loop
    ###ergo, i've placed them in this function even though 
    ###it doesnt make a huge amount of sense based on what they do
    ###move them if you want
    pygame.display.update()
    settings.clock.tick(60)        