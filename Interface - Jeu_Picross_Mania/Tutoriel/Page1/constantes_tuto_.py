﻿#Créé par Fabien, le 21/03/2016 en Python 3.2
#Constantes du programme "grille"

import pygame
from pygame.locals import *

#CARACTERISTIQUES DE LA FENETRE
#Longueur de la fenetre
LONGUEUR_FENETRE = 800
#Largeur de la fenetre
HAUTEUR_FENETRE = 650
#Titre de la fenetre
TITRE_FENETRE = "Picross Mania"

#NOM DES COULEURS
NOIR = (0,0,0)
VERT_PIN = (1,121,111)
CANARD = (4,139,154)
BLANC_CREME = (253, 241, 184)

#IMAGES
TITRE_TUTORIEL = pygame.image.load("tutoriel_titre2.PNG")

#TEXTE A AFFICHER
TEXTE = "Je suis un tutoriel à compléter (Au fait Sinan est moche :-p)"