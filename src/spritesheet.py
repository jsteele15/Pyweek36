from settings import*
from pathlib import Path

class SpriteSheet:
    def __init__(self, image, animation_steps, x_pos, y_pos, x_cut, y_cut):
        self.sheet = image
        self.animation_list = []
        self.animation_steps = animation_steps
        
        ###ind is used to define what image in the animation_list is used
        self.ind = 0
        
        ### an x and y pos for setting the location of the rect and stuff
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        ###this defines the size of the smaller sub image to be cut out of the picture
        self.x_cut = x_cut
        self.y_cut = y_cut
        
        ###the colour used in the background of sprites that gets cut out to make it transparent
        BLACK_GRE = (11, 158, 3)
        
        for x in range(self.animation_steps):
            self.animation_list.append(self.get_image(x, self.x_cut, self.y_cut, BLACK_GRE))
            
        for i in self.animation_list:
            self.rect = i.get_rect(topleft = (self.x_pos, self.y_pos))
            
    def get_image(self, frame, width, height, colour):
        image = pygame.Surface((width, height))
        image.blit(self.sheet, (0, 0), ((frame * width), 0 , width, height))
        image.set_colorkey(colour)
        return image
        

####an example of how to make an object of the sprite class        
###main_char_im = pygame.image.load(Path(r"../res/Fall_sprite_sheet.png")).convert_alpha()
#main_char = SpriteSheet(main_char_im, 3, 600, 100, 30, 52)  


#change the ind to change what happens
#settings.screen.blit(self.animation_list[self.ind], self.rect) 