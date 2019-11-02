# Créé par Fabien ( et Quentin ) le 21/03/2016 en Python 3.2
# création d'une grille de jeu picross de dimension 5x5
# corps du programme

# on importe le module pygame qui nous permet de créer l'interface graphique
import pygame
from pygame.locals import *

# on rattache le corps du programme aux annexes pour plus de clarté:
# les classes et les constantes du programme
from classes import *
from constantes import *

# initialisation du module pygame (étape nécessaire pour utiliser le module)
pygame.init()

# création d'une variable fenetre qui affiche la fenetre du jeu
fenetre = pygame.display.set_mode((longueur_fenetre, largeur_fenetre))

# Variable qui continue la boucle si = 1, stoppe si = 0
# cela permet de garder la fenetre ouverte
continuer = 1

#BOUCLE PRINCIPAL
"""while continuer: Boucle permettant de mettre en place un ecran d'accueil
	accueil = pygame.image.load(image_accueil).convert() # affichage de la page d'accueil ( fond à chercher et à inserer)
	fenetre.blit(accueil, (0,0))

	pygame.display.flip() #Rafraichissement de la fenetre (nécessaire pour afficher l'image)

	#On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu = 1
	continuer_accueil = 1"""

while continuer_accueil:
    for event in pygame.event.get():   #On parcourt la liste de tous les événements reçus
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = 0      #On arrête la boucle ce qui ferme la fenetre


    fond = pygame.image.load(image_fond_contour).convert()  #Chargement du fond blanc avec ses contours
                                    #Affichages du fond blanc aux nouvelles positions
    fenetre.blit(fond, (0,0))	#Rafraichissement de la fenetre (nécessaire pour afficher l'image)
    pygame.display.flip()

    #Génération d'un niveau à partir d'un fichier
	niveau = Grille("grille5x5.txt") #Gère la grille qui va etre la base du jeu
	niveau.generer()
	niveau.afficher(fenetre)
#NB : il faudra gérer "grille" dans les classe

    # Création des différentes variables concernant les différentes possibilités des cases, il faut au passage noter qu'il est indispensable de gérer Case dans les classes
    état_case = Case("images\case_vide.png","images\carre_noircie.png", "images\croix.png", "images\croix_rouge.png","images\case_rouge.png",)
    #permet au code d'aller chercher les images nécessaires dans la suite de celui ci



# permet de fermet la fenetre sans bug (sans cela le programme ne repond plus
# lors de la fermeture de la fenetre)
pygame.quit()
