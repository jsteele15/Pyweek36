import pygame
from pathlib import Path

try:
    pygame.mixer.init()
    sound =  True
except:
    sound = False
###before doing anything music related, put it in an if statment

class Music_Sound:
    def __init__(self, tag, file_loc):
        self.tag = tag
        self.file_loc = file_loc
        
    def play(self):
        name = pygame.mixer.Sound(self.file_loc)
        ###zero indicates the background tracks that will play on loop
        if self.tag == 0:
            name.play(-1)
        ###1 is for the sound effects, thisll play once  
        if self.tag == 1:
            name.play()
            
    def load(self):
        ###need to load a track first before playing it
        pygame.mixer.music.load(self.file_loc)

#track.play()
#track = Music_Sound("./res/Dark Matter Long.wav") ##an example of how this will work 
#track.Load() this is to load what ever track has been made
#load the track then play it