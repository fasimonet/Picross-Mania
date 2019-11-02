# Créé par Fabien et Quentin, le 21/03/2016 en Python 3.2
# Classes du programme "grille"
import pygame
from pygame.locals import *

#-------------------------------------------------------------------------------
#                AFFICHAGE DES EN-TETES DES PAGES DES NIVEAUX
#-------------------------------------------------------------------------------

"""Cette fonction créé une en-tête pour chaque niveau qui est composée d'une icone
représentant le niveau (image) et du nom du niveau (texte) et l'affiche. """

def affichage_entete_niveau(ICONE_NIVEAU, COORDONNEE_POINT_COLLAGE_ICONE_NIVEAU):
    #- On affiche l'icone du niveau
    FENETRE.blit(ICONE_NIVEAU, COORDONNEE_POINT_COLLAGE_ICONE_NIVEAU)

#-------------------------------------------------------------------------------
#                CALCUL DE LA SOMME DES ELEMENTS D'UNE LISTE
#-------------------------------------------------------------------------------

"""Cette fonction calcule et retourne la somme des éléments d'une liste."""

def somme_elements_liste(LISTE):
    INDEX = 0
    SOMME = 0
    while INDEX < len(LISTE):
        SOMME += LISTE[INDEX]
        INDEX += 1
    return SOMME


