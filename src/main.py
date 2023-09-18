import pygame
from events_and_inputs import*
from settings import Settings
from characters_and_backgrounds import Ent

def Start_Menu():
    #tells the game its a menu
    settings.level_or_menu = 0
    #removes any previous buttons and puts the start buttons in
    button_list.clear()
    for i in menu_button_list:
        button_list.append(i)
    
    while settings.Running:
        Drawing()
        Actions(button_list)
<<<<<<< HEAD
        
    
=======


def main():
    pygame.init()
    settings = Settings()
    ent_list = []
    testent = Ent("../res/ship.png", Vec2(50, 50), Vec2(50, 50), Vec2(0, 0), 0.1)
    testent2 = Ent("../res/ship.png", Vec2(50, 50), Vec2(350, 300), Vec2(0, 0), 1000000)
    testent3 = Ent("../res/ship.png", Vec2(50, 50), Vec2(500, 590), Vec2(0, 0), 1.5, thrust = Vec2(0, -2)) 
    ent_list.append(testent)
    ent_list.append(testent2)
    ent_list.append(testent3)
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

    while settings.Running:
        screen.fill((0,0,0))
        move_ents(ent_list)
        draw_ents(ent_list, screen)

        pygame.display.update()
        settings.clock.tick(60) 

        for event in pygame.event.get():
            if event.type == QUIT:
                settings.Running = False
                sys.exit()

def draw_ents(ent_list, screen):
    for ent in ent_list:
        ent.draw(screen)

def move_ents(ent_list):
    for ent in ent_list:
        ent.move(ent_list)

>>>>>>> merge_char_ent_classes
if __name__ == "__main__":
    #Start_Menu()
    main()