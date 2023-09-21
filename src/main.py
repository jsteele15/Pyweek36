import pygame
from events_and_inputs import*
from settings import Settings
from characters_and_backgrounds import Ent
from levels import Level, win_cond1, win_cond2
from ui import Buttons
from copy import copy
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

    testent = Ship(Vec2(50, 50))
    testent2 = DarkMatter(Vec2(400, 400))
    testent3 = PlanetS(Vec2(100, 350)) 
    ent_list.append(testent)
    #ent_list.append(testent2)
    ent_list.append(testent3)


    butt1 = Buttons(0, "../res/play_but.png", Vec2(100, 500))
    butt2 = Buttons(3, "../res/dark_matter.png", Vec2(200, 500))
    butt4 = Buttons(3, "../res/dark_matter.png", Vec2(300, 500))
    butt3 = Buttons(1, "../res/restart.png", Vec2(400, 500))
    button_list.append(butt1)
    button_list.append(butt2)
    button_list.append(butt3)

    l2_button = [butt1, butt2, butt3, butt4]

    l2_ents = [Ship(Vec2(50, 100), thrust = Vec2(0.1, 0)), PlanetM(Vec2(400, 75)), PlanetM(Vec2(401, 350)) ]

    level1 = Level(button_list, ent_list, win_cond1)
    level2 = Level(l2_button, l2_ents, win_cond2)

    settings.level_list.append(level1)
    settings.level_list.append(level2)

    settings.load_level()

    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

    while settings.Running:
        screen.fill((0,0,0))

        actions(settings.ent_list, settings.button_list, settings)
        if settings.PAUSED == False:
            move_ents(settings.ent_list)
        draw_ents(settings.ent_list, settings.button_list, settings, screen)

        if settings.level_list[settings.current_level].win_cond(settings.level_list[settings.current_level], settings):
            settings.current_level += 1
            settings.load_level()
            print("Win!!!!")

        pygame.display.update()
        settings.clock.tick(60) 

def draw_ents(ent_list, button_list, settings, screen):
    for ent in ent_list:
        ent.draw(screen)
    for button in button_list:
        button.draw(screen)
    settings.mouse.draw(screen)

def move_ents(ent_list):
    for ent in ent_list:
        ent.move(ent_list)

if __name__ == "__main__":
    #Start_Menu()
    main()