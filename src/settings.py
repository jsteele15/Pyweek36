import pygame
from music_and_sound import*
pygame.init()

class Settings():
    #colours to use for debugging
    GREEN = (130, 255, 130)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    
    #screen
    #height and width are just temp numbers to get the window working
    HEIGHT = 600
    WIDTH = 600
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    ###THIS SETS IT TO FULLSCREEN, PROBABLY NEEDS TO BE AN ON OFF THING, BUT I DONT WANT TO DEAL WITH IT RN
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    ##to find the relative size of the screen
    S_WIDTH = pygame.display.get_surface().get_width()
    S_HEIGHT = pygame.display.get_surface().get_height()
    
    #clock
    clock = pygame.time.Clock()
    
    #running bool
    Running = True
    
    #if its zero its a menu, if its a level its a 1
    ###could be used to split up the draw into two sections
    level_or_menu = 0
    
    ###to go into the levels to determin if its the setup stage or not
    #level_started = False
    
    
settings = Settings()