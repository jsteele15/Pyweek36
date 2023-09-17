import pygame
from spritesheet import*
from settings import*

class Buttons(SpriteSheet):
    def __init__(self, Function_Reference, image, animation_steps, x_pos, y_pos, x_cut, y_cut, Clicked_Once = False, Clicked_Twice = False):
        ###we can give the button an int 0, 1, 2 ect. The use that later when it gets pressed
        ###to call methods from a list
        
        self.Function_Reference = Function_Reference
        self.Clicked_Once = False
        self.Clicked_Twice = False
        
        ###this button class inherits from sprites sheet, this will allow us to make the buttons
        ###squishy?
        super().__init__(image, animation_steps, x_pos, y_pos, x_cut, y_cut)
    
    def Pressed(self, function_list, *args):
        ###takes unlimited args to feed into whichever function it uses
        
        ###need to remember that one is the down possition of the button
            
        if self.Clicked_Once == True and self.Clicked_Twice == True:
            function_list[self.Function_Reference](*args)
        
    def Reset(self):
        #a method to reset the functionality of buttons
        self.Clicked_Once = False
        

###this is just a test to see if this works
practise_button = Buttons(0, main_char_im, 3, 100, 100, 30, 52)

