import pygame
from events_and_inputs import*
from settings import Settings
from characters_and_backgrounds import Ent
from ui import Buttons

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


def main():
    pygame.init()
    settings = Settings()
    ent_list = []
    button_list = []

    testent = Ship(Vec2(50, 50), thrust = Vec2(0.1, 0))
    testent2 = DarkMatter(Vec2(400, 400))
    testent3 = PlanetL(Vec2(100, 350)) 
    ent_list.append(testent)
    ent_list.append(testent2)
    ent_list.append(testent3)

    butt1 = Buttons(0, "../res/play_but.png", Vec2(100, 500))
    button_list.append(butt1)

    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

    while settings.Running:
        screen.fill((0,0,0))

        actions(button_list, settings)
        if settings.PAUSED == False:
            move_ents(ent_list)
        draw_ents(ent_list, button_list, screen)

        pygame.display.update()
        settings.clock.tick(60) 

def draw_ents(ent_list, button_list, screen):
    for ent in ent_list:
        ent.draw(screen)
    for button in button_list:
        button.draw(screen)

def move_ents(ent_list):
    for ent in ent_list:
        ent.move(ent_list)

if __name__ == "__main__":
    #Start_Menu()
    main()