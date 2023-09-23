import pygame
from spritesheet import*
from settings import*
from pathlib import Path

class Buttons(SpriteSheet):
    def __init__(self, Function_Reference, image_path: str, pos: Vec2, visible: bool = True, size_x = 120, size_y = 40, ind = 0, second_ind = 0, dm_but = False):
        ###we can give the button an int 0, 1, 2 ect. The use that later when it gets pressed
        ###to call methods from a list
        
        self.Function_Reference = Function_Reference
        self.visible = visible
        self.Clicked_Once = False
        self.Clicked_Twice = False
        self.rect = pygame.Rect(pos.x, pos.y, size_x, size_y)
        self.second_ind = second_ind
        self.dm_but = dm_but
        
        ###this button class inherits from sprites sheet, this will allow us to make the buttons
        ###squishy?
        super().__init__(pygame.image.load(Path(image_path)), 6, pos.x, pos.y, size_x, size_y, ind)

     
    def pressed(self, func_list, settings):        
        ###need to remember that one is the down possition of the button
            
        if self.Clicked_Once == True and self.Clicked_Twice == True:
            if self.visible == True:
                func_list[self.Function_Reference](self, settings)
                

    def draw(self, screen, settings):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            new_ind = self.second_ind
        else:
            new_ind = self.ind
        
        if self.visible:
            if self.dm_but == False:
                screen.blit(self.animation_list[new_ind], self.rect)
            if self.dm_but == True:
                if settings.started == False:
                    screen.blit(self.animation_list[new_ind], self.rect)
                if settings.started == True:
                    pass
        
        
    def Reset(self):
        #a method to reset the functionality of buttons
        self.Clicked_Once = False
        



class Text():
    def __init__(self, size, level_text, x, y, colour = (255, 255, 255)):
        self.size = size
        self.level_text = level_text
        self.x = x
        self.y = y
        self.colour = colour
        self.game_font = pygame.font.Font(Path(r'../res/Audiowide-Regular.ttf'), self.size)
        
    def draw(self, screen):
        #(text, colour, x, y)
        text_surface = self.game_font.render(self.level_text, False, self.colour)
        text2_surface = self.game_font.render(self.level_text, False, (63, 63, 116))
        
        screen.blit(text2_surface, (self.x, self.y))
        screen.blit(text_surface, (self.x +2, self.y+2))
        
        
