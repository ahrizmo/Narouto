import pygame


#Map

carte = pygame.image.load("../../CarteNarutoExemple.png")
carte.convert()

map = pygame.image.load("../../Map1.jpg")
map.convert()

parchemin = pygame.image.load("../../FondParchemin1.png")
parchemin.convert()
fondParchemin = pygame.transform.scale(parchemin, (400, 980))

fond = pygame.transform.scale(map, (1250, 980))


carteHeroN = pygame.image.load("../../HeroN1.png")
carteHeroN.convert()
carteHeroN_small = pygame.transform.scale(carteHeroN, (300, 300))

carteHeroS = pygame.image.load("../../HeroS1.png")
carteHeroS.convert()
carteHeroS_small = pygame.transform.scale(carteHeroS, (300, 300))