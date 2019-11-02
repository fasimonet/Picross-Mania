#!usr/bin/python
# -*- coding: utf-8 -*- 

# py2048, clone of 2048 game
# (C) Jean Ingrasciotta 2016 ginoingras@gmail.com
# licencied under GPLV3
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    see COPYING file.
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

# How to contribute:
# see README.TXT
# check "FIXME:" in code
# check "WARNING:" in code
# check "TODO:" in code
# Sourceforge link: http://sourceforge.net/projects/py2048/
# github: git clone git://git.code.sf.net/p/py2048/code py2048-code
#
# report bug, comments and ideas at adresse below
# ginoingras@gmail.com 
#
# V0.1.0:
# add Small, Medium and Large preconfig Panel Game.
# add Hiscore for Small, Medium And Large Panel Game
# check for close windows as QUIT event.
# add Change theme screen BckGnd while one tile reach 1024, 2048, 4096, 8192.
# add counter move
#
# V0.1.2:
# compliant (at least) python3.4
# improve menu keys system
# add AI Auto Boot when press ENTER ( F2 switch 3 AI levels) 
# add 2 players Human/AI, see py2048.cfg for config keyboard player2
#
#FIXME:
#
#TODO:
# add hiTileMaxValue attached to hiScore Small/Medium/Large.
# AI boot sould be Level3 deep with more efficient if get no point at Level2, preserve "low tile scored free"
# have a saved game for each level
# save player name with HiScore
# add 2~4 multiplayers network (as my usual objective, but how 4 players to do with this game?)
# 

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
                        
try:
	import pygame
	from pygame.locals import *
	import sys, os, random, time, math

	import json
	
	#for network
	import platform, threading	
	import socket, urllib
	
	#local imports
	import py2048_VG as VG
	from py2048_sounds import *
	from py2048_threat import threat
	from py2048_Tab2Play import Tab2Play

	from py2048_Tab2PlayAI import Tab2PlayAI
	#import py2048_error

except ImportError:
	tb = sys.exc_info()
	tb = tb[1]
	#tb = tb[2]
	#print ("ERROR IMPORTING MODULES: %s" % message)
	print ("ERROR IMPORTING MODULES: %s" % tb)
	#raise SystemExit, "ERROR IMPORTING MODULES: %s" % tb
	raise SystemExit ("ERROR IMPORTING MODULES: %s" % tb)
	sys.exit(1)

try:
	with open("hiscores.json", "rt") as infile:
		temp = json.load(infile)
		VG.hiScore = temp[0]
		VG.hiMove = temp[1]
		VG.hiScoreSmall = temp[2]
		VG.hiMoveSmall = temp[3]
		VG.hiScoreMedium = temp[4]
		VG.hiMoveMedium = temp[5]
		VG.hiScoreLarge = temp[6]
		VG.hiMoveLarge = temp[7]
		VG.ParSizeActu = temp[8]
		
	if VG.ParSizeActu < 0:
		VG.ParSizeActu = 0
	if VG.ParSizeActu > 2:
		VG.ParSizeActu = 2
	if VG.ParSizeActu == 0:
		VG.hiScore = VG.hiScoreSmall
	if VG.ParSizeActu == 1:
		VG.hiScore = VG.hiScoreMedium
	if VG.ParSizeActu == 2:
		VG.hiScore = VG.hiScoreLarge

except:
	print ("WARNING: unable to load HiScore")
	VG.hiScore = 512
	VG.hiScoreSmall = 512
	VG.hiMoveSmall = 0
	VG.hiScoreMedium = 1024
	VG.hiMoveMedium = 0
	VG.hiScoreLarge = 2048
	VG.hiMoveLarge = 0
	VG.ParSizeActu = 0
	
	
#################################################
def wait_key():
	""" wait for a valide keyDown event """
	
	# 2nd Player AI
	#Tab2Play1.whoP1P2 = 1
	#Tab2Play1.howPlayer = 1
	#Tab2Play1.player2Human = True
	if (Tab2Play1.howPlayer == 2) and (Tab2Play1.whoP1P2 == 2) and (Tab2Play1.player2Human == False):
		wait_KeyDwn = False
		KeyCode = VG.autoAILevel
		return KeyCode
	
	KeyCode = ""
	wait_KeyDwn = True

	clock = pygame.time.Clock()

	while wait_KeyDwn:
		clock.tick(VG.ParFPS)
		Tab2Play1.update(fenetre)
		#Tab2Play1.updateTexts(fenetre)
		#showMenu()

		# if panel full, do not limit time to move
		if Tab2Play1.isFull():
			VG.LimitTime2Move = time.clock()
		elif VG.ParLimitTime2Move >0:
			if (VG.LimitTime2Move - time.clock()) <= 0 :
				VG.LimitTime2Move = time.clock() + VG.ParLimitTime2Move
				if VG.ParMusicYN:
					S_gong3.play()
				KeyCode = ""
				return KeyCode


		for event in pygame.event.get():
			if event.type == QUIT:
				#is_running = False
				wait_KeyDwn = False
				KeyCode = "QUIT"

			if event.type == MOUSEBUTTONDOWN:
				wait_KeyDwn = False
				
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					wait_KeyDwn = False
					KeyCode = "escape"
					VG.autoAIToggle = False

				if (Tab2Play1.whoP1P2 == 1) or ((Tab2Play1.whoP1P2 == 2) and (VG.ParP2UseArrow)):
					if event.key == K_UP:
						wait_KeyDwn = False
						KeyCode = "up"
					if event.key == K_DOWN:
						wait_KeyDwn = False
						KeyCode = "down"
					if event.key == K_LEFT:
						wait_KeyDwn = False
						KeyCode = "left"
					if event.key == K_RIGHT:
						wait_KeyDwn = False
						KeyCode = "right"
				
				#elif (Tab2Play1.whoP1P2 == 2) and not(VG.ParP2UseArrow):
				if (Tab2Play1.whoP1P2 == 2): # and not(VG.ParP2UseArrow):
					print (event.key)
					if event.key == ord(VG.ParP2Up):
						wait_KeyDwn = False
						KeyCode = "up"
					if event.key == ord(VG.ParP2Down):
						wait_KeyDwn = False
						KeyCode = "down"
					if event.key == ord(VG.ParP2Left):
						wait_KeyDwn = False
						KeyCode = "left"
					if event.key == ord(VG.ParP2Right):
						wait_KeyDwn = False
						KeyCode = "right"

				if event.key == K_F1:
					wait_KeyDwn = False
					KeyCode = "newGame"

				if event.key == K_F2:
					wait_KeyDwn = False
					KeyCode = "changeSize"

				if event.key == K_F7:
					wait_KeyDwn = False
					Tab2Play1.player2Human = not(Tab2Play1.player2Human)

				if event.key == K_F8:
					wait_KeyDwn = False
					Tab2Play1.howPlayer += 1
					if Tab2Play1.howPlayer >= 3:
						Tab2Play1.howPlayer = 1

				if event.key == K_F9:
					wait_KeyDwn = False
					KeyCode = VG.autoAILevel

				if event.key == K_F10:
					wait_KeyDwn = False
					if VG.autoAILevel == "ai3":
						VG.autoAILevel = "ai1"
					elif VG.autoAILevel == "ai2":
						VG.autoAILevel = "ai3"
					elif VG.autoAILevel == "ai1":
						VG.autoAILevel = "ai2"
						
				if event.key == K_RETURN:
					wait_KeyDwn = False
					VG.autoAIToggle = not(VG.autoAIToggle)

		if VG.autoAIToggle:
			wait_KeyDwn = False
			KeyCode = VG.autoAILevel

	return KeyCode

#################################################
def wait_any_key():
	""" wait for any key event """

	clock = pygame.time.Clock()

	for event in pygame.event.get(): #purge pygame event queue
		pass

	KeyCode = ""
	wait_KeyDwn = True
	while wait_KeyDwn:
		clock.tick(VG.ParFPS)
		#Tab2Play1.update(fenetre)
		Tab2Play1.updateTexts(fenetre)

		for event in pygame.event.get():
			if event.type == QUIT:
				#is_running = False
				wait_KeyDwn = False
				KeyCode = "QUIT"
			if event.type == KEYDOWN:
				wait_KeyDwn = False
				KeyCode = event.key

	wait_KeyUp = True
	while wait_KeyUp:
		if KeyCode == "QUIT":
			wait_KeyUp = False

		clock.tick(VG.ParFPS)
		#Tab2Play1.update(fenetre)
		Tab2Play1.updateTexts(fenetre)

		for event in pygame.event.get():
			if event.type == KEYUP:
				wait_KeyUp = False

	return KeyCode

#################################################
def save_hiscore(score):
	""" Save HiScore if new record """
	if VG.hiScore < score:
		VG.hiScore = score
		VG.hiMove = Tab2Play1.nbMove
		
	if (VG.ParSizeActu == 0) and (VG.hiScoreSmall < score):
		VG.hiScoreSmall = score
		VG.hiMoveSmall = Tab2Play1.nbMove
	if (VG.ParSizeActu == 1) and (VG.hiScoreMedium < score):
		VG.hiScoreMedium = score
		VG.hiMoveMedium = Tab2Play1.nbMove
	if (VG.ParSizeActu == 2) and (VG.hiScoreLarge < score):
		VG.hiScoreLarge = score
		VG.hiMoveLarge = Tab2Play1.nbMove

	try:
		with open('hiscores.json', 'w') as jsonfile:
			#json.dump(VG.hiScore, jsonfile)

			temp=[]				
			temp.append(VG.hiScore)
			temp.append(VG.hiMove)
			temp.append(VG.hiScoreSmall)
			temp.append(VG.hiMoveSmall)
			temp.append(VG.hiScoreMedium)
			temp.append(VG.hiMoveMedium)
			temp.append(VG.hiScoreLarge)
			temp.append(VG.hiMoveLarge)
			temp.append(VG.ParSizeActu)

			json.dump(temp, jsonfile)

	except:
		print ("WARNING: unable to write HiScore")

#################################################
def showMessage(msg1, msg2 = "", msg3 = "", msg4 = "", msg5 = "", msg6 = ""):
	""" Display a 2 lines message within panel game """
	textMsg = VG.minileter32.render(msg1, 1, VG.Black)
	textMsg2 = VG.minileter32.render(msg1, 1, VG.Yellow)
	fenetre.blit( textMsg, (0, (Tab2Play1.y*90) /3) )
	fenetre.blit( textMsg2, ( 0+2, ((Tab2Play1.y*90) /3) + 2) )

	textMsg3 = VG.minileter32.render(msg2, 1, VG.Black)
	textMsg4 = VG.minileter32.render(msg2, 1, VG.Yellow)
	fenetre.blit( textMsg3, (0, ((Tab2Play1.y*90) /3) + textMsg.get_rect()[3]) )
	fenetre.blit( textMsg4, ( 0+2, (((Tab2Play1.y*90) /3) + textMsg.get_rect()[3]) + 2) )

	textMsg5 = VG.minileter32.render(msg3, 1, VG.Black)
	textMsg6 = VG.minileter32.render(msg3, 1, VG.Yellow)
	fenetre.blit( textMsg5, (0, ((Tab2Play1.y*90) /3) + textMsg.get_rect()[3] + textMsg3.get_rect()[3]) )
	fenetre.blit( textMsg6, ( 0+2, (((Tab2Play1.y*90) /3) + textMsg.get_rect()[3] + textMsg3.get_rect()[3]) + 2) )

	textMsg7 = VG.minileter32.render(msg4, 1, VG.Black)
	textMsg8 = VG.minileter32.render(msg4, 1, VG.Yellow)
	fenetre.blit( textMsg7, (0, ((Tab2Play1.y*90) /3) + textMsg.get_rect()[3] + textMsg3.get_rect()[3] + textMsg5.get_rect()[3]) )
	fenetre.blit( textMsg8, ( 0+2, (((Tab2Play1.y*90) /3) + textMsg.get_rect()[3] + textMsg3.get_rect()[3] + textMsg5.get_rect()[3]) + 2) )

	textMsg9 = VG.minileter32.render(msg5, 1, VG.Black)
	textMsg10 = VG.minileter32.render(msg5, 1, VG.Yellow)
	fenetre.blit( textMsg9, (0, ((Tab2Play1.y*90) /3) + textMsg.get_rect()[3] + textMsg3.get_rect()[3] + textMsg5.get_rect()[3] + textMsg7.get_rect()[3]) )
	fenetre.blit( textMsg10, ( 0+2, (((Tab2Play1.y*90) /3) + textMsg.get_rect()[3] + textMsg3.get_rect()[3] + textMsg5.get_rect()[3] + textMsg7.get_rect()[3]) + 2) )

	textMsg11 = VG.minileter32.render(msg6, 1, VG.Black)
	textMsg12 = VG.minileter32.render(msg6, 1, VG.Yellow)
	fenetre.blit( textMsg11, (0, ((Tab2Play1.y*90) /3) + textMsg.get_rect()[3] + textMsg3.get_rect()[3] + textMsg5.get_rect()[3] + textMsg7.get_rect()[3] + textMsg9.get_rect()[3]) )
	fenetre.blit( textMsg12, ( 0+2, (((Tab2Play1.y*90) /3) + textMsg.get_rect()[3] + textMsg3.get_rect()[3] + textMsg5.get_rect()[3] + textMsg7.get_rect()[3] + textMsg9.get_rect()[3]) + 2) )

	pygame.display.flip()

#################################################
def showMenu():
	# display menu
	# showMessage("Esc=Quit", "N=New Game", "F1=New Small", "F2=New Medium", "F3=New Large", "Other=Resume")
	textMenu1 = VG.minileter28.render("Esc=Quit", 1, VG.Black)
	textMenu1a = VG.minileter28.render("Esc=Quit", 1, VG.Yellow)
	fenetre.blit( textMenu1, ( Tab2Play1.y*90 + 10, (Tab2Play1.y*90) /4) )
	fenetre.blit( textMenu1a, ( Tab2Play1.y*90 + 12, ((Tab2Play1.y*90) /4) + 2) )

	textMenu2 = VG.minileter28.render("N=New Game", 1, VG.Black)
	textMenu2a = VG.minileter28.render("N=New Game", 1, VG.Yellow)
	fenetre.blit( textMenu2, ( Tab2Play1.y*90 + 10, ((Tab2Play1.y*90) /4) + textMenu1.get_rect()[3]) )
	fenetre.blit( textMenu2a, ( Tab2Play1.y*90 + 12, (((Tab2Play1.y*90) /4) + textMenu1.get_rect()[3]) + 2) )

	textMenu3 = VG.minileter28.render("F1=New Small", 1, VG.Black)
	textMenu3a = VG.minileter28.render("F1=New Small", 1, VG.Yellow)
	fenetre.blit( textMenu3, ( Tab2Play1.y*90 + 10, ((Tab2Play1.y*90) /4) + textMenu1.get_rect()[3] + textMenu2.get_rect()[3]) )
	fenetre.blit( textMenu3a, ( Tab2Play1.y*90 + 12, (((Tab2Play1.y*90) /4) + textMenu1.get_rect()[3] + textMenu2.get_rect()[3]) + 2) )

	textMenu4 = VG.minileter28.render("F2=New Medium", 1, VG.Black)
	textMenu4a = VG.minileter28.render("F2=New Medium", 1, VG.Yellow)
	fenetre.blit( textMenu4, ( Tab2Play1.y*90 + 10, ((Tab2Play1.y*90) /4) + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3]) )
	fenetre.blit( textMenu4a, ( Tab2Play1.y*90 + 12, (((Tab2Play1.y*90) /4) + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3]) + 2) )

	textMenu5 = VG.minileter28.render("F3=New Large", 1, VG.Black)
	textMenu5a = VG.minileter28.render("F3=New Large", 1, VG.Yellow)
	fenetre.blit( textMenu5, ( Tab2Play1.y*90 + 10, ((Tab2Play1.y*90) /4) + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3]) )
	fenetre.blit( textMenu5a, ( Tab2Play1.y*90 + 12, (((Tab2Play1.y*90) /4) + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3]) + 2) )

	textMenu6 = VG.minileter28.render("F9=One Move AI", 1, VG.Black)
	textMenu6a = VG.minileter28.render("F9=One Move AI", 1, VG.Yellow)
	fenetre.blit( textMenu6, ( Tab2Play1.y*90 + 10, ((self.y*90) /4) + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] + textMenu5.get_rect()[3]) )
	fenetre.blit( textMenu6a, ( Tab2Play1.y*90 + 12, (((self.y*90) /4) + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] + textMenu5.get_rect()[3]) + 2) )

	textMenu7 = VG.minileter28.render("F10=AI level: %s" %(VG.autoAILevel), 1, VG.Black)
	textMenu7a = VG.minileter28.render("F10=AI level: %s" %(VG.autoAILevel), 1, VG.Yellow)
	fenetre.blit( textMenu7, ( Tab2Play1.y*90 + 10, ((self.y*90) /4) + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] + textMenu5.get_rect()[3] + textMenu6.get_rect()[3]) )
	fenetre.blit( textMenu7a, ( Tab2Play1.y*90 + 12, (((self.y*90) /4) + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] + textMenu5.get_rect()[3])  + textMenu6.get_rect()[3] + 2) )

	textMenu8 = VG.minileter28.render("ENTER=AutoAI: %s" %(VG.autoAIToggle), 1, VG.Black)
	textMenu8a = VG.minileter28.render("ENTER=AutoAI: %s" %(VG.autoAIToggle), 1, VG.Yellow)
	fenetre.blit( textMenu8, ( Tab2Play1.y*90 + 10, ((self.y*90) /4) + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] + textMenu5.get_rect()[3] + textMenu6.get_rect()[3] + textMenu7.get_rect()[3]) )
	fenetre.blit( textMenu8a, ( Tab2Play1.y*90 + 12, (((self.y*90) /4) + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] + textMenu5.get_rect()[3] + textMenu6.get_rect()[3] + textMenu7.get_rect()[3]) + 2) )

	pygame.display.flip()

#################################################
def changePanelSize(panelSize):
	""" change the panel game size, according pref in py2048.cfg """

	if panelSize < 0:
		panelSize = 0
	if panelSize > 2:
		panelSize = 2
	VG.ParSizeActu == panelSize

	if VG.ParSizeActu == 0:
		VG.ParRaws = VG.ParRawsSmall
		VG.ParColumns = VG.ParColumnsSmall
		VG.hiScore = VG.hiScoreSmall
		VG.hiMove = VG.hiMoveSmall
	if VG.ParSizeActu == 1:
		VG.ParRaws = VG.ParRawsMedium
		VG.ParColumns = VG.ParColumnsMedium
		VG.hiScore = VG.hiScoreMedium
		VG.hiMove = VG.hiMoveMedium
	if VG.ParSizeActu == 2:
		VG.ParRaws = VG.ParRawsLarge
		VG.ParColumns = VG.ParColumnsLarge
		VG.hiScore = VG.hiScoreLarge
		VG.hiMove = VG.hiMoveLarge

	tempMode = "Small"
	if VG.ParSizeActu == 1:
		tempMode = "Medium"
	if VG.ParSizeActu == 2:
		tempMode = "Large"

	#fenetre = pygame.display.set_mode((VG.ParColumns*90, VG.ParRaws*90 + 120))
	#pygame.display.set_mode((VG.ParColumns*90, VG.ParRaws*90 + 120))
	pygame.display.set_mode((VG.ParColumns*90 + 350, VG.ParRaws*90 + 160))

	VG.bckGnd0000 = pygame.image.load("Images/L0000.jpg")
	VG.bckGnd0000 = pygame.transform.scale(VG.bckGnd0000, (VG.ParColumns*90 + 350, VG.ParRaws*90 + 160))
	VG.bckGnd1024 = pygame.image.load("Images/L1024.jpg")
	VG.bckGnd1024 = pygame.transform.scale(VG.bckGnd1024, (VG.ParColumns*90 + 350, VG.ParRaws*90 + 160))
	VG.bckGnd2048 = pygame.image.load("Images/L2048.jpg")
	VG.bckGnd2048 = pygame.transform.scale(VG.bckGnd2048, (VG.ParColumns*90 + 350, VG.ParRaws*90 + 160))
	VG.bckGnd4096 = pygame.image.load("Images/L4096.jpg")
	VG.bckGnd4096 = pygame.transform.scale(VG.bckGnd4096, (VG.ParColumns*90 + 350, VG.ParRaws*90 + 160))
	VG.bckGnd8192 = pygame.image.load("Images/L8192.jpg")
	VG.bckGnd8192 = pygame.transform.scale(VG.bckGnd8192, (VG.ParColumns*90 + 350, VG.ParRaws*90 + 160))

	pygame.display.set_caption("py2048-v%s - Mode: %s" %(VG.py2048_version, tempMode))

#################################################
def newGame():
	""" reninit new panel game """
	
	Tab2Play1.newGame(x=VG.ParRaws, y=VG.ParColumns)
	Tab2Play1.newThreat()
	Tab2Play1.newThreat()
	#Tab2Play1.setHasMoved( False )
	Tab2Play1.update(fenetre)






pygame.init()

changePanelSize(VG.ParSizeActu)
#fenetre = pygame.display.set_mode((480,480))
#fenetre = pygame.display.set_mode((VG.ParColumns*90, VG.ParRaws*90 + 120))
fenetre = pygame.display.set_mode((VG.ParColumns*90 + 350, VG.ParRaws*90 + 160))

icone = pygame.image.load("Images/icone2048.png").convert_alpha()
pygame.display.set_icon(icone)
#pygame.mouse.set_visible(False)

pygame.mixer.init()
pygame.mixer.music.set_volume(VG.ParMusicVol)

if VG.ParMusicYN:
	#S_Menu.play()
	S_end1a.play()


Tab2Play1 = Tab2Play(x=VG.ParRaws, y=VG.ParColumns)
fenetre.blit(VG.bckGnd,(0,0))
if not(VG.ParAutoSaveOnExit):
	#welcome screen
	showMessage("See Config", "In py2048.cfg")
	time.sleep(0.2)
	wait_any_key()

	# New Game begin with 2 elements
	#Tab2Play1 = Tab2Play()
	Tab2Play1.newThreat()
	Tab2Play1.newThreat()
else:
	Tab2Play1.loadGame()
	
	Tab2Play1.update(fenetre)
	showMessage("Load Saved Game", "See py2048.cfg")
	time.sleep(0.2)
	wait_any_key()

Tab2Play1.setHasMoved( False )

clock = pygame.time.Clock()

VG.LimitTime2Move = time.clock() + VG.ParLimitTime2Move
if VG.ParLimitTime2Move >0:
	VG.ParAllowNoMove = True


isRunning = True
while isRunning:

	clock.tick(VG.ParFPS)

	Tab2Play1.update(fenetre)
	#showMenu()


	Tab2Play1AI = Tab2PlayAI(list(Tab2Play1.Tab2Play))

	#Tab2Play1.whoP1P2 = 1
	#Tab2Play1.howPlayer = 1
	#Tab2Play1.player2Human = True
	if Tab2Play1.howPlayer == 2:
		Tab2Play1.whoP1P2 += 1
		if Tab2Play1.whoP1P2 >= 3:
			Tab2Play1.whoP1P2 = 1


	KeyCode = wait_key()	
	print ("KeyCode: " + KeyCode)

	#otherwise shitch P1,P2 colors too fast
	Tab2Play1.updateTexts(fenetre)

	if KeyCode == "QUIT":
		if VG.ParAutoSaveOnExit:
			Tab2Play1.saveGame()
		isRunning = False
		break

	if KeyCode == "newGame":
	#elif retKey == K_F1: # NEW GAME
		save_hiscore(Tab2Play1.score)
		# New Game
		changePanelSize(VG.ParSizeActu)
		#fenetre = pygame.display.set_mode((VG.ParColumns*90, VG.ParRaws*90 + 120))
		fenetre = pygame.display.set_mode((VG.ParColumns*90 + 350, VG.ParRaws*90 + 160))
		KeyCode = ""
		Tab2Play1.newGame(x=VG.ParRaws, y=VG.ParColumns)
		#Tab2Play1 = Tab2Play()
		Tab2Play1.newThreat()
		Tab2Play1.newThreat()
		#Tab2Play1.setHasMoved( False )
		Tab2Play1.update(fenetre)
		VG.LimitTime2Move = time.clock() + VG.ParLimitTime2Move

		msgSizePanel =["Small Panel", "Medium Panel", "Large Panel"]
		showMessage("New Game", msgSizePanel[VG.ParSizeActu])
		time.sleep(0.9)

	if KeyCode == "changeSize":
	#elif retKey.key == K_F2: # CHANGE PANEL SIZE
		save_hiscore(Tab2Play1.score)
		VG.ParSizeActu += 1
		if VG.ParSizeActu >= 3:
			VG.ParSizeActu = 0
		changePanelSize(VG.ParSizeActu)
		#fenetre = pygame.display.set_mode((VG.ParColumns*90, VG.ParRaws*90 + 120))
		fenetre = pygame.display.set_mode((VG.ParColumns*90 + 350, VG.ParRaws*90 + 160))
		KeyCode = ""
		Tab2Play1.newGame(x=VG.ParRaws, y=VG.ParColumns)
		#Tab2Play1 = Tab2Play()
		Tab2Play1.newThreat()
		Tab2Play1.newThreat()
		Tab2Play1.update(fenetre)
		VG.LimitTime2Move = time.clock() + VG.ParLimitTime2Move
		
		msgSizePanel =["Small Panel", "Medium Panel", "Large Panel"]
		showMessage("New Game", msgSizePanel[VG.ParSizeActu])
		time.sleep(0.9)

	
	if KeyCode == "escape":
		#showMessage("PAUSED", "Esc=Quit", "F1=New Game", "F2=Change Size", "F3=New Large", "Other=Resume")
		showMessage("PAUSED", "", "Esc to Quit", "", "Any Key", "To Resume")
		time.sleep(0.2)
		print ("Escape Key")
		
		retKey =  wait_any_key()
		print (retKey)
		
		if retKey == K_ESCAPE:
			#Tab2Play1.update(fenetre)
			if VG.ParAutoSaveOnExit:
				Tab2Play1.saveGame()
			isRunning = False
			break


		else:
			KeyCode = ""

	isMoving = False
	
	if (KeyCode=="ai1"):
		KeyCode = Tab2Play1AI.bestMoveLevel1()

	if (Tab2Play1.howPlayer == 2) and (Tab2Play1.whoP1P2 == 2) and (Tab2Play1.player2Human == False):
		if (KeyCode=="ai2"):
			KeyCode = Tab2Play1AI.bestMoveLevel2vsH()
		if (KeyCode=="ai3"):
			KeyCode = Tab2Play1AI.bestMoveLevel3vsH()
			#KeyCode = Tab2Play1AI.bestMoveLevel2vsH()
	else:
		if (KeyCode=="ai2"):
			KeyCode = Tab2Play1AI.bestMoveLevel2()
		if (KeyCode=="ai3"):
			KeyCode = Tab2Play1AI.bestMoveLevel3()
		
	if (KeyCode=="up") or (KeyCode=="down") or (KeyCode=="left") or (KeyCode=="right"):
		isMoving = True

	Tab2Play1.StopMovingClear()
	
	
	isMoving = Tab2Play1.move(fenetre, KeyCode)

	if isMoving:
		Tab2Play1.nbMove += 1
		if VG.ParMusicYN:
			S_Beep5a.play()
			#time.sleep(0.7)

	while isMoving:
		#print ("isMoving 1 : %s" %(isMoving))
		#print ("checkIfMoving 1 : %s" %(Tab2Play1.checkIfMoving() ))
		
		while Tab2Play1.checkIfMoving():
			#print ("checkIfMoving 2 : %s" %(Tab2Play1.checkIfMoving() ))
			Tab2Play1.updateMoving(fenetre)

		if VG.Par1StepMove == False:
			isMoving = Tab2Play1.move(fenetre, KeyCode)
		else:
			isMoving = False

	Tab2Play1.update(fenetre)

	#new threat only if a real movement as been or ParAllowNoMove
	if Tab2Play1.getHasMoved() or VG.ParAllowNoMove:
		Tab2Play1.newThreat()
		VG.LimitTime2Move = time.clock() + VG.ParLimitTime2Move

	if Tab2Play1.isFull():
		#save_hiscore(Tab2Play1.score)
		print ("Panel Full, Check Possible Move")
		if not( Tab2Play1.canMove() ):
			save_hiscore(Tab2Play1.score)
			VG.LimitTime2Move = time.clock()
			Tab2Play1.update(fenetre) # to update hiScores correctly

			if (Tab2Play1.howPlayer == 1):
				showMessage("Panel Full,", "You Lose")
			else:
				if Tab2Play1.score == Tab2Play1.scoreP2:
					showMessage("Panel Full,", "No Winner")
				elif Tab2Play1.score > Tab2Play1.scoreP2:
					showMessage("Panel Full,", "Player 1 WIN")
				else:
					showMessage("Panel Full,", "Player 2 WIN")

			print ("Panel Full, No Move Possible, You Lose")
			if VG.ParMusicYN:
				S_end1b.play()
			time.sleep(0.3)
			wait_any_key()
			KeyCode = ""
			# New Game
			Tab2Play1.newGame(x=VG.ParRaws, y=VG.ParColumns)
			#Tab2Play1 = Tab2Play()
			Tab2Play1.newThreat()
			Tab2Play1.newThreat()
			#Tab2Play1.setHasMoved( False )

			VG.LimitTime2Move = time.clock() + VG.ParLimitTime2Move

	if Tab2Play1.getHasMoved():
		Tab2Play1.setHasMoved( False )

	#do not allow to not move if 2 players:
	elif (Tab2Play1.howPlayer == 2): # and not (Tab2Play1.getHasMoved()):
		Tab2Play1.whoP1P2 -= 1
		if Tab2Play1.whoP1P2 <= 0:
			Tab2Play1.whoP1P2 = 2
		isMoving =  False

	print (Tab2Play1.Tab2Play)

save_hiscore(Tab2Play1.score)

pygame.quit()
sys.exit(0)
