#Cree par Fabien, Sinan et Quentin le 21/03/2016 en Python 3.2
#Création d'une grille de jeu picross de dimension 5x5
#Corps du programme

#On importe le module pygame qui nous permet de créer l'interface graphique et l'initialise
import pygame
from pygame.locals import *
pygame.init()

#On rattache le corps du programme aux annexes pour plus de clarté:
#Les fonctions et les constantes du programme
from constantes_tuto import *
from fonctions_tuto import *

#Creation d'une variable fenetre qui affiche la fenetre du jeu
FENETRE = pygame.display.set_mode((LONGUEUR_FENETRE, HAUTEUR_FENETRE))
#Titre de la fenetre
pygame.display.set_caption(TITRE_FENETRE)

#Variable qui continue la boucle si = 1, stoppe si = 0
#cela permet de garder la fenetre du menu ouverte
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
    FENETRE.blit(TITRE_TUTORIEL, (350, 30))
                    #- bouton tuto1
    FENETRE.blit(BOUTON_TUTO_1, (150, 190))
            #- bouton tuto2
    FENETRE.blit(BOUTON_TUTO_2, (150, 310))
            #- bouton tuto3
    FENETRE.blit(BOUTON_TUTO_3,(150, 430))
            #- bouton précédent
    FENETRE.blit(BOUTON_AVANT, (650, 575))
            #- bouton aprés
    FENETRE.blit(BOUTON_APRES, (725, 575))

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


#Permet de fermet la fenêtre sans bug (sans cela le programme ne répond plus
#lors de la fermeture de la fenêtre)
pygame.quit()




















