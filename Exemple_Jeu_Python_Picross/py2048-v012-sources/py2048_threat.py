#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys, os, random, time, math

import pygame
from pygame.locals import *

import py2048_VG as VG

pygame.init()

class threat(pygame.sprite.Sprite):
	def __init__(self, image=0, x=0, y=0, score=0):
		pygame.sprite.Sprite.__init__(self)

		self.x = x
		self.y = y
		if score == 0:
			self.score = 0
		else: 
			self.score = 2**score

		#self.image = pygame.image.load("Images/%s" %image)
		if image<0:
			image = 0
		if image>14:
			image = 14
		self.image = VG.cList[image]
		
		#tostring(Surface, format, flipped=False) -> string
		self.imageOri = pygame.image.tostring(self.image, "RGBA_PREMULT")
		#fromstring(string, size, format, flipped=False) -> Surface
		#self.image = pygame.image.fromstring(self.imageOri, self.rect, "RGBA_PREMULT")
		
		self.rect = self.image.get_rect()
		self.rect.x = self.x * 90
		self.rect.y = self.y * 90
		
		self.shooted(self.score) #only to blit the score
		
	def shooted(self, score):
		self.score = score
		if self.score < 0:
			self.score = 0

		self.image = pygame.image.fromstring(self.imageOri, (self.rect[2], self.rect[3]), "RGBA")
		# Score remain
		if self.score > 1:
			#rebuilt completly the new png image with new score
			#self.image = pygame.image.fromstring(self.imageOri, (self.rect[2], self.rect[3]), "RGBA")

			self.textScore = VG.minileter48.render(str(self.score), 1, VG.Red) #red
			self.textScore2 = VG.minileter48.render(str(self.score), 1, (0,0,0)) #black
			if self.score > 99:
				self.textScore = VG.minileter42.render(str(self.score), 1, (255,0,0)) #red
				self.textScore2 = VG.minileter42.render(str(self.score), 1, (0,0,0)) #black
			if self.score > 999:
				self.textScore = VG.minileter32.render(str(self.score), 1, VG.DeepYellow) #red
				self.textScore2 = VG.minileter32.render(str(self.score), 1, (0,0,0)) #black
				self.textScore2 = VG.minileter32.render(str(self.score), 1, VG.DeepRed) #white

			self.textScorePos = self.textScore.get_rect()
			self.textScorePos[0] = (self.rect[2]-self.textScorePos[2])/2
			self.textScorePos[1] = (self.rect[3]-self.textScorePos[3])/2
			#for contrast
			self.textScore2Pos = self.textScore2.get_rect()
			self.textScore2Pos[0] = (self.rect[2]-self.textScore2Pos[2])/2 + 3
			self.textScore2Pos[1] = (self.rect[3]-self.textScore2Pos[3])/2 + 3

			self.image.blit(self.textScore2, (self.textScore2Pos[0], self.textScore2Pos[1])) # 1st black
			self.image.blit(self.textScore, (self.textScorePos[0], self.textScorePos[1])) # then red

	def getScore(self):
		return self.score
		
	def getImage(self):
		return self.image

	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def getRectX(self):
		return self.rect.x
		
	def getRectY(self):
		return self.rect.y
		
	def getRect(self):
		return self.rect
		
