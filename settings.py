import pygame

pygame.init()

class Settings():
    #colours to use for debugging
    GREEN = (130, 255, 130)
    RED = (255, 0, 0)
    
    #screen
    #height and width are just temp numbers to get the window working
    HEIGHT = 600
    WIDTH = 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    #clock
    clock = pygame.time.Clock()
    
    #running bool
    Running = True
    
    #if its zero its a menu, if its a level its a 1
    ###could be used to split up the draw into two sections
    level_or_menu = 0
    
settings = Settings()