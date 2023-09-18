import pygame
from pathlib import Path
from spritesheet import*

class Characters(SpriteSheet):
    def __init__(self, direction, name, rotate, move_points ,image, animation_steps, x_pos, y_pos, x_cut, y_cut, health = 100):
        self.direction = direction
        
        ###dont need a name really, i just think it would be cool if you could hover over a ship and it gives you a name
        ###maybe we could have a list of generic names in a random list 
        ###and then have a few ships that are "famous" sci fi references
        self.name = name
        
        ###an initial rotation factor
        self.rotate = rotate
        ###move_points will be its initial tragectory upon being blited, maybe once it gets to a certain point past the screen
        ###it you lose the option to destroy it
        self.move_points = move_points
        
        ###health of ships and meteors, we can have a destruction animation when it falls to zero
        self.health = health
        
        super().__init__(image, animation_steps, x_pos, y_pos, x_cut, y_cut)
        
        self.explosion_sprite = SpriteSheet(exp_im, 114, self.x_pos, self.y_pos, 100, 100)
        self.exp_list = [self.explosion_sprite]
        
    def Draw(self, obstacle_list, character_list):
        ###we should also stop blitting it once it gets off screen to help with performance
        #if settings.level_started == True:
        ###this changes the rotation of the image, right now it just does it before
        rotate_im = pygame.transform.rotate(self.animation_list[self.ind], self.rotate)
        for i in obstacle_list:
            if i.rect.colliderect(self.rect):
                self.health = 0
        
        for i in character_list:
            if i.rect == self.rect:
                pass
            elif i.rect.colliderect(self.rect):
                self.health = 0
        
        if self.health >= 1:
            settings.screen.blit(rotate_im, self.rect)
            
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
        if self.direction == "left":
            if self.health >= 1:
                self.rect.move_ip(self.move_points, 0)
                
        if self.direction == "up":
            if self.health >= 1:
                self.rect.move_ip(0, -self.move_points)

####some ships to see whats working 
ship_temp = pygame.image.load(Path(r"../res/ship.png")).convert_alpha()
practise_ship = Characters("left", "Star Bug", 270, 1, ship_temp, 1, 200, 200, 50, 50)

enterprise = Characters("up", "Star Bug", 0, 1, ship_temp, 1, 300, 300, 50, 50)



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
            #self.x_pos = pos[0]
            #self.y_pos = pos[1]
            ##yeah, this doesnt work as intended, it does move though
            self.rect.move_ip((pos[0]-self.x_pos), (pos[1]-self.y_pos))
            
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

dm = pygame.image.load(Path(r"../res/dm.png")).convert_alpha()
practise_entity = Entity(dm, 1, 150, 150, 100, 100)


###an obstacles class for ships to collide into
class Obstacle(SpriteSheet):
    def __init__(self, image, animation_steps, x_pos, y_pos, x_cut, y_cut):
        
        super().__init__(image, animation_steps, x_pos, y_pos, x_cut, y_cut)
    
    def Draw(self):
        settings.screen.blit(self.animation_list[self.ind], self.rect)
        
px = pygame.image.load(Path(r"../res/px.png")).convert_alpha()
planetx = Entity(px, 1, 500, 200, 120, 120)


class BackGround(SpriteSheet):
    pass
    ###probably dont need a spritesheet for the background stuff
    ###might not even need a class
    #def __init__(self, image, animation_steps, x_pos, y_pos, x_cut, y_cut):
        
        #super().__init__(image, animation_steps, x_pos, y_pos, x_cut, y_cut)