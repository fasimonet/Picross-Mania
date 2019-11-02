#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys, os, random, time, math

import pygame
from pygame.locals import *

from py2048_threat import threat
import py2048_VG as VG
from py2048_sounds import *

import json

pygame.init()

class Tab2Play():
	def __init__(self, x=VG.ParColumns, y=VG.ParRaws):

		if x<3:
			x=3
		if y<3:
			y=3

		self.x = x # ParColumns
		self.y = y # ParRaws

		#self.Tab2Play = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]
		self.Tab2Play = []
		self.Tab2PlayThreat = []
		self.Tab2PlayCanAdd = []
		self.Tab2PlayIsMoving = []
		self.Tab2PlayDisplayMoving = []

		for i in range(0, self.x):
			self.Tab2Play.append([])
			self.Tab2PlayThreat.append([])
			self.Tab2PlayCanAdd.append([])
			self.Tab2PlayIsMoving.append([])
			for j in range(0, self.y):
				self.Tab2Play[i].append(0)
				self.Tab2PlayThreat[i].append( threat( image=0, x=i, y=j, score=0 ) )
				self.Tab2PlayCanAdd.append(True)
				self.Tab2PlayIsMoving.append(0)
			
		#test
		#self.Tab2Play = [[2, 4, 6, 8], [0, 12, 11, 13], [1, 3, 9, 5], [9, 1, 2, 9] ]
		
		self.howFree = 0
		self.Full = False
		self.hasMoved = False
		self.score = 0
		self.maxTile = 0
		self.nbMove = 0
		
		self.scoreP2 = 0
		self.whoP1P2 = 1
		self.howPlayer = 1
		self.player2Human = True

	def newGame(self, x=VG.ParColumns, y=VG.ParRaws):

		if x<3:
			x=3
		if y<3:
			y=3

		self.x = x # ParColumns
		self.y = y # ParRaws

		self.Tab2Play = []
		self.Tab2PlayThreat = []
		self.Tab2PlayCanAdd = []
		self.Tab2PlayIsMoving = []
		self.Tab2PlayDisplayMoving = []

		for i in range(0, self.x):
			self.Tab2Play.append([])
			self.Tab2PlayThreat.append([])
			self.Tab2PlayCanAdd.append([])
			self.Tab2PlayIsMoving.append([])
			for j in range(0, self.y):
				self.Tab2Play[i].append(0)
				self.Tab2PlayThreat[i].append( threat( image=0, x=i, y=j, score=0 ) )
				self.Tab2PlayCanAdd.append(True)
				self.Tab2PlayIsMoving.append(0)

		self.howFree = 0
		self.Full = False
		self.hasMoved = False
		self.score = 0
		self.maxTile = 0
		self.nbMove = 0

		self.scoreP2 = 0
		self.whoP1P2 = 1
		#self.howPlayer = 1
		#self.player2Human = True


	def newThreat(self):
		""" add a new threat in panel """

		self.isFull()
		if self.Full:
			# prevent deadlock while if panel full
			print ("WARNING: Attempt New Threat While Panel Full")
			return
			
		#vRandScore = random.randrange(1, 3)
		vRandScore = random.randrange(VG.ParBrickNewMin, VG.ParBrickNewMax)
		
		vRandi = random.randrange(0, self.x)
		vRandj = random.randrange(0, self.y)
		while self.Tab2Play[vRandi][vRandj] != 0:
		#while Tab2Play[vRandi][vRandj].getScore() != 0:
			vRandScore = random.randrange(VG.ParBrickNewMin, VG.ParBrickNewMax)
			vRandi = random.randrange(0, self.x)
			vRandj = random.randrange(0, self.y)
		self.Tab2Play[vRandi][vRandj] = vRandScore

		threat1 = threat(image=self.Tab2Play[vRandi][vRandj], x=vRandi, y=vRandj, score=self.Tab2Play[vRandi][vRandj])
		self.Tab2PlayThreat[vRandi][vRandj] = threat1

	def isFull(self):
		""" check if panel is full of threat """

		self.Full = True
		self.howFree = 0
		for i in range(0,self.x):
			for j in range(0,self.y):
				if self.Tab2Play[i][j] == 0:
					self.howFree += 1
					self.Full = False
		
		return self.Full

	def canMove(self):
		""" check if panel can move at least one side """

		movePossible = False
		#stopMoving = [False, False, False, False] #prevent if other raw/column need to continu move
		#if sens == "left":
		for i in range(1,self.x):
			for j in range(0,self.y):
				if (self.Tab2Play[i][j] != 0):			#something
					#print ("found %s @ x=%s, y=%s)" %(self.Tab2Play[i][j], i, j) )
					if (self.Tab2Play[i-1][j] == 0):	#empty => switch to left
						#print ("switch to left x=%s, y=%s, sc=%s" %( i, j, self.Tab2Play[i][j]) )
						movePossible = True
					elif (self.Tab2Play[i-1][j] == self.Tab2Play[i][j]): #same value => add onto one threat
						#print ("ADD2RIGHT x=%s, y=%s, sc=%s" %( i, j, self.Tab2Play[i][j]) )
						movePossible = True
		
		#if sens == "right":
		for i in range(self.x - 2, -1, -1):
			for j in range(0,self.y):
				if (self.Tab2Play[i][j] != 0):			#something
					#print ("found %s @ x=%s, y=%s)" %(self.Tab2Play[i][j], i, j) )
					if (self.Tab2Play[i+1][j] == 0):	#empty => switch to left
						#print ("switch to right x=%s, y=%s, sc=%s" %( i, j, self.Tab2Play[i][j]) )
						movePossible = True
					elif (self.Tab2Play[i+1][j] == self.Tab2Play[i][j]): #same value => add onto one threat
						#print ("ADD2RIGHT x=%s, y=%s, sc=%s" %( i, j, self.Tab2Play[i][j]) )
						movePossible = True
		
		#if sens == "up":
		for i in range(0,self.x):
			for j in range(1,self.y):
				if (self.Tab2Play[i][j] != 0):			#something
					#print ("found %s @ x=%s, y=%s)" %(self.Tab2Play[i][j], i, j) )
					if (self.Tab2Play[i][j-1] == 0):	#empty => switch to left
						#print ("switch to up x=%s, y=%s, sc=%s" %( i, j, self.Tab2Play[i][j]) )
						movePossible = True
					elif (self.Tab2Play[i][j-1] == self.Tab2Play[i][j]): #same value => add onto one threat
						#print ("ADD2UP x=%s, y=%s, sc=%s" %( i, j, self.Tab2Play[i][j]) )
						movePossible = True

		#if sens == "down":
		for i in range(0,self.x):
			for j in range(self.y - 2, -1, -1):
				if (self.Tab2Play[i][j] != 0):			#something
					#print ("found %s @ x=%s, y=%s)" %(self.Tab2Play[i][j], i, j) )
					if (self.Tab2Play[i][j+1] == 0):	#empty => switch to left
						#print ("switch to right x=%s, y=%s, sc=%s" %( i, j, self.Tab2Play[i][j]) )
						movePossible = True
					elif (self.Tab2Play[i][j+1] == self.Tab2Play[i][j]): #same value => add onto one threat
						#print ("ADD2DOWN x=%s, y=%s, sc=%s" %( i, j, self.Tab2Play[i][j]) )
						movePossible = True		

		return movePossible

	def move(self, fenetre, sens="left"):
		""" shift panel from point to new position point left, right, up, down """
		
		#self.Tab2Play = [x0[y0, y1, y2, y3], x1[y0, y1, y2, y3], x2[y0, y1, y2, y3], x3[y0, y1, y2, y3] ]
		self.Tab2PlayDisplayMoving = []

		isMoving = False
		#stopMoving = [False, False, False, False] #prevent if other raw/column need to continu move
		if sens == "left":
			for i in range(1,self.x):
				for j in range(0,self.y):
					if (self.Tab2Play[i][j] != 0):			#something
						#print ("found %s @ x=%s, y=%s)" %(self.Tab2Play[i][j], i, j) )
						if (self.Tab2Play[i-1][j] == 0):	#empty => switch to left
							print ("switch to left x=%s, y=%s, sc=%s" %( i, j, self.Tab2Play[i][j]) )
							self.Tab2PlayIsMoving[i][j] = 1
							self.Tab2PlayDisplayMoving.append( threat(image=self.Tab2Play[i][j], x=i, y=j, score=self.Tab2Play[i][j]) )
							#self.updateMoving(fenetre)
							self.Tab2Play[i-1][j] = self.Tab2Play[i][j]
							self.Tab2Play[i][j] = 0
							self.Tab2PlayCanAdd[i-1][j] = self.Tab2PlayCanAdd[i][j]
							self.Tab2PlayCanAdd[i][j] = True
							isMoving = True
						elif (self.Tab2Play[i-1][j] == self.Tab2Play[i][j]): #same value => add onto one threat
							if (self.Tab2PlayCanAdd[i][j]) and (self.Tab2PlayCanAdd[i-1][j]):
								print ("ADD2LEFT x=%s, y=%s, sc=%s" %( i, j, self.Tab2Play[i][j]) )
								self.Tab2PlayIsMoving[i][j] = 1
								self.Tab2PlayDisplayMoving.append( threat(image=self.Tab2Play[i][j], x=i, y=j, score=self.Tab2Play[i][j]) )
								#self.updateMoving(fenetre)
								self.Tab2Play[i-1][j] += 1
								if self.Tab2Play[i-1][j] > VG.ParBrickMaxValue:
									self.Tab2Play[i-1][j] = VG.ParBrickMaxValue
								if self.whoP1P2 == 1:
									self.score += 2**self.Tab2Play[i-1][j]
								else:
									self.scoreP2 +=  2**self.Tab2Play[i-1][j]
								self.Tab2Play[i][j] = 0
								self.Tab2PlayCanAdd[i-1][j] = False
								self.Tab2PlayCanAdd[i][j] = True
								isMoving = True
								if VG.ParMusicYN:
									S_Bomb1.play()
		
		if sens == "right":
			for i in range(self.x - 2, -1, -1):
				for j in range(0,self.y):
					if (self.Tab2Play[i][j] != 0):			#something
						#print ("found %s @ x=%s, y=%s)" %(self.Tab2Play[i][j], i, j) )
						if (self.Tab2Play[i+1][j] == 0):	#empty => switch to left
							print ("switch to right x=%s, y=%s, sc=%s" %( i, j, self.Tab2Play[i][j]) )
							self.Tab2PlayIsMoving[i][j] = 2
							self.Tab2PlayDisplayMoving.append( threat(image=self.Tab2Play[i][j], x=i, y=j, score=self.Tab2Play[i][j]) )
							#self.updateMoving(fenetre)
							self.Tab2Play[i+1][j] = self.Tab2Play[i][j]
							self.Tab2Play[i][j] = 0
							self.Tab2PlayCanAdd[i+1][j] = self.Tab2PlayCanAdd[i][j]
							self.Tab2PlayCanAdd[i][j] = True
							isMoving = True
						elif (self.Tab2Play[i+1][j] == self.Tab2Play[i][j]): #same value => add onto one threat
							if (self.Tab2PlayCanAdd[i][j]) and (self.Tab2PlayCanAdd[i+1][j]):
								print ("ADD2RIGHT x=%s, y=%s, sc=%s" %( i, j, self.Tab2Play[i][j]) )
								self.Tab2PlayIsMoving[i][j] = 2
								self.Tab2PlayDisplayMoving.append( threat(image=self.Tab2Play[i][j], x=i, y=j, score=self.Tab2Play[i][j]) )
								#self.updateMoving(fenetre)
								self.Tab2Play[i+1][j] += 1
								if self.Tab2Play[i+1][j] > VG.ParBrickMaxValue:
									self.Tab2Play[i+1][j] = VG.ParBrickMaxValue
								#self.score += 2**self.Tab2Play[i+1][j] 
								if self.whoP1P2 == 1:
									self.score += 2**self.Tab2Play[i+1][j]
								else:
									self.scoreP2 +=  2**self.Tab2Play[i+1][j]
								self.Tab2Play[i][j] = 0
								self.Tab2PlayCanAdd[i+1][j] = False
								self.Tab2PlayCanAdd[i][j] = True
								isMoving = True
								if VG.ParMusicYN:
									S_Bomb1.play()
		
		if sens == "up":
			for i in range(0,self.x):
				for j in range(1,self.y):
					if (self.Tab2Play[i][j] != 0):			#something
						#print ("found %s @ x=%s, y=%s)" %(self.Tab2Play[i][j], i, j) )
						if (self.Tab2Play[i][j-1] == 0):	#empty => switch to left
							print ("switch to up x=%s, y=%s, sc=%s" %( i, j, self.Tab2Play[i][j]) )
							self.Tab2PlayIsMoving[i][j] = 3
							self.Tab2PlayDisplayMoving.append( threat(image=self.Tab2Play[i][j], x=i, y=j, score=self.Tab2Play[i][j]) )
							#self.updateMoving(fenetre)
							self.Tab2Play[i][j-1] = self.Tab2Play[i][j]
							self.Tab2Play[i][j] = 0
							self.Tab2PlayCanAdd[i][j-1] = self.Tab2PlayCanAdd[i][j]
							self.Tab2PlayCanAdd[i][j] = True
							isMoving = True
						elif (self.Tab2Play[i][j-1] == self.Tab2Play[i][j]): #same value => add onto one threat
							if (self.Tab2PlayCanAdd[i][j]) and (self.Tab2PlayCanAdd[i][j-1]):
								print ("ADD2UP x=%s, y=%s, sc=%s" %( i, j, self.Tab2Play[i][j]) )
								self.Tab2PlayIsMoving[i][j] = 3
								self.Tab2PlayDisplayMoving.append( threat(image=self.Tab2Play[i][j], x=i, y=j, score=self.Tab2Play[i][j]) )
								#self.updateMoving(fenetre)
								self.Tab2Play[i][j-1] += 1
								if self.Tab2Play[i][j-1] > VG.ParBrickMaxValue:
									self.Tab2Play[i][j-1] = VG.ParBrickMaxValue
								#self.score += 2**self.Tab2Play[i][j-1]
								if self.whoP1P2 == 1:
									self.score += 2**self.Tab2Play[i][j-1]
								else:
									self.scoreP2 +=  2**self.Tab2Play[i][j-1]
								self.Tab2Play[i][j] = 0
								self.Tab2PlayCanAdd[i][j-1] = False
								self.Tab2PlayCanAdd[i][j] = True
								isMoving = True
								if VG.ParMusicYN:
									S_Bomb1.play()

		if sens == "down":
			for i in range(0,self.x):
				for j in range(self.y - 2, -1, -1):
					if (self.Tab2Play[i][j] != 0):			#something
						#print ("found %s @ x=%s, y=%s)" %(self.Tab2Play[i][j], i, j) )
						if (self.Tab2Play[i][j+1] == 0):	#empty => switch to left
							print ("switch to right x=%s, y=%s, sc=%s" %( i, j, self.Tab2Play[i][j]) )
							self.Tab2PlayIsMoving[i][j] = 4
							self.Tab2PlayDisplayMoving.append( threat(image=self.Tab2Play[i][j], x=i, y=j, score=self.Tab2Play[i][j]) )
							#self.updateMoving(fenetre)
							self.Tab2Play[i][j+1] = self.Tab2Play[i][j]
							self.Tab2Play[i][j] = 0
							self.Tab2PlayCanAdd[i][j+1] = self.Tab2PlayCanAdd[i][j]
							self.Tab2PlayCanAdd[i][j] = True
							isMoving = True
						elif (self.Tab2Play[i][j+1] == self.Tab2Play[i][j]): #same value => add onto one threat
							if (self.Tab2PlayCanAdd[i][j]) and (self.Tab2PlayCanAdd[i][j+1]):
								print ("ADD2DOWN x=%s, y=%s, sc=%s" %( i, j, self.Tab2Play[i][j]) )
								self.Tab2PlayIsMoving[i][j] = 4
								self.Tab2PlayDisplayMoving.append( threat(image=self.Tab2Play[i][j], x=i, y=j, score=self.Tab2Play[i][j]) )
								#self.updateMoving(fenetre)
								self.Tab2Play[i][j+1] += 1
								if self.Tab2Play[i][j+1] > VG.ParBrickMaxValue:
									self.Tab2Play[i][j+1] = VG.ParBrickMaxValue
								#self.score += 2**self.Tab2Play[i][j+1] 
								if self.whoP1P2 == 1:
									self.score += 2**self.Tab2Play[i][j+1]
								else:
									self.scoreP2 +=  2**self.Tab2Play[i][j+1]
								self.Tab2Play[i][j] = 0
								self.Tab2PlayCanAdd[i][j+1] = False
								self.Tab2PlayCanAdd[i][j] = True
								isMoving = True
								if VG.ParMusicYN:
									S_Bomb1.play()
									
				
		print (self.Tab2PlayCanAdd)
		return isMoving
		
	def checkMaxTile(self):
		""" return the tile max value """

		maxTile = 0
		for i in range(0,self.x):
			for j in range(0,self.y):
				if self.Tab2Play[i][j] > maxTile:
					maxTile = self.Tab2Play[i][j]					

		return maxTile

	def update(self, fenetre): # used for (sprite.Group).update
		""" display all Tab2Play panel within fenetre """

		self.maxTile = self.checkMaxTile()
		#print ("maxTile: %s" %(self.maxTile) )
		if self.maxTile <10: #1024:
			VG.bckGnd = VG.bckGnd0000
		elif self.maxTile <11: #2048:
			VG.bckGnd = VG.bckGnd1024
		elif self.maxTile <12: #4096:
			VG.bckGnd = VG.bckGnd2048
		elif self.maxTile <13: #8192:
			VG.bckGnd = VG.bckGnd4096
		else:
			VG.bckGnd = VG.bckGnd8192

		fenetre.blit(VG.bckGnd,(0,0))

		for i in range(0,self.x):
			for j in range(0,self.y):
				threat1 = threat(image=self.Tab2Play[i][j], x=i, y=j, score=self.Tab2Play[i][j])
				self.Tab2PlayThreat[i][j] = threat1

				fenetre.blit( threat1.getImage(), (threat1.getRectX(), threat1.getRectY()) )
				#fenetre.blit( threat1.getImage(), (i*90, j*90) )

		self.updateTexts(fenetre)
		#pygame.display.flip()
		
	def updateTexts(self, fenetre): # used for (sprite.Group).update
		""" display Texts bottom Tab2Play panel within fenetre """

		# change font according panel size
		Font2Disp = VG.minileter32
		if VG.ParSizeActu == 0:
			Font2Disp = VG.minileter24
		if VG.ParSizeActu == 1:
			Font2Disp = VG.minileter28
		if VG.ParSizeActu == 2:
			Font2Disp = VG.minileter32

		# display score
		textScore = Font2Disp.render("Score ", 1, VG.DeepBlue)
		textScore2 = Font2Disp.render("Score ", 1, VG.Black)
		textScorePos = textScore.get_rect()

		if self.whoP1P2 == 1:
			textScoreP1 = Font2Disp.render("P1:%s  "%(self.score), 1, VG.Lime)
		else:
			textScoreP1 = Font2Disp.render("P1:%s  "%(self.score), 1, VG.DeepBlue)
		textScore2P1 = Font2Disp.render("P1:%s  "%(self.score), 1, VG.Black)
		textScorePosP1 = textScoreP1.get_rect()

		if self.whoP1P2 == 2:
			textScoreP2 = Font2Disp.render("P2:%s"%(self.scoreP2), 1, VG.Lime)
		else:
			textScoreP2 = Font2Disp.render("P2:%s"%(self.scoreP2), 1, VG.DeepBlue)			
		textScore2P2 = Font2Disp.render("P2:%s"%(self.scoreP2), 1, VG.Black)
		textScorePosP2 = textScoreP2.get_rect()

		textMov = Font2Disp.render("Movments:%s"%(self.nbMove), 1, VG.DeepBlue)
		textMov2 = Font2Disp.render("Movments:%s"%(self.nbMove), 1, VG.Black)
		textMovPos = textMov.get_rect()

		textHiScore = Font2Disp.render("HiScore:%s, Mv:%s"%(VG.hiScore, VG.hiMove), 1, VG.NavyBlue)
		textHiScore2 = Font2Disp.render("HiScore:%s, Mv:%s"%(VG.hiScore, VG.hiMove), 1, VG.Black)
		textHiScorePos = textHiScore.get_rect()
		
		DispTime = VG.LimitTime2Move - time.clock()
		if DispTime < 0:
			DispTime = 0
		#DispTime = str(int(VG.LimitTime2Move))+"."+str(int((VG.LimitTime2Move-int(VG.LimitTime2Move))*10))
		DispTime2 = str(int(DispTime))+"."+str(int((DispTime - int(DispTime))*10))
		if DispTime > 2:
			textTime2Move = Font2Disp.render("Time Move:"+DispTime2, 1, VG.NavyBlue)
		elif DispTime > 1:
			textTime2Move = Font2Disp.render("Time Move:"+DispTime2, 1, VG.Green)
		else:
			textTime2Move = Font2Disp.render("Time Move:"+DispTime2, 1, VG.Red)				
		textTime2Move2 = Font2Disp.render("Time Move:"+DispTime2, 1, VG.Black)
		textTime2MovePos = textTime2Move.get_rect()

		fenetre.blit( textScore2, (2, (self.y*90) + 12) )
		fenetre.blit( textScore, (0, (self.y*90) + 10) )
		fenetre.blit( textScore2P1, (2 + textScorePos[2], (self.y*90) + 12) )
		fenetre.blit( textScoreP1, (0 + textScorePos[2], (self.y*90) + 10) )
		fenetre.blit( textScore2P2, (2 + textScorePos[2] + textScorePosP1[2], (self.y*90) + 12) )
		fenetre.blit( textScoreP2, (0 + textScorePos[2] + textScorePosP1[2], (self.y*90) + 10) )
		
		fenetre.blit( textMov2, (0 + 2, (self.y*90) + 12 + textScorePos[3] ) )
		fenetre.blit( textMov, (0, (self.y*90) + 10 + textScorePos[3] ) )
		
		fenetre.blit( textHiScore2, (0 + 2, (self.y*90) + 12 + textMovPos[3] + textScorePos[3] ) )
		fenetre.blit( textHiScore, (0, (self.y*90) + 10 + textMovPos[3] + textScorePos[3] ) )
		if VG.ParLimitTime2Move != 0 :
			fenetre.blit( VG.bckGnd, (0 + 2, (self.y*90) + 12 + textMovPos[3] + textScorePos[3] + textHiScorePos[3] ) , (0, (self.y*90) + 10 + textScorePos[3] + textHiScorePos[3], textTime2Move2.get_rect()[2], textTime2Move2.get_rect()[3] ) ) 
			fenetre.blit( VG.bckGnd, (0, (self.y*90) + 10 + textMovPos[3] + textScorePos[3] + textHiScorePos[3] ) , (0, (self.y*90) + 10 + textScorePos[3] + textHiScorePos[3], textTime2Move.get_rect()[2], textTime2Move.get_rect()[3] ) ) 
			fenetre.blit( textTime2Move2, (0 + 2, (self.y*90) + 12 + textMovPos[3] + textScorePos[3] + textHiScorePos[3] ) )
			fenetre.blit( textTime2Move, (0, (self.y*90) + 10 + textMovPos[3] + textScorePos[3] + textHiScorePos[3]) )


		#################################################
		#def showMenu():
		# display menu
		# showMessage("Esc=Quit", "N=New Game", "F1=New Small", "F2=New Medium", "F3=New Large", "Other=Resume")
		textMenu1 = VG.minileter28.render("Esc=Quit", 1, VG.Black)
		textMenu1a = VG.minileter28.render("Esc=Quit", 1, VG.Yellow)
		fenetre.blit( textMenu1, ( self.y*90 + 10, self.y +10 ) )
		fenetre.blit( textMenu1a, ( self.y*90 + 12, self.y +10 + 2 ) )

		textMenu2 = VG.minileter28.render("F1=New Game", 1, VG.Black)
		textMenu2a = VG.minileter28.render("F1=New Game", 1, VG.Yellow)
		fenetre.blit( textMenu2, ( self.y*90 + 10, self.y +10 + textMenu1.get_rect()[3]) ) 
		fenetre.blit( textMenu2a, ( self.y*90 + 12, self.y +12 + textMenu1.get_rect()[3] ) )

		msgSizePanel =["Small", "Medium", "Large"]
		textMenu3 = VG.minileter28.render("F2=Panel Size (%s)" %(msgSizePanel[VG.ParSizeActu]), 1, VG.Black)
		textMenu3a = VG.minileter28.render("F2=Panel Size (%s)" %(msgSizePanel[VG.ParSizeActu]), 1, VG.Yellow)
		fenetre.blit( textMenu3, ( self.y*90 + 10, self.y +10 + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] ) )
		fenetre.blit( textMenu3a, ( self.y*90 + 12, self.y +12 + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] ) )

		textMenu4 = VG.minileter28.render("F3=None", 1, VG.Black)
		textMenu4a = VG.minileter28.render("F3=None", 1, VG.Yellow)
		fenetre.blit( textMenu4, ( self.y*90 + 10, self.y +10 + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] ) )
		fenetre.blit( textMenu4a, ( self.y*90 + 12, self.y +12 + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] ) )

		textMenu5 = VG.minileter28.render("F4=None", 1, VG.Black)
		textMenu5a = VG.minileter28.render("F4=None", 1, VG.Yellow)
		fenetre.blit( textMenu5, ( self.y*90 + 10, self.y +10 + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] ) )
		fenetre.blit( textMenu5a, ( self.y*90 + 12, self.y +12 + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] ) )

		if self.player2Human:
			textMenu6 = VG.minileter28.render("F7=Player2 Human", 1, VG.Black)
			textMenu6a = VG.minileter28.render("F7=Player2 Human", 1, VG.Yellow)
		else:
			textMenu6 = VG.minileter28.render("F7=Player2 AI", 1, VG.Black)
			textMenu6a = VG.minileter28.render("F7=Player2 AI", 1, VG.Yellow)
		fenetre.blit( textMenu6, ( self.y*90 + 10, self.y +10 + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] + textMenu5.get_rect()[3] ) )
		fenetre.blit( textMenu6a, ( self.y*90 + 12, self.y +12 + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] + textMenu5.get_rect()[3] ) )

		if self.howPlayer == 1:
			textMenu7 = VG.minileter28.render("F8=One Player Game", 1, VG.Black)
			textMenu7a = VG.minileter28.render("F8=One Player Game", 1, VG.Yellow)
		else:
			textMenu7 = VG.minileter28.render("F8=Two Players Game", 1, VG.Black)
			textMenu7a = VG.minileter28.render("F8=Two Players Game", 1, VG.Yellow)
		fenetre.blit( textMenu7, ( self.y*90 + 10, self.y +10 + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] + textMenu5.get_rect()[3] + textMenu6.get_rect()[3] ) )
		fenetre.blit( textMenu7a, ( self.y*90 + 12, self.y +12 + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] + textMenu5.get_rect()[3] + textMenu6.get_rect()[3] ) )

		textMenu8 = VG.minileter28.render("F9=Hint Move AI", 1, VG.Black)
		textMenu8a = VG.minileter28.render("F9=Hint Move AI", 1, VG.Yellow)
		fenetre.blit( textMenu8, ( self.y*90 + 10, self.y +10 + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] + textMenu5.get_rect()[3] + textMenu6.get_rect()[3] + textMenu7.get_rect()[3] ) )
		fenetre.blit( textMenu8a, ( self.y*90 + 12, self.y +12 + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] + textMenu5.get_rect()[3] + textMenu6.get_rect()[3] + textMenu7.get_rect()[3] ) )

		textMenu9 = VG.minileter28.render("F10=AI level: %s" %(VG.autoAILevel), 1, VG.Black)
		textMenu9a = VG.minileter28.render("F10=AI level: %s" %(VG.autoAILevel), 1, VG.Yellow)
		fenetre.blit( textMenu9, ( self.y*90 + 10, self.y +10 + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] + textMenu5.get_rect()[3] + textMenu6.get_rect()[3] + textMenu7.get_rect()[3] + textMenu8.get_rect()[3] ) )
		fenetre.blit( textMenu9a, ( self.y*90 + 12, self.y +12 + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] + textMenu5.get_rect()[3] + textMenu6.get_rect()[3] + textMenu7.get_rect()[3] + textMenu8.get_rect()[3] ) )

		textMenu10 = VG.minileter28.render("ENTER=AutoAI: %s" %(VG.autoAIToggle), 1, VG.Black)
		textMenu10a = VG.minileter28.render("ENTER=AutoAI: %s" %(VG.autoAIToggle), 1, VG.Yellow)
		fenetre.blit( textMenu10, ( self.y*90 + 10, self.y +10 + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] + textMenu5.get_rect()[3] + textMenu6.get_rect()[3] + textMenu7.get_rect()[3] + textMenu8.get_rect()[3] + textMenu9.get_rect()[3] ) )
		fenetre.blit( textMenu10a, ( self.y*90 + 12, self.y +12 + textMenu1.get_rect()[3] + textMenu2.get_rect()[3] + textMenu3.get_rect()[3] + textMenu4.get_rect()[3] + textMenu5.get_rect()[3] + textMenu6.get_rect()[3] + textMenu7.get_rect()[3] + textMenu8.get_rect()[3] + textMenu9.get_rect()[3] ) )

		pygame.display.flip()
	
	def StopMovingClear(self):
		""" Tab2PlayIsMoving = 0, 1, 2, 3, 4 for noMove, left, right, up, down"""

		self.Tab2PlayCanAdd = []
		self.Tab2PlayIsMoving = []
		for i in range(0,self.x):
			self.Tab2PlayCanAdd.append([])
			self.Tab2PlayIsMoving.append([])
			for j in range(0,self.y):
				self.Tab2PlayCanAdd[i].append(True)
				self.Tab2PlayIsMoving[i].append(0)

	def checkIfMoving(self):
		""" Tab2PlayIsMoving = 0, 1, 2, 3, 4 for noMove, left, right, up, down"""
		
		ifMoving = False
		for i in range(0,self.x):
			for j in range(0,self.y):
				if self.Tab2PlayIsMoving[i][j] != 0:
					ifMoving = True
		return ifMoving

	def updateMoving(self, fenetre): # used for (sprite.Group).update
		""" display Tab2Play panel within fenetre """

		# increase speed moving to avoid anoying when large panel
		speedMove = 10 # speedMove sould be 90 multiple
		if VG.ParSizeActu == 2:
			speedMove = 15
			
		clock = pygame.time.Clock()

		threat0 = threat(image=0, x=0, y=0, score=0)

		#TODO: movement sould be one complete movement (otherwise too long)
		#self.Tab2PlayDisplayMoving = []
		hasMoved2Left = False
		hasMoved2Right = False
		hasMoved2Up = False
		hasMoved2Down = False

		for i in range(0,self.x):
			for j in range(0,self.y):
				if self.Tab2PlayIsMoving[i][j] == 1:
					hasMoved2Left = True
					self.hasMoved = True
					self.Tab2PlayIsMoving[i][j] = 0

				if self.Tab2PlayIsMoving[i][j] == 2:
					hasMoved2Right = True
					self.hasMoved = True
					self.Tab2PlayIsMoving[i][j] = 0

				if self.Tab2PlayIsMoving[i][j] == 3:
					hasMoved2Up = True
					self.hasMoved = True
					self.Tab2PlayIsMoving[i][j] = 0

				if self.Tab2PlayIsMoving[i][j] == 4:
					hasMoved2Down = True
					self.hasMoved = True
					self.Tab2PlayIsMoving[i][j] = 0
					
		if hasMoved2Left: #Left
			#for f in range (0, 90 + 10, 10):
			for f in range (0, 90 + speedMove, speedMove):
				for it in self.Tab2PlayDisplayMoving:
					#threat1 = threat(image=self.Tab2Play[i][j], x=i, y=j, score=self.Tab2Play[i][j])
					fenetre.blit( VG.bckGnd, (it.getRectX(), it.getRectY()) , it.getRect() )
					fenetre.blit( threat0.getImage(), (it.getRectX(), it.getRectY()) )
					fenetre.blit( it.getImage(), (it.getRectX() - f, it.getRectY()) )

				clock.tick(VG.ParFPS)
				pygame.display.flip()
				
		if hasMoved2Right: #Right
			#for f in range (0, 90 + 10, 10):
			for f in range (0, 90 + speedMove, speedMove):
				for it in self.Tab2PlayDisplayMoving:
					#threat1 = threat(image=self.Tab2Play[i][j], x=i, y=j, score=self.Tab2Play[i][j])
					fenetre.blit( VG.bckGnd, (it.getRectX(), it.getRectY()) , it.getRect() )
					fenetre.blit( threat0.getImage(), (it.getRectX(), it.getRectY()) )
					fenetre.blit( it.getImage(), (it.getRectX() + f, it.getRectY()) )

				clock.tick(VG.ParFPS)
				pygame.display.flip()

		if hasMoved2Up: #Up
			#for f in range (0, 90 + 10, 10 + speedMove):
			for f in range (0, 90 + speedMove, speedMove):
				for it in self.Tab2PlayDisplayMoving:
					#threat1 = threat(image=self.Tab2Play[i][j], x=i, y=j, score=self.Tab2Play[i][j])
					fenetre.blit( VG.bckGnd, (it.getRectX(), it.getRectY()) , it.getRect() )
					fenetre.blit( threat0.getImage(), (it.getRectX(), it.getRectY()) )
					fenetre.blit( it.getImage(), (it.getRectX(), it.getRectY() - f) )

				clock.tick(VG.ParFPS)
				pygame.display.flip()

		if hasMoved2Down: #Down
			#for f in range (0, 90 + 10, 10):
			for f in range (0, 90 + speedMove, speedMove):
				for it in self.Tab2PlayDisplayMoving:
					#threat1 = threat(image=self.Tab2Play[i][j], x=i, y=j, score=self.Tab2Play[i][j])
					fenetre.blit( VG.bckGnd, (it.getRectX(), it.getRectY()) , it.getRect() )
					fenetre.blit( threat0.getImage(), (it.getRectX(), it.getRectY()) )
					fenetre.blit( it.getImage(), (it.getRectX(), it.getRectY() + f) )

				clock.tick(VG.ParFPS)
				pygame.display.flip()


	def saveGame(self):
		""" Save Game Panel When Quit """
		try:
			with open('SavedGame.json', 'w') as jsonfile:
				
				temp=[]
				
				temp.append(self.Tab2Play)
				#temp.append(self.Tab2PlayThreat)
				temp.append(self.Tab2PlayCanAdd)
				temp.append(self.Tab2PlayIsMoving)
				temp.append(self.Tab2PlayDisplayMoving)

				temp.append(self.x)
				temp.append(self.y)

				temp.append(self.howFree)
				temp.append(self.Full)
				temp.append(self.hasMoved)
				temp.append(self.score)
				temp.append(self.nbMove)

				temp.append(self.scoreP2)
				temp.append(self.whoP1P2)
				temp.append(self.howPlayer)
				temp.append(self.player2Human)


				json.dump(temp, jsonfile)
				
		except:
			print ("WARNING: unable to write SavedGame.json")


	def loadGame(self):
		""" Load Game Panel At StartUp """
		print ("AutoLoad SavedGame.json ...")
		try:
			with open("SavedGame.json", "rt") as infile:
				print ("AutoLoad temp ...")
				temp = json.load(infile)

				self.Tab2Play = temp[0]
				print ("AutoLoad Tab2Play=%s ..." %(self.Tab2Play) )
				#self.Tab2PlayThreat = json.load(infile)
				self.Tab2PlayCanAdd = temp[1]
				print ("AutoLoad Tab2PlayCanAdd=%s ..." %(self.Tab2PlayCanAdd) )
				self.Tab2PlayIsMoving = temp[2]
				print ("AutoLoad Tab2PlayIsMoving=%s ..." %(self.Tab2PlayIsMoving) )
				self.Tab2PlayDisplayMoving = temp[3]
				print ("AutoLoad Tab2PlayDisplayMoving=%s ..." %(self.Tab2PlayDisplayMoving) )

				self.x = temp[4]
				self.y = temp[5]
				print ("AutoLoad x=%s, y=%s ..." %(self.x, self.y) )

				self.howFree = temp[6]
				self.Full = temp[7]
				self.hasMoved = temp[8]
				self.score = temp[9]
				self.nbMove = temp[10]
				
				self.scoreP2 = temp[11]
				self.whoP1P2 = temp[12]
				self.howPlayer = temp[13]
				self.player2Human = temp[14]

				print ("AutoLoad  howFree=%s, Full=%s, hasMoved=%s, score=%s ..." %(self.howFree, self.Full, self.hasMoved, self.score) )
				
			print ("rebuild Tab2PlayThreat ...")
			self.Tab2PlayThreat = []
			for i in range(0, self.x):
				self.Tab2PlayThreat.append([])
				for j in range(0, self.y):
					self.Tab2PlayThreat[i].append( threat( image=self.Tab2Play[i][j], x=i, y=j, score=self.Tab2Play[i][j] ) )

		except:
			print ("WARNING: unable to load SavedGame.json")
			# reinit panel
			self.x = VG.ParColumns # ParColumns
			self.y = VG.ParRaws # ParRaws

			self.Tab2Play = []
			self.Tab2PlayThreat = []
			self.Tab2PlayCanAdd = []
			self.Tab2PlayIsMoving = []
			self.Tab2PlayDisplayMoving = []

			for i in range(0, self.x):
				self.Tab2Play.append([])
				self.Tab2PlayThreat.append([])
				self.Tab2PlayCanAdd.append([])
				self.Tab2PlayIsMoving.append([])
				for j in range(0, self.y):
					self.Tab2Play[i].append(0)
					self.Tab2PlayThreat[i].append( threat( image=0, x=i, y=j, score=0 ) )
					self.Tab2PlayCanAdd.append(True)
					self.Tab2PlayIsMoving.append(0)
				
			#test
			#self.Tab2Play = [[2, 4, 6, 8], [0, 12, 11, 13], [1, 3, 9, 5], [9, 1, 2, 9] ]
			
			self.howFree = 0
			self.Full = False
			self.hasMoved = False
			self.score = 0

			self.scoreP2 = 0
			self.whoP1P2 = 1
			self.howPlayer = 1
			self.player2Human = True

			self.newThreat()
			self.newThreat()


	def getScore(self):
		return self.score

	def getScoreP2(self):
		return self.scoreP2

	def getWhoP1P2(self):
		return self.whoP1P2

	def getHowPlayer(self):
		return self.howPlayer

	def getPlayer2Human(self):
		return self.player2Human

	def getHasMoved(self):
		return self.hasMoved

	def setHasMoved(self, state):
		self.hasMoved = state
	
	def getTab2Play(self):
		return self
		
