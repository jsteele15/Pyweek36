import pygame
from pathlib import Path
"""
pygame.mixer.init()

class Music_Sound:
    def __init__(self, tag, file_loc):
        self.tag
        self.file_loc = file_loc
        
    def Play(self):
        name = pygame.mixer.Sound(self.file_loc)
        ###zero indicates the background tracks that will play on loop
        if self.tag == 0:
            name.play(-1)
        ###1 is for the sound effects, thisll play once  
        if self.tag == 1:
            name.play()
            
    def Load(self):
        ###need to load a track first before playing it
        pygame.mixer.music.load(self.file_loc)
"""

#track = Music_Sound("./res/tracklist_1.wav") ##an example of how this will work 
#track.Load() this is to load what ever track has been made
#load the track then play it