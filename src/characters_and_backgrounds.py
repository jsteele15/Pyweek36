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
        #if self.angle != self.prev_angle:
        rotated_image = pygame.transform.rotate(self.sprites.animation_list[self.sprites.ind], self.angle)
        
        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox) #draw hitbox
        if self.is_alive: #draw only if not collided
            screen.blit(rotated_image, self.rect)

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
        size = Vec2(39,46)
        self.mass = 1
        self.can_move = True
        self.is_alive = True
        animation_steps = 19
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
    def __init__(self, pos: Vec2, vel: Vec2 = Vec2(0,0), ind = 0, angle: int = 0, thrust = Vec2(0,0), can_move = False, mass = 20000000, is_invincible = True):
        self.image_path = "../res/large_planet_ss.png"
        size = Vec2(150,150)
        self.mass = mass
        self.can_move = can_move
        self.is_alive = True
        animation_steps = 6
        self.hitoff = Vec2(10, 10)
        self.is_collidable = True
        self.is_invincible = is_invincible

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
    def __init__(self, pos: Vec2, vel: Vec2 = Vec2(0,0), ind = 0, angle: int = 0, thrust = Vec2(0,0), can_move = False, mass = 1000000, is_invincible = True):
        self.image_path = "../res/medium_planet_ss.png"
        size = Vec2(100,100)
        self.mass = mass
        self.can_move = can_move
        self.is_alive = True
        animation_steps = 6
        self.hitoff = Vec2(7, 7)

        self.is_collidable = True
        self.is_invincible = is_invincible

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
    def __init__(self, pos: Vec2, vel: Vec2 = Vec2(0,0), ind = 0, angle: int = 0, thrust = Vec2(0,0), can_move = False, mass = 300000, is_invincible = True):
        self.image_path = "../res/small_planet_ss.png"
        size = Vec2(50,50)
        self.mass = mass
        self.can_move = can_move
        self.is_alive = True
        animation_steps = 7
        self.hitoff = Vec2(5, 5)

        self.is_collidable = True
        self.is_invincible = is_invincible

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

       
class AsteroidF(Ent):
    def __init__(self, pos: Vec2, vel: Vec2 = Vec2(0,0), ind = 0, angle: int = 0, thrust = Vec2(0,0), can_move = True, mass = 0):
        self.image_path = "../res/meteor_field_ss.png"
        size = Vec2(200,200)
        self.mass = mass
        self.can_move = False
        self.is_alive = True
        animation_steps = 3
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

