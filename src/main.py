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

####load the music
if sound:
    track = Music_Sound(0, "../res/Dark Matter Long.wav")

if sound:
    track.load()
    
def main():
    pygame.init()
    
    ###adds a title
    pygame.display.set_caption("Untitled Gravity Puzzler")
    
    ###adds an icon
    icon = pygame.image.load("../res/icon.png")
    pygame.display.set_icon(icon)
    
    settings = Settings()
    ####level 1 stuff
    
    ent_list = []
    button_list = []
    text_list = []
    
    
    ####mission texts
    menu_text = Text(100, " Untitled \n Gravity\n Puzzler", 5, 5)
    menu_text_high = Text(100, " Untitled \n Gravity\n Puzzler", 0, 0, colour = (63, 63, 116))
    
    help_text = Text(20, "Press f for fullscreen\nPress ESC to exit", 0, settings.HEIGHT - 65)
    text1 = Text(30, "Dark matter can pull\nships and single commets with their gavity\n\nClick this grey dark matter here ->\n\n\n\n\n\n\nThen place it here ->   <- once purple, the dark \n                                         matter has gravity\n\n       <-Then click here to start the level\n       <-Or click here to restart the level", 0, 0)
    text2 = Text(30, "Good, now\n\nget the Red \n\nship past \n\nthe planet and \n\nthe moon safely", settings.WIDTH - 280, 80)
    text3 = Text(30, "Lets make something cool. \n\nCrash all these meteorites into each other\n\nTo make a new planet", 0, 0)
    text4 = Text(30, "That was lame.\n\n\n\n\n\n\n\n\n\n                   NOW LETS HIT THAT SAME PLANET \n                                              WITH A METEORITE! \n                                           DON'T HIT THE MOON", 0, 0)
    text5 = Text(30, "I bet we'll never hear from them again.\n\n\n\n\n\n\n\n\n\n\n\n                                             Lets get our friends\n                                                 to this small moon", 0, 0)
    text6 = Text(30, "We saved a life today, well done.\n\nNow lets murder, \n\nIdk, \n\nSix Federation ships\n\n\n\n\n\n\n\n\n\n\n\n\n", 0, 0)
    
    text7 = Text(30, "*YOU NOW HAVE TO TAKE INTO ACCOUNT THE \nGRAVITY OF PLANETS AND MOONS*\n\n\n\n\n\n\n\nLook there, a ship is \ngoing to be pulled into \nthat gas giant. Get them \nout of the planets orbit!", 0, 0)
    text8 = Text(30, "That was close.\n\n\n\n\n\n\n\n\n\n\n\n\n       Return this           family\n       home to the red planet ->", 0, 0)
    text9 = Text(30, "The Spice must flow!\n\n\n\n\n\n\n\n\n\nGet the cargo ships to the \nplanet on the left here", 0, 0)
    text10 = Text(30, "                                                Get the green ship\n                                                 to investigate the\n                                                       distress signal \n                                                    coming from the\n                                                         space station\n\n\n\n\n\n                                                   ->\n\n                                                     *AVOID \n                                                     ASTEROID \n                                                     FEILDS*", 0, 0)
    text11 = Text(30, "Destroy the Imperial ship (left), \nbefore the Rebel ship (right) crashes!", 0, 0)
    text12 = Text(30, "                                                These guys again!\n\n\n\n\n\n\n\n\n\n\n\n\n\n                          Destroy the Earth for good!", 0, 0)
    textend = Text(30, "This was a mistake, destroy the universe\nand with it, all life\n\n\n\n\n\n\n\n\n\n\n\n      *DARK MATTER GRAVITY NOW AFFECTS\n       PLANETS AND MOONS*", 0, 0)
    last_text = Text(25, "And with that, the\n   universe ends.\n\nThanks for playing.\n\n\n\n\n\n\n\n\nCredits - Lime Gang\nPreatomicprince, Jimbo Jones, Vaugbe\nPress r to return to the main menu", 100, 100)
    
    
    
    ###training level
    testent = Ship(Vec2(50, 80), ind = 1, angle = 0)
    testent2 = DarkMatter(Vec2(400, 400))
    testent3 = PlanetS(Vec2(300, 350), ind = 2, mass = 0)
    ent_list.append(testent)
    #ent_list.append(testent2)
    ent_list.append(testent3)
    
    
    #play button and restart
    butt1 = Buttons(0, "../res/level_buttons_ss.png", Vec2(0, 510), size_x = 60, ind = 2, second_ind = 3)
    butt3 = Buttons(1, "../res/level_buttons_ss.png", Vec2(0, 550), size_x = 60, second_ind = 1)
    skip_butt = Buttons(5, "../res/level_buttons_ss.png", Vec2(settings.WIDTH - 60, 550), size_x = 60, ind = 4, second_ind = 5, dm_but = True)
    
    ###dark_matter
    butt2 = Buttons(3, "../res/dark_matter.png", Vec2(630, 110), size_x = 50, size_y = 50, ind = 1, dm_but = True)
    butt4 = Buttons(3, "../res/dark_matter.png", Vec2(300, 500), size_x = 50, size_y = 50, ind = 1, dm_but = True)
    butt5 = Buttons(3, "../res/dark_matter.png", Vec2(350, 250), size_x = 50, size_y = 50, ind = 1, dm_but = True)
    butt6 = Buttons(3, "../res/dark_matter.png", Vec2(490, 250), size_x = 50, size_y = 50, ind = 1, dm_but = True)
    butt7 = Buttons(3, "../res/dark_matter.png", Vec2(200, 250), size_x = 50, size_y = 50, ind = 1, dm_but = True)
    butt8 = Buttons(3, "../res/dark_matter.png", Vec2(200, 400), size_x = 50, size_y = 50, ind = 1, dm_but = True)
    butt9 = Buttons(3, "../res/dark_matter.png", Vec2(550, 550), size_x = 50, size_y = 50, ind = 1, dm_but = True)
    butt10 = Buttons(3, "../res/dark_matter.png", Vec2(100, 100), size_x = 50, size_y = 50, ind = 1, dm_but = True)
    menu_dm = Buttons(3, "../res/dark_matter.png", Vec2(500, 180), size_x = 50, size_y = 50, ind = 0)
    
    
    start_button = Buttons(4, "../res/menu_ss.png", Vec2(settings.WIDTH/2 - 140, settings.HEIGHT -60), size_x = 120, size_y = 40, second_ind = 1)
    end_button = Buttons(2, "../res/menu_ss.png", Vec2(settings.WIDTH/2 +20, settings.HEIGHT -60), size_x = 120, size_y = 40, ind = 2, second_ind = 3)
    
    button_list.append(butt1)
    button_list.append(butt2)
    button_list.append(butt3)
    
    ###menu
    menu_button = [start_button, end_button, menu_dm]
    menu_ents = [Ship(Vec2(505, settings.HEIGHT/2+10), thrust = Vec2(-0.1, 0), ind = 7, angle = 180), PlanetS(Vec2(500, 50), mass = 0, ind = 6)]
    
    ###level 2 stuff
    l2_button = [butt1, butt5, butt3, butt4, skip_butt]
    l2_ents = [Ship(Vec2(50, 100), thrust = Vec2(0.1, 0), ind = 2, angle = 90), PlanetM(Vec2(400, 75), ind = 2), PlanetS(Vec2(401, 350), ind = 1) ]
    
    ###level 3 ents, use meteorites to make a new planet
    l3_button = [butt1, butt5, butt3, butt4, skip_butt]
    l3_ents = [Ship(Vec2(100 * i, settings.HEIGHT/2), thrust = Vec2(0, 0.01), ind = 8 + i, angle = 180) for x, i in enumerate(range(1, 7))]
    

    ###level 4 ents
    l4_button = [butt1, butt2, butt3, butt4, butt5, skip_butt]
    l4_ents = [Ship(Vec2(50, settings.HEIGHT/2), thrust = Vec2(0.01, 0), ind = 9, angle = 90), 
        PlanetM(Vec2(settings.WIDTH - 100, settings.HEIGHT/3), ind = 1, mass = 0), PlanetS(Vec2(settings.WIDTH/3, settings.HEIGHT/2), mass = 0)]
    
    
    ###level  ents
    l5_button = [butt1, butt2, butt3, butt4, butt5, skip_butt]
    l5_ents = [Ship(Vec2(100, settings.HEIGHT/3 - 50), thrust = Vec2(0.01, 0), ind = 4, angle = 180), Ship(Vec2(50, settings.HEIGHT/2 - 50), thrust = Vec2(0.01, 0), ind = 6, angle = 180), 
        PlanetS(Vec2(settings.WIDTH-100, settings.HEIGHT/2 -50), mass = 0, ind = 4), PlanetL(Vec2(settings.WIDTH/3, settings.HEIGHT/2), mass = 0, ind = 4), PlanetL(Vec2(settings.WIDTH-100, settings.HEIGHT/4 - 100), mass = 0, ind = 5)]
    
    ####level 6 ents
    l6_button = [butt1, butt2, butt3, butt4, butt5, butt6, skip_butt]
    l6_ents = [Ship(Vec2(100, settings.HEIGHT/3 - 50), thrust = Vec2(0.01, 0), ind = 0, angle = 90), Ship(Vec2(100, settings.HEIGHT/2), thrust = Vec2(0.01, 0), ind = 0, angle = 90),
        Ship(Vec2(600, settings.HEIGHT/4 - 50), thrust = Vec2(-0.01, 0), ind = 0, angle = 270), Ship(Vec2(600, settings.HEIGHT - 100), thrust = Vec2(-0.01, 0), ind = 0, angle = 270),
        Ship(Vec2(300, 100), thrust = Vec2(0, 0.1), ind = 0, angle = 0), Ship(Vec2(400, 100), thrust = Vec2(0, 0.01), ind = 0, angle = 0)]
    
    

    ###level 7 ents  LEVEL 7 IS WHEN YOU HAVE TO TAKE INTO ACCOUNT THE PLANETS GRAVITY
    l7_button = [butt1, butt2, butt3, butt4, butt5, butt6, skip_butt]
    l7_ents = [Ship(Vec2(100, settings.HEIGHT/3 - 50), thrust = Vec2(0.01, 0), ind = 7, angle = 180), PlanetL(Vec2(settings.WIDTH/2, settings.HEIGHT/2), ind = 0, mass = 5000000)]
    
    ###level 8 ents
    l8_button = [butt1, butt2, butt3, butt4, butt5, butt6, skip_butt]
    l8_ents = [Ship(Vec2(100, settings.HEIGHT/3 - 50), thrust = Vec2(0.05, 0), ind = 7, angle = 90), PlanetM(Vec2(settings.WIDTH/2 + 100, settings.HEIGHT -100), ind = 2, mass = 0),
        PlanetL(Vec2(settings.WIDTH/2 + 100, settings.HEIGHT -280), ind = 3, mass = 1000000)]
    
    ###level 9 ents, the spice must flow
    l9_button = [butt1, butt2, butt3, butt4, butt5, butt6, skip_butt]
    l9_ents = [PlanetL(Vec2(settings.WIDTH/4-75, settings.HEIGHT/2- 75), ind = 2, mass = 500000), PlanetL(Vec2(settings.WIDTH/2 + 100, settings.HEIGHT/2-75), ind = 4, mass = 400000),
        Ship(Vec2(100, 100), thrust = Vec2(0, 0), ind = 8, angle = 0),  Ship(Vec2(500, 100), thrust = Vec2(0.05, 0), ind = 8, angle = 0), Ship(Vec2(settings.WIDTH/3 +80, settings.HEIGHT - 100), thrust = Vec2(-0.05, 0), ind = 8, angle = 180)]
    
    ###level 10 ents, investigate a distress beekon through a mine field
    l10_button = [butt1, butt6, butt3, butt4, butt5, skip_butt]
    l10_ents = [PlanetS(Vec2(settings.WIDTH/2, 100), mass = 500000, ind = 5), Ship(Vec2(50, 300), thrust = Vec2(0, 0), ind = 3, angle = 90), PlanetS(Vec2(550, 370), mass = 500000, ind = 6),
        AsteroidF(Vec2(0, 0), ind = 1), AsteroidF(Vec2(200, 0), ind = 0), AsteroidF(Vec2(100, settings.HEIGHT-200), ind = 1), AsteroidF(Vec2(300, settings.HEIGHT-250), ind = 0),
        AsteroidF(Vec2(300, settings.HEIGHT-50), ind = 0, angle = 90), AsteroidF(Vec2(-100, settings.HEIGHT-200), angle = 180, ind = 0), AsteroidF(Vec2(-100, settings.HEIGHT), angle = 180, ind = 1), AsteroidF(Vec2(100, settings.HEIGHT), angle = 180, ind = 0)]
    
    ###level 11 ents, rescue the rebel ship destroy the empire ship
    l11_button = [butt1, butt6, butt3, butt4, butt5, skip_butt]
    l11_ents = [Ship(Vec2(200, 100), thrust = Vec2(0, 0.1), ind = 18, angle = 0), Ship(Vec2(100, 100), thrust = Vec2(0.1, 0), ind = 5, angle = 0), PlanetM(Vec2(settings.WIDTH/2 - 100, settings.HEIGHT/2 - 100), ind = 5, mass = 400000), PlanetM(Vec2(500, 300), ind = 4, mass = 400000),
        AsteroidF(Vec2(300, settings.HEIGHT-100), ind = 0, angle = 90), AsteroidF(Vec2(-100, settings.HEIGHT-100), angle = 180, ind = 0), AsteroidF(Vec2(500, settings.HEIGHT - 100), angle = 180, ind = 1), AsteroidF(Vec2(100, settings.HEIGHT-100), angle = 180, ind = 0), AsteroidF(Vec2(700, settings.HEIGHT-100), ind = 1, angle = 90),
        AsteroidF(Vec2(200, settings.HEIGHT-100), ind = 0, angle = 0), AsteroidF(Vec2(0, settings.HEIGHT-100), angle = 90, ind = 0), AsteroidF(Vec2(400, settings.HEIGHT - 100), angle = 0, ind = 1), AsteroidF(Vec2(600, settings.HEIGHT-100), angle = 0, ind = 0), AsteroidF(Vec2(800, settings.HEIGHT-100), ind = 1, angle = 180)]
    
    ###level 12 ents, destroy the earth again
    l12_button = [butt1, butt6, butt3, butt4, butt5, butt2, skip_butt]
    l12_ents = [PlanetM(Vec2(settings.WIDTH/3-150, settings.HEIGHT/2), ind = 0, mass = 500000), PlanetS(Vec2(10, settings.HEIGHT/3 + 100), mass = 200000), PlanetM(Vec2(settings.WIDTH/2, settings.HEIGHT/3 + 100), ind = 2, mass = 500000),
        Ship(Vec2(settings.WIDTH -100, settings.HEIGHT/2), thrust = Vec2(0, 0), ind = 17, angle = 0)]
    
    ###end ents, end of the universe
    lend_button = [butt1, butt6, butt3, butt4, butt5, butt2, butt7, butt8, butt9, butt10, skip_butt]
    lend_ents = [PlanetM(Vec2(100, 150), ind = 2, mass = 5000000, can_move = True, is_invincible = False), PlanetM(Vec2(500, 100), ind = 3, mass = 500000,can_move = True, is_invincible = False ),
        PlanetM(Vec2(300, 200), ind = 4, mass = 500000, can_move = True, is_invincible = False),PlanetM(Vec2(350, 400), ind = 5, mass = 500000, can_move = True, is_invincible = False),
        PlanetL(Vec2(100, 350), ind = 4, mass = 500000, can_move = True, is_invincible = False), PlanetL(Vec2(550, 300), ind = 2, mass = 500000, can_move = True, is_invincible = False),
        PlanetS(Vec2(300, 50), mass = 200000, ind = 3, can_move = True, is_invincible = False), PlanetS(Vec2(10, settings.HEIGHT/3 + 100), mass = 200000, can_move = True, is_invincible = False)]
    
    ###last sections
    last_button = []
    last_ents = []
    
    ###where it gets appended to the level lists
    menu = Level(menu_button, menu_ents, win_cond0)
    level1 = Level(button_list, ent_list, win_cond1)
    level2 = Level(l2_button, l2_ents, win_cond2)
    level3 = Level(l3_button, l3_ents, win_cond3)
    level4 = Level(l4_button, l4_ents, win_cond4)
    level5 = Level(l5_button, l5_ents, win_cond5)
    level6 = Level(l6_button, l6_ents, win_cond6)
    level7 = Level(l7_button, l7_ents, win_cond7)
    level8 = Level(l8_button, l8_ents, win_cond8)
    level9 = Level(l9_button, l9_ents, win_cond9)
    level10 = Level(l10_button, l10_ents, win_cond10)
    level11 = Level(l11_button, l11_ents, win_cond11)
    level12 = Level(l12_button, l12_ents, win_cond12)
    levelend = Level(lend_button, lend_ents, win_cond1end)
    last = Level(last_button, last_ents, win_end)
    
    settings.level_list.append(menu)
    settings.level_list.append(level1)
    settings.level_list.append(level2)
    settings.level_list.append(level3)
    settings.level_list.append(level4)
    settings.level_list.append(level5)
    settings.level_list.append(level6)
    settings.level_list.append(level7)
    settings.level_list.append(level8)
    settings.level_list.append(level9)
    settings.level_list.append(level10)
    settings.level_list.append(level11)
    settings.level_list.append(level12)
    settings.level_list.append(levelend)
    settings.level_list.append(last)
    
    ###appending texts
    text_list.append(menu_text)
    text_list.append(text1)
    text_list.append(text2)
    text_list.append(text3)
    text_list.append(text4)
    text_list.append(text5)
    text_list.append(text6)
    text_list.append(text7)
    text_list.append(text8)
    text_list.append(text9)
    text_list.append(text10)
    text_list.append(text11)
    text_list.append(text12)
    text_list.append(textend)
    text_list.append(last_text)
    text_list.append("")
    
    settings.load_level()

    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    ###background image
    star_map = pygame.image.load("../res/testsky.png").convert_alpha()
    scaled_im2 = pygame.transform.scale(star_map,(1400,800))
    
    exp_im1 = pygame.image.load(Path(r"../res/explosion.png")).convert_alpha()
    exp_im = pygame.transform.scale(exp_im1, (45600, 400))
    explosion_sprite = SpriteSheet(exp_im, 114, settings.WIDTH/2, settings.HEIGHT/2, 400, 400)
    exp_list = [explosion_sprite]
    
    ####for the music
    if sound:
        track.play()
        
    while settings.Running:
        
        
        screen.fill((0,0,0))
        ###blit background
        screen.blit(scaled_im2, (0, 0))
        
        ###for a press f to do fullscreen
        if settings.current_level == 0:
            menu_text_high.draw(screen)
            help_text.draw(screen)

        actions(settings.ent_list, settings.button_list, settings)
        if settings.PAUSED == False:
            move_ents(settings.ent_list, settings)
            
        draw_ents(settings.ent_list, settings.button_list, text_list, settings, screen, exp_list)
        
        pygame.display.update()
        settings.clock.tick(60) 

def draw_ents(ent_list, button_list, text_list, settings, screen, exp_list):
        
    for i in range(0, len(settings.prev_trail_points)):  #draw prev trail live
        if len(settings.prev_trail_points[i]) >= 2:
            current_point = 0
            point_max = len(settings.prev_trail_points[i]) - len(settings.prev_trail_points[i])%2 -2 #makes even number
            while current_point < point_max:
                pygame.draw.line(screen, (64, 64, 128) ,settings.prev_trail_points[i][current_point], settings.prev_trail_points[i][current_point+1])
                current_point += 1

    for i in range(0, len(settings.trail_points)):
        if len(settings.trail_points[i]) >= 2:
            current_point = 0
            point_max = len(settings.trail_points[i]) - len(settings.trail_points[i])%2 -2 #makes even number
            while current_point < point_max:
                pygame.draw.line(screen, (0, 0, 255), settings.trail_points[i][current_point], settings.trail_points[i][current_point+1])
                current_point += 1

    text_list[settings.current_level].draw(screen)
    for ent in ent_list:
        ent.draw(screen)
    for button in button_list:
        button.draw(screen, settings)
    settings.mouse.draw(screen)
    
    ###to handle the end
    if settings.current_level == 14:
        screen.fill((0,0,0))
        if settings.exp_ind <= 113:
            for i in exp_list:
                screen.blit(i.animation_list[int(settings.exp_ind)], (0, 0))
            
            settings.exp_ind += 1
        else:
            text_list[settings.current_level].draw(screen)

    

def move_ents(ent_list, settings):
    for ent in ent_list:
        ent.move(ent_list)
    
    settings.trail_count += 1
    for index, ent in enumerate(ent_list):
        if type(ent) == Ship and ent.is_alive == True: #create list of points for light trail
            if settings.trail_count >= 3:
                settings.trail_points[index].append((ent.rect.x + 0.5*ent.rect.w, ent.rect.y+0.5*ent.rect.h))
    if settings.trail_count >= 3:
        settings.trail_count = 0
        
    if settings.level_list[settings.current_level].win_cond(settings.level_list[settings.current_level], settings):
        settings.current_level += 1
        settings.trail_points = []
        settings.prev_trail_points = []
        settings.load_level()

if __name__ == "__main__":
    #Start_Menu()
    main()