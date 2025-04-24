import pygame



#Liste  cartes
noms_cartes = [
    "Akashi", "Akashi1", "Akashi2", "Ashurama", "Ashurama1", "Asouma", "Chinata", "Fangs",
    "Gaarou", "Gaarou1", "GuayThai", "GuayThai1", "Guyraya", "Guyraya1", "Hey", "Hey1",
    "Hirouzen", "Hirouzen1", "Hydane", "Ineau", "Itashi", "Itashi1", "Itashi2", "Jeni",
    "Kayate", "King_B", "King_B1", "Kizame", "Kizame1", "Kourenai", "Madarame", "Madarame1",
    "Minamoto", "Minamoto1", "Misery", "Misery1", "Mizurama", "Mizurama1", "Narouto",
    "Narouto1", "Narouto3", "NineNine", "Onytaro", "PierreLee", "PierreLee1", "Sakoura",
    "Sasouke", "Sasouke1", "Sasouke2", "Shikakou", "Shikamarou", "Shin", "Shôji", "Tony",
    "Tsounade", "Tsounade1"
]


cartes = {}
cartes_small = {}
cpt = 0

# Chargement + mise à l’échelle

for nom in noms_cartes:
    chemin = f"../../CartesMinis/{nom}.png"
    carte_key = f"carte{nom}"

    carte = pygame.image.load(chemin).convert()
    carte_small_img = pygame.transform.scale(carte, (180, 150))  # Renommé ici

    cartes[cpt] = carte
    cartes_small[cpt] = carte_small_img
    cpt = cpt + 1









# # Chargement Images ----------------------------------------------------------------------------------------

# #HAUT

# carteNarouto = pygame.image.load("../CartesMinis/Narouto.png")
# carteNarouto.convert()

# carteAkashi2 = pygame.image.load("../CartesMinis/Akashi2.png")
# carteAkashi2.convert()

# carteMinamoto = pygame.image.load("../CartesMinis/Minamoto.png")
# carteMinamoto.convert()

# cartePierreLee = pygame.image.load("../CartesMinis/PierreLee.png")
# cartePierreLee.convert()

# carteSasouke = pygame.image.load("../CartesMinis/Sasouke.png")
# carteSasouke.convert()

# carteTony = pygame.image.load("../CartesMinis/Tony.png")
# carteTony.convert()

# carteGuyraya = pygame.image.load("../CartesMinis/Guyraya.png")
# carteGuyraya.convert()

# carteMadarame1 = pygame.image.load("../CartesMinis/Madarame1.png")
# carteMadarame1.convert()



# #BAS

# carteMizurama = pygame.image.load("../CartesMinis/Mizurama.png")
# carteMizurama.convert()

# carteKizame1 = pygame.image.load("../CartesMinis/Kizame1.png")
# carteKizame1.convert()

# carteJeni = pygame.image.load("../CartesMinis/Jeni.png")
# carteJeni.convert()

# carteSasouke1 = pygame.image.load("../CartesMinis/Sasouke1.png")
# carteSasouke1.convert()

# carteMisery = pygame.image.load("../CartesMinis/Misery.png")
# carteMisery.convert()

# carteGaarou1 = pygame.image.load("../CartesMinis/Gaarou1.png")
# carteGaarou1.convert()

# carteAshurama1 = pygame.image.load("../CartesMinis/Ashurama1.png")
# carteAshurama1.convert()

# carteNarouto3 = pygame.image.load("../CartesMinis/Narouto3.png")
# carteNarouto3.convert()


# #Mise à l'echelle

# narouto_small = pygame.transform.scale(carteNarouto, (180, 150))
# akashi2_small = pygame.transform.scale(carteAkashi2, (180, 150))
# minamoto_small = pygame.transform.scale(carteMinamoto, (180, 150))
# pierreLee_small = pygame.transform.scale(cartePierreLee, (180, 150))
# sasouke_small = pygame.transform.scale(carteSasouke, (180, 150))
# tony_small = pygame.transform.scale(carteTony, (180, 150))
# guyraya_small = pygame.transform.scale(carteGuyraya, (180, 150))
# madarame1_small = pygame.transform.scale(carteMadarame1, (180, 150))


# mizurama_small = pygame.transform.scale(carteMizurama, (180, 150))
# kizame1_small = pygame.transform.scale(carteKizame1, (180, 150))
# jeni_small = pygame.transform.scale(carteJeni, (180, 150))
# sasouke1_small = pygame.transform.scale(carteSasouke1, (180, 150))
# misery_small = pygame.transform.scale(carteMisery, (180, 150))
# gaarou1_small = pygame.transform.scale(carteGaarou1, (180, 150))
# ashurama1_small = pygame.transform.scale(carteAshurama1, (180, 150))
# narouto3_small = pygame.transform.scale(carteNarouto3, (180, 150))