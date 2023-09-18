import pygame
from spritesheet import*
from settings import*
from pathlib import Path

class Buttons(SpriteSheet):
    def __init__(self, Function_Reference, image_path: str, pos: Vec2):
        ###we can give the button an int 0, 1, 2 ect. The use that later when it gets pressed
        ###to call methods from a list
        
        self.Function_Reference = Function_Reference
        self.Clicked_Once = False
        self.Clicked_Twice = False
        self.rect = pygame.Rect(pos.x, pos.y, 100, 40)
        
        ###this button class inherits from sprites sheet, this will allow us to make the buttons
        ###squishy?
        super().__init__(pygame.image.load(Path(image_path)), 2, pos.x, pos.y, 100, 40)

     
    def pressed(self, func_list, settings):        
        ###need to remember that one is the down possition of the button
            
        if self.Clicked_Once == True and self.Clicked_Twice == True:
            func_list[self.Function_Reference](settings)
                

    def draw(self, screen):
        screen.blit(self.animation_list[self.ind], self.rect)
        
        
    def Reset(self):
        #a method to reset the functionality of buttons
        self.Clicked_Once = False
        



###actual buttons i think well need, need to remember to change the function reference
"""
###to restart whatever level your on
rb = pygame.image.load(Path(r"../res/restart.png")).convert_alpha()
restart_button = Buttons(6, rb, 1, (settings.S_WIDTH - 100), (settings.S_HEIGHT - 100), 40, 40)

###when youve finished the set up phase
pb = pygame.image.load(Path(r"../res/play_but.png")).convert_alpha()
play_button = Buttons(1, pb, 2, (settings.S_WIDTH - 100), (settings.S_HEIGHT - 200), 100, 40)

###exit button
eb = pygame.image.load(Path(r"../res/exit.png")).convert_alpha()
exit_button = Buttons(7, eb, 1, (settings.S_WIDTH - 100), (settings.S_HEIGHT - 100), 40, 40)

###level one button
L1b = pygame.image.load(Path(r"../res/lv1.png")).convert_alpha()
level_1_button = Buttons(2, L1b, 1, (settings.S_WIDTH - 100), (settings.S_HEIGHT - 200), 100, 40)

###level two button
L2b = pygame.image.load(Path(r"../res/lv2.png")).convert_alpha()
level_2_button = Buttons(3, L2b, 1, (settings.S_WIDTH - 100), (settings.S_HEIGHT - 150), 100, 40)

###level three button
L3b = pygame.image.load(Path(r"../res/lv3.png")).convert_alpha()
level_3_button = Buttons(4, L3b, 1, (settings.S_WIDTH - 100), (settings.S_HEIGHT - 100), 100, 40)

###ready button, after youve finished setting everything up
readb = pygame.image.load(Path(r"../res/ready.png")).convert_alpha()
ready_button = Buttons(5, readb, 1, (settings.S_WIDTH - 100), (settings.S_HEIGHT - 200), 40, 40)



#save, load button, idk, stretch goals init
#save_button = Buttons(0, main_char_im, 3, 100, 100, 30, 52)
#load_button = Buttons(0, main_char_im, 3, 100, 100, 30, 52)

"""
class Text():
    def __init__(self, size):
        self.size = size
        self.game_font = pygame.font.Font(Path(r'../res/Audiowide-Regular.ttf'), self.size)
        
    def Draw(self, *tuple_of_elements):
        #(text, colour, x, y)
        list_of_tuples = [*tuple_of_elements]
        
        lengh_of_line = 0
        
        for i in range(len(list_of_tuples)):
            text_surface = self.game_font.render(list_of_tuples[i][0], False, (list_of_tuples[i][1]))
            
            text_rect = text_surface.get_rect(topleft = ((list_of_tuples[i][2]+lengh_of_line*(i)), list_of_tuples[i][3]))
            
            lengh_of_line = text_surface.get_width()
            
        ###these tuples will contain all the elements needed to blit different aspects of the ui; also maybe a number
        ###at the begining to decide if its going to be a status bar of a simple number text ect

text = Text(200)

###text.Draw(f"Number of Kills: {0}", settings.RED, 30, 30) example of use

