import pygame

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
    
    if __name__ == "__main__": #temporary before I can remove the settings =Settings() below without breaking everything
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        ###THIS SETS IT TO FULLSCREEN, PROBABLY NEEDS TO BE AN ON OFF THING, BUT I DONT WANT TO DEAL WITH IT RN
        #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        ##to find the relative size of the screen
        S_WIDTH = pygame.display.get_surface().get_width()
        S_HEIGHT = pygame.display.get_surface().get_height()
    else:
        S_WIDTH = WIDTH 
        S_HEIGHT = HEIGHT
    
    #clock
    clock = pygame.time.Clock()
    
    #running bool
    Running = True
    
    #if its zero its a menu, if its a level its a 1
    ###could be used to split up the draw into two sections
    level_or_menu = 0
    
    ###to go into the levels to determin if its the setup stage or not
    #level_started = False

class Vec2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y =  y

    def __add__(self, o):
        return Vec2(self.x + o.x, self.y + o.y)
    
    def __sub__(self, o):
        return Vec2(self.x - o.x, self.y - o.y)

    def __mul__(self, o):
        if type(o) is Vec2:
            return Vec2(self.x*o.x, self.y*o.y)
        else:
            return Vec2(self.x*o, self.y*o)
        
    def __div__(self, o):
        if type(o) is Vec2:
            return Vec2(self.x/o.x, self.y/o.y)
        else:
            return Vec2(self.x/o, self.y/o)
        
G_Const = 0.001 #constant to multipy gravity. Increasing makes grav stronger and vice versa

