import pygame



pygame.init()


WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle Cliquable")


BLACK = (0, 0, 0)
RED = (200, 0, 0)


rect = pygame.Rect(200, 200, 100, 100)  # (x, y, largeur, hauteur)
is_red = False  # Booléen pour stocker l'état du rectangle


running = True
while running:
    screen.fill((255, 255, 255))  # Fond blanc


    pygame.draw.rect(screen, RED if is_red else BLACK, rect)

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):  # Vérifie si on clique sur le rectangle
                is_red = not is_red  # Inversion de la couleur

    pygame.display.flip()  # Mettre à jour l'affichage

pygame.quit()