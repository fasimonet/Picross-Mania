﻿#Créé par Fabien, le 21/03/2016 en Python 3.2
#Constantes du programme "grille"
#FICHIER TEST

#LISTE DES VARIABLES
#Longueur de la fenetre
LONGUEUR_FENETRE = 800
#Largeur de la fenetre
HAUTEUR_FENETRE = 650
#Titre de la fenetre
TITRE_FENETRE = "Picross Mania"
#Recuperation de l'abscisse de la position de la souris
ABSCISSE_CLIC = event.pos[0]
#Recuperation de l'ordonnee de la position de la souris
ORDONNEE_CLIC = event.pos[1]

#NOM DES COULEURS
NOIR = (0,0,0)
VERT_PIN = (1,121,111)
CANARD = (4,139,154)
BLANC_CREME = (253, 241, 184)

#Grille
MATRICE_GRILLE = [[0, 0, 0, 0, 0]
                  [0, 0, 0, 0, 0]
                  [0, 0, 0, 0, 0]
                  [0, 0, 0, 0, 0]
                  [0, 0, 0, 0, 0]]

"""pygame.Rect.collidepoint	—	test if a point is inside a rectangle"""