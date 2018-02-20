#!/usr/bin/env python
# coding=utf-8
__author__ = 'Vaijayanthi Mala Kesavan'
__date__   = '14-Feb-2018'

import pygame, sys
import mainMenu, menu
 
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
  
class HelpMenu:
	def __init__(self):
		helpWinSur = pygame.display.set_mode((display_width,display_height))
		pygame.display.set_caption('Home Tour - Help')
		clock = pygame.time.Clock()

		def showText(text, font, color):
			textSurface = font.render(text, True, color)
			return textSurface, textSurface.get_rect()
			
		def createButton(msg,x,y,w,h,ic,ac,action=None):
			mouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			if x+w > mouse[0] > x and y+h > mouse[1] > y:
				pygame.draw.rect(helpWinSur, ac,(x,y,w,h))

				if click[0] == 1 and action != None:
					action()         
			else:
				pygame.draw.rect(helpWinSur, ic,(x,y,w,h))

			smallText = pygame.font.Font('resources/ComicSansMSRegular.ttf',20)
			textSurf, textRect = showText(msg, smallText, black)
			textRect.center = ( (x+(w/2)), (y+(h/2)) )
			helpWinSur.blit(textSurf, textRect)
			
		def letMeIn():
			menu.HouseMenu()
			
		def help():
			helpMe = True
			while helpMe:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
						
				helpWinSur.fill(bgColor)
				fontStyle = pygame.font.Font('resources/ComicSansMSRegular.ttf',40)
				TextSurf, TextRect = showText("Help", fontStyle, black)
				TextRect.center = ((display_width/2),(display_height/10))
				helpWinSur.blit(TextSurf, TextRect)
				
				messageToScreen("* Use Mouse to access the Sub Menus", 18, black, 30, 100)
				messageToScreen("* Use UP / DOWN / LEFT / RIGHT keys to ", 18, black, 30, 150)
				messageToScreen("    move the character in the house", 18, black, 30, 170)
				messageToScreen("* Use 'Choose Room' menu to navigate directly ", 18, black, 30, 220)
				messageToScreen("    into any desier room", 18, black, 30, 240)
				messageToScreen("* Use 'Pick Item' menu to pick the item to be placed ", 18, black, 30, 290)
				messageToScreen("    in the respective rooms", 18, black, 30, 310)
				createButton("Back",180,370,150,50,red,bright_red,returnBack)
			
				pygame.display.flip()
				clock.tick(15)
			
		def quitMenu():
			pygame.quit()
			sys.exit()

		def messageToScreen(msg, size, color, x, y):
			myfont = pygame.font.SysFont("Comic Sans MS", size)
			label = myfont.render(msg, 1, color)
			helpWinSur.blit(label, (x, y))
		
		def returnBack():
			helpWindow()
			
		def aboutMe():
			aboutMe = True
			while aboutMe:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
						
				helpWinSur.fill(bgColor)
				fontStyle = pygame.font.Font('resources/ComicSansMSRegular.ttf',40)
				TextSurf, TextRect = showText("About", fontStyle, black)
				TextRect.center = ((display_width/2),(display_height/10))
				helpWinSur.blit(TextSurf, TextRect)
				
				
				messageToScreen("Python v3.6.4 & Pygame v1.9.2", 20, black, 30, 100)
				messageToScreen("Developed on : "+__date__, 20, black, 30, 150)
				messageToScreen("Author: "+__author__, 20, black, 30, 200)
				messageToScreen("Email:    vaijayanthi.k@lntinfotech.com", 20, black, 30, 250)
				createButton("Back",180,350,150,50,red,bright_red,returnBack)
			
				pygame.display.flip()
				clock.tick(15)
			
		def helpWindow():
			intro = True
			while intro:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
						
				helpWinSur.fill(bgColor)
				fontStyle = pygame.font.Font('resources/ComicSansMSRegular.ttf',40)
				TextSurf, TextRect = showText("Help Menu", fontStyle, black)
				TextRect.center = ((display_width/2),(display_height/10))
				helpWinSur.blit(TextSurf, TextRect)

				createButton("About",150,120,250,50,green,bright_green,aboutMe)
				createButton("Help",150,180,250,50,green,bright_green,help)
				createButton("Let Me In",150,240,250,50,green,bright_green,letMeIn)
				createButton("Exit",150,300,250,50,red,bright_red,quitMenu)

				pygame.display.flip()
				clock.tick(15)

		#aboutMe()
		helpWindow()
		#pygame.quit()
		#quit()
