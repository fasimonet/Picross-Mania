# Créé par Quentin, le 07/05/2016 en Python 3.2

#Création de Picross


#===============================================================================
#                            PRINCIPE DU PROGRAMME
#===============================================================================

#ce programme consiste a la partie "Création de Picross"
#cette partie permet en realité à l'utilisateur de crée ses propres picross
#en vue de pouvoir les réutiliser dans l'avenir, ce programme sert donc à
#récupérer toutes les données nécessaires à cela

#===============================================================================
#                  Import des Bibliothèques et des Annexes
#===============================================================================

# On importe le module pygame qui nous permet de créer l'interface graphique.
import pygame
from pygame.locals import *
from numpy import *

# On initialise l'interface graphique.
pygame.init()

# On rattache le corps du programme aux annexes pour plus de clarté:
# Les fonctions et les constantes du programme
from fonctions5x5_3 import *
from constantes5x5_3 import *
#===============================================================================
#                              Initialisation
#===============================================================================

# Creation d'une variable fenetre qui affiche la fenetre du jeu
FENETRE = pygame.display.set_mode((LONGUEUR_FENETRE, HAUTEUR_FENETRE))

# Titre de la fenetre
pygame.display.set_caption(TITRE_FENETRE)

# Variable "continuer" à laquelle on affecte la valeur 1
# Cela va nous permettre de garder la fenêtre ouverte
continuer = 1
CASE_X = 0
CASE_Y= 0
NBR_CARRE_CENTRAL = 5

# Création de la matrice représentant la grille de dimension 5x5 remplie de 0
MATRICE_GRILLE = zeros((LIGNES, COLONNES))

"""# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 1
#---------------------------------------------
Matrice_grille_gauche1_niveau1 = array([(0, 1, 1),
                                        (0, 0, 5),
                                        (0, 1, 1),
                                        (0, 0, 5),
                                        (0, 1, 1)])"""

# MATRICE DE LA GRILLE CENTRALE DU PICROSS 1
#--------------------------------------------

Matrice_grille_centrale1_niveau1 =   array([(2, 1, 2, 1, 2),
                                            (1, 1, 1, 1, 1),
                                            (2, 1, 2, 1, 2),
                                            (1, 1, 1, 1, 1),
                                            (2, 1, 2, 1, 2)])

# MATRICE DE LA GRILLE DE HAUT DU PICROSS 1
#-------------------------------------------

"""Matrice_grille_haut1_niveau1 = zeros((3,5))"""

#===============================================================================
#                            CORPS DU PROGRAMME
#===============================================================================




#BOUCLE D'EXECUTION - Qui s'exécute tant que la variable "continuer" vaut 1
while continuer == 1:
#-------------------------------------------------------------------------------
#                              AFFICHAGE DU FOND
#-------------------------------------------------------------------------------

# Affichage d'une couleur de fond
    FENETRE.fill(BLANC_CREME)

# Affichage des différentes grilles
    Affichage_Grille(FENETRE, X_ORIGINE, Y_ORIGINE, 5, 5, 3)

    """Afficher_Indic_Gauche(FENETRE, BLUE_PEGASUS, X_ORIGINE, Y_ORIGINE, 3, 5, Matrice_grille_gauche1_niveau1)"""

    """Afficher_Indic_Haut(FENETRE, BLUE_PEGASUS, X_ORIGINE,Y_ORIGINE, 3, 5, Matrice_grille_haut1_niveau1)"""

#-------------------------------------------------------------------------------
#      AFFICHAGE DES FORMES DANS LES CASES DE LA GRILLE : CARRES ET CROIX
#-------------------------------------------------------------------------------

#PARCOURS DES CASES DE LA GRILLE
# Dans ce bloc, on parcourt les cases de la grille en largeur puis en longueur.
#BOUCLE AFFICHAGE_FORMES - Qui s'exécute dans la BOUCLE D'EXECUTION soit tant que la variable "continuer" vaut 1
# Cette boucle parcourt la grille centrale en longueur.
    for x in range(L):

#BOUCLE AFFICHAGE_FORMES.1 - Qui s'exécute dans la BOUCLE AFFICHAGE_FORMES
# Cette boucle parcourt la grille centrale en hauteur.
        for y in range(H):

#BOUCLE AFFICHAGE_FORMES.VIDE - Qui s'exécute dans la BOUCLE AFFICHAGE_FORMES.1
# Cette boucle affiche un carré de la couleur de fond lorsque la matrice aux coordonnées [x,y] est égale à 0 càd dans le cas d'une case vide.
            if MATRICE_GRILLE[x,y]== 0:
                Afficher_Carre(FENETRE, BLANC_CREME, X_ORIGINE, Y_ORIGINE, x, y)

#BOUCLE AFFICHAGE_FORMES.CARRE - Qui s'exécute dans la BOUCLE AFFICHAGE_FORMES.1
# Cette boucle affiche un carré de couleur prédéfinie lorsque la matrice aux coordonnées [x,y] est égale à 1 càd dans le cas d'une case noircie.
            elif MATRICE_GRILLE[x,y]== 1:
                Afficher_Carre(FENETRE, NOIR, X_ORIGINE, Y_ORIGINE, x, y)

#BOUCLE AFFICHAGE_FORMES.CROIX - Qui s'exécute dans la BOUCLE AFFICHAGE_FORMES.1
# Cette boucle affiche une croix de couleur prédéfinie lorsque la matrice aux coordonnées [x,y] est égale à 2 càd dans le cas d'une case cochée.
            elif MATRICE_GRILLE[x,y]== 2:
                Afficher_Croix(FENETRE, VERT_PIN, X_ORIGINE, Y_ORIGINE, x, y)

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
            continuer = 0

#-------------------------------------------------------------------------------
#           CALCUL DES COORDONNEES DES CASES DE LA GRILLE CENTRALE
#-------------------------------------------------------------------------------

#BOUCLE D'EVENEMENT DE TYPE "CLIC" - Qui s'éxécute dans la BOUCLE PRINCIPALE
# Si un de ces événements est de type MOUSEBUTTONDOWN, càd un clic quel qu'il soit alors :
        if event.type == MOUSEBUTTONDOWN:

            if event.pos[0] >= X_ORIGINE and event.pos[0] <= X_ORIGINE + NBR_CARRE_CENTRAL * TAILLE_CARRE and event.pos[1] >= Y_ORIGINE and event.pos[1] <= Y_ORIGINE + TAILLE_CARRE * NBR_CARRE_CENTRAL:
                # Coordonnées des cases de la grille centrale
                CASE_Y = (event.pos[0] - MARGE_X1)//TAILLE_CARRE
                CASE_X = (event.pos[1] - MARGE_Y1)//TAILLE_CARRE
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
                    for Y in range (L):   #Pour Y allant de 0 au nombre de ligne de la matrice
#BOUCLE EVENT.CLICGAUCHE.2 - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE et dans la BOUCLE EVENT.CLICGAUCHE.1
# Cette boucle parcourt la grille centrale en hauteur.
                        for X in range (H):       #Pour X allant de 0 à la longueur d’une ligne de la matrice - 1 (= nombre de colonnes -1) = 4
#BOUCLE EVENT.CLICGAUCHE.3 - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1 et BOUCLE EVENT.CLICGAUCHE.2.
# Cette boucle s'effectue SI ET SEULEMENT SI les compteurs (X,Y) sont équivalents aux coordonnées des cases (CASE_X,CASE_Y)
                            if X == CASE_X and Y == CASE_Y:

#BOUCLE EVENT.CLICGAUCHE.VIDE - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1, BOUCLE EVENT.CLICGAUCHE.2, BOUCLE EVENT.CLICGAUCHE.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee [CASE_X;CASE_Y] est vide (0)
                                if MATRICE_GRILLE[CASE_X, CASE_Y] == 0:
                                    # Assignation d'un 1 dans la matrice pour la coordonnee [CASE_X;CASE_Y] pour indiquer que la case contient un CARRE
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 1

#BOUCLE EVENT.CLICGAUCHE.CARRE - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1, BOUCLE EVENT.CLICGAUCHE.2, BOUCLE EVENT.CLICGAUCHE.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee [CASE_X;CASE_Y] comporte un CARRE noire (1)
                                elif MATRICE_GRILLE[CASE_X, CASE_Y] == 1:
                                    # Assignation de la valeur 0 (Case_Vide) dans la matrice pour la coordonnée [CASE_X;CASE_Y] ayant pour conséquence d'effacer le CARRE
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 0

#BOUCLE EVENT.CLICGAUCHE.CROIX - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1, BOUCLE EVENT.CLICGAUCHE.2, BOUCLE EVENT.CLICGAUCHE.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee (CASE_X;CASE_Y) comporte une CROIX noire (2)
                                elif MATRICE_GRILLE[CASE_X, CASE_Y] == 2:
                                    # Assignation d'un 1 dans la matrice pour la coordonnee (case_x;case_y) pour indiquer que la case contient un CARRE
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 1
                                print(MATRICE_GRILLE)

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
                    for Y in range (L): #Pour X allant de 0 à la longueur d’une ligne de la matrice-1(= nombre de colonnes -1)
#BOUCLE EVENT.CLICDROIT.2 - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT et dans la BOUCLE EVENT.CLICDROIT.1
# Cette boucle parcourt la grille centrale en hauteur.
                        for X in range (H): #Pour Y allant de 0 au nombre de ligne de la matrice – 1 
#BOUCLE EVENT.CLICDROIT.3 - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT, BOUCLE EVENT.CLICDROIT.1 et BOUCLE EVENT.CLICDROIT.2.
# Cette boucle s'effectue SI ET SEULEMENT SI les compteurs (X,Y) sont équivalents aux coordonnées des cases (CASE_X,CASE_Y)
                            if X == CASE_X and Y == CASE_Y:

#BOUCLE EVENT.CLICDROIT.VIDE - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT, BOUCLE EVENT.CLICDROIT.1, BOUCLE EVENT.CLICDROIT.2, BOUCLE EVENT.CLICDROIT.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee [CASE_X;CASE_Y] est vide (0)
                                if MATRICE_GRILLE[CASE_X, CASE_Y] == 0: # comporte un 1 dans la matrice , c'est a dire si la case est vide
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 2 #on assigne 2 dans la matrice pour la coordonnée [CASE_X;CASE_Y]

#BOUCLE EVENT.CLICDROIT.CARRE - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT, BOUCLE EVENT.CLICDROIT.1, BOUCLE EVENT.CLICDROIT.2, BOUCLE EVENT.CLICDROIT.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee [CASE_X;CASE_Y] comporte un CARRE noir (1)
                                elif MATRICE_GRILLE[CASE_X, CASE_Y] == 1: # comporte un 1 dans la matrice , c'est a dire si la case est noire
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 2 # on assigne 2 dans la matrice pour la coordonnée [CASE_X;CASE_Y]

#BOUCLE EVENT.CLICDROIT.CROIX - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT, BOUCLE EVENT.CLICDROIT.1, BOUCLE EVENT.CLICDROIT.2, BOUCLE EVENT.CLICDROIT.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee (CASE_X;CASE_Y) comporte une CROIX noire (2)
                                elif MATRICE_GRILLE[CASE_X, CASE_Y] == 2: #comporte un 2 dans la matrice c'est a dire si la case est cochée
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 0 # on assigne 0 dans la matrice pour la coordonnée [CASE_X;CASE_Y]
                                print(MATRICE_GRILLE)

#-------------------------------------------------------------------------------
#                              INDEX - LISTE
#-------------------------------------------------------------------------------

# Cette boucle parcourt la grille centrale en longueur.
            GRILLE_GAUCHE = [] # défini la grille de gauche comme une liste
            for y in range (NBR_CARRE_CENTRAL):

#                print(GRILLE_GAUCHE)
                # initialise l'index de la grille gauche comme vide

                PRECEDENT = MATRICE_GRILLE[CASE_X-1, CASE_Y]  # défini PRECEDENT comme la case precedente a CASE_X
                PRECEDENT = 0 #intialise la variable PRECEDENT à 0 soit comme une case vide

# Cette boucle parcourt la grille centrale en hauteur.
                for x in range(NBR_CARRE_CENTRAL):
                    if MATRICE_GRILLE[CASE_X, CASE_Y] == 1 and PRECEDENT ==0: #si comporte un 1 dans la matrice ET si la case précédente est vide
                        GRILLE_GAUCHE.append(1) #si les conditions ci dessus sont respectées, on ajoute une valeure dans la liste

                    if MATRICE_GRILLE[CASE_X, CASE_Y] == 1 and PRECEDENT ==1: #si comporte un 1 dans la matrice ET si la case précédente est noire
                        GRILLE_GAUCHE[len(GRILLE_GAUCHE)-1]+= 1 #si on est dans le cas ci dessus, on ajoute 1 grace a la fonction len() à la valeure actuelle déjà présente

                    PRECEDENT= CASE_X #à chaque fois que la boucle se termine, on redéfini precedent comme la case_x qui va ensuite etre utilisé

                if GRILLE_GAUCHE == []: #si à la fin de la boucle, la liste est vide
                        #la fonction .append permet de créer une valeure dans une liste déjà existante, d'ajouter une valeure
                        GRILLE_GAUCHE.append(0) #on affiche un 0, qui correspond à une ligne sans case noire

                #la fonction .reverse() permet de renverser l'ordre des éléments d'une liste, pour que, dans la situation de notre picross, l'ordre des chiffre concorde avec la grille
                GRILLE_GAUCHE.reverse()
            print(GRILLE_GAUCHE)
            pygame.display.flip()

# Cette boucle parcourt la grille centrale en longueur.
            for x in range (NBR_CARRE_CENTRAL):
                GRILLE_HAUT = []
  #              print (GRILLE_HAUT)
                PRECEDENT = MATRICE_GRILLE[CASE_X, CASE_Y-1]  # défini PRECEDENT comme la case precedente a CASE_Y
                PRECEDENT = 0 #intialise la variable PRECEDENT à 0 soit comme une case vide

                for y in range(NBR_CARRE_CENTRAL):
                    if MATRICE_GRILLE[CASE_X, CASE_Y] == 1 and PRECEDENT ==0: #si comporte un 1 dans la matrice ET si la case précédente est vide
                        GRILLE_HAUT.append(1) #si les conditions ci dessus sont respectées, on ajoute une valeure dans la liste

                    if MATRICE_GRILLE[CASE_X, CASE_Y] == 1 and PRECEDENT ==1: #si comporte un 1 dans la matrice ET si la case précédente est noire
                        GRILLE_HAUT[len(GRILLE_HAUT)-1]+=1

                PRECEDENT= CASE_Y #à chaque fois que la boucle se termine, on redéfini precedent comme la case_y qui va ensuite etre utilisé

                if GRILLE_HAUT == []: # dans le cas ou la liste est vide
                    #la fonction .append permet de créer une valeure dans une liste déjà existante, d'ajouter une valeure
                    GRILLE_HAUT.append(0) #on ajoute une valeure pour ne pas garder une liste vide mais pour avoir une valeure

            #la fonction .reverse() permet de renverser l'ordre des éléments d'une liste, pour que, dans la situation de notre picross, l'ordre des chiffre concorde avec la grille
            GRILLE_HAUT.reverse()

            # Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
pygame.display.flip()



#Permet de fermet la fenetre sans bug (sans cela le programme ne repond plus
#lors de la fermeture de la fenetre)
pygame.quit()