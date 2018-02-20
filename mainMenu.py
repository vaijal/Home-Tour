#!/usr/bin/env python
# coding=utf-8
__author__ = 'Vaijayanthi Mala Kesavan'
__date__   = '14-Feb-2018'

import pygame, sys, os, time, random
import helpMenu
 
display_width = 545
display_height = 448
 
black = (0,0,0)
white = (255,255,255)
red = (205,85,85)
green = (0,200,0)
bgColor = (238,232,170)

bright_red = (255,0,0)
bright_green = (0,255,0)
 
block_color = (53,115,255)
  
class MainMenu:
	def __init__(self):
		windowSur = pygame.display.set_mode((display_width,display_height))
		pygame.display.set_caption('Welcome - Home Tour')
		clock = pygame.time.Clock()
		
		#BG Sound
		pygame.init()
		pygame.mixer.music.load(os.path.join('resources','sound/littleidea.mp3'))
		pygame.mixer.music.play(-1, 0.0)
		pygame.mixer.music.set_volume(0.25)

		def house_image_display(image):
			houseImage = pygame.image.load(image)
			windowSur.blit(houseImage, (90,100))

		def showText(text, font):
			textSurface = font.render(text, True, black)
			return textSurface, textSurface.get_rect()
		
		def messageToScreen(msg, size, color, x, y):
			myfont = pygame.font.SysFont("Comic Sans MS", size)
			label = myfont.render(msg, 1, color)
			windowSur.blit(label, (x, y))
			
		def createButton(msg,x,y,w,h,ic,ac,action=None):
			mouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			if x+w > mouse[0] > x and y+h > mouse[1] > y:
				pygame.draw.rect(windowSur, ac,(x,y,w,h))

				if click[0] == 1 and action != None:
					action()         
			else:
				pygame.draw.rect(windowSur, ic,(x,y,w,h))

			smallText = pygame.font.Font('resources/ComicSansMSRegular.ttf',20)
			textSurf, textRect = showText(msg, smallText)
			textRect.center = ( (x+(w/2)), (y+(h/2)) )
			windowSur.blit(textSurf, textRect)
			
		def subMenu():
			helpMenu.HelpMenu()
			
		def quitMenu():
			pygame.quit()
			sys.exit()
				
		def startWindow():

			intro = True

			while intro:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
						
				windowSur.fill(bgColor)
				house_image_display('resources/house1.png')
				fontStyle = pygame.font.Font('resources/ComicSansMSRegular.ttf',40)
				TextSurf, TextRect = showText("Welcome to Home Tour", fontStyle)
				TextRect.center = ((display_width/2),(display_height/10))
				windowSur.blit(TextSurf, TextRect)

				createButton("Menu",80,350,100,50,green,bright_green,subMenu)
				createButton("Exit",350,350,100,50,red,bright_red,quitMenu)
				messageToScreen("Created By:- "+__author__, 20, black, 100, 415)

				pygame.display.flip()
				clock.tick(15)

		startWindow()
		pygame.quit()
		quit()
