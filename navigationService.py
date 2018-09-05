from tkinter import *
import PIL
from PIL import ImageTk, Image
import os
import threading
import time
from queue import Queue
import json

import sys
import pygame
from pygame.locals import *

class NavigationService(threading.Thread):
    def run(self):
        pygame.init()
        pygame.font.init()
        
        chosenFont = pygame.font.get_default_font()
        fontRenderer = pygame.font.Font(chosenFont, 50) # Font, Size
        textOverlay = fontRenderer.render("Hi", 1, (255, 255, 255)) # Text, Anti Aliasing, RGB
        
        #screen = pygame.display.set_mode((3200, 1800), 0, 32) # 1280, 1080 represents screen size
        #screen = pygame.display.set_mode((3200, 1800), pygame.FULLSCREEN) # 3200, 1800 represents screen size, this is the screen size of Dell XPS 15
        screen = pygame.display.set_mode((1500, 1000), pygame.NO_FRAME) # 720, 540 is raspberry pi screen size
        picture = pygame.image.load("navigation_pictures/0.png")
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                        
        
            screen.blit(picture, (0, 0)) # x, y represents image location
            screen.blit(textOverlay, (350, 350)) # x, y represents font location
            pygame.display.flip()


    def update_picture(self, data):
        print("Processing notification")
        
        json_string = data.decode("utf-8")
        print(json_string)
        navigation_data = json.loads(json_string)
        
        angle = float(navigation_Data["text"])
        
        # positive angle means left, negative angle means right
        if(angle > -22.5 and angle <= 22.5):
            picture = pygame.image.load("navigation_pictures/0.png")
        elif(angle > 22.5 and angle <= 67.5):
            picture = pygame.image.load("navigation_pictures/1.png")
        elif(angle > 67.5 and angle <= 112.5):
            picture = pygame.image.load("navigation_pictures/2.png")
        elif(angle > 112.5 and angle <= 157.5):
            picture = pygame.image.load("navigation_pictures/3.png")
        elif(angle > 157.5 or angle <= -157.5):
            picture = pygame.image.load("navigation_pictures/4.png")
        elif(angle > -157.5 and angle <= -112.5):
            picture = pygame.image.load("navigation_pictures/5.png")
        elif(angle > -112.5 and angle <= -67.5):
            picture = pygame.image.load("navigation_pictures/6.png")
        elif(angle > -67.5 and angle <= -22.5):
            picture = pygame.image.load("navigation_pictures/7.png")