import pygame
from music_and_sound import*
from spritesheet import SpriteSheet
from copy import deepcopy
pygame.init()


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

class Mouse:
    def __init__(self) -> None:
        self.has_dm = False
        self.pos = Vec2(0,0)
        self.dm = SpriteSheet(pygame.image.load(r"../res/dark_matter.png"), 1, self.pos.x, self.pos.y, 50, 50, 0)
        self.rect = pygame.Rect(self.pos.x, self.pos.y, 50, 50)

    def draw(self, screen):
        if self.has_dm:
            screen.blit(self.dm.animation_list[self.dm.ind], self.rect)

class Settings():
    #colours to use for debugging
    GREEN = (130, 255, 130)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    
    #screen
    #height and width are just temp numbers to get the window working
    HEIGHT = 600
    WIDTH = 800

    PAUSED = True
    started = False

    level_list = []
    current_level = 2
    
    ent_list = []
    button_list = []
    
    ####level 4 attributes
    FIRST_SHIP = False
    SECOND_SHIP = False


    ###level 9 attributes
    FAILURE = False

    trail_count = 0
    trail_points = []
    prev_trail_points = []

    
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
    
    mouse = Mouse()

    #if its zero its a menu, if its a level its a 1
    ###could be used to split up the draw into two sections
    level_or_menu = 0
    
    ###to go into the levels to determin if its the setup stage or not
    #level_started = False

    def load_level(self):
        self.started = False
        self.PAUSED = True
        self.prev_trail_points = deepcopy(self.trail_points)
        self.trail_points = []
        self.ent_list = deepcopy(self.level_list[self.current_level].ent_list)
        self.button_list = deepcopy(self.level_list[self.current_level].button_list)
        for ent in self.ent_list:
                self.trail_points.append([])
                self.prev_trail_points.append([])

        

        
G_Const = 0.000006 #constant to multipy gravity. Increasing makes grav stronger and vice versa

