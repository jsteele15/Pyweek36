import pygame

pygame.init()

class Settings():
    #colours to use for debugging
    GREEN = (130, 255, 130)
    RED = (255, 0, 0)
    
    #screen
    #height and width are just temp numbers to get the window working
    HEIGHT = 400
    WIDTH = 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    #clock
    clock = pygame.time.Clock()
    
    #running bool
    Running = True
        
settings = Settings()