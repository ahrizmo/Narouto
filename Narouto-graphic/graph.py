import pygame
import sys

# Initialiser Pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (169, 169, 169)
PINK = (255, 192, 203)
PURPLE = (128, 0, 128)


image_paths = ["images/Cartes/Akashi.png", "images/Cartes/Akashi1.png", "images/Cartes/Akashi2.png", "images/Cartes/Chinata.png",
               "images/Cartes/Hey.png", "images/Cartes/Fangs.png", "images/Cartes/GuyRaya.png", "images/Cartes/Tsounade.png"]

# Obtenir la taille de l'écran pour définir une fenêtre en plein écran
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

# Créer une fenêtre en plein écran
screen = pygame.display.set_mode((0,0),pygame.NOFRAME)
pygame.display.set_caption("Cartes")
print(screen_width, screen_height)
# Définir le titre de la fenêtre
pygame.display.set_caption("Plein écran avec une image")

# Charger l'image
#image = pygame.image.load("images/Cartes/Akashi.png")

images = [pygame.image.load(path) for path in image_paths]

zone_width = screen_width * 0.7
zone_height = screen_height * 0.4

zone_x = 0
zone_y = 917  # Zone dans le haut de l'écran

image_width = zone_width // 4
image_height = zone_height // 2

images = [pygame.transform.scale(image, (100, 150)) for image in images]

# Calculer l'espace entre les images (espacement horizontal et vertical)
spacing_x = (zone_width - image_width * 4) // 5  # Espacement horizontal
spacing_y = (zone_height - image_height * 2) // 3  # Espacement vertical
print(zone_height,image_height)
# Placer les images dans la zone
image_rects = []
for i in range(8):
    # Calculer la position de chaque image
    row = i // 4  # Ligne 0 ou 1
    col = i % 4  # Colonne 0 à 3

    # Positionner l'image
    x = zone_x + spacing_x + col * (image_width + spacing_x)
    y = zone_y + spacing_y + row * (image_height + spacing_y)
    print(x, y)
    # Créer un rectangle pour chaque image
    image_rect = pygame.Rect(x, y, image_width, image_height)
    image_rects.append(image_rect)

# Redimensionner l'image pour qu'elle s'adapte à l'écran
#image = pygame.transform.scale(image, (300, 450))

# Obtenir la position de l'image pour qu'elle couvre tout l'écran
#image_rect = image.get_rect()


# Créer une police pour le texte
font = pygame.font.SysFont('Arial', 36)

# Créer le texte
# Créer le texte en gris
text = font.render('Bonjour', True, GRAY)

# Créer le texte pour le contour en noir
text_contour = font.render('Bonjour', True, BLACK)

# Obtenir la position du texte pour le centrer
text_rect = text.get_rect(center=(300, 200))
text_contour_rect = text_contour.get_rect(center=(300, 200))

square_width = 5
square_height = 5

# Définir la position du carré (en haut à gauche, position 0,0)
square_position = (100, 0)

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche de la souris
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(f"Position du clic : ({mouse_x}, {mouse_y})")


    screen.fill(GRAY)
    # Afficher l'image
    for i, image in enumerate(images):
        screen.blit(image, image_rects[i])

    screen.blit(text, text_rect)

    pygame.draw.rect(screen, RED, pygame.Rect(square_position[0], square_position[1], square_width, square_height))


    screen.blit(text_contour, (text_contour_rect.x - 2, text_contour_rect.y - 2))
    screen.blit(text_contour, (text_contour_rect.x + 2, text_contour_rect.y - 2))
    screen.blit(text_contour, (text_contour_rect.x - 2, text_contour_rect.y + 2))
    screen.blit(text_contour, (text_contour_rect.x + 2, text_contour_rect.y + 2))

    # Afficher le texte en gris par-dessus
    screen.blit(text, text_rect)
    # Mettre à jour l'écran
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
