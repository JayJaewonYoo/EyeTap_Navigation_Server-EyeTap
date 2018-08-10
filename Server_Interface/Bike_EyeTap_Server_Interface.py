import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

chosenFont = pygame.font.get_default_font()
fontRenderer = pygame.font.Font(chosenFont, 50) # Font, Size
textOverlay = fontRenderer.render("Hi", 1, (255, 255, 255)) # Text, Anti Aliasing, RGB

#screen = pygame.display.set_mode((3200, 1800), 0, 32) # 1280, 1080 represents screen size
#screen = pygame.display.set_mode((3200, 1800), pygame.FULLSCREEN) # 3200, 1800 represents screen size, this is the screen size of Dell XPS 15
screen = pygame.display.set_mode((720, 540), pygame.FULLSCREEN) # 720, 540 is raspberry pi screen size
picture = pygame.image.load("Test_Image.png")
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

## Original:
#pygame.init()
##screen = pygame.display.set_mode((3200, 1800), 0, 32) # 1280, 1080 represents screen size
#screen = pygame.display.set_mode((3200, 1800), pygame.FULLSCREEN) # 1280, 1080 represents screen size
#picture = pygame.image.load("Test_Image.png")
#while True:
#	for event in pygame.event.get():
#		if event.type == QUIT:
#			pygame.display.quit()
#			pygame.quit()
#			sys.exit()
#		if event.type == KEYDOWN:
#			pygame.display.quit()
#			pygame.quit()
#			sys.exit()
#				
#
#	screen.blit(picture, (0, 0)) # x, y represents image location
#	pygame.display.flip()
