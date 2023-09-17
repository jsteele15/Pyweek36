import pygame
from spritesheet import*

class Characters(SpriteSheet):
    def __init__(self, name, move_points ,image, animation_steps, x_pos, y_pos, x_cut, y_cut, health = 100):
        ###dont need a name really, i just think it would be cool if you could hover over a ship and it gives you a name
        ###maybe we could have a list of generic names in a random list 
        ###and then have a few ships that are "famous" sci fi references
        self.name = name
        
        ###move_points will be its initial tragectory upon being blited, maybe once it gets to a certain point past the screen
        ###it you lose the option to destroy it
        self.move_points = move_points
        
        ###health of ships and meteors, we can have a destruction animation when it falls to zero
        self.health = health

        super().__init__(image, animation_steps, x_pos, y_pos, x_cut, y_cut)
        
    def Draw(self):
        ###we should also stop blitting it once it gets off screen to help with performance
        if self.health >= 1:
            settings.screen.blit(self.animation_list[self.ind], self.rect)
            
        else:
            pass
            ###it needs to show a destroyed animation first instead of just being unblitted
            ###but that a future issue to work out
            ###maybe the character has bool like "death animation"
            ###and it runs on a timer, then gets unblitted idk
            
    def Move(self):
        ###not sure how best to do this yet, maybe work out which direction the ship starts at
        ###then decide whether to add or takeaway movment ect
        ###for now im just going to put +move_points
        if self.health >= 1:
            self.rect.move_ip(self.move_points, 0)
            
        else:
            pass

####some ships to see whats working 
practise_ship = Characters("Star Bug", 5, main_char_im, 3, 200, 200, 30, 52)




###a class for the blobs        
class Entity(SpriteSheet):
    def __init__(self, image, animation_steps, x_pos, y_pos, x_cut, y_cut, Clicked = False):
        ###this works out if the blob is currently selected
        self.Clicked = Clicked
        super().__init__(image, animation_steps, x_pos, y_pos, x_cut, y_cut)
        
    
    def Draw(self):
        settings.screen.blit(self.animation_list[self.ind], self.rect)
        
    def Move(self, pos):
        ###if we use pygame.mouse.get_pos it returns a tuple, it might not work now that i think about it,
        ###itll probably have to be ((pos[0] - self.x_pos), pos[1] - self.y_pos) instead of what ive just written
        ###will need to move based on being clicked 
        if self.Clicked == True:
            self.rect.move_ip(pos[0], pos[1])
        else:
            pass
        
    def Gravity(self, character_list):
        ###figiure out the location of the enitiy and the characters relative to each other
        ###then change the characters movment trajectory based on closeness
        for i in character_list:
            change = i.x_pos - self.x_pos
            if i.x_pos - self.x_pos == range(0, 100):
                i.move_points += change
                
        ##############################this formula definatly doesnt work, i havnt had a chance to test it        
        ##############################i just wrote this as an example, refinment can come later

practise_entity = Entity(main_char_im, 3, 300, 250, 30, 52)

class BackGround(SpriteSheet):
    pass
    ###probably dont need a spritesheet for the background stuff
    ###might not even need a class
    #def __init__(self, image, animation_steps, x_pos, y_pos, x_cut, y_cut):
        
        #super().__init__(image, animation_steps, x_pos, y_pos, x_cut, y_cut)