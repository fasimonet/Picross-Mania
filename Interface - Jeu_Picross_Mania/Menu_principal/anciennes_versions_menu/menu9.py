#Cree par Fabien et Sinan le 11/04/2016 en Python 3.2
"""
________________________________________________________________________________

                            PRINCIPE DU PROGRAMME
________________________________________________________________________________


INTERFACE GRAPHIQUE DU JEU PICROSS MANIA

Elle est composée de plusieurs parties :
    - le menu principal
    - la page "picross à résoudre"
        - le niveau 1
        - le niveau 2
        - le niveau 3
        - le niveau 4
    - la page "création de picross"
    - la page "résolution de picross"
    - le tutoriel
        - comment résoudre un picross?
        - comment utiliser le résolveur automatique?
        - comment créer un picross?"""


################################################################################
#                  Import des Bibliothèques et des Annexes
################################################################################
#On importe le module pygame qui nous permet de créer l'interface graphique

import pygame
from pygame.locals import *
from numpy import *
# On initialise l'interface graphique.
pygame.init()


#On rattache le corps du programme aux annexes pour plus de clarté:
    #- les fonctions du menu
    #- les constantes du menu
    #- le corps du tutoriel
    #- les fonctions du tutoriel
    #- les constantes du tutoriel

from fonctions_menu import *
from constantes_menu import *
from fonctions_tuto import *
from constantes_tuto import *
from fonctions5x5_3 import *
from constantes5x5_3 import *
from niveau1 import *
from niveau2 import *

son_on = True

################################################################################
#                              Initialisation
################################################################################

#===============================================================================
#                        CARACTERISTIQUES DE LA FENETRE
#===============================================================================

# Création d'une variable "FENETRE" qui affiche la fenêtre du jeu
FENETRE = pygame.display.set_mode((LONGUEUR_FENETRE, HAUTEUR_FENETRE))

# Titre de la fenêtre
pygame.display.set_caption(TITRE_FENETRE)

#===============================================================================
#             RECAPITULATIF DE L'ETAT DE PROGRESSION DES GRILLES
#===============================================================================

#-------------------------------------------------------------------------------
#                                  NIVEAU 1
#-------------------------------------------------------------------------------

#Liste qui regarde si une grille est en cours et laquelle dans le niveau 1
PICROSS_EN_COURS_NIV1 = [False, False, False, False, False, False, False, False, False]

#Liste qui regarde quelles grilles sont complétées dans le niveau 1
PICROSS_COMPLETS_NIV1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

#Variable qui représente le nombre de picross complétés
SOMME_PICROSS_COMPLETS_NIV1 = 0

#-------------------------------------------------------------------------------
#                                  NIVEAU 2
#-------------------------------------------------------------------------------

#Liste qui regarde si une grille est en cours et laquelle dans le niveau 1
PICROSS_EN_COURS_NIV2 = [False, False, False, False, False, False, False, False, False]

#Liste qui regarde quelles grilles sont complétées dans le niveau 1
PICROSS_COMPLETS_NIV2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

#Variable qui représente le nombre de picross complétés
SOMME_PICROSS_COMPLETS_NIV2 = 0


#on initialise a "page_precedente" la valeur "aucune"
page_precedente = "aucune"

# Variable "continuer" à laquelle on affecte la valeur 1
# Cela va nous permettre de garder la fenêtre ouverte
continuer = 1

"""
________________________________________________________________________________

                            CORPS DU PROGRAMME
________________________________________________________________________________

"""
################################################################################
#                              Ecran Titre
################################################################################
#BOUCLE D'EXECUTION - Qui s'exécute tant que la variable "continuer" vaut 1
while continuer == 1:

# Initialisation des fenêtres : au départ seul le menu principal est ouvert
    continuer_picross_a_resoudre = 0
    continuer_niveau1 = 0
    continuer_niveau2 = 0
    continuer_niveau3 = 0
    continuer_niveau4 = 0
    continuer_mon_niveau = 0
    continuer_tutoriel = 0
    continuer_comment_resoudre_picross1 = 0
    continuer_comment_resoudre_picross2 = 0
    continuer_comment_creer_picross1 = 0
    continuer_comment_utiliser_resolveur1 = 0
    continuer_grille5x5 = 0
    continuer_grille10x10 = 0
    animation = 0
    continuer_menu = 1

    if continuer_menu == 1:
        if son_on == True:
            pygame.mixer.music.load("Menu_Picross.ogg")
            pygame.mixer.music.set_volume(0.25)
            pygame.mixer.music.play(-1, 0)
            FENETRE.blit(BOUTON_SON_ON, (725,25))
            pygame.display.flip()
        elif son_on == False:
            pygame.mixer.music.stop()
            FENETRE.blit(BOUTON_SON_OFF, (725,25))
            pygame.display.flip()


#BOUCLE D'AFFICHAGE DU MENU PRINCIPAL - Qui s'exécute tant que la variable "continuer_menu" vaut 1
    while continuer_menu == 1:

    # Met une couleur de fond
        FENETRE.fill(BLANC_CREME)
# Collage des différents boutons sur la fenêtre :
        #- le bouton "picross à résoudre"
        FENETRE.blit(BOUTON_PICROSS_A_RESOUDRE, (57,300))
        #- le bouton "résolution de picross"
        FENETRE.blit(BOUTON_RESOLUTION_DE_PICROSS, (304,300))
        #- le bouton "création de picross"
        FENETRE.blit(BOUTON_CREATION_DE_PICROSS, (551,300))
        #- le bouton "tutoriel"
        FENETRE.blit(BOUTON_TUTORIEL, (30,585))
        #- le logo du jeu "Picross Mania"
        FENETRE.blit(LOGO, (130,120))
        #- image son-on
        FENETRE.blit(BOUTON_SON_ON, (725, 25))

        if pygame.mouse.get_focused():
            if Rect_picross_a_resoudre.collidepoint(event.pos):
                FENETRE.blit(BOUTON_PICROSS_A_RESOUDRE_INTER, (38, 278))
            if Rect_resolution_de_picross.collidepoint(event.pos):
                FENETRE.blit(BOUTON_RESOLUTION_DE_PICROSS_INTER, (285, 278))
            if Rect_creation_picross.collidepoint(event.pos):
                FENETRE.blit(BOUTON_CREATION_DE_PICROSS_INTER, (532, 278))

        pygame.display.flip()

#BOUCLE PRINCIPALE - Qui s'exécute dans la BOUCLE D'AFFICHAGE DU MENU PRINCIPAL soit tant que la variable "continuer_menu" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

#BOUCLE DE FERMETURE - Qui s'exécute dans la BOUCLE PRINCIPALE
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
            if event.type == QUIT:
                continuer_menu = 0
                continuer = 0

#BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE" - Qui s'exécute dans la BOUCLE PRINCIPALE
# Si un de ces événements est de type "CLIC" ET que ce clic est un "CLIC GAUCHE"
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

################################################################################
#                     Bouton de la page "Ecran Titre"
################################################################################
#BOUCLE DU BOUTON "PICROSS A RESOUDRE" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
# Si l'utilisateur clique sur la zone correspondant au bouton "picross à résoudre"
                if event.pos[0] >= 54 and event.pos[0] <= 54 + LONGUEUR_BOUTONS_PARTIES and event.pos[1] >= 319 and event.pos[1] <= 319 + HAUTEUR_BOUTONS_PARTIES:
                    # Fermeture du menu principal
                    continuer_menu = 0
                    # Ouverture de la fenêtre "picross à résoudre"
                    continuer_picross_a_resoudre = 1
                    # On affecte a "page_precedente" la valeur "menu principal"
                    page_precedente = "menu principal"

#BOUCLE DU BOUTON "RESOLUTION DE PICROSS" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "résolution de picross"
                if event.pos[0] >= 285 and event.pos[0] <= 285 + LONGUEUR_BOUTONS_PARTIES and event.pos[1] >= 300 and event.pos[1] <= 300 + HAUTEUR_BOUTONS_PARTIES:
                    # Fermeture du menu principal
                    continuer_menu = 0
                    # Ouverture de la fenêtre "résolution de picross"
                    """continuer_resolution_de_picross = 1"""
                    # On affecte a "page_precedente" la valeur "menu principal"
                    page_precedente = "menu principal"

#BOUCLE DU BOUTON "CREATION DE PICROSS" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "création de picross"
                if event.pos[0] >= 535 and event.pos[0] <= 535 + LONGUEUR_BOUTONS_PARTIES and event.pos[1] >= 300 and event.pos[1] <= 300 + HAUTEUR_BOUTONS_PARTIES:
                    # Fermeture du menu principal
                    continuer_menu = 0
                    # Ouverture de la fenêtre "création de picross"
                    """continuer_creation_de_picross = 1"""
                    # On affecte a "page_precedente" la valeur "menu principal"
                    page_precedente = "menu principal"

#BOUCLE DU BOUTON "TUTORIEL" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "tutoriel"
                if event.pos[0] >= 30 and event.pos[0] <= 30+LONGUEUR_BOUTON_TUTORIEL and event.pos[1] >= 585 and event.pos[1] <= 585+HAUTEUR_BOUTON_TUTORIEL:
                    # Fermeture du menu principal
                    continuer_menu = 0
                    # Ouverture du tutoriel
                    continuer_tutoriel = 1
                    # On affecte a "page_precedente" la valeur "menu principal"
                    page_precedente = "menu principal"

                if event.pos[0] >= 725 and event.pos[0] <= 725 + 50 and event.pos[1] >= 25 and event.pos[1] <= 25 + 50:
                    if son_on == True:
                        son_on = False
                        FENETRE.blit(BOUTON_SON_OFF, (725,25))
                    if son_on == False:
                        son_on = True
                        FENETRE.blit(BOUTON_SON_ON, (725,25))
                    pygame.display.flip()

################################################################################
#                           Picross à Résoudre
################################################################################

#BOUCLE D'AFFICHAGE DE LA PAGE "Picross à Résoudre" - Qui s'exécute tant que la variable "continuer_picross_a_resoudre" vaut 1
    while continuer_picross_a_resoudre == 1:

# Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

# Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30, 40))
            #- titre "picross à résoudre"
        FENETRE.blit(TITRE_PICROSS_A_RESOUDRE, (240, 30))
            #- bouton "niveau 1" du "picross à résoudre"
        FENETRE.blit(BOUTON_NIVEAU1, (262, 112))
            #- bouton "niveau 2" du "picross à résoudre"
        FENETRE.blit(BOUTON_NIVEAU2, (542, 112))
            #- bouton "niveau 3" du "picross à résoudre"
        FENETRE.blit(BOUTON_NIVEAU3, (262, 422))
            #- bouton "niveau 4" du "picross à résoudre"
        FENETRE.blit(BOUTON_NIVEAU4, (542, 422))
            #- bouton "mon niveau" du "picross à résoudre"
        FENETRE.blit(BOUTON_MON_NIVEAU, (402, 267))
            #- le bouton "tutoriel"
        FENETRE.blit(BOUTON_TUTORIEL, (30, 585))
            #- image son-on
        FENETRE.blit(BOUTON_SON_ON, (725, 25))

        #Si la souris est positionnée sur l'interface :
        #condition nécessaire pour que le jeu continue de tourner même si la souris quitte l'interface
        #en effet la position de la souris n'est pas définie lorque la souris n'est pas sur l'interface du jeu
        if pygame.mouse.get_focused():
            if Rect_bouton_Niveau1.collidepoint(event.pos):
                FENETRE.blit(BOUTON_NIVEAU1_INTER, (250, 100))
            if Rect_bouton_Niveau2.collidepoint(event.pos):
                FENETRE.blit(BOUTON_NIVEAU2_INTER, (530,100))
            if Rect_bouton_Niveau3.collidepoint(event.pos):
                FENETRE.blit(BOUTON_NIVEAU3_INTER, (250, 410))
            if Rect_bouton_Niveau4.collidepoint(event.pos):
                FENETRE.blit(BOUTON_NIVEAU4_INTER, (530, 410))
            if Rect_bouton_MonNiveau.collidepoint(event.pos):
                FENETRE.blit(MON_NIVEAU_INTER, (390, 255))

# Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

#BOUCLE PRINCIPALE.1 - Qui s'exécute dans la BOUCLE D'AFFICHAGE DE LA PAGE "Picross à Résoudre" soit tant que la variable "continuer_picross_a_resoudre" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

#BOUCLE DE FERMETURE.1 - Qui s'exécute dans la BOUCLE PRINCIPALE.1
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" ainsi qu'à "continuer_picross_a_resoudre" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
            if event.type == QUIT:
                #On arrête la boucle ce qui ferme la fenetre
                continuer_picross_a_resoudre = 0
                continuer = 0

#BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE" - Qui s'exécute dans la BOUCLE PRINCIPALE.1
# Si un de ces événements est de type "CLIC" ET que ce clic est un "CLIC GAUCHE"
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

################################################################################
#                  Bouton de la page "Picross à Résoudre"
################################################################################

#BOUCLE DU BOUTON "RETOUR" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "Retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30 + LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40 + HAUTEUR_BOUTON_RETOUR:
                    # Fermeture de la fenêtre "picross à résoudre"
                    continuer_picross_a_resoudre = 0
                    # Ouverture du menu principal
                    continuer_menu = 1
                    # On affecte a "page_precedente" la valeur "picross à résoudre"
                    page_precedente = "picross à résoudre"

#BOUCLE DU BOUTON "TUTORIEL" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "tutoriel"
                if event.pos[0] >= 30 and event.pos[0] <= 30 + LONGUEUR_BOUTON_TUTORIEL and event.pos[1] >= 585 and event.pos[1] <= 585 + HAUTEUR_BOUTON_TUTORIEL:
                    # Fermeture du menu principal
                    continuer_picross_a_resoudre = 0
                    # Ouverture du tutoriel
                    continuer_tutoriel = 1
                    # On affecte a "page_precedente" la valeur "picross à résoudre"
                    page_precedente = "picross à résoudre"

#BOUCLE DU BOUTON "NIVEAU 1" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "NIVEAU 1"
                if event.pos[0] >= 250 and event.pos[0] <= 250 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 100 and event.pos[1] <= 100 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    # Fermeture de la fenêtre "picross à résoudre"
                    continuer_picross_a_resoudre = 0
                    # Ouverture de la fenêtre "Niveau 1"
                    continuer_niveau1 = 1
                    # On affecte a "page_precedente" la valeur "picross à résoudre"
                    page_precedente = "picross à résoudre"

#BOUCLE DU BOUTON "NIVEAU 2" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "NIVEAU 2"
                if event.pos[0] >= 530 and event.pos[0] <= 530 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 100 and event.pos[1] <= 100 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    # Fermeture de la fenêtre "picross à résoudre"
                    continuer_picross_a_resoudre = 0
                    # Ouverture de la fenêtre "Niveau 2"
                    continuer_niveau2 = 1
                    # On affecte a "page_precedente" la valeur "picross à résoudre"
                    page_precedente = "picross à résoudre"

#BOUCLE DU BOUTON "NIVEAU 3" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "NIVEAU 3"
                if event.pos[0] >= 250 and event.pos[0] <= 250 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 410 and event.pos[1] <= 410 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    # Fermeture de la fenêtre "picross à résoudre"
                    continuer_picross_a_resoudre = 0
                    # Ouverture de la fenêtre "Niveau 3"
                    continuer_niveau3 = 1
                    # On affecte a "page_precedente" la valeur "picross à résoudre"
                    page_precedente = "picross à résoudre"

#BOUCLE DU BOUTON "NIVEAU 4" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "NIVEAU 4"
                if event.pos[0] >= 530 and event.pos[0] <= 530 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 410 and event.pos[1] <= 410 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    # Fermeture de la fenêtre "picross à résoudre"
                    continuer_picross_a_resoudre = 0
                    # Ouverture de la fenêtre "Niveau 4"
                    continuer_niveau4 = 1
                    # On affecte a "page_precedente" la valeur "picross à résoudre"
                    page_precedente = "picross à résoudre"

#BOUCLE DU BOUTON "MON NIVEAU" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "MON NIVEAU"
                if event.pos[0] >= 390 and event.pos[0] <= 390 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 255 and event.pos[1] <= 255 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    # Fermeture de la fenêtre "picross à résoudre"
                    continuer_picross_a_resoudre = 0
                    # Ouverture de la fenêtre "Niveau 4"
                    continuer_mon_niveau = 1
                    # On affecte a "page_precedente" la valeur "picross à résoudre"
                    page_precedente = "picross à résoudre"

                if event.pos[0] >= 725 and event.pos[0] <= 725 + 50 and event.pos[1] >= 25 and event.pos[1] <= 25 + 50:
                    son_on = False

################################################################################
#          Page d'affichage du Niveau 1 (Appartenant à Picross à Résoudre)
################################################################################

#BOUCLE D'AFFICHAGE DE LA PAGE "Niveau 1" - Qui s'exécute tant que la variable "continuer_niveau1" vaut 1
    while continuer_niveau1 == 1:

# Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

# Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30,40))
            #- le bouton "tutoriel"
        FENETRE.blit(BOUTON_TUTORIEL, (30,585))
            #- l'icone "Niveau 1"
        FENETRE.blit(ICONE_NIVEAU1, (200, 15))
            #- les icones des numéros des différentes grilles
        FENETRE.blit(BOUTON_GRILLE1, (200,130))
        FENETRE.blit(BOUTON_GRILLE2, (405,130))
        FENETRE.blit(BOUTON_GRILLE3, (610,130))
        FENETRE.blit(BOUTON_GRILLE4, (200,305))
        FENETRE.blit(BOUTON_GRILLE5, (405,305))
        FENETRE.blit(BOUTON_GRILLE6, (610,305))
        FENETRE.blit(BOUTON_GRILLE7, (200,480))
        FENETRE.blit(BOUTON_GRILLE8, (405,480))
        FENETRE.blit(BOUTON_GRILLE9, (610,480))

        #Si la souris est positionnée sur l'interface :
        #condition nécessaire pour que le jeu continue de tourner même si la souris quitte l'interface
        #en effet la position de la souris n'est pas définie lorque la souris n'est pas sur l'interface du jeu
        if pygame.mouse.get_focused():
            #Affichage de l'image représentant une grille vide
            if Rectgrille1.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV1[0] == 0 :
                    FENETRE.blit(BOUTON_GRILLE1_NIVEAU1, (200, 130))
                elif PICROSS_COMPLETS_NIV1[0] == 1:
                    FENETRE.blit(BOUTON_GRILLE1_NIVEAU1_RESOLUE, (200,130))
            #Affichage de l'image représentant un 2
            elif Rectgrille2.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV1[1] == 0 :
                    FENETRE.blit(BOUTON_GRILLE2_NIVEAU1, (405, 130))
                elif PICROSS_COMPLETS_NIV1[1] == 1:
                    FENETRE.blit(BOUTON_GRILLE2_NIVEAU1_RESOLUE, (405,130))
            #Affichage de l'image représentant un 3
            elif Rectgrille3.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV1[2] == 0 :
                    FENETRE.blit(BOUTON_GRILLE3_NIVEAU1, (610, 130))
                elif PICROSS_COMPLETS_NIV1[2] == 1:
                    FENETRE.blit(BOUTON_GRILLE3_NIVEAU1_RESOLUE, (610,130))
            #Affichage de l'image représentant un 4
            elif Rectgrille4.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV1[3] == 0 :
                    FENETRE.blit(BOUTON_GRILLE4_NIVEAU1, (200, 305))
                elif PICROSS_COMPLETS_NIV1[3] == 1:
                    FENETRE.blit(BOUTON_GRILLE4_NIVEAU1_RESOLUE, (200,305))
            #Affichage de l'image représentant un 5
            elif Rectgrille5.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV1[4] == 0 :
                    FENETRE.blit(BOUTON_GRILLE5_NIVEAU1, (405, 305))
                elif PICROSS_COMPLETS_NIV1[4] == 1:
                    FENETRE.blit(BOUTON_GRILLE5_NIVEAU1_RESOLUE, (405,305))
            #Affichage de l'image représentant un 6
            elif Rectgrille6.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV1[5] == 0 :
                    FENETRE.blit(BOUTON_GRILLE6_NIVEAU1, (610, 305))
                elif PICROSS_COMPLETS_NIV1[5] == 1:
                    FENETRE.blit(BOUTON_GRILLE6_NIVEAU1_RESOLUE, (610,305))
            #Affichage de l'image représentant un 7
            elif Rectgrille7.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV1[6] == 0 :
                    FENETRE.blit(BOUTON_GRILLE7_NIVEAU1, (200, 480))
                elif PICROSS_COMPLETS_NIV1[6] == 1:
                    FENETRE.blit(BOUTON_GRILLE7_NIVEAU1_RESOLUE, (200,480))
            #Affichage de l'image représentant un 8
            elif Rectgrille8.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV1[7] == 0 :
                    FENETRE.blit(BOUTON_GRILLE8_NIVEAU1, (405, 480))
                elif PICROSS_COMPLETS_NIV1[7] == 1:
                    FENETRE.blit(BOUTON_GRILLE8_NIVEAU1_RESOLUE, (405,480))
            #Affichage de l'image représentant un 9
            elif Rectgrille9.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV1[8] == 0 :
                    FENETRE.blit(BOUTON_GRILLE9_NIVEAU1, (610, 480))
                elif PICROSS_COMPLETS_NIV1[8] == 1:
                    FENETRE.blit(BOUTON_GRILLE9_NIVEAU1_RESOLUE, (610,480))

        # Affichage du texte
        Texte(FENETRE, TITRE_NIVEAU1, 310, 50, NOIR, None, 30)

# On dessine une ligne verte qui sépare l'entête et la partie basse de l'interface
        pygame.draw.line(FENETRE, VERT_NIVEAU1, (310,110), (760,110), 5)
# Affichage de la barre de progression
        if SOMME_PICROSS_COMPLETS_NIV1 == 0 :
            FENETRE.blit(pygame.image.load("barre_progression_0sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV1 == 1 :
            FENETRE.blit(pygame.image.load("barre_progression_1sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV1 == 2 :
            FENETRE.blit(pygame.image.load("barre_progression_2sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV1 == 3 :
            FENETRE.blit(pygame.image.load("barre_progression_3sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV1 == 4 :
            FENETRE.blit(pygame.image.load("barre_progression_4sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV1 == 5 :
            FENETRE.blit(pygame.image.load("barre_progression_5sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV1 == 6 :
            FENETRE.blit(pygame.image.load("barre_progression_6sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV1 == 7 :
            FENETRE.blit(pygame.image.load("barre_progression_7sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV1 == 8 :
            FENETRE.blit(pygame.image.load("barre_progression_8sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV1 == 9 :
            FENETRE.blit(pygame.image.load("barre_progression_9sur9.PNG"), (310, 80))

# Rafraichissement de la fenêtre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()


#BOUCLE PRINCIPALE.2 - Qui s'exécute dans la BOUCLE D'AFFICHAGE DE LA PAGE "Niveau 1" soit tant que la variable "continuer__niveau1" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

#BOUCLE DE FERMETURE.2 - Qui s'exécute dans la BOUCLE PRINCIPALE.2
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" ainsi qu'à "continuer_niveau1" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
            if event.type == QUIT:
                # On arrête la boucle ce qui ferme la fenêtre
                continuer_niveau1 = 0
                continuer = 0

#BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE" - Qui s'exécute dans la BOUCLE PRINCIPALE.2
# Si un de ces événements est de type "CLIC" ET que ce clic est un "CLIC GAUCHE"
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

################################################################################
#                       Bouton de la page "Niveau_1"
################################################################################

#BOUCLE DU BOUTON "RETOUR" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "Retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30+LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40+HAUTEUR_BOUTON_RETOUR:
                    # Fermeture de la fenêtre "Niveau 1"
                    continuer_niveau1 = 0
                    # Ouverture de "picross à résoudre"
                    continuer_picross_a_resoudre = 1
                    # On affecte a "page_precedente" la valeur "niveau 1"
                    page_precedente = "niveau 1"

#BOUCLE DU BOUTON "TUTORIEL" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "tutoriel"
                if event.pos[0] >= 30 and event.pos[0] <= 30+LONGUEUR_BOUTON_TUTORIEL and event.pos[1] >= 585 and event.pos[1] <= 585+HAUTEUR_BOUTON_TUTORIEL:
                    # Fermeture du menu principal
                    continuer_niveau1 = 0
                    # Ouverture du tutoriel
                    continuer_tutoriel = 1
                    # On affecte a "page_precedente" la valeur "niveau 1"
                    page_precedente = "niveau 1"

                if event.pos[0] >= 200 and event.pos[0] <= 200 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 130 and event.pos[1] <= 130 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau1 = 0
                    continuer_grille5x5 = 1
                    MAT_CENT = MAT_CENT_NIV1_PIC1
                    MAT_GAUC = MAT_GAUC_NIV1_PIC1
                    MAT_HAUT = MAT_HAUT_NIV1_PIC1
                    PICROSS_EN_COURS_NIV1[0] = True
                    print(PICROSS_EN_COURS_NIV1)

                if event.pos[0] >= 405 and event.pos[0] <= 405 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 130 and event.pos[1] <= 130 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau1 = 0
                    continuer_grille5x5 = 1
                    MAT_CENT = MAT_CENT_NIV1_PIC2
                    MAT_GAUC = MAT_GAUC_NIV1_PIC2
                    MAT_HAUT = MAT_HAUT_NIV1_PIC2
                    PICROSS_EN_COURS_NIV1[1] = True
                    print(PICROSS_EN_COURS_NIV1)

                if event.pos[0] >= 610 and event.pos[0] <= 610 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 130 and event.pos[1] <= 130 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau1 = 0
                    continuer_grille5x5 = 1
                    MAT_CENT = MAT_CENT_NIV1_PIC3
                    MAT_GAUC = MAT_GAUC_NIV1_PIC3
                    MAT_HAUT = MAT_HAUT_NIV1_PIC3
                    PICROSS_EN_COURS_NIV1[2] = True
                    print(PICROSS_EN_COURS_NIV1)

                if event.pos[0] >= 200 and event.pos[0] <= 200 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 305 and event.pos[1] <= 305 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau1 = 0
                    continuer_grille5x5 = 1
                    MAT_CENT = MAT_CENT_NIV1_PIC4
                    MAT_GAUC = MAT_GAUC_NIV1_PIC4
                    MAT_HAUT = MAT_HAUT_NIV1_PIC4
                    PICROSS_EN_COURS_NIV1[3] = True
                    print(PICROSS_EN_COURS_NIV1)

                if event.pos[0] >= 405 and event.pos[0] <= 405 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 305 and event.pos[1] <= 305 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau1 = 0
                    continuer_grille5x5 = 1
                    MAT_CENT = MAT_CENT_NIV1_PIC5
                    MAT_GAUC = MAT_GAUC_NIV1_PIC5
                    MAT_HAUT = MAT_HAUT_NIV1_PIC5
                    PICROSS_EN_COURS_NIV1[4] = True
                    print(PICROSS_EN_COURS_NIV1)

                if event.pos[0] >= 610 and event.pos[0] <= 610 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 305 and event.pos[1] <= 305 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau1 = 0
                    continuer_grille5x5 = 1
                    MAT_CENT = MAT_CENT_NIV1_PIC6
                    MAT_GAUC = MAT_GAUC_NIV1_PIC6
                    MAT_HAUT = MAT_HAUT_NIV1_PIC6
                    PICROSS_EN_COURS_NIV1[5] = True
                    print(PICROSS_EN_COURS_NIV1)

                if event.pos[0] >= 200 and event.pos[0] <= 200 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 480 and event.pos[1] <= 480 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau1 = 0
                    continuer_grille5x5 = 1
                    MAT_CENT = MAT_CENT_NIV1_PIC7
                    MAT_GAUC = MAT_GAUC_NIV1_PIC7
                    MAT_HAUT = MAT_HAUT_NIV1_PIC7
                    PICROSS_EN_COURS_NIV1[6] = True
                    print(PICROSS_EN_COURS_NIV1)

                if event.pos[0] >= 405 and event.pos[0] <= 405 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 480 and event.pos[1] <= 480 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau1 = 0
                    continuer_grille5x5 = 1
                    MAT_CENT = MAT_CENT_NIV1_PIC8
                    MAT_GAUC = MAT_GAUC_NIV1_PIC8
                    MAT_HAUT = MAT_HAUT_NIV1_PIC8
                    PICROSS_EN_COURS_NIV1[7] = True
                    print(PICROSS_EN_COURS_NIV1)

                if event.pos[0] >= 610 and event.pos[0] <= 610 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 480 and event.pos[1] <= 480 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau1 = 0
                    continuer_grille5x5 = 1
                    MAT_CENT = MAT_CENT_NIV1_PIC9
                    MAT_GAUC = MAT_GAUC_NIV1_PIC9
                    MAT_HAUT = MAT_HAUT_NIV1_PIC9
                    PICROSS_EN_COURS_NIV1[8] = True
                    print(PICROSS_EN_COURS_NIV1)

################################################################################
#                       Page d'affichage du Niveau 2
################################################################################
#BOUCLE D'AFFICHAGE DE LA PAGE "Niveau 2" - Qui s'exécute tant que la variable "continuer_niveau2" vaut 1
    while continuer_niveau2 == 1:

# Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

# Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30,40))
            #- le bouton "tutoriel"
        FENETRE.blit(BOUTON_TUTORIEL, (30,585))
            #- l'icone "Niveau 2"
        FENETRE.blit(ICONE_NIVEAU2, (200, 15))
            #- les icones des différentes grilles
        FENETRE.blit(BOUTON_GRILLE1, (200,130))
        FENETRE.blit(BOUTON_GRILLE2, (405,130))
        FENETRE.blit(BOUTON_GRILLE3, (610,130))
        FENETRE.blit(BOUTON_GRILLE4, (200,305))
        FENETRE.blit(BOUTON_GRILLE5, (405,305))
        FENETRE.blit(BOUTON_GRILLE6, (610,305))
        FENETRE.blit(BOUTON_GRILLE7, (200,480))
        FENETRE.blit(BOUTON_GRILLE8, (405,480))
        FENETRE.blit(BOUTON_GRILLE9, (610,480))

        #Si la souris est positionnée sur l'interface :
        #condition nécessaire pour que le jeu continue de tourner même si la souris quitte l'interface
        #en effet la position de la souris n'est pas définie lorque la souris n'est pas sur l'interface du jeu
        if pygame.mouse.get_focused():
            #Affichage de l'image représentant une grille vide
            if Rectgrille1.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV2[0] == 0 :
                    FENETRE.blit(BOUTON_GRILLE1_NIVEAU2, (200, 130))
                elif PICROSS_COMPLETS_NIV2[0] == 1:
                    FENETRE.blit(BOUTON_GRILLE1_NIVEAU2_RESOLUE, (200,130))
            #Affichage de l'image représentant un 2
            elif Rectgrille2.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV2[1] == 0 :
                    FENETRE.blit(BOUTON_GRILLE2_NIVEAU2, (405, 130))
                elif PICROSS_COMPLETS_NIV2[1] == 1:
                    FENETRE.blit(BOUTON_GRILLE2_NIVEAU2_RESOLUE, (405,130))
            #Affichage de l'image représentant un 3
            elif Rectgrille3.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV2[2] == 0 :
                    FENETRE.blit(BOUTON_GRILLE3_NIVEAU2, (610, 130))
                elif PICROSS_COMPLETS_NIV2[2] == 1:
                    FENETRE.blit(BOUTON_GRILLE3_NIVEAU2_RESOLUE, (610,130))
            #Affichage de l'image représentant un 4
            elif Rectgrille4.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV2[3] == 0 :
                    FENETRE.blit(BOUTON_GRILLE4_NIVEAU2, (200, 305))
                elif PICROSS_COMPLETS_NIV2[3] == 1:
                    FENETRE.blit(BOUTON_GRILLE4_NIVEAU2_RESOLUE, (200,305))
            #Affichage de l'image représentant un 5
            elif Rectgrille5.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV2[4] == 0 :
                    FENETRE.blit(BOUTON_GRILLE5_NIVEAU2, (405, 305))
                elif PICROSS_COMPLETS_NIV2[4] == 1:
                    FENETRE.blit(BOUTON_GRILLE5_NIVEAU2_RESOLUE, (405,305))
            #Affichage de l'image représentant un 6
            elif Rectgrille6.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV2[5] == 0 :
                    FENETRE.blit(BOUTON_GRILLE6_NIVEAU2, (610, 305))
                elif PICROSS_COMPLETS_NIV2[5] == 1:
                    FENETRE.blit(BOUTON_GRILLE6_NIVEAU2_RESOLUE, (610,305))
            #Affichage de l'image représentant un 7
            elif Rectgrille7.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV2[6] == 0 :
                    FENETRE.blit(BOUTON_GRILLE7_NIVEAU2, (200, 480))
                elif PICROSS_COMPLETS_NIV2[6] == 1:
                    FENETRE.blit(BOUTON_GRILLE7_NIVEAU2_RESOLUE, (200,480))
            #Affichage de l'image représentant un 8
            elif Rectgrille8.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV2[7] == 0 :
                    FENETRE.blit(BOUTON_GRILLE8_NIVEAU2, (405, 480))
                elif PICROSS_COMPLETS_NIV2[7] == 1:
                    FENETRE.blit(BOUTON_GRILLE8_NIVEAU2_RESOLUE, (405,480))
            #Affichage de l'image représentant un 9
            elif Rectgrille9.collidepoint(event.pos):
                if PICROSS_COMPLETS_NIV2[8] == 0 :
                    FENETRE.blit(BOUTON_GRILLE9_NIVEAU2, (610, 480))
                elif PICROSS_COMPLETS_NIV2[8] == 1:
                    FENETRE.blit(BOUTON_GRILLE9_NIVEAU2_RESOLUE, (610,480))

# Affichage du texte
        Texte(FENETRE, TITRE_NIVEAU2, 310, 50, NOIR, None, 30)

# On dessine une ligne jaune qui sépare l'entête et la partie basse de l'interface
        pygame.draw.line(FENETRE, JAUNE_NIVEAU2, (310,110), (760,110), 5)

# Affichage de la barre de progression
        if SOMME_PICROSS_COMPLETS_NIV2 == 0 :
            FENETRE.blit(pygame.image.load("barre_progression_0sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV2 == 1 :
            FENETRE.blit(pygame.image.load("barre_progression_1sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV2 == 2 :
            FENETRE.blit(pygame.image.load("barre_progression_2sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV2 == 3 :
            FENETRE.blit(pygame.image.load("barre_progression_3sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV2 == 4 :
            FENETRE.blit(pygame.image.load("barre_progression_4sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV2 == 5 :
            FENETRE.blit(pygame.image.load("barre_progression_5sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV2 == 6 :
            FENETRE.blit(pygame.image.load("barre_progression_6sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV2 == 7 :
            FENETRE.blit(pygame.image.load("barre_progression_7sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV2 == 8 :
            FENETRE.blit(pygame.image.load("barre_progression_8sur9.PNG"), (310, 80))
        elif SOMME_PICROSS_COMPLETS_NIV2 == 9 :
            FENETRE.blit(pygame.image.load("barre_progression_9sur9.PNG"), (310, 80))

# Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()


#BOUCLE PRINCIPALE.3 - Qui s'exécute dans la BOUCLE D'AFFICHAGE DE LA PAGE "Niveau 2" soit tant que la variable "continuer__niveau2" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

#BOUCLE DE FERMETURE.3 - Qui s'exécute dans la BOUCLE PRINCIPALE.3
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" ainsi qu'à "continuer_niveau2" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
            if event.type == QUIT:
                # On arrête la boucle ce qui ferme la fenetre
                continuer_niveau2 = 0
                continuer = 0

#BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE" - Qui s'éxécute dans la BOUCLE PRINCIPALE.2
# Si un de ces événements est de type "CLIC" ET que ce clic est un "CLIC GAUCHE"
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

################################################################################
#                       Bouton de la page "Niveau_2"
################################################################################

#BOUCLE DU BOUTON "RETOUR" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "Retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30+LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40+HAUTEUR_BOUTON_RETOUR:
                    # Fermeture de la fenêtre "Niveau 2"
                    continuer_niveau2 = 0
                    # Ouverture de "picross à résoudre"
                    continuer_picross_a_resoudre = 1
                    # On affecte a "page_precedente" la valeur "picross à résoudre"
                    page_precedente = "niveau 2"

#BOUCLE DU BOUTON "TUTORIEL" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "tutoriel"
                if event.pos[0] >= 30 and event.pos[0] <= 30+LONGUEUR_BOUTON_TUTORIEL and event.pos[1] >= 585 and event.pos[1] <= 585+HAUTEUR_BOUTON_TUTORIEL:
                    # Fermeture du menu principal
                    continuer_niveau2 = 0
                    # Ouverture du tutoriel
                    continuer_tutoriel = 1

                if event.pos[0] >= 200 and event.pos[0] <= 200 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 130 and event.pos[1] <= 130 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau2 = 0
                    continuer_grille10x10 = 1
                    MAT_CENT = MAT_CENT_NIV2_PIC1
                    MAT_GAUC = MAT_GAUC_NIV2_PIC1
                    MAT_HAUT = MAT_HAUT_NIV2_PIC1
                    PICROSS_EN_COURS_NIV2[0] = True
                    print(PICROSS_EN_COURS_NIV2)

                if event.pos[0] >= 405 and event.pos[0] <= 405 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 130 and event.pos[1] <= 130 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau2 = 0
                    continuer_grille10x10 = 1
                    MAT_CENT = MAT_CENT_NIV2_PIC2
                    MAT_GAUC = MAT_GAUC_NIV2_PIC2
                    MAT_HAUT = MAT_HAUT_NIV2_PIC2
                    PICROSS_EN_COURS_NIV2[1] = True
                    print(PICROSS_EN_COURS_NIV2)

                if event.pos[0] >= 610 and event.pos[0] <= 610 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 130 and event.pos[1] <= 130 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau2 = 0
                    continuer_grille10x10 = 1
                    MAT_CENT = MAT_CENT_NIV2_PIC3
                    MAT_GAUC = MAT_GAUC_NIV2_PIC3
                    MAT_HAUT = MAT_HAUT_NIV2_PIC3
                    PICROSS_EN_COURS_NIV2[2] = True
                    print(PICROSS_EN_COURS_NIV2)

                if event.pos[0] >= 200 and event.pos[0] <= 200 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 305 and event.pos[1] <= 305 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau2 = 0
                    continuer_grille10x10 = 1
                    MAT_CENT = MAT_CENT_NIV2_PIC4
                    MAT_GAUC = MAT_GAUC_NIV2_PIC4
                    MAT_HAUT = MAT_HAUT_NIV2_PIC4
                    PICROSS_EN_COURS_NIV2[3] = True
                    print(PICROSS_EN_COURS_NIV2)

                if event.pos[0] >= 405 and event.pos[0] <= 405 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 305 and event.pos[1] <= 305 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau2 = 0
                    continuer_grille10x10 = 1
                    MAT_CENT = MAT_CENT_NIV2_PIC5
                    MAT_GAUC = MAT_GAUC_NIV2_PIC5
                    MAT_HAUT = MAT_HAUT_NIV2_PIC5
                    PICROSS_EN_COURS_NIV2[4] = True
                    print(PICROSS_EN_COURS_NIV2)

                if event.pos[0] >= 610 and event.pos[0] <= 610 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 305 and event.pos[1] <= 305 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau2 = 0
                    continuer_grille10x10 = 1
                    MAT_CENT = MAT_CENT_NIV2_PIC6
                    MAT_GAUC = MAT_GAUC_NIV2_PIC6
                    MAT_HAUT = MAT_HAUT_NIV2_PIC6
                    PICROSS_EN_COURS_NIV2[5] = True
                    print(PICROSS_EN_COURS_NIV2)

                if event.pos[0] >= 200 and event.pos[0] <= 200 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 480 and event.pos[1] <= 480 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau2 = 0
                    continuer_grille10x10 = 1
                    MAT_CENT = MAT_CENT_NIV2_PIC7
                    MAT_GAUC = MAT_GAUC_NIV2_PIC7
                    MAT_HAUT = MAT_HAUT_NIV2_PIC7
                    PICROSS_EN_COURS_NIV2[6] = True
                    print(PICROSS_EN_COURS_NIV2)

                if event.pos[0] >= 405 and event.pos[0] <= 405 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 480 and event.pos[1] <= 480 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau2 = 0
                    continuer_grille10x10 = 1
                    MAT_CENT = MAT_CENT_NIV2_PIC8
                    MAT_GAUC = MAT_GAUC_NIV2_PIC8
                    MAT_HAUT = MAT_HAUT_NIV2_PIC8
                    PICROSS_EN_COURS_NIV2[7] = True
                    print(PICROSS_EN_COURS_NIV2)

                if event.pos[0] >= 610 and event.pos[0] <= 610 + DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 480 and event.pos[1] <= 480 + DIMENSION_COTE_BOUTONS_NIVEAUX:
                    continuer_niveau2 = 0
                    continuer_grille10x10 = 1
                    MAT_CENT = MAT_CENT_NIV2_PIC9
                    MAT_GAUC = MAT_GAUC_NIV2_PIC9
                    MAT_HAUT = MAT_HAUT_NIV2_PIC9
                    PICROSS_EN_COURS_NIV2[8] = True
                    print(PICROSS_EN_COURS_NIV2)

################################################################################
#                       Page d'affichage du Niveau 3
################################################################################
#BOUCLE D'AFFICHAGE DE LA PAGE "Niveau 3" - Qui s'exécute tant que la variable "continuer_niveau3" vaut 1
    while continuer_niveau3 == 1:

# Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

# Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30,40))
            #- le bouton "tutoriel"
        FENETRE.blit(BOUTON_TUTORIEL, (30,585))
            #- l'icone "Niveau 3"
        FENETRE.blit(ICONE_NIVEAU3, (200, 15))
            #- les icones des différentes grilles
        FENETRE.blit(BOUTON_GRILLE1, (200,130))
        FENETRE.blit(BOUTON_GRILLE2, (405,130))
        FENETRE.blit(BOUTON_GRILLE3, (610,130))
        FENETRE.blit(BOUTON_GRILLE4, (200,305))
        FENETRE.blit(BOUTON_GRILLE5, (405,305))
        FENETRE.blit(BOUTON_GRILLE6, (610,305))
        FENETRE.blit(BOUTON_GRILLE7, (200,480))
        FENETRE.blit(BOUTON_GRILLE8, (405,480))
        FENETRE.blit(BOUTON_GRILLE9, (610,480))

        #Si la souris est positionnée sur l'interface :
        #condition nécessaire pour que le jeu continue de tourner même si la souris quitte l'interface
        #en effet la position de la souris n'est pas définie lorque la souris n'est pas sur l'interface du jeu
        if pygame.mouse.get_focused():
            #Affichage de l'image représentant un 1
            if Rectgrille1.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (200, 130))
            #Affichage de l'image représentant un 2
            if Rectgrille2.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (405, 130))
            #Affichage de l'image représentant un 3
            if Rectgrille3.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (610, 130))
            #Affichage de l'image représentant un 4
            if Rectgrille4.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (200, 305))
            #Affichage de l'image représentant un 5
            if Rectgrille5.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (405, 305))
            #Affichage de l'image représentant un 6
            if Rectgrille6.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (610, 305))
            #Affichage de l'image représentant un 7
            if Rectgrille7.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (200, 480))
            #Affichage de l'image représentant un 8
            if Rectgrille8.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (405, 480))
            #Affichage de l'image représentant un 9
            if Rectgrille9.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (610, 480))

# On dessine une ligne jaune qui sépare l'entête et la partie basse de l'interface
        pygame.draw.line(FENETRE, ORANGE_NIVEAU3, (310,110), (760,110), 5)

# Affichage du texte
        Texte(FENETRE, TITRE_NIVEAU3, 325, 50, NOIR, None, 30)

# Rafraichissement de la fenêtre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

#BOUCLE PRINCIPALE.4 - Qui s'exécute dans la BOUCLE D'AFFICHAGE DE LA PAGE "Niveau 3" soit tant que la variable "continuer__niveau3" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

#BOUCLE DE FERMETURE.4 - Qui s'exécute dans la BOUCLE PRINCIPALE.4
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" ainsi qu'à "continuer_niveau3" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
            if event.type == QUIT:
                # On arrête la boucle ce qui ferme la fenetre
                continuer_niveau3 = 0
                continuer = 0

#BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE" - Qui s'exécute dans la BOUCLE PRINCIPALE.4
# Si un de ces événements est de type "CLIC" ET que ce clic est un "CLIC GAUCHE"
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

################################################################################
#                       Bouton de la page "Niveau_3"
################################################################################

#BOUCLE DU BOUTON "RETOUR" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "Retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30+LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40+HAUTEUR_BOUTON_RETOUR:
                    # Fermeture de la fenêtre "Niveau 3"
                    continuer_niveau3 = 0
                    # Ouverture de "picross à résoudre"
                    continuer_picross_a_resoudre = 1

#BOUCLE DU BOUTON "TUTORIEL" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "tutoriel"
                if event.pos[0] >= 30 and event.pos[0] <= 30+LONGUEUR_BOUTON_TUTORIEL and event.pos[1] >= 585 and event.pos[1] <= 585+HAUTEUR_BOUTON_TUTORIEL:
                    # Fermeture du "Niveau 3"
                    continuer_niveau3 = 0
                    # Ouverture du tutoriel
                    continuer_tutoriel = 1

################################################################################
#                       Page d'affichage du Niveau 4
################################################################################
#BOUCLE D'AFFICHAGE DE LA PAGE "Niveau 4" - Qui s'exécute tant que la variable "continuer_niveau4" vaut 1
    while continuer_niveau4 == 1:

# Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

# Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30,40))
            #- le bouton "tutoriel"
        FENETRE.blit(BOUTON_TUTORIEL, (30,585))
            #- l'icone "Niveau 4"
        FENETRE.blit(ICONE_NIVEAU4, (200, 15))
            #- les icones des différentes grilles
        FENETRE.blit(BOUTON_GRILLE1, (200,130))
        FENETRE.blit(BOUTON_GRILLE2, (405,130))
        FENETRE.blit(BOUTON_GRILLE3, (610,130))
        FENETRE.blit(BOUTON_GRILLE4, (200,305))
        FENETRE.blit(BOUTON_GRILLE5, (405,305))
        FENETRE.blit(BOUTON_GRILLE6, (610,305))
        FENETRE.blit(BOUTON_GRILLE7, (200,480))
        FENETRE.blit(BOUTON_GRILLE8, (405,480))
        FENETRE.blit(BOUTON_GRILLE9, (610,480))

        #Si la souris est positionnée sur l'interface :
        #condition nécessaire pour que le jeu continue de tourner même si la souris quitte l'interface
        #en effet la position de la souris n'est pas définie lorque la souris n'est pas sur l'interface du jeu
        if pygame.mouse.get_focused():
            #Affichage de l'image représentant un 1
            if Rectgrille1.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (200, 130))
            #Affichage de l'image représentant un 2
            if Rectgrille2.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (405, 130))
            #Affichage de l'image représentant un 3
            if Rectgrille3.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (610, 130))
            #Affichage de l'image représentant un 4
            if Rectgrille4.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (200, 305))
            #Affichage de l'image représentant un 5
            if Rectgrille5.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (405, 305))
            #Affichage de l'image représentant un 6
            if Rectgrille6.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (610, 305))
            #Affichage de l'image représentant un 7
            if Rectgrille7.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (200, 480))
            #Affichage de l'image représentant un 8
            if Rectgrille8.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (405, 480))
            #Affichage de l'image représentant un 9
            if Rectgrille9.collidepoint(event.pos):
                FENETRE.blit(BOUTON_GRILLE_VIDE, (610, 480))

# On dessine une ligne jaune qui sépare l'entête et la partie basse de l'interface
        pygame.draw.line(FENETRE, ROUGE_NIVEAU4, (310,110), (760,110), 5)

# Affichage du texte
        Texte(FENETRE, TITRE_NIVEAU4, 325, 50, NOIR, None, 30)

# Rafraichissement de la fenêtre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

#BOUCLE PRINCIPALE.5 - Qui s'exécute dans la BOUCLE D'AFFICHAGE DE LA PAGE "Niveau 4" soit tant que la variable "continuer__niveau4" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

#BOUCLE DE FERMETURE.5 - Qui s'exécute dans la BOUCLE PRINCIPALE.5
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" ainsi qu'à "continuer_niveau4" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
            if event.type == QUIT:
                # On arrête la boucle ce qui ferme la fenetre
                continuer_niveau4 = 0
                continuer = 0

#BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE" - Qui s'exécute dans la BOUCLE PRINCIPALE.5
# Si un de ces événements est de type "CLIC" ET que ce clic est un "CLIC GAUCHE"
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

################################################################################
#                       Bouton de la page "Niveau_4"
################################################################################

#BOUCLE DU BOUTON "RETOUR" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "Retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30+LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40+HAUTEUR_BOUTON_RETOUR:
                    # Fermeture de la fenêtre "Niveau 4"
                    continuer_niveau4 = 0
                    # Ouverture du menu principal
                    continuer_picross_a_resoudre = 1

#BOUCLE DU BOUTON "TUTORIEL" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "tutoriel"
                if event.pos[0] >= 30 and event.pos[0] <= 30+LONGUEUR_BOUTON_TUTORIEL and event.pos[1] >= 585 and event.pos[1] <= 585+HAUTEUR_BOUTON_TUTORIEL:
                    #Fermeture du "Niveau 4"
                    continuer_niveau4 = 0
                    #Ouverture du tutoriel
                    continuer_tutoriel = 1

################################################################################
#                  Page d'affichage du "Niveau personnalisé"
################################################################################
#BOUCLE D'AFFICHAGE DE LA PAGE "Niveau personnalisé" - Qui s'exécute tant que la variable "continuer_mon_niveau" vaut 1

    while continuer_mon_niveau == 1:

# Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

# Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30,40))
            #- le bouton "tutoriel"
        FENETRE.blit(BOUTON_TUTORIEL, (30,585))
            #- l'icone "Niveau 4"
        FENETRE.blit(ICONE_MON_NIVEAU, (200, 15))

# On dessine une ligne jaune qui sépare l'entête et la partie basse de l'interface
        pygame.draw.line(FENETRE, BLEU_MON_NIVEAU, (310,110), (760,110), 5)

            #- les icones des numéros des différentes grilles
        FENETRE.blit(BOUTON_GRILLE1, (200,130))
        FENETRE.blit(BOUTON_GRILLE2, (405,130))
        FENETRE.blit(BOUTON_GRILLE3, (610,130))
        FENETRE.blit(BOUTON_GRILLE4, (200,305))
        FENETRE.blit(BOUTON_GRILLE5, (405,305))
        FENETRE.blit(BOUTON_GRILLE6, (610,305))
        FENETRE.blit(BOUTON_GRILLE7, (200,480))
        FENETRE.blit(BOUTON_GRILLE8, (405,480))
        FENETRE.blit(BOUTON_GRILLE9, (610,480))

        #Si la souris est positionnée sur l'interface :
        #condition nécessaire pour que le jeu continue de tourner même si la souris quitte l'interface
        #en effet la position de la souris n'est pas définie lorque la souris n'est pas sur l'interface du jeu
        if pygame.mouse.get_focused():
            #Affichage de l'image représentant un 1
            if Rectgrille1.collidepoint(event.pos):
                FENETRE.blit(ICONE_PICROSS_NON_CREE, (200, 130))
            #Affichage de l'image représentant un 2
            if Rectgrille2.collidepoint(event.pos):
                FENETRE.blit(ICONE_PICROSS_NON_CREE, (405, 130))
            #Affichage de l'image représentant un 3
            if Rectgrille3.collidepoint(event.pos):
                FENETRE.blit(ICONE_PICROSS_NON_CREE, (610, 130))
            #Affichage de l'image représentant un 4
            if Rectgrille4.collidepoint(event.pos):
                FENETRE.blit(ICONE_PICROSS_NON_CREE, (200, 305))
            #Affichage de l'image représentant un 5
            if Rectgrille5.collidepoint(event.pos):
                FENETRE.blit(ICONE_PICROSS_NON_CREE, (405, 305))
            #Affichage de l'image représentant un 6
            if Rectgrille6.collidepoint(event.pos):
                FENETRE.blit(ICONE_PICROSS_NON_CREE, (610, 305))
            #Affichage de l'image représentant un 7
            if Rectgrille7.collidepoint(event.pos):
                FENETRE.blit(ICONE_PICROSS_NON_CREE, (200, 480))
            #Affichage de l'image représentant un 8
            if Rectgrille8.collidepoint(event.pos):
                FENETRE.blit(ICONE_PICROSS_NON_CREE, (405, 480))
            #Affichage de l'image représentant un 9
            if Rectgrille9.collidepoint(event.pos):
                FENETRE.blit(ICONE_PICROSS_NON_CREE, (610, 480))

# Affichage du texte
        Texte(FENETRE, TITRE_NIVEAU_PERSONNALISE, 325, 50, NOIR, None, 30)

# Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

#BOUCLE PRINCIPALE.6 - Qui s'exécute dans la BOUCLE D'AFFICHAGE DE LA PAGE "Niveau Personalisé" soit tant que la variable "continuer_mon_niveau" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

#BOUCLE DE FERMETURE.6 - Qui s'exécute dans la BOUCLE PRINCIPALE.6
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" ainsi qu'à "continuer_mon_niveau" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
            if event.type == QUIT:
                # On arrête la boucle ce qui ferme la fenetre
                continuer_mon_niveau = 0
                continuer = 0

#BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE" - Qui s'exécute dans la BOUCLE PRINCIPALE.6
# Si un de ces événements est de type "CLIC" ET que ce clic est un "CLIC GAUCHE"
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

################################################################################
#                       Bouton de la page "Mon Niveau"
################################################################################
#BOUCLE DU BOUTON "RETOUR" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "Retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30+LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40+HAUTEUR_BOUTON_RETOUR:
                    # Fermeture de la fenêtre "Mon Niveau"
                    continuer_mon_niveau = 0
                    # Ouverture du menu principal
                    continuer_picross_a_resoudre = 1

#BOUCLE DU BOUTON "TUTORIEL" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "tutoriel"
                if event.pos[0] >= 30 and event.pos[0] <= 30+LONGUEUR_BOUTON_TUTORIEL and event.pos[1] >= 585 and event.pos[1] <= 585+HAUTEUR_BOUTON_TUTORIEL:
                    # Fermeture de la fenêtre "Mon Niveau"
                    continuer_mon_niveau = 0
                    # Ouverture du tutoriel
                    continuer_tutoriel = 1
################################################################################
#                           PROGRAMME de la Grille 5x5
################################################################################
# Cree par Fabien et Sinan le 21/03/2016 en Python 3.2
#===============================================================================
#                            PRINCIPE DU PROGRAMME
#===============================================================================
# Ce programme est la clef de notre projet,
# il se sert d'autres programmes et bibliothèques sous-jacent(e)s afin d'oeuvrer
# à la création d'une grille de jeu picross de dimension 5x5.
#===============================================================================
#                            CORPS DU PROGRAMME
#===============================================================================
#BOUCLE D'EXECUTION - Qui s'exécute tant que la variable "continuer" vaut 1
    while continuer_grille5x5 == 1:
#-------------------------------------------------------------------------------
#                              AFFICHAGE DU FOND
#-------------------------------------------------------------------------------
# Affichage d'une couleur de fond
        FENETRE.fill(BLANC_CREME)
        #- le logo du jeu "Picross Mania"
        FENETRE.blit(LOGO, (130,75))

# Affichage des différentes grilles
        Affichage_Grille(FENETRE, X_ORIGINE_5x5, Y_ORIGINE_5x5, 5, 5, 3, TAILLE_CARRE_5x5)

        Afficher_Indic_Gauche(FENETRE, BLUE_PEGASUS, X_ORIGINE_5x5, Y_ORIGINE_5x5, 3, 5, 35, TAILLE_CARRE_5x5, MAT_GAUC, DIVISEUR_5x5)

        Afficher_Indic_Haut(FENETRE, BLUE_PEGASUS, X_ORIGINE_5x5,Y_ORIGINE_5x5, 3, 5, 35, TAILLE_CARRE_5x5, MAT_HAUT, DIVISEUR_5x5)

        if allclose(MAT_CENT, MATRICE_GRILLE_5x5):
                continuer_grille5x5 = 0
                animation_son = 1
                animation = 1

# Réactualisation de la liste de picross complétés
# Remise a zéro de la liste des picross en cours
                for i in range (len(PICROSS_EN_COURS_NIV1)):
                    if PICROSS_EN_COURS_NIV1[i] == True :
                        PICROSS_COMPLETS_NIV1[i] = 1
                        PICROSS_EN_COURS_NIV1[i] = False
                        SOMME_PICROSS_COMPLETS_NIV1 = somme_elements_liste(PICROSS_COMPLETS_NIV1)
                        print(PICROSS_EN_COURS_NIV1)
                        print(PICROSS_COMPLETS_NIV1)
                        print(SOMME_PICROSS_COMPLETS_NIV1)
        else :
                continuer_grille5x5 = 1
#-------------------------------------------------------------------------------
#      AFFICHAGE DES FORMES DANS LES CASES DE LA GRILLE : CARRES ET CROIX
#-------------------------------------------------------------------------------

#PARCOURS DES CASES DE LA GRILLE
# Dans ce bloc, on parcourt les cases de la grille en largeur puis en longueur.
#BOUCLE AFFICHAGE_FORMES - Qui s'exécute dans la BOUCLE D'EXECUTION soit tant que la variable "continuer" vaut 1
# Cette boucle parcourt la grille centrale en longueur.
        for x in range(L_5x5):

#BOUCLE AFFICHAGE_FORMES.1 - Qui s'exécute dans la BOUCLE AFFICHAGE_FORMES
# Cette boucle parcourt la grille centrale en hauteur.
            for y in range(H_5x5):

#BOUCLE AFFICHAGE_FORMES.VIDE - Qui s'exécute dans la BOUCLE AFFICHAGE_FORMES.1
# Cette boucle affiche un carré de la couleur de fond lorsque la matrice aux coordonnées [x,y] est égale à 0 càd dans le cas d'une case vide.
                if MATRICE_GRILLE_5x5[x,y]== 0:
                    Afficher_Carre(FENETRE, BLANC_CREME, BLANC_CREME, X_ORIGINE_5x5, Y_ORIGINE_5x5, x, y, TAILLE_CARRE_5x5, 1)

#BOUCLE AFFICHAGE_FORMES.CARRE - Qui s'exécute dans la BOUCLE AFFICHAGE_FORMES.1
# Cette boucle affiche un carré de couleur prédéfinie lorsque la matrice aux coordonnées [x,y] est égale à 1 càd dans le cas d'une case noircie.
                elif MATRICE_GRILLE_5x5[x,y]== 1:
                    Afficher_Carre(FENETRE, VERT_PIN, BLANC_CREME, X_ORIGINE_5x5, Y_ORIGINE_5x5, x, y, TAILLE_CARRE_5x5, 1)

#BOUCLE AFFICHAGE_FORMES.CROIX - Qui s'exécute dans la BOUCLE AFFICHAGE_FORMES.1
# Cette boucle affiche une croix de couleur prédéfinie lorsque la matrice aux coordonnées [x,y] est égale à 2 càd dans le cas d'une case cochée.
                elif MATRICE_GRILLE_5x5[x,y]== 2:
                    Afficher_Croix(FENETRE, VERT_PIN, X_ORIGINE_5x5, Y_ORIGINE_5x5, x, y, TAILLE_CARRE_5x5)

# Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

#BOUCLE PRINCIPALE - Qui s'exécute dans la BOUCLE D'EXECUTION soit tant que la variable "continuer" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

#-------------------------------------------------------------------------------
#                   EVENEMENT DE FERMETURE DE LA FENETRE
#-------------------------------------------------------------------------------

#BOUCLE DE FERMETURE - Qui s'éxécute dans la BOUCLE PRINCIPALE
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
            if event.type == QUIT:
                continuer_grille5x5 = 0
                MATRICE_GRILLE_5x5 = zeros((COLONNES_5x5,LIGNES_5x5))

#-------------------------------------------------------------------------------
#           CALCUL DES COORDONNEES DES CASES DE LA GRILLE CENTRALE
#-------------------------------------------------------------------------------

#BOUCLE D'EVENEMENT DE TYPE "CLIC" - Qui s'éxécute dans la BOUCLE PRINCIPALE
# Si un de ces événements est de type MOUSEBUTTONDOWN, càd un clic quel qu'il soit alors :
            if event.type == MOUSEBUTTONDOWN:

                if event.pos[0] >= X_ORIGINE_5x5 and event.pos[0] <= X_ORIGINE_5x5 + NBR_CARRE_CENTRAL_5x5 * TAILLE_CARRE_5x5 and event.pos[1] >= Y_ORIGINE_5x5 and event.pos[1] <= Y_ORIGINE_5x5 + TAILLE_CARRE_5x5 * NBR_CARRE_CENTRAL_5x5:
                    # Coordonnées des cases de la grille centrale
                    CASE_Y = (event.pos[0] - MARGE_X1_5x5)//TAILLE_CARRE_5x5
                    CASE_X = (event.pos[1] - MARGE_Y1_5x5)//TAILLE_CARRE_5x5
                    print((CASE_X,CASE_Y))

#-------------------------------------------------------------------------------
#                              CLIC GAUCHE
#-------------------------------------------------------------------------------

#BOUCLE EVENT.1 - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC"
# S'exécute que SI le clic est effectué SUR la grille centrale :

#BOUCLE EVENT.CLICGAUCHE - Qui s'exécute dans la BOUCLE EVENT.1
# Cette boucle s'effectue si on est dans le cas d'un clic gauche (1)
                    if event.button == 1: # dans le cas d'un clic gauche

#PARCOURS DES CASES DE LA GRILLE
# Dans ce bloc, on parcourt les cases de la grille en longueur puis en hauteur.
#BOUCLE EVENT.CLICGAUCHE.1 - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE
# Cette boucle parcourt la grille centrale en longueur.
                        for Y in range (L_5x5):   #Pour Y allant de 0 au nombre de ligne de la matrice
#BOUCLE EVENT.CLICGAUCHE.2 - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE et dans la BOUCLE EVENT.CLICGAUCHE.1
# Cette boucle parcourt la grille centrale en hauteur.
                            for X in range (H_5x5):       #Pour X allant de 0 à la longueur d’une ligne de la matrice - 1 (= nombre de colonnes -1) = 4
#BOUCLE EVENT.CLICGAUCHE.3 - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1 et BOUCLE EVENT.CLICGAUCHE.2.
# Cette boucle s'effectue SI ET SEULEMENT SI les compteurs (X,Y) sont équivalents aux coordonnées des cases (CASE_X,CASE_Y)
                                if X == CASE_X and Y == CASE_Y:

#BOUCLE EVENT.CLICGAUCHE.VIDE - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1, BOUCLE EVENT.CLICGAUCHE.2, BOUCLE EVENT.CLICGAUCHE.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee [CASE_X;CASE_Y] est vide (0)
                                    if MATRICE_GRILLE_5x5[CASE_X, CASE_Y] == 0:
                                        # Assignation d'un 1 dans la matrice pour la coordonnee [CASE_X;CASE_Y] pour indiquer que la case contient un CARRE
                                        MATRICE_GRILLE_5x5[CASE_X, CASE_Y] = 1

#BOUCLE EVENT.CLICGAUCHE.CARRE - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1, BOUCLE EVENT.CLICGAUCHE.2, BOUCLE EVENT.CLICGAUCHE.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee [CASE_X;CASE_Y] comporte un CARRE noire (1)
                                    elif MATRICE_GRILLE_5x5[CASE_X, CASE_Y] == 1:
                                        # Assignation de la valeur 0 (Case_Vide) dans la matrice pour la coordonnée [CASE_X;CASE_Y] ayant pour conséquence d'effacer le CARRE
                                        MATRICE_GRILLE_5x5[CASE_X, CASE_Y] = 0

#BOUCLE EVENT.CLICGAUCHE.CROIX - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1, BOUCLE EVENT.CLICGAUCHE.2, BOUCLE EVENT.CLICGAUCHE.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee (CASE_X;CASE_Y) comporte une CROIX noire (2)
                                    elif MATRICE_GRILLE_5x5[CASE_X, CASE_Y] == 2:
                                        # Assignation d'un 1 dans la matrice pour la coordonnee (case_x;case_y) pour indiquer que la case contient un CARRE
                                        MATRICE_GRILLE_5x5[CASE_X, CASE_Y] = 1
                                    print(MATRICE_GRILLE_5x5)

#-------------------------------------------------------------------------------
#                              CLIC DROIT
#-------------------------------------------------------------------------------

#BOUCLE EVENT.2 - Qui s'éxécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC"
# S'exécute que SI le clic est effectué SUR la grille centrale :

#BOUCLE EVENT.CLICDROIT - Qui s'exécute dans la BOUCLE EVENT.2
# Cette boucle s'effectue si on est dans le cas d'un clic droit (3)
                    elif event.button == 3: #Dans le cas d'un clic droit

#PARCOURS DES CASES DE LA GRILLE
# Dans ce bloc, on parcourt les cases de la grille en longueur puis en hauteur.
#BOUCLE EVENT.CLICDROIT.1 - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT
# Cette boucle parcourt la grille centrale en longueur.
                        for Y in range (L_5x5): #Pour X allant de 0 à la longueur d’une ligne de la matrice-1(= nombre de colonnes -1)
#BOUCLE EVENT.CLICDROIT.2 - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT et dans la BOUCLE EVENT.CLICDROIT.1
# Cette boucle parcourt la grille centrale en hauteur.
                            for X in range (H_5x5): #Pour Y allant de 0 au nombre de ligne de la matrice – 1 
#BOUCLE EVENT.CLICDROIT.3 - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT, BOUCLE EVENT.CLICDROIT.1 et BOUCLE EVENT.CLICDROIT.2.
# Cette boucle s'effectue SI ET SEULEMENT SI les compteurs (X,Y) sont équivalents aux coordonnées des cases (CASE_X,CASE_Y)
                                if X == CASE_X and Y == CASE_Y:

#BOUCLE EVENT.CLICDROIT.VIDE - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT, BOUCLE EVENT.CLICDROIT.1, BOUCLE EVENT.CLICDROIT.2, BOUCLE EVENT.CLICDROIT.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee [CASE_X;CASE_Y] est vide (0)
                                    if MATRICE_GRILLE_5x5[CASE_X, CASE_Y] == 0: # comporte un 1 dans la matrice , c'est a dire si la case est vide
                                        MATRICE_GRILLE_5x5[CASE_X, CASE_Y] = 2 #on assigne 2 dans la matrice pour la coordonnée [CASE_X;CASE_Y]

#BOUCLE EVENT.CLICDROIT.CARRE - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT, BOUCLE EVENT.CLICDROIT.1, BOUCLE EVENT.CLICDROIT.2, BOUCLE EVENT.CLICDROIT.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee [CASE_X;CASE_Y] comporte un CARRE noir (1)
                                    elif MATRICE_GRILLE_5x5[CASE_X, CASE_Y] == 1: # comporte un 1 dans la matrice , c'est a dire si la case est noire
                                        MATRICE_GRILLE_5x5[CASE_X, CASE_Y] = 2 # on assigne 2 dans la matrice pour la coordonnée [CASE_X;CASE_Y]

#BOUCLE EVENT.CLICDROIT.CROIX - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT, BOUCLE EVENT.CLICDROIT.1, BOUCLE EVENT.CLICDROIT.2, BOUCLE EVENT.CLICDROIT.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee (CASE_X;CASE_Y) comporte une CROIX noire (2)
                                    elif MATRICE_GRILLE_5x5[CASE_X, CASE_Y] == 2: #comporte un 2 dans la matrice c'est a dire si la case est cochée
                                        MATRICE_GRILLE_5x5[CASE_X, CASE_Y] = 0 # on assigne 0 dans la matrice pour la coordonnée [CASE_X;CASE_Y]
                                    print(MATRICE_GRILLE_5x5)

################################################################################
#                         PROGRAMME de la Grille 10x10
################################################################################
# Cree par Fabien et Sinan le 21/03/2016 en Python 3.2
#===============================================================================
#                            PRINCIPE DU PROGRAMME
#===============================================================================
# Ce programme est la clef de notre projet,
# il se sert d'autres programmes et bibliothèques sous-jacent(e)s afin d'oeuvrer
# à la création d'une grille de jeu picross de dimension 10x10.
#===============================================================================
#                            CORPS DU PROGRAMME
#===============================================================================
#BOUCLE D'EXECUTION - Qui s'exécute tant que la variable "continuer" vaut 1
    while continuer_grille10x10 == 1:
#-------------------------------------------------------------------------------
#                              AFFICHAGE DU FOND
#-------------------------------------------------------------------------------
# Affichage d'une couleur de fond
        FENETRE.fill(BLANC_CREME)
        #- le logo du jeu "Picross Mania"
        #FENETRE.blit(LOGO, (130,75))

# Affichage des différentes grilles
        Affichage_Grille(FENETRE, X_ORIGINE_10x10, Y_ORIGINE_10x10, 10, 10, 5, TAILLE_CARRE_10x10)

        Afficher_Indic_Gauche(FENETRE, BLUE_PEGASUS, X_ORIGINE_10x10, Y_ORIGINE_10x10, 5, 10, 30, TAILLE_CARRE_10x10, MAT_GAUC, DIVISEUR_10x10)

        Afficher_Indic_Haut(FENETRE, BLUE_PEGASUS, X_ORIGINE_10x10, Y_ORIGINE_10x10, 5, 10, 30, TAILLE_CARRE_10x10, MAT_HAUT, DIVISEUR_10x10)

        if allclose(MAT_CENT, MATRICE_GRILLE_10x10):
                continuer_grille10x10 = 0
                animation_son = 1
                animation = 1

# Réactualisation de la liste de picross complétés
# Remise a zéro de la liste des picross en cours
                for i in range (len(PICROSS_EN_COURS_NIV2)):
                    if PICROSS_EN_COURS_NIV2[i] == True :
                        PICROSS_COMPLETS_NIV2[i] = 1
                        PICROSS_EN_COURS_NIV2[i] = False
                        SOMME_PICROSS_COMPLETS_NIV2 = somme_elements_liste(PICROSS_COMPLETS_NIV2)
                        print(PICROSS_EN_COURS_NIV2)
                        print(PICROSS_COMPLETS_NIV2)
                        print(SOMME_PICROSS_COMPLETS_NIV2)
        else :
                continuer_grille10x10 = 1
#-------------------------------------------------------------------------------
#      AFFICHAGE DES FORMES DANS LES CASES DE LA GRILLE : CARRES ET CROIX
#-------------------------------------------------------------------------------

#PARCOURS DES CASES DE LA GRILLE
# Dans ce bloc, on parcourt les cases de la grille en largeur puis en longueur.
#BOUCLE AFFICHAGE_FORMES - Qui s'exécute dans la BOUCLE D'EXECUTION soit tant que la variable "continuer" vaut 1
# Cette boucle parcourt la grille centrale en longueur.
        for x in range(L_10x10):

#BOUCLE AFFICHAGE_FORMES.1 - Qui s'exécute dans la BOUCLE AFFICHAGE_FORMES
# Cette boucle parcourt la grille centrale en hauteur.
            for y in range(H_10x10):

#BOUCLE AFFICHAGE_FORMES.VIDE - Qui s'exécute dans la BOUCLE AFFICHAGE_FORMES.1
# Cette boucle affiche un carré de la couleur de fond lorsque la matrice aux coordonnées [x,y] est égale à 0 càd dans le cas d'une case vide.
                if MATRICE_GRILLE_10x10[x,y]== 0:
                    Afficher_Carre(FENETRE, BLANC_CREME, BLANC_CREME, X_ORIGINE_10x10, Y_ORIGINE_10x10, x, y, TAILLE_CARRE_10x10, 1)

#BOUCLE AFFICHAGE_FORMES.CARRE - Qui s'exécute dans la BOUCLE AFFICHAGE_FORMES.1
# Cette boucle affiche un carré de couleur prédéfinie lorsque la matrice aux coordonnées [x,y] est égale à 1 càd dans le cas d'une case noircie.
                elif MATRICE_GRILLE_10x10[x,y]== 1:
                    Afficher_Carre(FENETRE, VERT_PIN, BLANC_CREME, X_ORIGINE_10x10, Y_ORIGINE_10x10, x, y, TAILLE_CARRE_10x10, 1)

#BOUCLE AFFICHAGE_FORMES.CROIX - Qui s'exécute dans la BOUCLE AFFICHAGE_FORMES.1
# Cette boucle affiche une croix de couleur prédéfinie lorsque la matrice aux coordonnées [x,y] est égale à 2 càd dans le cas d'une case cochée.
                elif MATRICE_GRILLE_10x10[x,y]== 2:
                    Afficher_Croix(FENETRE, VERT_PIN, X_ORIGINE_10x10, Y_ORIGINE_10x10, x, y, TAILLE_CARRE_10x10)

# Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

#BOUCLE PRINCIPALE - Qui s'exécute dans la BOUCLE D'EXECUTION soit tant que la variable "continuer" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

#-------------------------------------------------------------------------------
#                   EVENEMENT DE FERMETURE DE LA FENETRE
#-------------------------------------------------------------------------------

#BOUCLE DE FERMETURE - Qui s'éxécute dans la BOUCLE PRINCIPALE
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
            if event.type == QUIT:
                continuer_grille10x10 = 0
                MATRICE_GRILLE_10x10 = zeros((COLONNES_10x10,LIGNES_10x10))

#-------------------------------------------------------------------------------
#           CALCUL DES COORDONNEES DES CASES DE LA GRILLE CENTRALE
#-------------------------------------------------------------------------------

#BOUCLE D'EVENEMENT DE TYPE "CLIC" - Qui s'éxécute dans la BOUCLE PRINCIPALE
# Si un de ces événements est de type MOUSEBUTTONDOWN, càd un clic quel qu'il soit alors :
            if event.type == MOUSEBUTTONDOWN:

                if event.pos[0] >= X_ORIGINE_10x10 and event.pos[0] <= X_ORIGINE_10x10 + NBR_CARRE_CENTRAL_10x10 * TAILLE_CARRE_10x10 and event.pos[1] >= Y_ORIGINE_10x10 and event.pos[1] <= Y_ORIGINE_10x10 + TAILLE_CARRE_10x10 * NBR_CARRE_CENTRAL_10x10:
                    # Coordonnées des cases de la grille centrale
                    CASE_Y = (event.pos[0] - MARGE_X1_10x10)//TAILLE_CARRE_10x10
                    CASE_X = (event.pos[1] - MARGE_Y1_10x10)//TAILLE_CARRE_10x10
                    print((CASE_X,CASE_Y))

#-------------------------------------------------------------------------------
#                              CLIC GAUCHE
#-------------------------------------------------------------------------------

#BOUCLE EVENT.1 - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC"
# S'exécute que SI le clic est effectué SUR la grille centrale :

#BOUCLE EVENT.CLICGAUCHE - Qui s'exécute dans la BOUCLE EVENT.1
# Cette boucle s'effectue si on est dans le cas d'un clic gauche (1)
                    if event.button == 1: # dans le cas d'un clic gauche

#PARCOURS DES CASES DE LA GRILLE
# Dans ce bloc, on parcourt les cases de la grille en longueur puis en hauteur.
#BOUCLE EVENT.CLICGAUCHE.1 - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE
# Cette boucle parcourt la grille centrale en longueur.
                        for Y in range (L_10x10):   #Pour Y allant de 0 au nombre de ligne de la matrice
#BOUCLE EVENT.CLICGAUCHE.2 - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE et dans la BOUCLE EVENT.CLICGAUCHE.1
# Cette boucle parcourt la grille centrale en hauteur.
                            for X in range (H_10x10):       #Pour X allant de 0 à la longueur d’une ligne de la matrice - 1 (= nombre de colonnes -1) = 4
#BOUCLE EVENT.CLICGAUCHE.3 - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1 et BOUCLE EVENT.CLICGAUCHE.2.
# Cette boucle s'effectue SI ET SEULEMENT SI les compteurs (X,Y) sont équivalents aux coordonnées des cases (CASE_X,CASE_Y)
                                if X == CASE_X and Y == CASE_Y:

#BOUCLE EVENT.CLICGAUCHE.VIDE - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1, BOUCLE EVENT.CLICGAUCHE.2, BOUCLE EVENT.CLICGAUCHE.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee [CASE_X;CASE_Y] est vide (0)
                                    if MATRICE_GRILLE_10x10[CASE_X, CASE_Y] == 0:
                                        # Assignation d'un 1 dans la matrice pour la coordonnee [CASE_X;CASE_Y] pour indiquer que la case contient un CARRE
                                        MATRICE_GRILLE_10x10[CASE_X, CASE_Y] = 1

#BOUCLE EVENT.CLICGAUCHE.CARRE - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1, BOUCLE EVENT.CLICGAUCHE.2, BOUCLE EVENT.CLICGAUCHE.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee [CASE_X;CASE_Y] comporte un CARRE noire (1)
                                    elif MATRICE_GRILLE_10x10[CASE_X, CASE_Y] == 1:
                                        # Assignation de la valeur 0 (Case_Vide) dans la matrice pour la coordonnée [CASE_X;CASE_Y] ayant pour conséquence d'effacer le CARRE
                                        MATRICE_GRILLE_10x10[CASE_X, CASE_Y] = 0

#BOUCLE EVENT.CLICGAUCHE.CROIX - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1, BOUCLE EVENT.CLICGAUCHE.2, BOUCLE EVENT.CLICGAUCHE.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee (CASE_X;CASE_Y) comporte une CROIX noire (2)
                                    elif MATRICE_GRILLE_10x10[CASE_X, CASE_Y] == 2:
                                        # Assignation d'un 1 dans la matrice pour la coordonnee (case_x;case_y) pour indiquer que la case contient un CARRE
                                        MATRICE_GRILLE_10x10[CASE_X, CASE_Y] = 1
                                    print(MATRICE_GRILLE_10x10)

#-------------------------------------------------------------------------------
#                              CLIC DROIT
#-------------------------------------------------------------------------------

#BOUCLE EVENT.2 - Qui s'éxécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC"
# S'exécute que SI le clic est effectué SUR la grille centrale :

#BOUCLE EVENT.CLICDROIT - Qui s'exécute dans la BOUCLE EVENT.2
# Cette boucle s'effectue si on est dans le cas d'un clic droit (3)
                    elif event.button == 3: #Dans le cas d'un clic droit

#PARCOURS DES CASES DE LA GRILLE
# Dans ce bloc, on parcourt les cases de la grille en longueur puis en hauteur.
#BOUCLE EVENT.CLICDROIT.1 - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT
# Cette boucle parcourt la grille centrale en longueur.
                        for Y in range (L_10x10): #Pour X allant de 0 à la longueur d’une ligne de la matrice-1(= nombre de colonnes -1)
#BOUCLE EVENT.CLICDROIT.2 - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT et dans la BOUCLE EVENT.CLICDROIT.1
# Cette boucle parcourt la grille centrale en hauteur.
                            for X in range (H_10x10): #Pour Y allant de 0 au nombre de ligne de la matrice – 1 
#BOUCLE EVENT.CLICDROIT.3 - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT, BOUCLE EVENT.CLICDROIT.1 et BOUCLE EVENT.CLICDROIT.2.
# Cette boucle s'effectue SI ET SEULEMENT SI les compteurs (X,Y) sont équivalents aux coordonnées des cases (CASE_X,CASE_Y)
                                if X == CASE_X and Y == CASE_Y:

#BOUCLE EVENT.CLICDROIT.VIDE - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT, BOUCLE EVENT.CLICDROIT.1, BOUCLE EVENT.CLICDROIT.2, BOUCLE EVENT.CLICDROIT.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee [CASE_X;CASE_Y] est vide (0)
                                    if MATRICE_GRILLE_10x10[CASE_X, CASE_Y] == 0: # comporte un 1 dans la matrice , c'est a dire si la case est vide
                                        MATRICE_GRILLE_10x10[CASE_X, CASE_Y] = 2 #on assigne 2 dans la matrice pour la coordonnée [CASE_X;CASE_Y]

#BOUCLE EVENT.CLICDROIT.CARRE - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT, BOUCLE EVENT.CLICDROIT.1, BOUCLE EVENT.CLICDROIT.2, BOUCLE EVENT.CLICDROIT.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee [CASE_X;CASE_Y] comporte un CARRE noir (1)
                                    elif MATRICE_GRILLE_10x10[CASE_X, CASE_Y] == 1: # comporte un 1 dans la matrice , c'est a dire si la case est noire
                                        MATRICE_GRILLE_10x10[CASE_X, CASE_Y] = 2 # on assigne 2 dans la matrice pour la coordonnée [CASE_X;CASE_Y]

#BOUCLE EVENT.CLICDROIT.CROIX - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT, BOUCLE EVENT.CLICDROIT.1, BOUCLE EVENT.CLICDROIT.2, BOUCLE EVENT.CLICDROIT.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee (CASE_X;CASE_Y) comporte une CROIX noire (2)
                                    elif MATRICE_GRILLE_10x10[CASE_X, CASE_Y] == 2: #comporte un 2 dans la matrice c'est a dire si la case est cochée
                                        MATRICE_GRILLE_10x10[CASE_X, CASE_Y] = 0 # on assigne 0 dans la matrice pour la coordonnée [CASE_X;CASE_Y]
                                    print(MATRICE_GRILLE_10x10)

################################################################################
#                       Page d'affichage du Tutoriel
################################################################################
#BOUCLE D'AFFICHAGE DE LA PAGE "Tutoriel" - Qui s'exécute tant que la variable "continuer_tutoriel" vaut 1
    while continuer_tutoriel == 1:

# Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

# Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30,40))
            #- titre du tutoriel
        FENETRE.blit(TITRE_TUTORIEL, (296, 30))
            #- bouton tuto1
        FENETRE.blit(BOUTON_TUTO_1, (150, 190))
            #- bouton tuto2
        FENETRE.blit(BOUTON_TUTO_2, (150, 310))
            #- bouton tuto3
        FENETRE.blit(BOUTON_TUTO_3,(150, 430))

        #Si la souris est positionnée sur l'interface :
        #condition nécessaire pour que le jeu continue de tourner même si la souris quitte l'interface
        #en effet la position de la souris n'est pas définie lorque la souris n'est pas sur l'interface du jeu
        if pygame.mouse.get_focused():
            if Rect_bouton_tuto_1.collidepoint(event.pos):
                FENETRE.blit(BOUTON_TUTO_1_INTER, (125, 185))
            if Rect_bouton_tuto_2.collidepoint(event.pos):
                FENETRE.blit(BOUTON_TUTO_2_INTER, (125, 305))
            if Rect_bouton_tuto_3.collidepoint(event.pos):
                FENETRE.blit(BOUTON_TUTO_3_INTER, (125, 425))

# Affichage du texte
        Texte(FENETRE, TEXTE_TUTORIEL, 100, 100, NOIR, None, 30)

# Rafraichissement de la fenêtre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

#BOUCLE PRINCIPALE.7 - Qui s'exécute dans la BOUCLE D'AFFICHAGE DE LA PAGE "Tuturiel" soit tant que la variable "continuer_tutoriel" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

#BOUCLE DE FERMETURE.7 - Qui s'exécute dans la BOUCLE PRINCIPALE.7
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" ainsi qu'à "continuer_tutoriel" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
            if event.type == QUIT:
                # On arrête la boucle ce qui ferme la fenetre
                continuer_tutoriel = 0
                continuer = 0

#BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE" - Qui s'exécute dans la BOUCLE PRINCIPALE.6
# Si un de ces événements est de type "CLIC" ET que ce clic est un "CLIC GAUCHE"
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

################################################################################
#                       Bouton de la page "Tutoriel"
################################################################################

#BOUCLE DU BOUTON "RETOUR" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "Retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30 + LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40 + HAUTEUR_BOUTON_RETOUR:
                    # Fermeture de la fenêtre "tutoriel"
                    continuer_tutoriel = 0
                    # Ouverture du menu principal
                    continuer_menu = 1

                if event.pos[0] >= 150 and event.pos[0] <= 150 + LONGUEUR_BOUTON_TUTO and event.pos[1] >= 190 and event.pos[1] <= 190 + HAUTEUR_BOUTON_TUTO:
                    # Fermeture de la fenêtre "tutoriel"
                    continuer_tutoriel = 0
                    # Ouverture du "Comment résoudre un picross ?"
                    continuer_comment_resoudre_picross1 = 1

                if event.pos[0] >= 150 and event.pos[0] <= 150 + LONGUEUR_BOUTON_TUTO and event.pos[1] >= 310 and event.pos[1] <= 310 + HAUTEUR_BOUTON_TUTO:
                    # Fermeture de la fenêtre "Tutoriel"
                    continuer_tutoriel = 0
                    # Ouverture du "Comment créer son Picross ?"
                    continuer_comment_creer_picross1 = 1

                if event.pos[0] >= 150 and event.pos[0] <= 150 + LONGUEUR_BOUTON_TUTO and event.pos[1] >= 430 and event.pos[1] <= 430 + HAUTEUR_BOUTON_TUTO:
                    # Fermeture de la fenêtre "Tutoriel"
                    continuer_tutoriel = 0
                    # Ouverture du "Comment utiliser le résolveur auto. ?"
                    continuer_comment_utiliser_resolveur1 = 1
################################################################################
#               Page d'affichage du "Comment résoudre un Picross ?"
################################################################################

#-------------------------------------------------------------------------------
#           Affichage de la page 1 de "Comment résoudre un Picross ?"
#-------------------------------------------------------------------------------

#BOUCLE D'AFFICHAGE DE LA PAGE "Tutoriel" - Qui s'exécute tant que la variable "continuer_cmt1" vaut 1
    while continuer_comment_resoudre_picross1 == 1:

# Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

# Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30, 40))
            #- titre du tutoriel
        FENETRE.blit(TITRE_TUTORIEL, (296, 30))
            #- bouton précédent
        FENETRE.blit(BOUTON_AVANT, (675, 590))
            #- bouton aprés
        FENETRE.blit(BOUTON_APRES, (725, 590))
        FENETRE.blit(pygame.image.load("diapo1.PNG"), (79,150))

# Affichage du texte
        Texte(FENETRE, "PAGE 1/3", 50, 600, VERT_PIN, None, 30)

        #Si la souris est positionnée sur l'interface :
        #condition nécessaire pour que le jeu continue de tourner même si la souris quitte l'interface
        #en effet la position de la souris n'est pas définie lorque la souris n'est pas sur l'interface du jeu
        if pygame.mouse.get_focused():
            if Rect_bouton_avant.collidepoint(event.pos):
                FENETRE.blit(BOUTON_AVANT_INTER, (675, 590))
            if Rect_bouton_apres.collidepoint(event.pos):
                FENETRE.blit(BOUTON_APRES_INTER, (725, 590))

# Rafraichissement de la fenêtre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

#BOUCLE PRINCIPALE.7 - Qui s'exécute dans la BOUCLE D'AFFICHAGE DE LA PAGE "Tuturiel" soit tant que la variable "continuer_tutoriel" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

#BOUCLE DE FERMETURE.7 - Qui s'exécute dans la BOUCLE PRINCIPALE.7
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" ainsi qu'à "continuer_tutoriel" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
            if event.type == QUIT:
                # On arrête la boucle ce qui ferme la fenetre
                continuer_comment_resoudre_picross1 = 0
                continuer = 0

#BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE" - Qui s'exécute dans la BOUCLE PRINCIPALE.6
# Si un de ces événements est de type "CLIC" ET que ce clic est un "CLIC GAUCHE"
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

################################################################################
#                Bouton de la page "Comment résoudre un picross ?"
################################################################################

#BOUCLE DU BOUTON "RETOUR" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "Retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30 + LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40 + HAUTEUR_BOUTON_RETOUR:
                    # Fermeture de la fenêtre "tutoriel"
                    continuer_comment_resoudre_picross1 = 0
                    # Ouverture du menu principal
                    continuer_tutoriel = 1

                if event.pos[0] >= 725 and event.pos[0] <= 725 + 35 and event.pos[1] >= 580 and event.pos[1] <= 580 + 35 :
                    # Fermeture de la fenêtre "tutoriel"
                    continuer_comment_resoudre_picross1 = 0
                    continuer_comment_resoudre_picross2 = 1

#-------------------------------------------------------------------------------
#           Affichage de la page 2 de "Comment résoudre un Picross ?"
#-------------------------------------------------------------------------------

#BOUCLE D'AFFICHAGE DE LA PAGE "Tutoriel" - Qui s'exécute tant que la variable "continuer_cmt1" vaut 1
    while continuer_comment_resoudre_picross2 == 1:

# Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

# Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30, 40))
            #- titre du tutoriel
        FENETRE.blit(TITRE_TUTORIEL, (296, 30))
            #- bouton précédent
        FENETRE.blit(BOUTON_AVANT, (675, 590))
            #- bouton aprés
        FENETRE.blit(BOUTON_APRES, (725, 590))
        FENETRE.blit(pygame.image.load("diapo2.PNG"), (79,150))

# Affichage du texte
        Texte(FENETRE, "PAGE 2/3", 50, 600, VERT_PIN, None, 30)

        #Si la souris est positionnée sur l'interface :
        #condition nécessaire pour que le jeu continue de tourner même si la souris quitte l'interface
        #en effet la position de la souris n'est pas définie lorque la souris n'est pas sur l'interface du jeu
        if pygame.mouse.get_focused():
            if Rect_bouton_avant.collidepoint(event.pos):
                FENETRE.blit(BOUTON_AVANT_INTER, (675, 590))
            if Rect_bouton_apres.collidepoint(event.pos):
                FENETRE.blit(BOUTON_APRES_INTER, (725, 590))

# Rafraichissement de la fenêtre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

#BOUCLE PRINCIPALE.7 - Qui s'exécute dans la BOUCLE D'AFFICHAGE DE LA PAGE "Tuturiel" soit tant que la variable "continuer_tutoriel" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

#BOUCLE DE FERMETURE.7 - Qui s'exécute dans la BOUCLE PRINCIPALE.7
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" ainsi qu'à "continuer_tutoriel" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
            if event.type == QUIT:
                # On arrête la boucle ce qui ferme la fenetre
                continuer_comment_resoudre_picross2 = 0
                continuer = 0

#BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE" - Qui s'exécute dans la BOUCLE PRINCIPALE.6
# Si un de ces événements est de type "CLIC" ET que ce clic est un "CLIC GAUCHE"
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

################################################################################
#                Bouton de la page "Comment résoudre un picross ?"
################################################################################

#BOUCLE DU BOUTON "RETOUR" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "Retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30 + LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40 + HAUTEUR_BOUTON_RETOUR:
                    # Fermeture de la fenêtre "tutoriel"
                    continuer_comment_resoudre_picross2 = 0
                    # Ouverture du menu principal
                    continuer_tutoriel = 1

                if event.pos[0] >= 675 and event.pos[0] <= 675 + 35 and event.pos[1] >= 580 and event.pos[1] <= 580 + 35 :
                    continuer_comment_resoudre_picross2 = 0
                    continuer_comment_resoudre_picross1 = 1


################################################################################
#                Page d'affichage du "Comment créer son Picross ?"
################################################################################
#BOUCLE D'AFFICHAGE DE LA PAGE "Tutoriel" - Qui s'exécute tant que la variable "continuer_tutoriel" vaut 1
    while continuer_comment_creer_picross1 == 1:

# Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

# Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30,40))
            #- titre du tutoriel
        FENETRE.blit(TITRE_TUTORIEL, (296, 30))

# Affichage du texte
        Texte(FENETRE, TEXTE_TUTORIEL, 100, 50, NOIR, None, 30)

# Rafraichissement de la fenêtre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

#BOUCLE PRINCIPALE.7 - Qui s'exécute dans la BOUCLE D'AFFICHAGE DE LA PAGE "Tuturiel" soit tant que la variable "continuer_tutoriel" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

#BOUCLE DE FERMETURE.7 - Qui s'exécute dans la BOUCLE PRINCIPALE.7
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" ainsi qu'à "continuer_tutoriel" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
            if event.type == QUIT:
                # On arrête la boucle ce qui ferme la fenetre
                continuer_cmt2 = 0
                continuer = 0

#BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE" - Qui s'exécute dans la BOUCLE PRINCIPALE.6
# Si un de ces événements est de type "CLIC" ET que ce clic est un "CLIC GAUCHE"
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

################################################################################
#                  Bouton de la page "Comment créer son Picross ?"
################################################################################

#BOUCLE DU BOUTON "RETOUR" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "Retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30 + LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40 + HAUTEUR_BOUTON_RETOUR:
                    # Fermeture de la fenêtre "tutoriel2"
                    continuer_cmt2 = 0
                    # Ouverture du tutoriel
                    continuer_tutoriel = 1

################################################################################
#       Page d'affichage du "Comment utiliser le résolveur automatique ?"
################################################################################
#BOUCLE D'AFFICHAGE DE LA PAGE "Comment utliser le résolveur automatique ?" - Qui s'exécute tant que la variable "continuer_cmt3" vaut 1
    while continuer_comment_utiliser_resolveur1 == 1:

# Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

# Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30,40))
            #- titre du tutoriel
        FENETRE.blit(TITRE_TUTORIEL, (350, 30))

# Affichage du texte
        Texte(FENETRE, TEXTE_TUTORIEL, 100, 100, NOIR, None, 30)

# Rafraichissement de la fenêtre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

#BOUCLE PRINCIPALE.7 - Qui s'exécute dans la BOUCLE D'AFFICHAGE DE LA PAGE "Tuturiel" soit tant que la variable "continuer_tutoriel" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

#BOUCLE DE FERMETURE.7 - Qui s'exécute dans la BOUCLE PRINCIPALE.7
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" ainsi qu'à "continuer_tutoriel" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
            if event.type == QUIT:
                # On arrête la boucle ce qui ferme la fenetre
                continuer_tutoriel = 0
                continuer = 0

#BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE" - Qui s'exécute dans la BOUCLE PRINCIPALE.6
# Si un de ces événements est de type "CLIC" ET que ce clic est un "CLIC GAUCHE"
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

################################################################################
#         Bouton de la page "Comment utliser le résolveur automatique ?"
################################################################################

#BOUCLE DU BOUTON "RETOUR" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "Retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30 + LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40 + HAUTEUR_BOUTON_RETOUR:
                    # Fermeture de la fenêtre "tutoriel"
                    continuer_cmt3 = 0
                    # Ouverture du menu principal
                    continuer_tutoriel = 1

################################################################################
#                                   Animation
################################################################################
#===============================================================================
#                            CORPS DU PROGRAMME
#===============================================================================

#BOUCLE D'EXECUTION - Qui s'exécute tant que la variable "continuer" vaut 1
    while animation == 1:


# Affichage d'une couleur de fond
        FENETRE.fill(BLANC_CREME)
        pygame.draw.line(FENETRE, NOIR, (154, 400), (650, 400), 4)
        pygame.draw.line(FENETRE, NOIR, (650, 204), (650, 402), 4)

# Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30,40))

        FENETRE.blit(pygame.image.load("animation.png"), (150, 200))
        """FENETRE.blit(pygame.image.load("Luigi3.gif"), (0, 400))
        FENETRE.blit(pygame.image.load("Luigi2.gif"), (600, 250))"""
        animation_son = 1

        if animation_son == 1:
            pygame.mixer.music.load("FF4VictoryFanfare.ogg")
            pygame.mixer.music.set_volume(0.175)
            pygame.mixer.music.play(-1, 0)

        MATRICE_GRILLE_5x5 = zeros((COLONNES_5x5,LIGNES_5x5))
        MATRICE_GRILLE_10x10 = zeros((COLONNES_10x10,LIGNES_10x10))


# Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

#BOUCLE PRINCIPALE - Qui s'exécute dans la BOUCLE D'EXECUTION soit tant que la variable "continuer" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

#BOUCLE DE FERMETURE - Qui s'éxécute dans la BOUCLE PRINCIPALE
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
            if event.type == QUIT:
                animation = 0
                continuer = 0

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

#Si l'utilisateur clique sur la zone correspondant au bouton "Retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30 + LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40 + HAUTEUR_BOUTON_RETOUR:
                    # Fermeture de la fenêtre "tutoriel"
                    animation = 0
                    # Ouverture du menu principal
                    continuer_menu = 1

#Permet de fermet la fenêtre sans bug (sans cela le programme ne répond plus
#lors de la fermeture de la fenêtre)
pygame.quit()




