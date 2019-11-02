#!/usr/bin/env python
# -*- coding: utf8 -*-

# py2048 Variables Globales

import os, sys, time, random #, platform, threading, math
import pygame
from pygame.locals import *

from py2048_threat import threat

py2048_version = "0.1.2"

pdb_debug = False
#pdb_debug = True

hiScore = 0
hiMove = 0
hiScoreSmall = 512
hiMoveSmall = 0
hiScoreMedium = 1024
hiMoveMedium = 0
hiScoreLarge = 2048
hiMoveLarge = 0

minileter48 = pygame.font.Font("freesansbold.ttf",48)
minileter42 = pygame.font.Font("freesansbold.ttf",42)
minileter32 = pygame.font.Font("freesansbold.ttf",32)
minileter28 = pygame.font.Font("freesansbold.ttf",28)
minileter24 = pygame.font.Font("freesansbold.ttf",24)

#bckGnd = pygame.image.load("Images/Ultimate_Matrix_1.jpg")
bckGnd = pygame.image.load("Images/L0000.jpg")
bckGnd0000 = pygame.image.load("Images/L0000.jpg")
bckGnd1024 = pygame.image.load("Images/L1024.jpg")
bckGnd2048 = pygame.image.load("Images/L2048.jpg")
bckGnd4096 = pygame.image.load("Images/L4096.jpg")
bckGnd8192 = pygame.image.load("Images/L8192.jpg")


cvide = pygame.image.load("Images/cvide.png")
c0 = pygame.image.load("Images/c0.png")
c1 = pygame.image.load("Images/c1.png")
c2 = pygame.image.load("Images/c2.png")
c3 = pygame.image.load("Images/c3.png")
c4 = pygame.image.load("Images/c4.png")
c5 = pygame.image.load("Images/c5.png")
c6 = pygame.image.load("Images/c6.png")
c7 = pygame.image.load("Images/c7.png")
c8 = pygame.image.load("Images/c8.png")
c9 = pygame.image.load("Images/c9.png")
c10 = pygame.image.load("Images/c10.png")
c11 = pygame.image.load("Images/c11.png")
c12 = pygame.image.load("Images/c12.png")
c13 = pygame.image.load("Images/c13.png")
cList = [cvide, c0, c1, c2, c3, c4, c5, c7, c6, c8, c9, c10, c11, c12, c13]

#Colors RGB
Aqua=(0, 255, 255)
Black=(0, 0, 0)
Blue=(0, 0, 255)
DeepBlue=(0, 0, 210)
#DeepBlue=(0, 0, 160)
Fuchsia=(255, 0, 255)
Gray=(128, 128, 128)
Green=(0, 255, 0)
#DeepGreen=(0, 164, 0)
DeepGreen=(0, 140, 0)
Lime=(0, 255, 0)
Brown=(128, 0, 0)
NavyBlue=(0, 0, 128)
Olive=(128, 128, 0)
Purple=(128, 0, 128)
LightRed=(255, 64, 64)
LightRed=(255, 96, 64)
Red=(255, 0, 0)
#DeepRed=(200, 0, 0)
DeepRed=(160, 0, 0)
Silver=(192, 192, 192)
Teal=(0, 128, 128)
White=(255, 255, 255)
Yellow=(255, 255, 0)
#DeepYellow=(210, 210, 0)
DeepYellow=(160, 160, 0)


## Loaded in py2048.cfg
ParFPS = 60

ParBrickNewMin = 1
ParBrickNewMax = 3
#ParBrickMinValue = 2
ParBrickMaxValue = 13
ParRaws = 4
ParColumns = 4
ParRawsSmall = 3
ParColumnsSmall = 3
ParRawsMedium = 6
ParColumnsMedium = 6
ParRawsLarge = 8
ParColumnsLarge = 8
# Saved In Hiscores, 0=Small, 1=Medium, 2=Large
ParSizeActu = 0

ParAllowNoMove = False

#Note: enable if ParLimitTime2Move >0, Then ParAllowNoMove will allways Set True
ParLimitTime2Move = 0
LimitTime2Move = 0

Par1StepMove = False
ParAutoSaveOnExit = False

ParMusicYN = True
ParMusicVol = 0.4

ParNetGamePort = 9666

autoAIToggle = False
autoAILevel = "ai2"

ParP2UseArrow = False
ParP2Left = "4"
ParP2Right = "6"
ParP2Up = "8"
ParP2Down = "2"

#################################################
def load_cfg(name="py2048.cfg"):
	""" Load file py2048.cfg and return config paramters
	return (ParFPS, ParBrickNewMin, ParBrickNewMax, ParBrickMaxValue, ParRaws, ParColumns
	ParAllowNoMove, ParLimitTime2Move, Par1StepMove, ParMusicYN, ParMusicVol)"""

	#DEFAULT VALUES IF NOT FOUND IN CONFIG FILE
	ParFPS = 60

	ParBrickNewMin = 1
	ParBrickNewMax = 3
	#ParBrickMinValue = 2
	ParBrickMaxValue = 13
	ParRaws = 4
	ParColumns = 4
	ParRawsSmall = 4
	ParColumnsSmall = 4
	ParRawsMedium = 6
	ParColumnsMedium = 6
	ParRawsLarge = 8
	ParColumnsLarge = 8

	ParAllowNoMove = False

	#Note: enable if ParLimitTime2Move >0, Then ParAllowNoMove will allways Set True
	ParLimitTime2Move = 0
	LimitTime2Move = 0

	Par1StepMove = False
	ParAutoSaveOnExit = False

	ParMusicYN = True
	ParMusicVol = 0.4
	
	ParNetGamePort = 9666

	autoAIToggle = False
	autoAILevel = "ai2"

	ParP2UseArrow = False
	ParP2Left = "4"
	ParP2Right = "6"
	ParP2Up = "8"
	ParP2Down = "2"

	try:
		#open config file extension ".cfg" in correct directory.
		fullname = os.path.join('', name)
		configstext = []
		fichier = open(fullname,'r')
		# pass on each lines with command for
		for ligne in fichier.readlines() :
			# split line in words - split remove spaces and carriage return
			donnees = ligne.split()
			# finally add to config array 
			configstext.extend(donnees)
		# end of loop for, close config file
		fichier.close()
		
		#print (configstext)
		#WARNING: somes parameters in v10x only, have to check version header file!
		for idx, line in enumerate(configstext):
			#print (idx)
			if line =="[ParFPS]":
				ParFPS = eval(configstext[idx+1])
				print ("ParFPS: %s" %(ParFPS))
			if line =="[ParBrickNewMin]":
				ParBrickNewMin = eval(configstext[idx+1])
				print ("ParBrickNewMin: %s" %(ParBrickNewMin))
			if line =="[ParBrickNewMax]":
				ParBrickNewMax = eval(configstext[idx+1])
				print ("ParBrickNewMax: %s" %(ParBrickNewMax))
			if line =="[ParBrickMaxValue]":
				ParBrickMaxValue = eval(configstext[idx+1])
				print ("ParBrickMaxValue: %s" %(ParBrickMaxValue))
			if line =="[ParRaws]":
				ParRaws = eval(configstext[idx+1])
				print ("ParRaws: %s" %(ParRaws))
			if line =="[ParColumns]":
				ParColumns = eval(configstext[idx+1])
				print ("ParColumns: %s" %(ParColumns))

			if line =="[ParRawsSmall]":
				ParRawsSmall = eval(configstext[idx+1])
				print ("ParRawsSmall: %s" %(ParRawsSmall))
			if line =="[ParColumnsSmall]":
				ParColumnsSmall = eval(configstext[idx+1])
				print ("ParColumnsSmall: %s" %(ParColumnsSmall))
			if line =="[ParRawsMedium]":
				ParRawsMedium = eval(configstext[idx+1])
				print ("ParRawsMedium: %s" %(ParRawsMedium))
			if line =="[ParColumnsMedium]":
				ParColumnsMedium = eval(configstext[idx+1])
				print ("ParColumnsMedium: %s" %(ParColumnsMedium))
			if line =="[ParRawsLarge]":
				ParRawsLarge = eval(configstext[idx+1])
				print ("ParRawsLarge: %s" %(ParRawsLarge))
			if line =="[ParColumnsLarge]":
				ParColumnsLarge = eval(configstext[idx+1])
				print ("ParColumnsLarge: %s" %(ParColumnsLarge))

			if line =="[ParAllowNoMove]":
				ParAllowNoMove = eval(configstext[idx+1])
				print ("ParAllowNoMove: %s" %(ParAllowNoMove))
			if line =="[ParLimitTime2Move]":
				ParLimitTime2Move = eval(configstext[idx+1])
				print ("ParLimitTime2Move: %s" %(ParLimitTime2Move))
			if line =="[Par1StepMove]":
				Par1StepMove = eval(configstext[idx+1])
				print ("Par1StepMove: %s" %(Par1StepMove))
			if line =="[ParAutoSaveOnExit]":
				ParAutoSaveOnExit = eval(configstext[idx+1])
				print ("ParAutoSaveOnExit: %s" %(ParAutoSaveOnExit))
			if line =="[ParMusicYN]":
				ParMusicYN = eval(configstext[idx+1])
				print ("ParMusicYN: %s" %(ParMusicYN))
			if line =="[ParMusicVol]":
				ParMusicVol = eval(configstext[idx+1])
				print ("ParMusicVol: %s" %(ParMusicVol))

			if line =="[ParNetGamePort]":
				ParNetGamePort = eval(configstext[idx+1])
				print ("ParNetGamePort: %s" %(ParNetGamePort))


			if line =="[ParP2UseArrow]":
				ParP2UseArrow = eval(configstext[idx+1])
				print ("ParP2UseArrow: %s" %(ParP2UseArrow))
			if line =="[ParP2Left]":
				ParP2Left = eval(configstext[idx+1])
				print ("ParP2Left: %s" %(ParP2Left))
			if line =="[ParP2Right]":
				ParP2Right = eval(configstext[idx+1])
				print ("ParP2Right: %s" %(ParP2Right))
			if line =="[ParP2Up]":
				ParP2Up = eval(configstext[idx+1])
				print ("ParP2Up: %s" %(ParP2Up))
			if line =="[ParP2Down]":
				ParP2Down = eval(configstext[idx+1])
				print ("ParP2Down: %s" %(ParP2Down))

	except:
		print ("Warning: INVALIDE PARAMETERS IN %s !!!" %(name))

	return (ParFPS, ParBrickNewMin, ParBrickNewMax, ParBrickMaxValue, ParRaws, ParColumns, \
	ParRawsSmall, ParColumnsSmall, ParRawsMedium, ParColumnsMedium, ParRawsLarge, ParColumnsLarge, \
	ParAllowNoMove, ParLimitTime2Move, Par1StepMove, ParAutoSaveOnExit, ParMusicYN, ParMusicVol, ParNetGamePort, \
	ParP2UseArrow, ParP2Left, ParP2Right, ParP2Up, ParP2Down)

#################################################
def save_cfg(name="py2048.cfg"):
	""" Not Used, do Nothing"""
	
	print ("Warning: save_cfgINVALIDE PARAMETERS IN %s !!!" %(name))
	return
	
	fullname = os.path.join("", name)
	try:
		fichier = open(fullname, "w")
		
		fichier.write("# py2048.cfg version: %s\n" %(VG.FW1789_version))
		fichier.write("# only the 1st line just downside paramater is checked\n")

		fichier.write("[ParFPS]\n")
		fichier.write(str(ParFPS)+"\n")

		fichier.write("[ParGrabMouse]\n")
		fichier.write(str(ParGrabMouse)+"\n")
		fichier.write("True | False\n")

		fichier.write("[ParLife]\n")
		fichier.write(str(ParLife)+"\n")

		fichier.write("[ParBulletQty]\n")
		fichier.write(str(ParBulletQty)+"\n")

		fichier.write("[ParGrenadeQty]\n")
		fichier.write(str(ParGrenadeQty)+"\n")
		fichier.write("[ParGrenadeSpeed]\n")
		fichier.write(str(ParGrenadeSpeed)+"\n")

		fichier.write("[ParMusicYN]\n")
		fichier.write(str(ParMusicYN)+"\n")
		fichier.write("True | False\n")

		fichier.write("[ParMusicVol]\n")
		fichier.write(str(ParMusicVol)+"\n")

		# NOT USED
		a="""
		fichier.write("# not need, updated by level config\n")
		fichier.write("[ParDwngrdBrick]\n")
		fichier.write(str(ParDwngrdBrick)+"\n")

		fichier.write("[ParBallSpeedSlow]\n")
		fichier.write(str(ParBallSpeedSlow)+"\n")

		fichier.write("[ParBallSpeedFast]\n")
		fichier.write(str(ParBallSpeedFast)+"\n")

		fichier.write("[ParScreenSize]\n")
		fichier.write(str(ParScreenSize[0])+"\n")
		fichier.write("480 640 800\n")
		a="""

		fichier.close()

		print ("%s saved" %(name))
	#except pygame.error, message:
	except IOError:
		#_, e, _ = sys.exc_info()
		tb = sys.exc_info()
		#print (tb)
		tb = tb[1]
		print ("Warning: unable to save %s" %(name))

ParFPS, ParBrickNewMin, ParBrickNewMax, ParBrickMaxValue, ParRaws, ParColumns, \
ParRawsSmall, ParColumnsSmall, ParRawsMedium, ParColumnsMedium, ParRawsLarge, ParColumnsLarge, \
ParAllowNoMove, ParLimitTime2Move, Par1StepMove, ParAutoSaveOnExit, ParMusicYN, ParMusicVol, ParNetGamePort, \
ParP2UseArrow, ParP2Left, ParP2Right, ParP2Up, ParP2Down = load_cfg("py2048.cfg")
