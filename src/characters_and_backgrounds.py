import pygame
from pathlib import Path
from spritesheet import SpriteSheet
from settings import Vec2, G_Const
from math import sqrt, atan, degrees

class Ent:
    ent_count = 0
    def __init__(self, image_path: str,  size: Vec2, 
                 pos: Vec2, vel: Vec2, mass:int , angle: int = 0, thrust = Vec2(0,0), hitoff = Vec2(1,1), can_move = True, animation_steps: int = 1):
        self.rect = pygame.Rect(pos.x, pos.y, size.x, size.y)
        self.hitoff = hitoff
        self.hitbox = pygame.Rect(pos.x+hitoff.x, pos.y+hitoff.y, size.x - hitoff.x*2, size.y - hitoff.y*2)
        self.pos = pos
        self.angle = angle
        self.prev_angle = angle
        self.vel = vel
        self.mass = mass
        self.is_alive = True
        self.is_collidable = True
        self.is_invincible = True
        self.thrust = thrust
        self.can_move = can_move

        self.ID = Ent.ent_count
        Ent.ent_count += 1
        
        self.sprites = SpriteSheet(pygame.image.load(Path(image_path)), animation_steps, pos.x, pos.y, size.x, size.y)
    
    def draw(self, screen):
        if self.angle != self.prev_angle:
            pygame.transform.rotate(self.sprites.animation_list[self.sprites.ind], self.angle)
        
        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox) #draw hitbox
        if self.is_alive: #draw only if not collided
            screen.blit(self.sprites.animation_list[self.sprites.ind], self.rect)

    def move(self, ent_list):
        if self.can_move == False:
            return
        #self.vel.x = 0
        #self.vel.y = 0
        
        
        for ent in ent_list:
            if self.ID != ent.ID:
                if self.is_alive and ent.is_alive:
                    dist_x = self.pos.x - ent.pos.x
                    dist_y = self.pos.y - ent.pos.y
                    dist = sqrt(dist_x*dist_x + dist_y*dist_y) #Pythagorean theorem to calculate direct distance

                    grav = calc_gravity(self.mass, ent.mass, dist) #calculates gravity based upon masses and distance

                    self.vel.x -= dist_x*grav
                    self.vel.y -= dist_y*grav
                    #adds all gravitational pulls for objects together before moving
                
                    if self.hitbox.colliderect(ent.hitbox): #collision check
                        if self.is_collidable and ent.is_collidable:
                            if self.is_invincible == False:
                                self.is_alive = False
                            if ent.is_invincible == False:
                                ent.is_alive = False

        self.vel += self.thrust
        self.vel.x /= self.mass #More massive objects require more force to move quickly
        self.vel.y /= self.mass
        
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.hitbox.x = self.pos.x + self.hitoff.x #Move hitbox to overlap image. Offset because it's smaller than image
        self.hitbox.y = self.pos.y + self.hitoff.y

        self.prev_angle = self.angle
        self.angle = calc_angle(self.vel.x, self.vel.y)

class Ship(Ent):
    def __init__(self, pos: Vec2, vel: Vec2= Vec2(0,0), ind = 0, angle: int = 0, thrust = Vec2(0,0), can_move = True):
        self.image_path = "../res/ship_and_astroid_ss.png"
        size = Vec2(40,50)
        self.mass = 1
        self.can_move = True
        self.is_alive = True
        animation_steps = 18
        self.hitoff = Vec2(2, 6)

        self.is_collidable = True
        self.is_invincible = False

        self.rect = pygame.Rect(pos.x, pos.y, size.x, size.y)
        self.hitbox = pygame.Rect(pos.x+self.hitoff.x, pos.y+self.hitoff.y, size.x - self.hitoff.x*2, size.y - self.hitoff.y*2)
        self.pos = pos
        self.vel = vel
        
        self.angle = angle
        self.prev_angle = angle
        self.thrust = thrust
        
        self.ID = Ent.ent_count
        Ent.ent_count += 1
        
        self.sprites = SpriteSheet(pygame.image.load(Path(self.image_path)), animation_steps, pos.x, pos.y, size.x, size.y, ind)

class PlanetL(Ent):
    def __init__(self, pos: Vec2, vel: Vec2 = Vec2(0,0), ind = 0, angle: int = 0, thrust = Vec2(0,0), can_move = True):
        self.image_path = "../res/large_planet_ss.png"
        size = Vec2(150,150)
        self.mass = 20000000
        self.can_move = False
        self.is_alive = True
        animation_steps = 6
        self.hitoff = Vec2(10, 10)
        self.is_collidable = True
        self.is_invincible = True

        self.rect = pygame.Rect(pos.x, pos.y, size.x, size.y)
        self.hitbox = pygame.Rect(pos.x+self.hitoff.x, pos.y+self.hitoff.y, size.x - self.hitoff.x*2, size.y - self.hitoff.y*2)
        self.pos = pos
        self.vel = vel
        
        self.angle = angle
        self.prev_angle = angle
        self.thrust = thrust
        
        self.ID = Ent.ent_count
        Ent.ent_count += 1
        
        self.sprites = SpriteSheet(pygame.image.load(Path(self.image_path)), animation_steps, pos.x, pos.y, size.x, size.y, ind)


class PlanetM(Ent):
    def __init__(self, pos: Vec2, vel: Vec2 = Vec2(0,0), ind = 0, angle: int = 0, thrust = Vec2(0,0), can_move = True):
        self.image_path = "../res/medium_planet_ss.png"
        size = Vec2(100,100)
        self.mass = 1000000
        self.can_move = False
        self.is_alive = True
        animation_steps = 6
        self.hitoff = Vec2(7, 7)

        self.is_collidable = True
        self.is_invincible = True

        self.rect = pygame.Rect(pos.x, pos.y, size.x, size.y)
        self.hitbox = pygame.Rect(pos.x+self.hitoff.x, pos.y+self.hitoff.y, size.x - self.hitoff.x*2, size.y - self.hitoff.y*2)
        self.pos = pos
        self.vel = vel
        
        self.angle = angle
        self.prev_angle = angle
        self.thrust = thrust
        
        self.ID = Ent.ent_count
        Ent.ent_count += 1
        
        self.sprites = SpriteSheet(pygame.image.load(Path(self.image_path)), animation_steps, pos.x, pos.y, size.x, size.y, ind)


class PlanetS(Ent):
    def __init__(self, pos: Vec2, vel: Vec2 = Vec2(0,0), ind = 0, angle: int = 0, thrust = Vec2(0,0), can_move = True):
        self.image_path = "../res/small_planet_ss.png"
        size = Vec2(50,50)
        self.mass = 300000
        self.can_move = False
        self.is_alive = True
        animation_steps = 6
        self.hitoff = Vec2(5, 5)

        self.is_collidable = True
        self.is_invincible = True

        self.rect = pygame.Rect(pos.x, pos.y, size.x, size.y)
        self.hitbox = pygame.Rect(pos.x+self.hitoff.x, pos.y+self.hitoff.y, size.x - self.hitoff.x*2, size.y - self.hitoff.y*2)
        self.pos = pos
        self.vel = vel
        
        self.angle = angle
        self.prev_angle = angle
        self.thrust = thrust
        
        self.ID = Ent.ent_count
        Ent.ent_count += 1
        
        self.sprites = SpriteSheet(pygame.image.load(Path(self.image_path)), animation_steps, pos.x, pos.y, size.x, size.y, ind)


class DarkMatter(Ent):
    def __init__(self, pos: Vec2, vel: Vec2 = Vec2(0,0), ind = 0, angle: int = 0):
        self.image_path = "../res/dark_matter.png"
        size = Vec2(50,50)
        self.mass = 1000000
        self.can_move = False
        self.is_alive = True
        animation_steps = 1
        self.hitoff = Vec2(5, 5)

        self.is_collidable = False
        self.is_invincible = True

        self.rect = pygame.Rect(pos.x, pos.y, size.x, size.y)
        self.hitbox = pygame.Rect(pos.x+self.hitoff.x, pos.y+self.hitoff.y, size.x - self.hitoff.x*2, size.y - self.hitoff.y*2)
        self.pos = pos
        self.vel = vel
        
        self.angle = angle
        self.prev_angle = angle
        
        self.ID = Ent.ent_count
        Ent.ent_count += 1
        
        self.sprites = SpriteSheet(pygame.image.load(Path(self.image_path)), animation_steps, pos.x, pos.y, size.x, size.y, ind)

       

        
def calc_gravity(m1: int, m2: int, dist: Vec2):
    #standard gravity equation. Google it
    if dist == 0:
        return 0
    return (G_Const*m1*m2)/(dist*dist) 

def calc_angle(x, y):
    ### Using trigonometry to calculate new angle (sohcahTOA). See notebook for diagram
    #Must split into quadrants so we get angles correct, else would always rbe < 90
    if x >= 0 and y >= 0:
        if y == 0:
            return 0
        return degrees(atan(x/y))
    elif x >= 0 and y < 0:
        if x == 0:
            return 90
        return degrees(atan(abs(y)/x)) + 90
    elif x < 0 and y <=0:
        if y == 0:
            return 180
        return degrees(atan(abs(x)/abs(y))) + 180
    elif x <= 0 and y >= 0:
        if x == 0:
            return 270
        return degrees(atan(y/abs(x))) + 270



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
# ship_temp = pygame.image.load(Path(r"../res/ship.png")).convert_alpha()
#practise_ship = Characters("left", "Star Bug", 270, 1, ship_temp, 1, 200, 200, 50, 50)

#enterprise = Characters("up", "Star Bug", 0, 1, ship_temp, 1, 300, 300, 50, 50)



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

#dm = pygame.image.load(Path(r"../res/dm.png")).convert_alpha()
#practise_entity = Entity(dm, 1, 150, 150, 100, 100)


###an obstacles class for ships to collide into
class Obstacle(SpriteSheet):
    def __init__(self, image, animation_steps, x_pos, y_pos, x_cut, y_cut):
        
        super().__init__(image, animation_steps, x_pos, y_pos, x_cut, y_cut)
        
    def Draw(self):
        settings.screen.blit(self.animation_list[self.ind], self.rect)
        
#px = pygame.image.load(Path(r"../res/px.png")).convert_alpha()
#planetx = Entity(px, 1, 500, 200, 120, 120)


class BackGround(SpriteSheet):
    pass
    ###probably dont need a spritesheet for the background stuff
    ###might not even need a class
    #def __init__(self, image, animation_steps, x_pos, y_pos, x_cut, y_cut):
        
        #super().__init__(image, animation_steps, x_pos, y_pos, x_cut, y_cut)