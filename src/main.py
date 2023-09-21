import pygame
from events_and_inputs import*
from settings import Settings
from characters_and_backgrounds import Ent
from levels import Level, win_cond1, win_cond2
from ui import Buttons, Text
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
    ####level 1 stuff
    
    ent_list = []
    button_list = []
    text_list = []
    
    
    ####mission texts
    text1 = Text(30, "Dark matter can pull\nships and single commets with their gavity\n\nClick this purple dark matter here ->\n\n\n\n\n\n\nThen place it here ->\n\n\n       <-Then click here to start the level\n       <-Or click here to restart the level", 0, 0)
    text2 = Text(30, "Good, now\n\nget the Red \n\nship through \n\nthe planet and \n\nthe moon safely", settings.WIDTH - 280, 80)
    text3 = Text(30, "That was lame.\n\n\n\n\n\n\n\n\n\n                     NOW LETS HIT THIS BLUE PLANET \n                                              WITH A METEORITE! \n                                           DON'T HIT THE MOON", 0, 0)
    text4 = Text(30, "I bet we'll never hear from them again.\n\n\n\n\n\n\n\n\n\n\n\n                                             Lets get our friends\n                                                 to this small moon", 0, 0)
    text5 = Text(30, "I don't think that was a moon...\n\n\n\n\n\n\n\n\nLook, there, a ship is \ngoing to be pulled into \nthat gas giant. Get them \nout of the planets orbit!", 0, 0)
    text6 = Text(30, "That was close.\n\n\n\n\n\n\n\n\n\n\n\n\n       Return this           family\n       home to the red planet ->", 0, 0)
    text7 = Text(30, "We saved a life today, well done.\n\nNow lets murder, \n\nIdk, \n\nSix Federation ships\n\n\n\n\n\n\n\n\n\n\n\n\n", 0, 0)
    text8 = Text(30, "Lv8", 0, 0)
    
    ###training level
    testent = Ship(Vec2(50, 100), ind = 1, angle = 180)
    testent2 = DarkMatter(Vec2(400, 400))
    testent3 = PlanetS(Vec2(300, 350), ind = 2)
    ent_list.append(testent)
    #ent_list.append(testent2)
    ent_list.append(testent3)

    #play button and restart
    butt1 = Buttons(0, "../res/level_buttons_ss.png", Vec2(0, 510), size_x = 60, ind = 2, second_ind = 3)
    butt3 = Buttons(1, "../res/level_buttons_ss.png", Vec2(0, 550), size_x = 60, second_ind = 1)
    ###dark_matter
    butt2 = Buttons(3, "../res/dark_matter.png", Vec2(630, 110), size_x = 50, size_y = 50)
    butt4 = Buttons(3, "../res/dark_matter.png", Vec2(300, 500), size_x = 50, size_y = 50)
    butt5 = Buttons(3, "../res/dark_matter.png", Vec2(350, 250), size_x = 50, size_y = 50)
    butt6 = Buttons(3, "../res/dark_matter.png", Vec2(490, 250), size_x = 50, size_y = 50)
    
    
    button_list.append(butt1)
    button_list.append(butt2)
    button_list.append(butt3)
    
    
    
    ###level 2 stuff
    l2_button = [butt1, butt5, butt3, butt4]
    l2_ents = [Ship(Vec2(50, 100), thrust = Vec2(0.1, 0), ind = 2), PlanetM(Vec2(400, 75), ind = 2), PlanetS(Vec2(401, 350), ind = 1) ]
    
    
    ###level 3 ents
    l3_button = [butt1, butt2, butt3, butt4, butt5]
    l3_ents = [Ship(Vec2(50, settings.HEIGHT/2), thrust = Vec2(0.01, 0), ind = 9, angle = 90), 
        PlanetM(Vec2(settings.WIDTH - 100, settings.HEIGHT/3), ind = 1, mass = 0), PlanetS(Vec2(settings.WIDTH/3, settings.HEIGHT/2), mass = 0)]
    
    
    ###level 4 ents
    l4_button = [butt1, butt2, butt3, butt4, butt5]
    l4_ents = [Ship(Vec2(100, settings.HEIGHT/3 - 50), thrust = Vec2(0.01, 0), ind = 4, angle = 180), Ship(Vec2(50, settings.HEIGHT/2 - 50), thrust = Vec2(0.01, 0), ind = 6, angle = 180), 
        PlanetS(Vec2(settings.WIDTH-100, settings.HEIGHT/2 -50), mass = 0, ind = 4), PlanetL(Vec2(settings.WIDTH/3, settings.HEIGHT/2), mass = 0, ind = 4), PlanetL(Vec2(settings.WIDTH-100, settings.HEIGHT/4 - 100), mass = 0, ind = 5)]
    
    ###level 5 ents
    l5_button = [butt1, butt2, butt3, butt4, butt5, butt6]
    l5_ents = [Ship(Vec2(100, settings.HEIGHT/3 - 50), thrust = Vec2(0.01, 0), ind = 7, angle = 180), PlanetL(Vec2(settings.WIDTH/2, settings.HEIGHT/2), ind = 0, mass = 10000000)]
    
    ###level 6 ents
    l6_button = [butt1, butt2, butt3, butt4, butt5, butt6]
    l6_ents = [Ship(Vec2(100, settings.HEIGHT/3 - 50), thrust = Vec2(0.1, 0), ind = 7, angle = 270), PlanetM(Vec2(settings.WIDTH/2 + 100, settings.HEIGHT -100), ind = 2, mass = 0),
        PlanetL(Vec2(settings.WIDTH/2 + 100, settings.HEIGHT -280), ind = 3, mass = 1000000)]
    
    ####level 7 ents
    l7_button = [butt1, butt2, butt3, butt4, butt5, butt6]
    l7_ents = [Ship(Vec2(100, settings.HEIGHT/3 - 50), thrust = Vec2(0.01, 0), ind = 0, angle = 270), Ship(Vec2(100, settings.HEIGHT/2), thrust = Vec2(0.01, 0), ind = 0, angle = 270),
        Ship(Vec2(600, settings.HEIGHT/4 - 50), thrust = Vec2(-0.01, 0), ind = 0, angle = 90), Ship(Vec2(600, settings.HEIGHT - 100), thrust = Vec2(-0.01, 0), ind = 0, angle = 90),
        Ship(Vec2(300, 100), thrust = Vec2(0, 0.1), ind = 0, angle = 180), Ship(Vec2(400, 100), thrust = Vec2(0, 0.01), ind = 0, angle = 180)]
    
    ###level 8 ents
    l8_button = []
    l8_ents = []
    
    ###where it gets appended to the level lists
    level1 = Level(button_list, ent_list, win_cond1)
    level2 = Level(l2_button, l2_ents, win_cond2)
    level3 = Level(l3_button, l3_ents, win_cond3)
    level4 = Level(l4_button, l4_ents, win_cond4)
    level5 = Level(l5_button, l5_ents, win_cond5)
    level6 = Level(l6_button, l6_ents, win_cond6)
    level7 = Level(l7_button, l7_ents, win_cond7)
    level8 = Level(l8_button, l8_ents, win_cond8)
    
    settings.level_list.append(level1)
    settings.level_list.append(level2)
    settings.level_list.append(level3)
    settings.level_list.append(level4)
    settings.level_list.append(level5)
    settings.level_list.append(level6)
    settings.level_list.append(level7)
    settings.level_list.append(level8)
    
    ###appending texts
    text_list.append(text1)
    text_list.append(text2)
    text_list.append(text3)
    text_list.append(text4)
    text_list.append(text5)
    text_list.append(text6)
    text_list.append(text7)
    text_list.append(text8)
    
    text_list.append("")
    
    settings.load_level()

    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    ###background image
    star_map = pygame.image.load("../res/testsky.png").convert_alpha()
    scaled_im2 = pygame.transform.scale(star_map,(1400,800))
    while settings.Running:
        screen.fill((0,0,0))
        ###blit background
        screen.blit(scaled_im2, (0, 0))
        
        actions(settings.ent_list, settings.button_list, settings)
        if settings.PAUSED == False:
            move_ents(settings.ent_list)
            
        draw_ents(settings.ent_list, settings.button_list, text_list, settings, screen)

        if settings.level_list[settings.current_level].win_cond(settings.level_list[settings.current_level], settings):
            settings.current_level += 1
            settings.load_level()
            print("Win!!!!")
        
        pygame.display.update()
        settings.clock.tick(60) 

def draw_ents(ent_list, button_list, text_list, settings, screen):
    
    text_list[settings.current_level].draw(screen)
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