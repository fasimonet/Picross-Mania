#Cree par Fabien et Sinan le 11/04/2016 en Python 3.2
"""
________________________________________________________________________________

                            PRINCIPE DU PROGRAMME
________________________________________________________________________________

"""





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
"""from tuto import *"""
from fonctions_tuto import *
from constantes_tuto import *

################################################################################
#                              Initialisation
################################################################################

# Creation d'une variable fenetre qui affiche la fenetre du jeu
FENETRE = pygame.display.set_mode((LONGUEUR_FENETRE, HAUTEUR_FENETRE))

# Titre de la fenetre
pygame.display.set_caption(TITRE_FENETRE)

# Variable "continuer" à laquelle on affecte la valeur 1
# Cela va nous permettre de garder la fenêtre ouverte
continuer = 1



#BOUCLE PRINCIPALE
#Fermeture de la fenetre
while continuer:

    #Met une couleur de fond
    FENETRE.fill(BLANC_CREME)
    #Collage des différents boutons sur la fenêtre :
        #- le bouton "picross à résoudre"
    FENETRE.blit(BOUTON_PICROSS_A_RESOUDRE, (35,300))
        #- le bouton "résolution de picross"
    FENETRE.blit(BOUTON_RESOLUTION_DE_PICROSS, (285,300))
        #- le bouton "création de picross"
    FENETRE.blit(BOUTON_CREATION_DE_PICROSS, (535,300))
        #- le bouton "tutoriel"
    FENETRE.blit(BOUTON_TUTORIEL, (660,588))
        #- le logo du jeu "Picross Mania"
    FENETRE.blit(LOGO, (130,120))

    #Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
    pygame.display.flip()

    #Initialisation des fenêtres : au départ seul le menu principal est ouvert
    continuer_picross_a_resoudre = 0
    continuer_niveau1 = 0
    continuer_niveau2 = 0
    continuer_niveau3 = 0
    continuer_niveau4 = 0
    continuer_tutoriel = 0
    continuer_menu = 1

    #BOUCLE concernant l'affichage du menu principal
    while continuer_menu:

        #On parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

            #Si un de ces événements est de type QUIT
            if event.type == QUIT:
                #On arrête la boucle ce qui ferme la fenetre
                continuer_menu = 0
                continuer_tutoriel = 0
                continuer = 0

            #Si l'utilisateur fait un clic gauche
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                #Si l'utilisateur clique sur la zone correspondant au bouton "picross à résoudre"
                if event.pos[0] >= 35 and event.pos[0] <= 35+LONGUEUR_BOUTONS_PARTIES and event.pos[1] >= 300 and event.pos[1] <= 300+HAUTEUR_BOUTONS_PARTIES:
                    #Fermeture du menu principal
                    continuer_menu = 0
                    #Ouverture de la fenêtre "picross à résoudre"
                    continuer_picross_a_resoudre = 1

                #Si l'utilisateur clique sur la zone correspondant au bouton "résolution de picross"
                if event.pos[0] >= 285 and event.pos[0] <= 285+LONGUEUR_BOUTONS_PARTIES and event.pos[1] >= 300 and event.pos[1] <= 300+HAUTEUR_BOUTONS_PARTIES:
                    #Fermeture du menu principal
                    continuer_menu = 0
                    #Ouverture de la fenêtre "résolution de picross"
                    """continuer_resolution_de_picross = 1"""

                #Si l'utilisateur clique sur la zone correspondant au bouton "création de picross"
                if event.pos[0] >= 535 and event.pos[0] <= 535+LONGUEUR_BOUTONS_PARTIES and event.pos[1] >= 300 and event.pos[1] <= 300+HAUTEUR_BOUTONS_PARTIES:
                    #Fermeture du menu principal
                    continuer_menu = 0
                    #Ouverture de la fenêtre "création de picross"
                    """continuer_creation_de_picross = 1"""

                #Si l'utilisateur clique sur la zone correspondant au bouton "tutoriel"
                if event.pos[0] >= 660 and event.pos[0] <= 660+LONGUEUR_BOUTON_TUTORIEL and event.pos[1] >= 588 and event.pos[1] <= 588+HAUTEUR_BOUTON_TUTORIEL:
                    #Fermeture du menu principal
                    continuer_menu = 0
                    #Ouverture du tutoriel
                    continuer_tutoriel = 1

 """           #Si l'utilisateur fait un clic gauche
            if event.type == MOUSEMOTION:

                #Si l'utilisateur clique sur la zone correspondant au bouton "picross à résoudre"
                if event.pos[0] >= 35 and event.pos[0] <= 35+LONGUEUR_BOUTONS_PARTIES and event.pos[1] >= 300 and event.pos[1] <= 300+HAUTEUR_BOUTONS_PARTIES:
                    FENETRE.blit((BOUTON_PICROSS_A_RESOUDRE_GRAND, (35-10,300-10), None))
                    #Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
                    pygame.display.flip()"""

    #BOUCLE concernant l'affichage de la partie "picross à résoudre"
    while continuer_picross_a_resoudre:

        #Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

        #Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30,40))
            #- titre "picross à résoudre"
        FENETRE.blit(TITRE_PICROSS_A_RESOUDRE, (240,30))
            #- bouton "niveau 1" du "picross à résoudre"
        FENETRE.blit(BOUTON_NIVEAU1, (250, 110))
            #- bouton "niveau 2" du "picross à résoudre"
        FENETRE.blit(BOUTON_NIVEAU2, (480, 110))
            #- bouton "niveau 3" du "picross à résoudre"
        FENETRE.blit(BOUTON_NIVEAU3, (250, 350))
            #- bouton "niveau 4" du "picross à résoudre"
        FENETRE.blit(BOUTON_NIVEAU4, (480, 350))
            #- le bouton "tutoriel"
        FENETRE.blit(BOUTON_TUTORIEL, (660,588))

        #Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

        #On parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

            #Si un de ces événements est de type QUIT
            if event.type == QUIT:
                #On arrête la boucle ce qui ferme la fenetre
                continuer_picross_a_resoudre = 0
                continuer = 0

            #Si l'utilisateur fait un clic gauche
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                #Si l'utilisateur clique sur la zone correspondant au bouton "picross à résoudre"
                if event.pos[0] >= 30 and event.pos[0] <= 30+LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40+HAUTEUR_BOUTON_RETOUR:
                    #Fermeture de la fenêtre "picross à résoudre"
                    continuer_picross_a_resoudre = 0
                    #Ouverture du menu principal
                    continuer_menu = 1

                #Si l'utilisateur clique sur la zone correspondant au bouton "tutoriel"
                if event.pos[0] >= 660 and event.pos[0] <= 660+LONGUEUR_BOUTON_TUTORIEL and event.pos[1] >= 588 and event.pos[1] <= 588+HAUTEUR_BOUTON_TUTORIEL:
                    #Fermeture du menu principal
                    continuer_picross_a_resoudre = 0
                    #Ouverture du tutoriel
                    continuer_tutoriel = 1

                #Si l'utilisateur clique sur la zone correspondant au bouton "NIVEAU 1"
                if event.pos[0] >= 250 and event.pos[0] <= 250+DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 110 and event.pos[1] <= 110+DIMENSION_COTE_BOUTONS_NIVEAUX:
                    #Fermeture de la fenêtre "picross à résoudre"
                    continuer_picross_a_resoudre = 0
                    #Ouverture de la fenêtre "Niveau 1"
                    continuer_niveau1 = 1

                #Si l'utilisateur clique sur la zone correspondant au bouton "NIVEAU 2"
                if event.pos[0] >= 480 and event.pos[0] <= 480+DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 110 and event.pos[1] <= 110+DIMENSION_COTE_BOUTONS_NIVEAUX:
                    #Fermeture de la fenêtre "picross à résoudre"
                    continuer_picross_a_resoudre = 0
                    #Ouverture de la fenêtre "Niveau 2"
                    continuer_niveau2 = 1

                #Si l'utilisateur clique sur la zone correspondant au bouton "NIVEAU 3"
                if event.pos[0] >= 250 and event.pos[0] <= 250+DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 350 and event.pos[1] <= 350+DIMENSION_COTE_BOUTONS_NIVEAUX:
                    #Fermeture de la fenêtre "picross à résoudre"
                    continuer_picross_a_resoudre = 0
                    #Ouverture de la fenêtre "Niveau 3"
                    continuer_niveau3 = 1

                #Si l'utilisateur clique sur la zone correspondant au bouton "NIVEAU 4"
                if event.pos[0] >= 480 and event.pos[0] <= 480+DIMENSION_COTE_BOUTONS_NIVEAUX and event.pos[1] >= 350 and event.pos[1] <= 350+DIMENSION_COTE_BOUTONS_NIVEAUX:
                    #Fermeture de la fenêtre "picross à résoudre"
                    continuer_picross_a_resoudre = 0
                    #Ouverture de la fenêtre "Niveau 4"
                    continuer_niveau4 = 1

    #BOUCLE concernant l'affichage du niveau 1 de "picross à résoudre"
    while continuer_niveau1:

        #Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

        #Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30,40))
            #- le bouton "tutoriel"
        FENETRE.blit(BOUTON_TUTORIEL, (660,588))

        #Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

        #On parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

            #Si un de ces événements est de type QUIT
            if event.type == QUIT:
                #On arrête la boucle ce qui ferme la fenetre
                continuer_niveau1 = 0
                continuer = 0

            #Si l'utilisateur fait un clic gauche
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                #Si l'utilisateur clique sur la zone correspondant au bouton "retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30+LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40+HAUTEUR_BOUTON_RETOUR:
                    #Fermeture de la fenêtre "Niveau 1"
                    continuer_niveau1 = 0
                    #Ouverture de "picross à résoudre"
                    continuer_picross_a_resoudre = 1

                #Si l'utilisateur clique sur la zone correspondant au bouton "tutoriel"
                if event.pos[0] >= 660 and event.pos[0] <= 660+LONGUEUR_BOUTON_TUTORIEL and event.pos[1] >= 588 and event.pos[1] <= 588+HAUTEUR_BOUTON_TUTORIEL:
                    #Fermeture du menu principal
                    continuer_niveau1 = 0
                    #Ouverture du tutoriel
                    continuer_tutoriel = 1

    #BOUCLE concernant l'affichage du niveau 2 de "picross à résoudre"
    while continuer_niveau2:

        #Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

        #Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30,40))
            #- le bouton "tutoriel"
        FENETRE.blit(BOUTON_TUTORIEL, (660,588))

        #Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

        #On parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

            #Si un de ces événements est de type QUIT
            if event.type == QUIT:
                #On arrête la boucle ce qui ferme la fenetre
                continuer_niveau2 = 0
                continuer = 0

            #Si l'utilisateur fait un clic gauche
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                #Si l'utilisateur clique sur la zone correspondant au bouton "retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30+LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40+HAUTEUR_BOUTON_RETOUR:
                    #Fermeture de la fenêtre "Niveau 2"
                    continuer_niveau2 = 0
                    #Ouverture de "picross à résoudre"
                    continuer_picross_a_resoudre = 1

                #Si l'utilisateur clique sur la zone correspondant au bouton "tutoriel"
                if event.pos[0] >= 660 and event.pos[0] <= 660+LONGUEUR_BOUTON_TUTORIEL and event.pos[1] >= 588 and event.pos[1] <= 588+HAUTEUR_BOUTON_TUTORIEL:
                    #Fermeture du menu principal
                    continuer_niveau1 = 0
                    #Ouverture du tutoriel
                    continuer_tutoriel = 1

    #BOUCLE concernant l'affichage du niveau 3 de "picross à résoudre"
    while continuer_niveau3:

        #Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

        #Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30,40))
            #- le bouton "tutoriel"
        FENETRE.blit(BOUTON_TUTORIEL, (660,588))

        #Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

        #On parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

            #Si un de ces événements est de type QUIT
            if event.type == QUIT:
                #On arrête la boucle ce qui ferme la fenetre
                continuer_niveau3 = 0
                continuer = 0

            #Si l'utilisateur fait un clic gauche
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                #Si l'utilisateur clique sur la zone correspondant au bouton "retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30+LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40+HAUTEUR_BOUTON_RETOUR:
                    #Fermeture de la fenêtre "Niveau 3"
                    continuer_niveau3 = 0
                    #Ouverture de "picross à résoudre"
                    continuer_picross_a_resoudre = 1

                #Si l'utilisateur clique sur la zone correspondant au bouton "tutoriel"
                if event.pos[0] >= 660 and event.pos[0] <= 660+LONGUEUR_BOUTON_TUTORIEL and event.pos[1] >= 588 and event.pos[1] <= 588+HAUTEUR_BOUTON_TUTORIEL:
                    #Fermeture du "Niveau 3"
                    continuer_niveau3 = 0
                    #Ouverture du tutoriel
                    continuer_tutoriel = 1

    #BOUCLE concernant l'affichage du niveau 3 de "picross à résoudre"
    while continuer_niveau4:

        #Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

        #Collage des différents boutons sur la fenêtre :
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30,40))
            #- le bouton "tutoriel"
        FENETRE.blit(BOUTON_TUTORIEL, (660,588))

        #Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

        #On parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

            #Si un de ces événements est de type QUIT
            if event.type == QUIT:
                #On arrête la boucle ce qui ferme la fenetre
                continuer_niveau4 = 0
                continuer = 0

            #Si l'utilisateur fait un clic gauche
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                #Si l'utilisateur clique sur la zone correspondant au bouton "retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30+LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40+HAUTEUR_BOUTON_RETOUR:
                    #Fermeture de la fenêtre "Niveau 4"
                    continuer_niveau4 = 0
                    #Ouverture du menu principal
                    continuer_picross_a_resoudre = 1

                #Si l'utilisateur clique sur la zone correspondant au bouton "tutoriel"
                if event.pos[0] >= 660 and event.pos[0] <= 660+LONGUEUR_BOUTON_TUTORIEL and event.pos[1] >= 588 and event.pos[1] <= 588+HAUTEUR_BOUTON_TUTORIEL:
                    #Fermeture du "Niveau 4"
                    continuer_niveau4 = 0
                    #Ouverture du tutoriel
                    continuer_tutoriel = 1

    #BOUCLE concernant l'affichage du tutoriel
    while continuer_tutoriel:

        #Met une couleur de fond
        FENETRE.fill(BLANC_CREME)

        #Collage des différents boutons sur la fenêtre :
            #- titre "tutoriel"
        FENETRE.blit(TITRE_TUTORIEL, (290,25))
            #- bouton "retour"
        FENETRE.blit(BOUTON_RETOUR, (30,40))

        #Affichage du texte
        Texte(FENETRE, TEXTE, 100, 100, NOIR, None, 30)

        #Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
        pygame.display.flip()

        #On parcourt la liste de tous les événements reçus
        for event in pygame.event.get():

            #Si un de ces événements est de type QUIT
            if event.type == QUIT:
                #On arrête la boucle ce qui ferme la fenetre
                continuer_tutoriel = 0
                continuer = 0

            #Si l'utilisateur fait un clic gauche
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                #Si l'utilisateur clique sur la zone correspondant au bouton "retour"
                if event.pos[0] >= 30 and event.pos[0] <= 30+LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40+HAUTEUR_BOUTON_RETOUR:
                    #Fermeture de la fenêtre "tutoriel"
                    continuer_tutoriel = 0
                    #Ouverture du menu principal
                    continuer_menu = 1


#Permet de fermet la fenetre sans bug (sans cela le programme ne repond plus
#lors de la fermeture de la fenetre)
pygame.quit()



