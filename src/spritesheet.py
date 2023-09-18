from settings import*
from pathlib import Path

class SpriteSheet:
    def __init__(self, image, animation_steps, x_pos, y_pos, x_cut, y_cut):
        self.sheet = image
        self.animation_list = []
        self.animation_steps = animation_steps
        
        ###ind is used to define what image in the animation_list is used
        self.ind = 0
        
        ###this defines the size of the smaller sub image to be cut out of the picture
        self.x_cut = x_cut
        self.y_cut = y_cut
        
        ###the colour used in the background of sprites that gets cut out to make it transparent
        BLACK_GRE = (11, 158, 3)
        
        for x in range(self.animation_steps):
            self.animation_list.append(self.get_image(x, self.x_cut, self.y_cut, BLACK_GRE))
            
            
    def get_image(self, frame, width, height, colour):
        image = pygame.Surface((width, height))
        image.blit(self.sheet, (0, 0), ((frame * width), 0 , width, height))
        image.set_colorkey(colour)
        return image
        

####an example of how to make an object of the sprite class        
#main_char = SpriteSheet(main_char_im, 3, 600, 100, 30, 52)  
#exp_im = pygame.image.load(Path(r"../res/explosion.png")).convert_alpha()


#change the ind to change what happens
#settings.screen.blit(self.animation_list[self.ind], self.rect) 



################################################################################################
### i popped the first bit in here in the spritesheet for characters,
###so that it blows up on the spot of the crash
"""
explosion_sprite = SpriteSheet(exp_im, 114, x_pos, y_pos, 100, 100)
exp_list = [explosion_sprite]


if i.health <= 0:
    for e in i.exp_list:
        if e.ind <=112:
            i.explosion_sprite.ind += 1
            settings.screen.blit(e.animation_list[int(e.ind)], e.rect)

"""    
###the second bit i put in the draw method to activate when a ship loses its health            