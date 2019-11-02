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
    - le tutoriel """


################################################################################
#                  Import des Bibliothèques et des Annexes
################################################################################
#On importe le module pygame qui nous permet de créer l'interface graphique

import pygame
from pygame.locals import *

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

################################################################################
#                              Initialisation
################################################################################

# Création d'une variable "FENETRE" qui affiche la fenêtre du jeu
FENETRE = pygame.display.set_mode((LONGUEUR_FENETRE, HAUTEUR_FENETRE))

# Titre de la fenêtre
pygame.display.set_caption(TITRE_FENETRE)

#on initialise a "page_precedente" la valeur "aucune"
page_precedente = "aucune"

# Variable "continuer" à laquelle on affecte la valeur 1
# Cela va nous permettre de garder la fenêtre ouverte
continuer = 1

if continuer == 1:
    pygame.mixer.music.load("Menu_Picross.ogg")
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1, 0)


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

# Met une couleur de fond
    FENETRE.fill(BLANC_CREME)
# Collage des différents boutons sur la fenêtre :
        #- le bouton "picross à résoudre"
    FENETRE.blit(BOUTON_PICROSS_A_RESOUDRE, (54,300))
        #- le bouton "résolution de picross"
    FENETRE.blit(BOUTON_RESOLUTION_DE_PICROSS, (285,300))
        #- le bouton "création de picross"
    FENETRE.blit(BOUTON_CREATION_DE_PICROSS, (535,300))
        #- le bouton "tutoriel"
    FENETRE.blit(BOUTON_TUTORIEL, (30,585))
        #- le logo du jeu "Picross Mania"
    FENETRE.blit(LOGO, (130,120))
        #- image son-on
    FENETRE.blit(BOUTON_SON_ON, (725, 25))

# Rafraichissement de la fenêtre (nécessaire pour afficher ce qui précède)
    pygame.display.flip()

# Initialisation des fenêtres : au départ seul le menu principal est ouvert
    continuer_picross_a_resoudre = 0
    continuer_niveau1 = 0
    continuer_niveau2 = 0
    continuer_niveau3 = 0
    continuer_niveau4 = 0
    continuer_mon_niveau = 0
    continuer_tutoriel = 0
    continuer_cmt1 = 0
    continuer_cmt2 = 0
    continuer_cmt3 = 0
    continuer_menu = 1

#BOUCLE D'AFFICHAGE DU MENU PRINCIPAL - Qui s'exécute tant que la variable "continuer_menu" vaut 1
    while continuer_menu == 1:

        if pygame.mouse.get_focused():
            if Rect_picross_a_resoudre.collidepoint(event.pos):
                FENETRE.blit(BOUTON_PICROSS_A_RESOUDRE_INTER, (35, 300))
            if Rect_resolution_de_picross.collidepoint(event.pos):
                FENETRE.blit(BOUTON_RESOLUTION_DE_PICROSS_INTER, (264, 300))
            if Rect_creation_picross.collidepoint(event.pos):
                FENETRE.blit(BOUTON_CREATION_DE_PICROSS_INTER, (514, 300))

        pygame.display.flip()

#BOUCLE PRINCIPALE - Qui s'exécute dans la BOUCLE D'AFFICHAGE DU MENU PRINCIPAL soit tant que la variable "continuer_menu" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

#BOUCLE DE FERMETURE - Qui s'exécute dans la BOUCLE PRINCIPALE
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
            if event.type == QUIT:
                continuer_menu = 0
                """continuer_tutoriel = 0"""
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

        # Affichage du texte
        Texte(FENETRE, TITRE_NIVEAU1, 325, 50, NOIR, None, 30)

# On dessine une ligne verte qui sépare l'entête et la partie basse de l'interface
        pygame.draw.line(FENETRE, VERT_NIVEAU1, (310,110), (760,110), 5)

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

# Affichage du texte
        Texte(FENETRE, TITRE_NIVEAU2, 325, 50, NOIR, None, 30)

# On dessine une ligne jaune qui sépare l'entête et la partie basse de l'interface
        pygame.draw.line(FENETRE, JAUNE_NIVEAU2, (310,110), (760,110), 5)

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
                    continuer_cmt1 = 1

                if event.pos[0] >= 150 and event.pos[0] <= 150 + LONGUEUR_BOUTON_TUTO and event.pos[1] >= 310 and event.pos[1] <= 310 + HAUTEUR_BOUTON_TUTO:
                    # Fermeture de la fenêtre "Tutoriel"
                    continuer_tutoriel = 0
                    # Ouverture du "Comment créer son Picross ?"
                    continuer_cmt2 = 1

                if event.pos[0] >= 150 and event.pos[0] <= 150 + LONGUEUR_BOUTON_TUTO and event.pos[1] >= 430 and event.pos[1] <= 430 + HAUTEUR_BOUTON_TUTO:
                    # Fermeture de la fenêtre "Tutoriel"
                    continuer_tutoriel = 0
                    # Ouverture du "Comment utiliser le résolveur auto. ?"
                    continuer_cmt3 = 1
################################################################################
#               Page d'affichage du "Comment résoudre un Picross ?"
################################################################################
#BOUCLE D'AFFICHAGE DE LA PAGE "Tutoriel" - Qui s'exécute tant que la variable "continuer_cmt1" vaut 1
    while continuer_cmt1 == 1:

# Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

# Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30, 40))
            #- titre du tutoriel
        FENETRE.blit(TITRE_TUTORIEL, (296, 30))
            #- bouton précédent
        FENETRE.blit(BOUTON_AVANT, (650, 575))
            #- bouton aprés
        FENETRE.blit(BOUTON_APRES, (725, 575))

        #Si la souris est positionnée sur l'interface :
        #condition nécessaire pour que le jeu continue de tourner même si la souris quitte l'interface
        #en effet la position de la souris n'est pas définie lorque la souris n'est pas sur l'interface du jeu
        if pygame.mouse.get_focused():
            if Rect_bouton_avant.collidepoint(event.pos):
                FENETRE.blit(BOUTON_AVANT_INTER, (650, 575))
            if Rect_bouton_apres.collidepoint(event.pos):
                FENETRE.blit(BOUTON_APRES_INTER, (725, 575))

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
#                Bouton de la page "Comment résoudre un picross ?"
################################################################################

#BOUCLE DU BOUTON "RETOUR" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC GAUCHE"
#Si l'utilisateur clique sur la zone correspondant au bouton "Retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30 + LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40 + HAUTEUR_BOUTON_RETOUR:
                    # Fermeture de la fenêtre "tutoriel"
                    continuer_cmt1 = 0
                    # Ouverture du menu principal
                    continuer_tutoriel = 1

################################################################################
#                Page d'affichage du "Comment créer son Picross ?"
################################################################################
#BOUCLE D'AFFICHAGE DE LA PAGE "Tutoriel" - Qui s'exécute tant que la variable "continuer_tutoriel" vaut 1
    while continuer_cmt2 == 1:

# Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

# Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30,40))
            #- titre du tutoriel
        FENETRE.blit(TITRE_TUTORIEL, (296, 30))

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
#       Page d'affichage du "Comment utliser le résolveur automatique ?"
################################################################################
#BOUCLE D'AFFICHAGE DE LA PAGE "Comment utliser le résolveur automatique ?" - Qui s'exécute tant que la variable "continuer_cmt3" vaut 1
    while continuer_cmt3 == 1:

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


#Permet de fermet la fenêtre sans bug (sans cela le programme ne répond plus
#lors de la fermeture de la fenêtre)
pygame.quit()




