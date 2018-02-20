#!/usr/bin/env python
# coding=utf-8
__author__ = 'Vaijayanthi Mala K'
__date__   = '14-Feb-2018'

import pygame, menu, homeTour, sys

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


class Item:
	def __init__(self, pickList):
		menuDisplay = pygame.display.set_mode((display_width,display_height))
		pygame.display.set_caption('Home Tour - Pick Item')
		clock = pygame.time.Clock()
		
		def textObjects(text, font):
			textSurface = font.render(text, True, black)
			return textSurface, textSurface.get_rect()
		  
		def pickDesk():
			homeTour.MainHouse('', 'desk')
			  
		def pickFood():
			homeTour.MainHouse('', 'food')
			
		def pickMat():
			homeTour.MainHouse('', 'mat')
		
		def resetItems():
			homeTour.MainHouse('', 'reset')
			
		def backToMainMenu():
			menu.HouseMenu()
						
		def quitGame():
			pygame.quit()
			sys.exit()
		
		def button(msg,x,y,w,h,ic,ac,action=None):
			mouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			if x+w > mouse[0] > x and y+h > mouse[1] > y:
				pygame.draw.rect(menuDisplay, ac,(x,y,w,h))

				if click[0] == 1 and action != None:
					action()         
			else:
				pygame.draw.rect(menuDisplay, ic,(x,y,w,h))

			smallText = pygame.font.Font('resources/ComicSansMSRegular.ttf',20)
			textSurf, textRect = textObjects(msg, smallText)
			textRect.center = ( (x+(w/2)), (y+(h/2)) )
			menuDisplay.blit(textSurf, textRect)	
			
		def loadSubMenu():
			menu = True
			while menu:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						quit()
						
				menuDisplay.fill(bgColor)
				largeText = pygame.font.Font('resources/ComicSansMSRegular.ttf',40)
				TextSurf, TextRect = textObjects("Pick Item", largeText)
				TextRect.center = ((display_width/2),(display_height/10))
				menuDisplay.blit(TextSurf, TextRect)
				
				if('desk' not in pickList):
					button("Desk => To be placed in Bed Room",100,100,350,50,green,bright_green,pickDesk)
					
				if('food' not in pickList):
					button("Food => To be placed in Kitchen Room",100,160,350,50,green,bright_green,pickFood)
				
				if('mat' not in pickList):
					button("Mat  => To be placed in Bath Room",100,220,350,50,green,bright_green,pickMat)
				
				if('desk' in pickList and 'food' in pickList and 'mat' in pickList):
					button("Reset Items",100,220,350,50,green,bright_green,resetItems)
				
				button("Back to Main Menu",100,280,350,50,green,bright_green,backToMainMenu)
				button("Exit",100,340,350,50,red,bright_red,quitGame)

				pygame.display.flip()
				clock.tick(15)
				
		loadSubMenu()
		pygame.quit()
		quit()
