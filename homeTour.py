#!/usr/bin/env python
# coding=utf-8
__author__ = 'Vaijayanthi Mala K'
__date__   = '14-Feb-2018'

import pygame, os
from pygame.locals import *
import sys, time, bg, pyganim, menu, items

# define some constants
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# set up the window
WINDOWWIDTH = 545
WINDOWHEIGHT = 500
MINWINDOWHEIGHT = 448

red = (205,85,85)
bright_red = (255,0,0)
black = (0,0,0)
green = (0,200,0)
bright_green = (0,255,0)
bgColor = (238,232,170)
pickList = []

class MainHouse:
	def __init__(self, room=None, pickItem=None):
	
		global playerHint
		global pickList
		x = 500 # x and y are the sprite's position
		y = 120
		WALKRATE = 4
		RUNRATE = 12
		
		windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
		pygame.display.set_caption('Welcome Home')
		if(pickItem == 'reset'):
			pickList = []
		
		playerHint = 'crono'
		bgHall = 'bg_hall.jpg'
		
		if(pickItem == "desk"):
			playerHint = 'desk/cronoDesk'
			bgHall = 'bg_hallDesk.jpg'
			x = 446
			y = 327
		elif(pickItem == "food"):
			playerHint = 'food/cronoFood'
			bgHall = 'bg_hallFood.jpg'
			x = 404
			y = 32
		elif(pickItem == "mat"):
			playerHint = 'mat/cronoMat'
			bgHall = 'bg_hallMat.jpg'
			x = 308
			y = 132
				
		def callSpriteAnimation(character):
			global moveConductor, front_standing, back_standing, left_standing, right_standing, playerWidth, playerHeight, animObjs
			# load the "standing" sprites (these are single images, not animations)
			front_standing = pygame.image.load(os.path.join('resources', character+"_front.gif"))
			back_standing = pygame.image.load(os.path.join('resources', character+"_back.gif"))
			left_standing = pygame.image.load(os.path.join('resources', character+"_left.gif"))
			right_standing = pygame.transform.flip(left_standing, True, False)

			playerWidth, playerHeight = front_standing.get_size()

			# creating the PygAnimation objects for walking/running in all directions
			animTypes = 'back_run back_walk front_run front_walk left_run left_walk'.split()
			animObjs = {}
			for animType in animTypes:
				imagesAndDurations = [((os.path.join('resources','%s_%s.%s.gif')) % (str(character), animType, str(num).rjust(3, '0')), 0.1) for num in range(6)]
				animObjs[animType] = pyganim.PygAnimation(imagesAndDurations)

			# create the right-facing sprites by copying and flipping the left-facing sprites
			animObjs['right_walk'] = animObjs['left_walk'].getCopy()
			animObjs['right_walk'].flip(True, False)
			animObjs['right_walk'].makeTransformsPermanent()
			animObjs['right_run'] = animObjs['left_run'].getCopy()
			animObjs['right_run'].flip(True, False)
			animObjs['right_run'].makeTransformsPermanent()

			# have the animation objects managed by a conductor.
			# With the conductor, we can call play() and stop() on all the animtion
			# objects at the same time, so that way they'll always be in sync with each
			# other.
			moveConductor = pyganim.PygConductor(animObjs)
			
		callSpriteAnimation(playerHint)
		direction = DOWN # sprites starts off facing down (front)
		mainClock = pygame.time.Clock()
		

		running = moveUp = moveDown = moveLeft = moveRight = False
		print (room)
		
		if(room == 'hall'):
			x = 302
			y = 203
		elif(room == 'kitchen'):
			x = 294
			y = 51
		elif(room == 'bedroom'):
			x = 126
			y = 87
		elif(room == 'bathroom'):
			x = 66
			y = 303

		# Load the background Image according to the sprites coordinations
		def changeBackground(bgImage):
			BackGround = bg.Background(bgImage, [0,0])
			windowSurface.fill(bgColor)
			windowSurface.blit(BackGround.image, BackGround.rect)
		
		def textObjects(text, font):
			textSurface = font.render(text, True, black)
			return textSurface, textSurface.get_rect()
		
		def button(msg,x,y,w,h,ic,ac,action=None):
			mouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			if x+w > mouse[0] > x and y+h > mouse[1] > y:
				pygame.draw.rect(windowSurface, ac,(x,y,w,h))

				if click[0] == 1 and action != None:
					action()         
			else:
				pygame.draw.rect(windowSurface, ic,(x,y,w,h))

			smallText = pygame.font.Font('resources/ComicSansMSRegular.ttf',20)
			textSurf, textRect = textObjects(msg, smallText)
			textRect.center = ( (x+(w/2)), (y+(h/2)) )
			windowSurface.blit(textSurf, textRect)
		
		def navigateBack():
			menu.HouseMenu()
			
		def navigateItem():
			items.Item(pickList)
			
		def quitGame():
			pygame.quit()
			sys.exit()
					
			
		while True:
			#Set Background
			if x >= 500:
				if(len(pickList) >0 and "desk" in pickList and 'food' in pickList and 'mat' in pickList):
					changeBackground('resources/bg_finalInitial.jpg')
				else:
					changeBackground('resources/bg.jpg')
			elif (((x >= 170 and x < 500) and (y >= 100 and y <= 378)) or
				  ((x >= 374 and x <= 496) and (y >=0 and y <= 120))):
				#print(pickList)
				if(len(pickList) >0):
					if(pickItem == None):
						if ('desk' in pickList and 'food' not in pickList and 'mat' not in pickList):
							bgHall = 'bg_hallDesk1.jpg'
						elif ('food' in pickList and 'desk' not in pickList and 'mat' not in pickList):
							bgHall = 'bg_hallFood1.jpg'
						elif ('mat' in pickList and 'desk' not in pickList and 'food' not in pickList):
							bgHall = 'bg_hallMat1.jpg'
						elif ('desk' in pickList and 'food' in pickList and 'mat' not in pickList):
							bgHall = 'bg_hallDeskFood.jpg'
						elif ('desk' in pickList and 'mat' in pickList and 'food' not in pickList):
							bgHall = 'bg_hallDeskMat.jpg'
						elif ('food' in pickList and 'mat' in pickList and 'desk' not in pickList):
							bgHall = 'bg_hallFoodMat.jpg'
						elif ('desk' in pickList and 'food' in pickList and 'mat' in pickList):
							bgHall = 'bg_finalInitialHall.jpg'
					else:
						if(pickItem == "desk" and 'food' in pickList and 'mat' not in pickList):
							bgHall = 'bg_hallFoodDesk.jpg'
						elif(pickItem == "desk" and 'mat' in pickList and 'food' not in pickList):
							bgHall = 'bg_hallDeskMat1.jpg'
						elif(pickItem == "desk" and 'mat' in pickList and 'food' in pickList):
							bgHall = 'bg_hallFoodMat2.jpg'
						elif(pickItem == "food" and 'desk' in pickList and 'mat' not in pickList):
							bgHall = 'bg_hallDeskFood1.jpg'
						elif(pickItem == "food" and 'mat' in pickList and 'desk' not in pickList):
							bgHall = 'bg_hallFoodMat1.jpg'
						elif(pickItem == "food" and 'mat' in pickList and 'desk' in pickList):
							bgHall = 'bg_hallDeskMat2.jpg'
						elif(pickItem == "mat" and 'desk' in pickList and 'food' not in pickList):
							bgHall = 'bg_hallMatDesk.jpg'
						elif(pickItem == "mat" and 'food' in pickList and 'desk' not in pickList):
							bgHall = 'bg_hallMatFood.jpg'
						elif(pickItem == "mat" and 'food' in pickList and 'desk' in pickList):
							bgHall = 'bg_hallFoodDesk1.jpg'
				
				
				changeBackground('resources/'+bgHall)
			elif ((x >= 188 and x <=376) and (y >= 0 and y<= 186)):
				if((pickItem != None and pickItem != 'reset') and (pickItem != 'desk' and pickItem != 'mat') and pickItem not in pickList):
					pickList.append(pickItem)
					pickItem=None
								
				if(len(pickList) ==0):
					if (pickItem == 'desk'):
						bgKitchen = 'bg_pickKitchenDesk.jpg'
					elif (pickItem == 'mat'):
						bgKitchen = 'bg_pickKitchenMat.jpg'
					else:
						bgKitchen = 'bg_kitchen.jpg'
						
				if (len(pickList) >0):
					if(pickItem == None):
						if ('desk' in pickList and 'food' not in pickList and 'mat' not in pickList):
							bgKitchen = 'bg_kitchenDesk.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('food' in pickList and 'desk' not in pickList and 'mat' not in pickList):
							bgKitchen = 'bg_kitchenFood.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('mat' in pickList and 'desk' not in pickList and 'food' not in pickList):
							bgKitchen = 'bg_kitchenMat.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('desk' in pickList and 'food' in pickList and 'mat' not in pickList):
							bgKitchen = 'bg_kitchenDeskFood.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('desk' in pickList and 'mat' in pickList and 'food' not in pickList):
							bgKitchen = 'bg_kitchenDeskMat.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('food' in pickList and 'mat' in pickList and 'desk' not in pickList):
							bgKitchen = 'bg_kitchenFoodMat.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('desk' in pickList and 'food' in pickList and 'mat' in pickList):
							bgKitchen = 'bg_finalInitialKitchen.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						else:
							bgKitchen = 'bg_kitchen.jpg'
					else:
						if(pickItem == "desk" and 'food' in pickList and 'mat' not in pickList):
							bgKitchen = 'bg_pickKitchenFood1.jpg'
						elif(pickItem == "desk" and 'mat' in pickList and 'food' not in pickList):
							bgKitchen = 'bg_pickKitchenMat1.jpg'
						elif(pickItem == "desk" and 'mat' in pickList and 'food' in pickList):
							bgKitchen = 'bg_pickKitchenMatFood1.jpg'
						elif(pickItem == "mat" and 'desk' in pickList and 'food' not in pickList):
							bgKitchen = 'bg_pickKitchenDes2.jpg'
						elif(pickItem == "mat" and 'food' in pickList and 'desk' not in pickList):
							bgKitchen = 'bg_pickKitchenFood2.jpg'
						elif(pickItem == "mat" and 'food' in pickList and 'desk' in pickList):
							bgKitchen = 'bg_pickKitchenDeskFood.jpg'
					
					
				changeBackground('resources/'+bgKitchen)
			elif ((x >=0 and x <= 184) and (y >=0 and y <= 218)):
				if((pickItem != None and pickItem != 'reset') and (pickItem != 'food' and pickItem != 'mat') and pickItem not in pickList):
					pickList.append(pickItem)
					pickItem=None
				
				if(len(pickList) ==0):
					if (pickItem == 'food'):
						bgBedRoom = 'bg_pickBedFood.jpg'
					elif (pickItem == 'mat'):
						bgBedRoom = 'bg_pickBedMat.jpg'
					else:
						bgBedRoom = 'bg_bedroom.jpg'

				if (len(pickList) >0):
					if (pickItem == None):
						if ('desk' in pickList and 'food' not in pickList and 'mat' not in pickList):
							bgBedRoom = 'bg_bedroomDesk.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('food' in pickList and 'desk' not in pickList and 'mat' not in pickList):
							bgBedRoom = 'bg_bedroomFood.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('mat' in pickList and 'desk' not in pickList and 'food' not in pickList):
							bgBedRoom = 'bg_bedroomMat.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('desk' in pickList and 'food' in pickList and 'mat' not in pickList):
							bgBedRoom = 'bg_bedroomDeskFood.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('desk' in pickList and 'mat' in pickList and 'food' not in pickList):
							bgBedRoom = 'bg_bedroomDeskMat.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('food' in pickList and 'mat' in pickList and 'desk' not in pickList):
							bgBedRoom = 'bg_bedroomFoodMat.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('desk' in pickList and 'food' in pickList and 'mat' in pickList):
							bgBedRoom = 'bg_finalInitialBed.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						else:
							bgBedRoom = 'bg_bedroom.jpg'
					else:		
						if(pickItem == "food" and 'desk' in pickList and 'mat' not in pickList):
							bgBedRoom = 'bg_pickBedDesk1.jpg'
						elif(pickItem == "food" and 'mat' in pickList and 'desk' not in pickList):
							bgBedRoom = 'bg_pickBedMat1.jpg'
						elif(pickItem == "food" and 'mat' in pickList and 'desk' in pickList):
							bgBedRoom = 'bg_pickBedDeskMat1.jpg'
						elif(pickItem == "mat" and 'desk' in pickList and 'food' not in pickList):
							bgBedRoom = 'bg_pickBedDesk2.jpg'
						elif(pickItem == "mat" and 'food' in pickList and 'desk' not in pickList):
							bgBedRoom = 'bg_pickBedFood2.jpg'
						elif(pickItem == "mat" and 'food' in pickList and 'desk' in pickList):
							bgBedRoom = 'bg_pickBedDeskFood2.jpg'

				changeBackground('resources/'+bgBedRoom)
			elif ((x >=0 and x <= 168) and (y >= 220 and y <=378)):
				if((pickItem != None and pickItem != 'reset') and (pickItem != 'desk' and pickItem != 'food') and pickItem not in pickList):
					pickList.append(pickItem)
					pickItem=None
							
				if(len(pickList) ==0):
					if (pickItem == 'desk'):
						bgBathRoom = 'bg_pickBathDesk.jpg'
					elif (pickItem == 'food'):
						bgBathRoom = 'bg_pickBathFood.jpg'
					else:
						bgBathRoom = 'bg_bathroom.jpg'

				if (len(pickList) >0):
					if(pickItem == None):
						if ('desk' in pickList and 'food' not in pickList and 'mat' not in pickList):
							bgBathRoom = 'bg_bathroomDesk.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('food' in pickList and 'desk' not in pickList and 'mat' not in pickList):
							bgBathRoom = 'bg_bathroomFood.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('mat' in pickList and 'desk' not in pickList and 'food' not in pickList):
							bgBathRoom = 'bg_bathroomMat.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('desk' in pickList and 'food' in pickList and 'mat' not in pickList):
							bgBathRoom = 'bg_bathroomDeskFood.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('desk' in pickList and 'mat' in pickList and 'food' not in pickList):
							bgBathRoom = 'bg_bathroomDeskMat.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('food' in pickList and 'mat' in pickList and 'desk' not in pickList):
							bgBathRoom = 'bg_bathroomFoodMat.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						elif ('desk' in pickList and 'food' in pickList and 'mat' in pickList):
							bgBathRoom = 'bg_finalInitialBath.jpg'
							playerHint = 'crono'
							callSpriteAnimation(playerHint)
						else:
							bgBathRoom = 'bg_bathroom.jpg'
					else:
						if(pickItem == "desk" and 'food' in pickList and 'mat' not in pickList):
							bgBathRoom = 'bg_pickBathFood1.jpg'
						elif(pickItem == "desk" and 'mat' in pickList and 'food' not in pickList):
							bgBathRoom = 'bg_pickBathMat1.jpg'
						elif(pickItem == "desk" and 'mat' in pickList and 'food' in pickList):
							bgBathRoom = 'bg_pickBathMatFood1.jpg'
						elif(pickItem == "food" and 'desk' in pickList and 'mat' not in pickList):
							bgBathRoom = 'bg_pickBathDesk2.jpg'
						elif(pickItem == "food" and 'mat' in pickList and 'desk' not in pickList):
							bgBathRoom = 'bg_pickBathMat3.jpg'
						elif(pickItem == "food" and 'mat' in pickList and 'desk' in pickList):
							bgBathRoom = 'bg_pickBathMatDesk1.jpg'
					
				changeBackground('resources/'+bgBathRoom)  
					
			#print(x,y)
			#pygame.display.flip()
			for event in pygame.event.get(): # event handling loop

				# handle ending the program
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						pygame.quit()
						sys.exit()

					if event.key in (K_LSHIFT, K_RSHIFT):
						# sprites has started running
						running = True

					if event.key == K_UP:
						moveUp = True
						moveDown = False
						if not moveLeft and not moveRight:
							# only change the direction to up if the sprites wasn't moving left/right
							direction = UP
					elif event.key == K_DOWN:
						moveDown = True
						moveUp = False
						if not moveLeft and not moveRight:
							direction = DOWN
					elif event.key == K_LEFT:
						moveLeft = True
						moveRight = False
						if not moveUp and not moveDown:
							direction = LEFT
					elif event.key == K_RIGHT:
						moveRight = True
						moveLeft = False
						if not moveUp and not moveDown:
							direction = RIGHT

				elif event.type == KEYUP:
					if event.key in (K_LSHIFT, K_RSHIFT):
						# sprites has stopped running
						running = False

					if event.key == K_UP:
						moveUp = False
						# if the sprites was moving in a sideways direction before, change the direction the sprites is facing.
						if moveLeft:
							direction = LEFT
						if moveRight:
							direction = RIGHT
					elif event.key == K_DOWN:
						moveDown = False
						if moveLeft:
							direction = LEFT
						if moveRight:
							direction = RIGHT
					elif event.key == K_LEFT:
						moveLeft = False
						if moveUp:
							direction = UP
						if moveDown:
							direction = DOWN
					elif event.key == K_RIGHT:
						moveRight = False
						if moveUp:
							direction = UP
						if moveDown:
							direction = DOWN

			if moveUp or moveDown or moveLeft or moveRight:
				# draw the correct walking/running sprite from the animation object
				moveConductor.play() # calling play() while the animation objects are already playing is okay; in that case play() is a no-op
				if running:
					if direction == UP:
						animObjs['back_run'].blit(windowSurface, (x, y))
					elif direction == DOWN:
						animObjs['front_run'].blit(windowSurface, (x, y))
					elif direction == LEFT:
						animObjs['left_run'].blit(windowSurface, (x, y))
					elif direction == RIGHT:
						animObjs['right_run'].blit(windowSurface, (x, y))
				else:
					# walking
					if direction == UP:
						animObjs['back_walk'].blit(windowSurface, (x, y))
					elif direction == DOWN:
						animObjs['front_walk'].blit(windowSurface, (x, y))
					elif direction == LEFT:
						animObjs['left_walk'].blit(windowSurface, (x, y))
					elif direction == RIGHT:
						animObjs['right_walk'].blit(windowSurface, (x, y))


				# actually move the position of the sprites
				if running:
					rate = RUNRATE
				else:
					rate = WALKRATE

				if moveUp:
					y -= rate
				if moveDown:
					y += rate
				if moveLeft:
					x -= rate
				if moveRight:
					x += rate

			else:
				# standing still
				moveConductor.stop() # calling stop() while the animation objects are already stopped is okay; in that case stop() is a no-op
				if direction == UP:
					windowSurface.blit(back_standing, (x, y))
				elif direction == DOWN:
					windowSurface.blit(front_standing, (x, y))
				elif direction == LEFT:
					windowSurface.blit(left_standing, (x, y))
				elif direction == RIGHT:
					windowSurface.blit(right_standing, (x, y))

			# make sure the sprites does move off the screen
			if x < 0:
				x = 0
			if x > WINDOWWIDTH - playerWidth:
				x = WINDOWWIDTH - playerWidth
			if y < 0:
				y = 0
			if y > MINWINDOWHEIGHT - playerHeight:
				y = MINWINDOWHEIGHT - playerHeight

            #Back Button
			button("Pick Item",100,450,100,45,green,bright_green,navigateItem)
			button("Back",250,450,100,45,red,bright_red,navigateBack)
			button("Exit",400,450,100,45,red,bright_red,quitGame)
			pygame.display.flip()
			mainClock.tick(30) 
