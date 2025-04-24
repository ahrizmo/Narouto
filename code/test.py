import pygame

# Initialisation
pygame.init()

# Chargement de l'image
image = pygame.image.load("../imgTest.png")

# Création d'une surface de texte
font = pygame.font.SysFont("Permanent Marker", 36)  # Police par défaut, taille 36
texte = font.render("Bonjour !", True, (0, 0, 0))  # Texte rouge

# Dessin du texte SUR l'image
image.blit(texte, (550, 550))  # Coordonnées où le texte sera placé

# Affichage dans une fenêtre
fenetre = pygame.display.set_mode((image.get_width(), image.get_height()))
fenetre.blit(image, (0, 0))
pygame.display.flip()

# Attente pour voir le résultat
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
