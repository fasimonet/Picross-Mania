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

class Tab2PlayAI():
	def __init__(self, Tableau):

		self.x = len(Tableau) #- 1
		self.y = len(Tableau[0]) #- 1

		self.Tab2PlayAI = []
		self.Tab2PlayAICanAdd = []

		for i in range(0, self.x):
			self.Tab2PlayAI.append([])
			self.Tab2PlayAICanAdd.append([])
			for j in range(0, self.y):
				#print ("populate Tab2PlayAI %s x %s" % (i , j) )
				self.Tab2PlayAI[i].append(Tableau[i][j])
				self.Tab2PlayAICanAdd[i].append(True)
					
		self.AIhowFree = 0
		self.AIFull = False
		self.AIhasMoved = False
		self.AIscore = 0
		self.AImaxTile = 0
		self.AInbMove = 0
		
	def isFull(self):
		""" check if panel is full of threat """

		self.Full = True
		self.howFree = 0
		for i in range(0,self.x):
			for j in range(0,self.y):
				if self.Tab2PlayAI[i][j] == 0:
					self.howFree += 1
					self.Full = False
		
		return self.Full

	def canMove(self):
		""" check if panel can move at least one side """

		movePossible = False
		moveSens = ""
		#stopMoving = [False, False, False, False] #prevent if other raw/column need to continu move
		#if sens == "left":
		for i in range(1,self.x):
			for j in range(0,self.y):
				if (self.Tab2PlayAI[i][j] != 0):			#something
					if (self.Tab2PlayAI[i-1][j] == 0):	#empty => switch to left
						movePossible = True
						moveSens = "left"
					elif (self.Tab2PlayAI[i-1][j] == self.Tab2PlayAI[i][j]): #same value => add onto one threat
						movePossible = True
						moveSens = "left"
		
		#if sens == "right":
		for i in range(self.x - 2, -1, -1):
			for j in range(0,self.y):
				if (self.Tab2PlayAI[i][j] != 0):			#something
					if (self.Tab2PlayAI[i+1][j] == 0):	#empty => switch to left
						movePossible = True
						moveSens = "right"
					elif (self.Tab2PlayAI[i+1][j] == self.Tab2PlayAI[i][j]): #same value => add onto one threat
						movePossible = True
						moveSens = "right"
		
		#if sens == "up":
		for i in range(0,self.x):
			for j in range(1,self.y):
				if (self.Tab2PlayAI[i][j] != 0):			#something
					if (self.Tab2PlayAI[i][j-1] == 0):	#empty => switch to left
						movePossible = True
						moveSens = "up"
					elif (self.Tab2PlayAI[i][j-1] == self.Tab2PlayAI[i][j]): #same value => add onto one threat
						movePossible = True
						moveSens = "up"

		#if sens == "down":
		for i in range(0,self.x):
			for j in range(self.y - 2, -1, -1):
				if (self.Tab2PlayAI[i][j] != 0):			#something
					if (self.Tab2PlayAI[i][j+1] == 0):	#empty => switch to left
						movePossible = True
						moveSens = "down"
					elif (self.Tab2PlayAI[i][j+1] == self.Tab2PlayAI[i][j]): #same value => add onto one threat
						movePossible = True
						moveSens = "down"

		return movePossible, moveSens

	#def move(self, fenetre, sens="left"):
	def move(self, sens="left"):
		""" shift panel from point to new position point left, right, up, down 
		return how many point increase """
		
		Tab2PlayAISaved = [list(i) for i in [list (j) for j in self.Tab2PlayAI] ]
		Tab2PlayAICanAddSaved = [list(i) for i in [list (j) for j in self.Tab2PlayAICanAdd] ]

		ScoreInc = 0
		hasMoved = False
		
		canMove, moveSens = self.canMove()
		if not(canMove):
				return ScoreInc, self.Tab2PlayAI, hasMoved
		
		isMoving = True

		while isMoving == True:
			isMoving = False
			if sens == "left":
				for i in range(1,self.x):
					for j in range(0,self.y):
						if (self.Tab2PlayAI[i][j] != 0):			#something
							if (self.Tab2PlayAI[i-1][j] == 0):	#empty => switch to left
								self.Tab2PlayAI[i-1][j] = self.Tab2PlayAI[i][j]
								self.Tab2PlayAI[i][j] = 0
								self.Tab2PlayAICanAdd[i-1][j] = self.Tab2PlayAICanAdd[i][j]
								self.Tab2PlayAICanAdd[i][j] = True
								isMoving = True
								hasMoved = True
							elif (self.Tab2PlayAI[i-1][j] == self.Tab2PlayAI[i][j]): #same value => add onto one threat
								if (self.Tab2PlayAICanAdd[i][j]) and (self.Tab2PlayAICanAdd[i-1][j]):
									self.Tab2PlayAI[i-1][j] += 1
									if self.Tab2PlayAI[i-1][j] > VG.ParBrickMaxValue:
										self.Tab2PlayAI[i-1][j] = VG.ParBrickMaxValue
									self.AIscore += 2**self.Tab2PlayAI[i-1][j]
									ScoreInc += 2**self.Tab2PlayAI[i-1][j]
									self.Tab2PlayAI[i][j] = 0
									self.Tab2PlayAICanAdd[i-1][j] = False
									self.Tab2PlayAICanAdd[i][j] = True
									isMoving = True
									hasMoved = True
			
			if sens == "right":
				for i in range(self.x - 2, -1, -1):
					for j in range(0,self.y):
						if (self.Tab2PlayAI[i][j] != 0):			#something
							if (self.Tab2PlayAI[i+1][j] == 0):	#empty => switch to left
								self.Tab2PlayAI[i+1][j] = self.Tab2PlayAI[i][j]
								self.Tab2PlayAI[i][j] = 0
								self.Tab2PlayAICanAdd[i+1][j] = self.Tab2PlayAICanAdd[i][j]
								self.Tab2PlayAICanAdd[i][j] = True
								isMoving = True
								hasMoved = True
							elif (self.Tab2PlayAI[i+1][j] == self.Tab2PlayAI[i][j]): #same value => add onto one threat
								if (self.Tab2PlayAICanAdd[i][j]) and (self.Tab2PlayAICanAdd[i+1][j]):
									self.Tab2PlayAI[i+1][j] += 1
									if self.Tab2PlayAI[i+1][j] > VG.ParBrickMaxValue:
										self.Tab2PlayAI[i+1][j] = VG.ParBrickMaxValue
									self.AIscore += 2**self.Tab2PlayAI[i+1][j] 
									ScoreInc += 2**self.Tab2PlayAI[i+1][j]
									self.Tab2PlayAI[i][j] = 0
									self.Tab2PlayAICanAdd[i+1][j] = False
									self.Tab2PlayAICanAdd[i][j] = True
									isMoving = True
									hasMoved = True
			
			if sens == "up":
				for i in range(0,self.x):
					for j in range(1,self.y):
						if (self.Tab2PlayAI[i][j] != 0):			#something
							if (self.Tab2PlayAI[i][j-1] == 0):	#empty => switch to left
								self.Tab2PlayAI[i][j-1] = self.Tab2PlayAI[i][j]
								self.Tab2PlayAI[i][j] = 0
								self.Tab2PlayAICanAdd[i][j-1] = self.Tab2PlayAICanAdd[i][j]
								self.Tab2PlayAICanAdd[i][j] = True
								isMoving = True
								hasMoved = True
							elif (self.Tab2PlayAI[i][j-1] == self.Tab2PlayAI[i][j]): #same value => add onto one threat
								if (self.Tab2PlayAICanAdd[i][j]) and (self.Tab2PlayAICanAdd[i][j-1]):
									self.Tab2PlayAI[i][j-1] += 1
									if self.Tab2PlayAI[i][j-1] > VG.ParBrickMaxValue:
										self.Tab2PlayAI[i][j-1] = VG.ParBrickMaxValue
									self.AIscore += 2**self.Tab2PlayAI[i][j-1]
									ScoreInc += 2**self.Tab2PlayAI[i][j-1]
									self.Tab2PlayAI[i][j] = 0
									self.Tab2PlayAICanAdd[i][j-1] = False
									self.Tab2PlayAICanAdd[i][j] = True
									isMoving = True
									hasMoved = True

			if sens == "down":
				for i in range(0,self.x):
					for j in range(self.y - 2, -1, -1):
						if (self.Tab2PlayAI[i][j] != 0):			#something
							if (self.Tab2PlayAI[i][j+1] == 0):	#empty => switch to left
								self.Tab2PlayAI[i][j+1] = self.Tab2PlayAI[i][j]
								self.Tab2PlayAI[i][j] = 0
								self.Tab2PlayAICanAdd[i][j+1] = self.Tab2PlayAICanAdd[i][j]
								self.Tab2PlayAICanAdd[i][j] = True
								isMoving = True
								hasMoved = True
							elif (self.Tab2PlayAI[i][j+1] == self.Tab2PlayAI[i][j]): #same value => add onto one threat
								if (self.Tab2PlayAICanAdd[i][j]) and (self.Tab2PlayAICanAdd[i][j+1]):
									self.Tab2PlayAI[i][j+1] += 1
									if self.Tab2PlayAI[i][j+1] > VG.ParBrickMaxValue:
										self.Tab2PlayAI[i][j+1] = VG.ParBrickMaxValue
									self.AIscore += 2**self.Tab2PlayAI[i][j+1] 
									ScoreInc += 2**self.Tab2PlayAI[i][j+1]
									self.Tab2PlayAI[i][j] = 0
									self.Tab2PlayAICanAdd[i][j+1] = False
									self.Tab2PlayAICanAdd[i][j] = True
									isMoving = True
									hasMoved = True
				
		Tab2PlayAIResult = [list(i) for i in [list (j) for j in self.Tab2PlayAI] ]
		self.Tab2PlayAI = [list(i) for i in [list (j) for j in Tab2PlayAISaved] ]
		self.Tab2PlayAICanAdd = [list(i) for i in [list (j) for j in Tab2PlayAICanAddSaved] ]
		return ScoreInc, Tab2PlayAIResult, hasMoved
		

	def bestMoveLevel1(self):
		""" shift panel from point to new position point all sens left, right, up, down 
		return dict how many point increase for each sens recursive level 2.
		this doesn't consider new tiles which will appears """

		sensListLevel = ["left", "right", "up", "down"]
		ScoreListLevel = []
		ScoreListLevel2 = []
		for ii, sens1 in enumerate(sensListLevel):
			ScoreListLevel.append([])
			ScoreListLevel2.append([])
			scoreMoving, Tab2Play1AIResult, hasMoved = self.move(sens1)
			ScoreListLevel2[ii].append((sens1, scoreMoving))
			ScoreListLevel[ii].append((sens1, scoreMoving))

			hasMoved = False
			if hasMoved:
				for jj, sens2 in enumerate(sensListLevel):
					Tab2Play1AIResultWorking = [list(i) for i in [list (j) for j in Tab2Play1AIResult] ]
					Tab2PlayAIRecursive = Tab2PlayAI(Tab2Play1AIResultWorking)
					scoreMoving, Tab2Play1AIResultWorking2, hasMoved = Tab2PlayAIRecursive.move(sens2)
					ScoreListLevel[ii].append((sens2, scoreMoving))
					ScoreListLevel2[ii].append((sens2, scoreMoving + ScoreListLevel2[ii][0][1]))
			else:
				for jj, sens2 in enumerate(sensListLevel):
					scoreMoving = 0
					ScoreListLevel[ii].append((sens2, scoreMoving))
					ScoreListLevel2[ii].append((sens2, scoreMoving + ScoreListLevel2[ii][0][1]))

		#print (ScoreListLevel)
		#print (ScoreListLevel2)
		Movement = "left"
		MovementScore1 = 0 # nb point of 1st mouvment
		MovementScore = 0 ## nb point of final mouvment
		# si le mouvement final remporte le plus de point, alors on garde le 1er mouvement de la liste
		# il faut egalement que le 1er mouvement ai shifté
		# sinon c'est le 1er mouvement qui compte
		for i, move3 in enumerate(ScoreListLevel2):
			for Score in move3:
				#print (move3, Score[1])
				if Score[1] > MovementScore:
					Movement = move3[0][0]
					MovementScore = Score[1]
					MovementScore1 = move3[0][1]
				if Score[1] == MovementScore:
					if move3[0][1] > MovementScore1:
						Movement = move3[0][0]
						MovementScore = Score[1]
						MovementScore1 = move3[0][1]
		
		# si tout les scores sont a zero
		if MovementScore == 0:
			canMove, Movement = self.canMove()
		
		print ("BEST MOVE: %s" %(Movement) )
		return Movement
		

	def bestMoveLevel2(self):
		""" shift panel from point to new position point all sens left, right, up, down 
		return dict how many point increase for each sens recursive level 2.
		this doesn't consider new tiles which will appears """

		sensListLevel = ["left", "right", "up", "down"]
		ScoreListLevel = []
		ScoreListLevel2 = []
		for ii, sens1 in enumerate(sensListLevel):
			ScoreListLevel.append([])
			ScoreListLevel2.append([])
			scoreMoving, Tab2Play1AIResult, hasMoved = self.move(sens1)
			ScoreListLevel2[ii].append((sens1, scoreMoving))
			ScoreListLevel[ii].append((sens1, scoreMoving))
			if hasMoved:
				for jj, sens2 in enumerate(sensListLevel):
					Tab2Play1AIResultWorking = [list(i) for i in [list (j) for j in Tab2Play1AIResult] ]
					Tab2PlayAIRecursive = Tab2PlayAI(Tab2Play1AIResultWorking)
					scoreMoving, Tab2Play1AIResultWorking2, hasMoved = Tab2PlayAIRecursive.move(sens2)
					ScoreListLevel[ii].append((sens2, scoreMoving))
					ScoreListLevel2[ii].append((sens2, scoreMoving + ScoreListLevel2[ii][0][1]))
			else:
				for jj, sens2 in enumerate(sensListLevel):
					scoreMoving = 0
					ScoreListLevel[ii].append((sens2, scoreMoving))
					ScoreListLevel2[ii].append((sens2, scoreMoving + ScoreListLevel2[ii][0][1]))

		#print (ScoreListLevel)
		#print (ScoreListLevel2)
		Movement = "left"
		MovementScore1 = 0 # nb point of 1st mouvment
		MovementScore = 0 ## nb point of final mouvment
		# si le mouvement final remporte le plus de point, alors on garde le 1er mouvement de la liste
		# il faut egalement que le 1er mouvement ai shifté
		# sinon c'est le 1er mouvement qui compte
		for i, move3 in enumerate(ScoreListLevel2):
			for Score in move3:
				#print (move3, Score[1])
				if Score[1] > MovementScore:
					Movement = move3[0][0]
					MovementScore = Score[1]
					MovementScore1 = move3[0][1]
				if Score[1] == MovementScore:
					if move3[0][1] > MovementScore1:
						Movement = move3[0][0]
						MovementScore = Score[1]
						MovementScore1 = move3[0][1]
		
		# si tout les scores sont a zero
		if MovementScore == 0:
			canMove, Movement = self.canMove()
		
		print ("BEST MOVE: %s" %(Movement) )
		return Movement
		

	def bestMoveLevel2vsH(self):
		""" best move as AI vs Human, (1st move)-(2nd move) >= 0 """

		sensListLevel = ["left", "right", "up", "down"]
		ScoreListLevel = []
		ScoreListLevel2 = []
		for ii, sens1 in enumerate(sensListLevel):
			ScoreListLevel.append([])
			ScoreListLevel2.append([])
			scoreMoving, Tab2Play1AIResult, hasMoved = self.move(sens1)
			ScoreListLevel2[ii].append((sens1, scoreMoving))
			ScoreListLevel[ii].append((sens1, scoreMoving))
			if hasMoved:
				for jj, sens2 in enumerate(sensListLevel):
					Tab2Play1AIResultWorking = [list(i) for i in [list (j) for j in Tab2Play1AIResult] ]
					Tab2PlayAIRecursive = Tab2PlayAI(Tab2Play1AIResultWorking)
					scoreMoving, Tab2Play1AIResultWorking2, hasMoved = Tab2PlayAIRecursive.move(sens2)
					ScoreListLevel[ii].append((sens2, scoreMoving))
					#best move as AI vs Human, (1st move)-(2nd move) >= 0
					ScoreListLevel2[ii].append((sens2, ScoreListLevel2[ii][0][1] - scoreMoving ))
			else:
				for jj, sens2 in enumerate(sensListLevel):
					scoreMoving = 0
					ScoreListLevel[ii].append((sens2, scoreMoving))
					ScoreListLevel2[ii].append((sens2, scoreMoving + ScoreListLevel2[ii][0][1]))

		#print (ScoreListLevel)
		#print (ScoreListLevel2)
		Movement = "left"
		MovementScore1 = -8192 # nb point of 1st mouvment
		MovementScore = -8192 ## nb point of final mouvment
		# si le mouvement final remporte le plus de point, alors on garde le 1er mouvement de la liste
		# il faut egalement que le 1er mouvement ai shifté
		# sinon c'est le 1er mouvement qui compte
		for i, move3 in enumerate(ScoreListLevel2):
			for Score in move3:
				#print (move3, Score[1])
				if Score[1] > MovementScore:
					Movement = move3[0][0]
					MovementScore = Score[1]
					MovementScore1 = move3[0][1]
				if Score[1] == MovementScore:
					if move3[0][1] > MovementScore1:
						Movement = move3[0][0]
						MovementScore = Score[1]
						MovementScore1 = move3[0][1]
		
		# if all scores at zero, there is no point to got
		if MovementScore == 0:
			canMove, Movement = self.canMove()
		
		print ("BEST MOVE: %s" %(Movement) )
		return Movement
		

	def bestMoveLevel3(self):
		""" shift panel from point to new position point all sens left, right, up, down 
		return dict how many point increase for each sens recursive level 2.
		this doesn't consider new tiles which will appears """

		sensListLevel = ["left", "right", "up", "down"]
		ScoreListLevel = []
		ScoreListLevel2 = []
		for ii, sens1 in enumerate(sensListLevel):
			ScoreListLevel.append([])
			ScoreListLevel2.append([])
			scoreMoving, Tab2Play1AIResult, hasMoved = self.move(sens1)
			ScoreListLevel2[ii].append((sens1, scoreMoving))
			ScoreListLevel[ii].append((sens1, scoreMoving))
			if hasMoved:
				for jj, sens2 in enumerate(sensListLevel):
					Tab2Play1AIResultWorking = [list(i) for i in [list (j) for j in Tab2Play1AIResult] ]
					Tab2PlayAIRecursive = Tab2PlayAI(Tab2Play1AIResultWorking)
					scoreMoving, Tab2Play1AIResultWorking2, hasMoved = Tab2PlayAIRecursive.move(sens2)
					ScoreListLevel[ii].append((sens2, scoreMoving))
					ScoreListLevel2[ii].append((sens2, scoreMoving + ScoreListLevel2[ii][0][1]))
					
					for kk, sens3 in enumerate(sensListLevel):
						Tab2Play1AIResultWorking3 = [list(i) for i in [list (j) for j in Tab2Play1AIResultWorking2] ]
						Tab2PlayAIRecursive2 = Tab2PlayAI(Tab2Play1AIResultWorking3)
						scoreMoving, Tab2Play1AIResultWorking4, hasMoved = Tab2PlayAIRecursive2.move(sens3)
						ScoreListLevel[ii].append((sens3, scoreMoving))
						ScoreListLevel2[ii].append((sens3, scoreMoving + ScoreListLevel2[ii][0][1]+ScoreListLevel2[ii][jj][1]))

			else:
				for jj, sens2 in enumerate(sensListLevel):
					scoreMoving = 0
					ScoreListLevel[ii].append((sens2, scoreMoving))
					ScoreListLevel2[ii].append((sens2, scoreMoving + ScoreListLevel2[ii][0][1]))
					for kk, sens3 in enumerate(sensListLevel):
						scoreMoving = 0
						ScoreListLevel[ii].append((sens3, scoreMoving))
						ScoreListLevel2[ii].append((sens3, scoreMoving + ScoreListLevel2[ii][0][1]))

		#print (ScoreListLevel)
		#print (ScoreListLevel2)
		Movement = "left"
		MovementScore1 = 0 # nb point of 1st mouvment
		MovementScore = 0 ## nb point of final mouvment
		# si le mouvement final remporte le plus de point, alors on garde le 1er mouvement de la liste
		# il faut egalement que le 1er mouvement ai shifté
		# sinon c'est le 1er mouvement qui compte
		for i, move3 in enumerate(ScoreListLevel2):
			for Score in move3:
				#print (move3, Score[1])
				if Score[1] > MovementScore:
					Movement = move3[0][0]
					MovementScore = Score[1]
					MovementScore1 = move3[0][1]
				if Score[1] == MovementScore:
					if move3[0][1] > MovementScore1:
						Movement = move3[0][0]
						MovementScore = Score[1]
						MovementScore1 = move3[0][1]
		
		# si tout les scores sont a zero
		if MovementScore == 0:
			canMove, Movement = self.canMove()
		
		print ("BEST MOVE: %s" %(Movement) )
		return Movement
		

	def bestMove(self):
		""" shift panel from point to new position point all sens left, right, up, down 
		return dict how many point increase for each sens"""
		
		sensList = ["left", "right", "up", "down"]
		ScoreDict = {"left":0, "right":0, "up":0, "down":0}

		canMove, moveSens = self.canMove()
		if not(canMove):
				return ScoreDict
			
		#print ("Tab2PlayAI: %s" % (self.Tab2PlayAI) )
		Tab2PlayAISaved = [list(i) for i in [list (j) for j in self.Tab2PlayAI] ]
		Tab2PlayAICanAddSaved = [list(i) for i in [list (j) for j in self.Tab2PlayAICanAdd] ]

		for sens in sensList:
			#print ("AI BEST MOVE FOR %s" % sens)
			self.Tab2PlayAI = [list(i) for i in [list (j) for j in Tab2PlayAISaved] ]
			self.Tab2PlayAICanAdd = [list(i) for i in [list (j) for j in Tab2PlayAICanAddSaved] ]
			#print (self.Tab2PlayAI)
			#print (self.Tab2PlayAICanAdd)
			
			ScoreInc = 0
			isMoving = True
			while isMoving == True:
				isMoving = False
				if sens == "left":
					for i in range(1,self.x):
						for j in range(0,self.y):
							if (self.Tab2PlayAI[i][j] != 0):			#something
								#print ("found %s @ x=%s, y=%s)" %(self.Tab2PlayAI[i][j], i, j) )
								if (self.Tab2PlayAI[i-1][j] == 0):	#empty => switch to left
									#print ("AI switch to left x=%s, y=%s, sc=%s" %( i, j, self.Tab2PlayAI[i][j]) )
									self.Tab2PlayAI[i-1][j] = self.Tab2PlayAI[i][j]
									self.Tab2PlayAI[i][j] = 0
									self.Tab2PlayAICanAdd[i-1][j] = self.Tab2PlayAICanAdd[i][j]
									self.Tab2PlayAICanAdd[i][j] = True
									isMoving = True
								elif (self.Tab2PlayAI[i-1][j] == self.Tab2PlayAI[i][j]): #same value => add onto one threat
									if (self.Tab2PlayAICanAdd[i][j]) and (self.Tab2PlayAICanAdd[i-1][j]):
										#print ("AI ADD2LEFT x=%s, y=%s, sc=%s" %( i, j, self.Tab2PlayAI[i][j]) )
										self.Tab2PlayAI[i-1][j] += 1
										if self.Tab2PlayAI[i-1][j] > VG.ParBrickMaxValue:
											self.Tab2PlayAI[i-1][j] = VG.ParBrickMaxValue
										self.AIscore += 2**self.Tab2PlayAI[i-1][j]
										ScoreInc += 2**self.Tab2PlayAI[i-1][j]
										self.Tab2PlayAI[i][j] = 0
										self.Tab2PlayAICanAdd[i-1][j] = False
										self.Tab2PlayAICanAdd[i][j] = True
										isMoving = True
				
				if sens == "right":
					for i in range(self.x - 2, -1, -1):
						for j in range(0,self.y):
							if (self.Tab2PlayAI[i][j] != 0):			#something
								if (self.Tab2PlayAI[i+1][j] == 0):	#empty => switch to left
									#print ("AI switch to right x=%s, y=%s, sc=%s" %( i, j, self.Tab2PlayAI[i][j]) )
									self.Tab2PlayAI[i+1][j] = self.Tab2PlayAI[i][j]
									self.Tab2PlayAI[i][j] = 0
									self.Tab2PlayAICanAdd[i+1][j] = self.Tab2PlayAICanAdd[i][j]
									self.Tab2PlayAICanAdd[i][j] = True
									isMoving = True
								elif (self.Tab2PlayAI[i+1][j] == self.Tab2PlayAI[i][j]): #same value => add onto one threat
									if (self.Tab2PlayAICanAdd[i][j]) and (self.Tab2PlayAICanAdd[i+1][j]):
										#print ("AI ADD2RIGHT x=%s, y=%s, sc=%s" %( i, j, self.Tab2PlayAI[i][j]) )
										self.Tab2PlayAI[i+1][j] += 1
										if self.Tab2PlayAI[i+1][j] > VG.ParBrickMaxValue:
											self.Tab2PlayAI[i+1][j] = VG.ParBrickMaxValue
										self.AIscore += 2**self.Tab2PlayAI[i+1][j] 
										ScoreInc += 2**self.Tab2PlayAI[i+1][j]
										self.Tab2PlayAI[i][j] = 0
										self.Tab2PlayAICanAdd[i+1][j] = False
										self.Tab2PlayAICanAdd[i][j] = True
										isMoving = True
				
				if sens == "up":
					for i in range(0,self.x):
						for j in range(1,self.y):
							if (self.Tab2PlayAI[i][j] != 0):			#something
								#print ("found %s @ x=%s, y=%s)" %(self.Tab2PlayAI[i][j], i, j) )
								if (self.Tab2PlayAI[i][j-1] == 0):	#empty => switch to left
									#print ("AI switch to up x=%s, y=%s, sc=%s" %( i, j, self.Tab2PlayAI[i][j]) )
									self.Tab2PlayAI[i][j-1] = self.Tab2PlayAI[i][j]
									self.Tab2PlayAI[i][j] = 0
									self.Tab2PlayAICanAdd[i][j-1] = self.Tab2PlayAICanAdd[i][j]
									self.Tab2PlayAICanAdd[i][j] = True
									isMoving = True
								elif (self.Tab2PlayAI[i][j-1] == self.Tab2PlayAI[i][j]): #same value => add onto one threat
									if (self.Tab2PlayAICanAdd[i][j]) and (self.Tab2PlayAICanAdd[i][j-1]):
										#print ("AI ADD2UP x=%s, y=%s, sc=%s" %( i, j, self.Tab2PlayAI[i][j]) )
										self.Tab2PlayAI[i][j-1] += 1
										if self.Tab2PlayAI[i][j-1] > VG.ParBrickMaxValue:
											self.Tab2PlayAI[i][j-1] = VG.ParBrickMaxValue
										self.AIscore += 2**self.Tab2PlayAI[i][j-1]
										ScoreInc += 2**self.Tab2PlayAI[i][j-1]
										self.Tab2PlayAI[i][j] = 0
										self.Tab2PlayAICanAdd[i][j-1] = False
										self.Tab2PlayAICanAdd[i][j] = True
										isMoving = True

				if sens == "down":
					for i in range(0,self.x):
						for j in range(self.y - 2, -1, -1):
							if (self.Tab2PlayAI[i][j] != 0):			#something
								#print ("found %s @ x=%s, y=%s)" %(self.Tab2PlayAI[i][j], i, j) )
								if (self.Tab2PlayAI[i][j+1] == 0):	#empty => switch to left
									#print ("AI switch to right x=%s, y=%s, sc=%s" %( i, j, self.Tab2PlayAI[i][j]) )
									self.Tab2PlayAI[i][j+1] = self.Tab2PlayAI[i][j]
									self.Tab2PlayAI[i][j] = 0
									self.Tab2PlayAICanAdd[i][j+1] = self.Tab2PlayAICanAdd[i][j]
									self.Tab2PlayAICanAdd[i][j] = True
									isMoving = True
								elif (self.Tab2PlayAI[i][j+1] == self.Tab2PlayAI[i][j]): #same value => add onto one threat
									if (self.Tab2PlayAICanAdd[i][j]) and (self.Tab2PlayAICanAdd[i][j+1]):
										#print ("AI ADD2DOWN x=%s, y=%s, sc=%s" %( i, j, self.Tab2PlayAI[i][j]) )
										self.Tab2PlayAI[i][j+1] += 1
										if self.Tab2PlayAI[i][j+1] > VG.ParBrickMaxValue:
											self.Tab2PlayAI[i][j+1] = VG.ParBrickMaxValue
										self.AIscore += 2**self.Tab2PlayAI[i][j+1] 
										ScoreInc += 2**self.Tab2PlayAI[i][j+1]
										self.Tab2PlayAI[i][j] = 0
										self.Tab2PlayAICanAdd[i][j+1] = False
										self.Tab2PlayAICanAdd[i][j] = True
										isMoving = True									
			
			#print ("AI BEST MOVE FOR %s: %s" % (sens, ScoreInc) )
			ScoreDict[sens] = ScoreInc
		
			self.Tab2PlayAI = [list(i) for i in [list (j) for j in Tab2PlayAISaved] ]
			self.Tab2PlayAICanAdd = [list(i) for i in [list (j) for j in Tab2PlayAICanAddSaved] ]

		self.Tab2PlayAI = [list(i) for i in [list (j) for j in Tab2PlayAISaved] ]
		self.Tab2PlayAICanAdd = [list(i) for i in [list (j) for j in Tab2PlayAICanAddSaved] ]
		return ScoreDict
		
