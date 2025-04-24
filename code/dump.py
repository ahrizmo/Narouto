# === IMPORTS ===
import pygame
from create_case import * # Les rectangles rect1 à rect18
from card import Card

# === CONSTANTES ===
WIDTH, HEIGHT = 1900, 1200
blue_color = (0, 0, 250)
red_color = (250, 0, 0)
unselect_color = (2, 209, 195)
select_color = (240, 9, 181)
black_color = (0, 0, 0)

tab_coord = [
    (410, 50),
    (620, 50),
    (830, 50),
    (1040, 50),

    (410, 210),
    (620, 210),
    (830, 210),
    (1040, 210),

    (410, 590),
    (620, 590),
    (830, 590),
    (1040, 590),

    (410, 750),
    (620, 750),
    (830, 750),
    (1040, 750)
]

tab_coord_main = [
    (1305,95),
    (1305,265),
    (1305,435),
    (1305,605),
    (1305,775)
]


# === FONCTIONS ===



def mise_a_false():
    return (False,) * 7

def deselect_all_upper():
    global  case1, case2, case3, case4, case5, case6, case7, case8
    case1.click = case2.click = case3.click = case4.click = case5.click = case6.click = case7.click = case8.click = False
    

def deselect_all_lower():
    global  case11, case12, case13, case14, case15, case16, case17, case18
    case11.click = case12.click = case13.click = case14.click = case15.click = case16.click = case17.click = case18.click = False

def deselect_hand():
    global case1_main, case2_main, case3_main, case4_main, case5_main
    case1_main.click = case2_main.click = case3_main.click = case4_main.click = case5_main.click = False


# Permet de mettre une carte en jeu
def get_img_path(card_id,case_id):
    noms_cartes = [
    "Akashi", "Akashi1", "Akashi2", "Ashurama", "Ashurama1", "Asouma", "Chinata", "Fangs",
    "Gaarou", "Gaarou1", "GuayThai", "GuayThai1", "Guyraya", "Guyraya1", "Hey", "Hey1",
    "Hirouzen", "Hirouzen1", "Hydane", "Ineau", "Itashi", "Itashi1", "Itashi2", "Jeni",
    "Kayate", "King_B", "King_B1", "Kizame", "Kizame1", "Kourenai", "Madarame", "Madarame1",
    "Minamoto", "Minamoto1", "Misery", "Misery1", "Mizurama", "Mizurama1", "Narouto",
    "Narouto1", "Narouto2", "NineNine", "Onytaro", "PierreLee", "PierreLee1", "Sakoura",
    "Sasouke", "Sasouke1", "Sasouke2", "Shikakou", "Shikamarou", "Shin", "Shôji", "Tony",
    "Tsounade", "Tsounade1"
    ]

    chemin = f"../CartesMinis/{noms_cartes[card_id]}.png"
    carte_small_img = pygame.image.load(chemin).convert_alpha()

    chemin1 = f"../Cartes/{noms_cartes[card_id]}.png"
    carte1 = pygame.image.load(chemin1).convert_alpha()
    carte1 = pygame.transform.scale(carte1, (400, 550))

    if case_id == 1:
        case1_main.carte_posee = None
        cartes_main[0] = None
        cartes_main_small[0] = None
    elif case_id == 2:
        case2_main.carte_posee = None
        cartes_main[1] = None
        cartes_main_small[1] = None
    elif case_id == 3:
        case3_main.carte_posee = None
        cartes_main[2] = None
        cartes_main_small[2] = None
    elif case_id == 4:
        case4_main.carte_posee = None
        cartes_main[3] = None
        cartes_main_small[3] = None
    else:
        case5_main.carte_posee = None
        cartes_main[4] = None
        cartes_main_small[4] = None


    for i in range(5):
        if main_Narouto[i] == card_id:
            main_Narouto[i] = None
            cartes_main[i] = None        
            

    return carte1, carte_small_img


# Simulation visuelle de l'attaque
def attack_thrown():
    global upper_case_select, lower_case_select
    if upper_case_select and lower_case_select:
        deselect_all_lower()
        deselect_all_upper()
        upper_case_select = lower_case_select = False

def load_card():
    global cartes, cartes_small, cartes_main,cartes_main_small,cartes_Sasouke, cartes_Narouto, main_Narouto, main_Sasouke
    global  case1, case2, case3, case4, case5, case6, case7, case8
    global  case11, case12, case13, case14, case15, case16, case17, case18
    global  case1_main, case2, case3, case4, case5, case6, case7, case8
    global  case11, case12, case13, case14, case15

    tab_Sasouke = [case1, case2, case3, case4, case5, case6, case7, case8]
    tab_Narouto = [case11, case12, case13, case14, case15, case16, case17, case18]
    tab_main_Sasouke = [case1_main,case2_main,case3_main,case4_main,case5_main]
    tab_main_Narouto = [case1_main,case2_main,case3_main,case4_main,case5_main]
    noms_cartes = [
    "Akashi", "Akashi1", "Akashi2", "Ashurama", "Ashurama1", "Asouma", "Chinata", "Fangs",
    "Gaarou", "Gaarou1", "GuayThai", "GuayThai1", "Guyraya", "Guyraya1", "Hey", "Hey1",
    "Hirouzen", "Hirouzen1", "Hydane", "Ineau", "Itashi", "Itashi1", "Itashi2", "Jeni",
    "Kayate", "King_B", "King_B1", "Kizame", "Kizame1", "Kourenai", "Madarame", "Madarame1",
    "Minamoto", "Minamoto1", "Misery", "Misery1", "Mizurama", "Mizurama1", "Narouto",
    "Narouto1", "Narouto2", "NineNine", "Onytaro", "PierreLee", "PierreLee1", "Sakoura",
    "Sasouke", "Sasouke1", "Sasouke2", "Shikakou", "Shikamarou", "Shin", "Shôji", "Tony",
    "Tsounade", "Tsounade1"
    ]

    
    

    cg_Narouto = Card("Narouto", "Combattant", [2],[0],"Vent",5)

    for i in range(8):
        j = cartes_Sasouke[i//4][i%4]
        if j != None:
            font = pygame.font.SysFont("Permanent Marker", 30) 
            attack = font.render("10", True, (0, 0, 0))
            pv = font.render(f"{cg_Narouto.PV}", True, (0, 0, 0))
            chakra = font.render("10", True, (0, 0, 0))
            chemin = f"../CartesMinis/{noms_cartes[j]}.png"
            carte_small_img = pygame.image.load(chemin).convert_alpha()
            tab_Sasouke[i].carte_posee = j
        

            chemin1 = f"../Cartes/{noms_cartes[j]}.png"
            carte1 = pygame.image.load(chemin1).convert_alpha()
            carte1 = pygame.transform.scale(carte1, (400, 550))

            cartes.append(carte1)
            cartes_small.append(carte_small_img)


            # Ecriture sur la carte

            carte_small_img.blit(attack, (12, 8))
            carte_small_img.blit(pv, (150,130))
            carte_small_img.blit(chakra, (0, 130))

            carte1.blit(attack, (45, 25))
            carte1.blit(pv, (360,505))
            carte1.blit(chakra, (10, 530))
        else:
            cartes.append(None)
            cartes_small.append(None)



        
    
    for i in range(8):
        j = cartes_Narouto[i//4][i%4]
        if j != None:
            chemin = f"../CartesMinis/{noms_cartes[j]}.png"
            carte_small_img = pygame.image.load(chemin).convert_alpha()
            tab_Narouto[i].carte_posee = j

            chemin1 = f"../Cartes/{noms_cartes[j]}.png"
            carte1 = pygame.image.load(chemin1).convert_alpha()
            cartes.append(carte1)
            cartes_small.append(carte_small_img)


            carte_small_img.blit(attack, (12, 8))
            carte_small_img.blit(pv, (150,130))
            carte_small_img.blit(chakra, (0, 130))

            carte1.blit(attack, (45, 25))
            carte1.blit(pv, (360,505))
            carte1.blit(chakra, (10, 530))
        else:
            cartes.append(None)
            cartes_small.append(None)


    # Cartes en main

    for i in range(5):
        j = main_Narouto[i]
        if j != None:

            font = pygame.font.SysFont("Permanent Marker", 30) 
            attack = font.render("10", True, (0, 0, 0))
            pv = font.render("10", True, (0, 0, 0))
            chakra = font.render("10", True, (0, 0, 0))

            chemin = f"../CartesMinis/{noms_cartes[j]}.png"
            carte_small_img = pygame.image.load(chemin).convert_alpha()
            tab_main_Narouto[i].carte_posee = j
            cartes_main_small.append(carte_small_img)

            chemin1 = f"../Cartes/{noms_cartes[j]}.png"
            carte1 = pygame.image.load(chemin1).convert_alpha()
            cartes_main.append(carte1)

            carte_small_img.blit(attack, (12, 8))
            carte_small_img.blit(pv, (150,130))
            carte_small_img.blit(chakra, (0, 130))

            carte1.blit(attack, (45, 25))
            carte1.blit(pv, (360,505))
            carte1.blit(chakra, (10, 530))

        else:
            cartes_main_small.append(None)
            cartes_main.append(None)

            


    
    
    


def load_map():
    # Creation du fond ===============================================
    carte = pygame.image.load("../CarteNarutoExemple.png")
    carte.convert_alpha()

    map = pygame.image.load("../Map1.jpg")
    map.convert_alpha()

    parchemin = pygame.image.load("../FondParchemin1.png")
    parchemin.convert_alpha()
    fondParchemin = pygame.transform.scale(parchemin, (400, 980))

    fond = pygame.transform.scale(map, (1250, 980))

    
    # Font pv/chakra
    font = pygame.font.SysFont("Permanent Marker", 50)

    deck_font = pygame.font.SysFont("Permanent Marker", 30)

    deck = deck_font.render("DECK", True, (0,0,0))
    number = font.render("20", True, (0,0,0))

    # Pioche/ Skip

    skip = pygame.image.load("../Skip.png").convert_alpha()
    skip = pygame.transform.scale(skip,(287,40))




    pioche =pygame.image.load("../PileCarte.png").convert_alpha()
    pioche = pygame.transform.scale(pioche,(100,120))
    pioche.blit(deck, (25,13))
    pioche.blit(number, (33,80))
    


    # Héros Naruto ===================================================
    carteHeroN = pygame.image.load("../HeroN1.png")
    carteHeroN.convert_alpha()
    carteHeroN_small = pygame.transform.scale(carteHeroN, (300, 300))

    pv_narouto = font.render("20", True, (0, 227, 47))
    chakra_narouto = font.render("10", True, (232, 120, 20))

    carteHeroN_small.blit(pv_narouto, (220,260))
    carteHeroN_small.blit(chakra_narouto, (10,260))

    #  Héros Sasouke =================================================

    carteHeroS = pygame.image.load("../HeroS1.png")
    carteHeroS.convert_alpha()
    carteHeroS_small = pygame.transform.scale(carteHeroS, (300, 300))

    pv_sasouke = font.render("20", True, (0, 227, 47))
    chakra_sasouke = font.render("10", True, (81, 14, 135))

    carteHeroS_small.blit(pv_sasouke, (220,260))
    carteHeroS_small.blit(chakra_sasouke, (10,260))


    return fond,fondParchemin,carteHeroN_small,carteHeroS_small,pioche, skip





# === FONCTION PRINCIPALE DU JEU ===
def afficher_jeu():
    global cartes_Sasouke, cartes_Narouto
    pygame.init()

    # Déclaration des états de sélection
    global  case1, case2, case3, case4, case5, case6, case7, case8
    global  case11, case12, case13, case14, case15, case16, case17, case18
    global upper_case_select, lower_case_select, hand_case_select
    upper_case_select = lower_case_select = hand_case_select = False
    card_hand_selected = case_hand_selected = None

    

    # Configuration de la fenêtre
    WIDTH, HEIGHT = 1900, 1200 #Résolution écran
    screen = pygame.display.set_mode([WIDTH, HEIGHT],pygame.FULLSCREEN)

    
    fond,fondParchemin,carteHeroN_small,carteHeroS_small, pioche, skip = load_map()
    load_card()
    


    running = True

    while running:
        # --- AFFICHAGE DE BASE ---
        screen.blit(fond, (0, 0))
        screen.blit(fondParchemin, (1230, 0))
        screen.blit(carteHeroS_small, (0, 0))
        screen.blit(carteHeroN_small, (0, 662))
        screen.blit(pioche,(230,770)) # Coord Narouto
        # screen.blit(pioche,(260,100)) # Coord Sasouke
        screen.blit(skip, (0,588)) # Coord Narouto
        # screen.blit(skip, (0,325)) # Coord Sasouke

        # --- SORTIE PAR CLAVIER ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        # --- GESTION DES ÉVÉNEMENTS SOURIS ---
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                click_x, click_y = pygame.mouse.get_pos()

                #Test case haut
                if 410 <= click_x <= 590 and 50 <= click_y <= 200:
                    if case1.carte_posee != None:
                        case1.click = not case1.click
                        pygame.draw.rect(screen, select_color,case1.rect,5)
                        upper_case_select = True
                        hand_case_select = False
                    elif hand_case_select:
                        case1.carte_posee = card_hand_selected
                        cartes[0], cartes_small[0] = get_img_path(card_hand_selected,case_hand_selected)
                    case2.click,case3.click,case4.click,case5.click,case6.click,case7.click,case8.click = mise_a_false()
                elif 615 <= click_x <= 795 and 50 <= click_y <= 200:
                    if case2.carte_posee != None:
                        case2.click = not case2.click
                        case1.click,case3.click,case4.click,case5.click,case6.click,case7.click,case8.click = mise_a_false()
                        pygame.draw.rect(screen, select_color,case2.rect,5)
                        upper_case_select = True
                        hand_case_select = False
                    elif hand_case_select:
                        case2.carte_posee = card_hand_selected
                        cartes[1], cartes_small[1] = get_img_path(card_hand_selected,case_hand_selected)
                    case1.click,case3.click,case4.click,case5.click,case6.click,case7.click,case8.click = mise_a_false()

                elif 825 <= click_x <= 1005 and 50 <= click_y <= 200:
                    if case3.carte_posee != None:
                        case3.click = not case3.click
                        pygame.draw.rect(screen, select_color,case3.rect,5)
                        upper_case_select = True
                        hand_case_select = False
                    elif hand_case_select:
                        case3.carte_posee = card_hand_selected
                        cartes[2], cartes_small[2] = get_img_path(card_hand_selected,case_hand_selected)
                    case2.click,case1.click,case4.click,case5.click,case6.click,case7.click,case8.click = mise_a_false()

                elif 1035 <= click_x <= 1215 and 50 <= click_y <= 200:
                    if case4.carte_posee != None:
                        case4.click = not case4.click
                        pygame.draw.rect(screen, select_color,case4.rect,5)
                        upper_case_select = True
                        hand_case_select = False
                    elif hand_case_select:
                        case4.carte_posee = card_hand_selected
                        cartes[3], cartes_small[3] = get_img_path(card_hand_selected,case_hand_selected)
                    case2.click,case3.click,case1.click,case5.click,case6.click,case7.click,case8.click = mise_a_false()

                elif 410 <= click_x <= 590 and 205 <= click_y <= 355:
                    if case5.carte_posee != None:
                        case5.click = not case5.click
                        pygame.draw.rect(screen, select_color,case5.rect,5)
                        upper_case_select = True
                        hand_case_select = False
                    elif hand_case_select:
                        case5.carte_posee = card_hand_selected
                        cartes[4], cartes_small[4] = get_img_path(card_hand_selected,case_hand_selected)
                    case2.click,case3.click,case4.click,case1.click,case6.click,case7.click,case8.click = mise_a_false()               
                elif 615 <= click_x <= 795 and 205 <= click_y <= 355:
                    if case6.carte_posee != None:
                        case6.click = not case6.click
                        pygame.draw.rect(screen, select_color,case6.rect,5)
                        upper_case_select = True
                        hand_case_select = False
                    elif hand_case_select:
                        case6.carte_posee = card_hand_selected
                        cartes[5], cartes_small[5] = get_img_path(card_hand_selected,case_hand_selected)
                    case2.click,case3.click,case4.click,case5.click,case1.click,case7.click,case8.click = mise_a_false()
                elif 825 <= click_x <= 1005 and 205 <= click_y <= 355:
                    if case7.carte_posee != None:
                        case7.click = not case7.click
                        pygame.draw.rect(screen, select_color,case7.rect,5)
                        upper_case_select = True
                        hand_case_select = False
                    elif hand_case_select:
                        case7.carte_posee = card_hand_selected
                        cartes[6], cartes_small[6] = get_img_path(card_hand_selected,case_hand_selected)
                    case2.click,case3.click,case4.click,case5.click,case6.click,case1.click,case8.click = mise_a_false()
                elif 1035 <= click_x <= 1215 and 205 <= click_y <= 355:
                    if case8.carte_posee != None:
                        case8.click = not case8.click
                        pygame.draw.rect(screen, select_color,case8.rect,5)
                        upper_case_select = True
                        hand_case_select = False
                    elif hand_case_select:
                        case8.carte_posee = card_hand_selected
                        cartes[7], cartes_small[7] = get_img_path(card_hand_selected,case_hand_selected)
                    case2.click,case3.click,case4.click,case5.click,case6.click,case7.click,case1.click = mise_a_false()                
                else:
                    deselect_all_upper()
                    
                     

                #Test case bas

                if 410 <= click_x <= 590 and 590 <= click_y <= 740:
                    if case11.carte_posee != None:
                        case11.click = not case11.click
                        pygame.draw.rect(screen, select_color, case11.rect, 5)
                        lower_case_select = True
                        hand_case_select = False
                    elif hand_case_select:
                        case11.carte_posee = card_hand_selected
                        cartes[8], cartes_small[8] = get_img_path(card_hand_selected,case_hand_selected)
                    case12.click,case13.click,case14.click,case15.click,case16.click,case17.click,case18.click = mise_a_false()
                elif 615 <= click_x <= 795 and 590 <= click_y <= 740:
                    if case12.carte_posee != None:
                        case12.click = not case12.click
                        pygame.draw.rect(screen, select_color, case12.rect, 5)
                        lower_case_select = True
                        hand_case_select = False
                    elif hand_case_select:
                        case12.carte_posee = card_hand_selected
                        cartes[9], cartes_small[9] = get_img_path(card_hand_selected,case_hand_selected)
                    case11.click,case13.click,case14.click,case15.click,case16.click,case17.click,case18.click = mise_a_false()
                elif 825 <= click_x <= 1005 and 590 <= click_y <= 740:
                    if case13.carte_posee != None:
                        case13.click = not case13.click
                        pygame.draw.rect(screen, select_color, case13.rect, 5)
                        lower_case_select = True
                        hand_case_select = False
                    elif hand_case_select:
                        case13.carte_posee = card_hand_selected
                        cartes[10], cartes_small[10] = get_img_path(card_hand_selected,case_hand_selected)
                    case11.click,case12.click,case14.click,case15.click,case16.click,case17.click,case18.click = mise_a_false()
                elif 1035 <= click_x <= 1215 and 590 <= click_y <= 740:
                    if case14.carte_posee != None:
                        case14.click = not case14.click
                        pygame.draw.rect(screen, select_color, case14.rect, 5)
                        lower_case_select = True
                        hand_case_select = False
                    elif hand_case_select:
                        case14.carte_posee = card_hand_selected
                        cartes[11], cartes_small[11] = get_img_path(card_hand_selected,case_hand_selected)
                    case11.click,case12.click,case13.click,case15.click,case16.click,case17.click,case18.click = mise_a_false()
                elif 410 <= click_x <= 590 and 750 <= click_y <= 900:
                    if case15.carte_posee != None:
                        case15.click = not case15.click
                        pygame.draw.rect(screen, select_color, case15.rect, 5)
                        lower_case_select = True
                        hand_case_select = False
                    elif hand_case_select:
                        case15.carte_posee = card_hand_selected
                        cartes[12], cartes_small[12] = get_img_path(card_hand_selected,case_hand_selected)
                    case11.click,case12.click,case13.click,case14.click,case16.click,case17.click,case18.click = mise_a_false()
                elif 615 <= click_x <= 795 and 750 <= click_y <= 900:
                    if case16.carte_posee != None:
                        case16.click = not case16.click
                        pygame.draw.rect(screen, select_color, case16.rect, 5)
                        lower_case_select = True
                        hand_case_select = False
                    elif hand_case_select:
                        case16.carte_posee = card_hand_selected
                        cartes[13], cartes_small[13] = get_img_path(card_hand_selected,case_hand_selected)
                    case11.click,case12.click,case13.click,case14.click,case15.click,case17.click,case18.click = mise_a_false()
                elif 825 <= click_x <= 1005 and 750 <= click_y <= 900:
                    if case17.carte_posee != None:
                        case17.click = not case17.click
                        pygame.draw.rect(screen, select_color, case17.rect, 5)
                        lower_case_select = True
                        hand_case_select = False
                    elif hand_case_select:
                        case17.carte_posee = card_hand_selected
                        cartes[14], cartes_small[14] = get_img_path(card_hand_selected,case_hand_selected)
                    case11.click,case12.click,case13.click,case14.click,case15.click,case16.click,case18.click = mise_a_false()
                elif 1035 <= click_x <= 1215 and 750 <= click_y <= 900:
                    if case18.carte_posee != None:
                        case18.click = not case18.click
                        pygame.draw.rect(screen, select_color, case18.rect, 5)
                        lower_case_select = True
                        hand_case_select = False
                    elif hand_case_select:
                        case18.carte_posee = card_hand_selected
                        cartes[15], cartes_small[15] = get_img_path(card_hand_selected,case_hand_selected)
                    case11.click,case12.click,case13.click,case14.click,case15.click,case16.click,case17.click = mise_a_false()
                else:
                    deselect_all_lower()
                    

                # Test cases mains

                if 1305 <= click_x <= 1495 and 95 <= click_y <= 255:
                    if case1_main.carte_posee != None:
                        case1_main.click = not case1_main.click
                        pygame.draw.rect(screen, select_color, case1_main.rect, 5)
                        hand_case_select = True
                        card_hand_selected = case1_main.carte_posee
                        case_hand_selected = 1
                    case2_main.click = case3_main.click = case4_main.click = case5_main.click = False
                elif 1305 <= click_x <= 1495 and 265 <= click_y <= 425:
                    if case2_main.carte_posee != None:
                        case2_main.click = not case2_main.click
                        pygame.draw.rect(screen, select_color, case2_main.rect, 5)
                        hand_case_select = True
                        card_hand_selected = case2_main.carte_posee
                        case_hand_selected = 2
                    case1_main.click = case3_main.click = case4_main.click = case5_main.click = False    
                elif 1305 <= click_x <= 1495 and 435 <= click_y <= 595:
                    if case3_main.carte_posee != None:
                        case3_main.click = not case3_main.click
                        pygame.draw.rect(screen, select_color, case3_main.rect, 5)
                        hand_case_select = True
                        card_hand_selected = case3_main.carte_posee
                        case_hand_selected = 3
                    case1_main.click = case2_main.click = case4_main.click = case5_main.click = False
                elif 1305 <= click_x <= 1495 and 605 <= click_y <= 765:
                    if case4_main.carte_posee != None:
                        case4_main.click = not case4_main.click
                        pygame.draw.rect(screen, select_color, case4_main.rect, 5)
                        hand_case_select = True
                        card_hand_selected = case4_main.carte_posee
                        case_hand_selected = 4
                    case1_main.click = case2_main.click = case3_main.click = case5_main.click = False
                elif 1305 <= click_x <= 1495 and 775 <= click_y <= 935:
                    if case5_main.carte_posee != None:
                        case5_main.click = not case5_main.click
                        pygame.draw.rect(screen, select_color, case5_main.rect, 5)
                        hand_case_select = True
                        card_hand_selected = case5_main.carte_posee
                        case_hand_selected = 5
                    case1_main.click = case2_main.click = case3_main.click = case4_main.click = False
                else :
                    deselect_hand()
                    hand_case_select = False
                    card_hand_selected = None
                    case_hand_selected = None


                    
                attack_thrown()

        # --- AFFICHAGE DES Cases ---
        pygame.draw.rect(screen, select_color if case1.click else unselect_color, case1.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case2.click else unselect_color, case2.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case3.click else unselect_color, case3.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case4.click else unselect_color, case4.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case5.click else unselect_color, case5.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case6.click else unselect_color, case6.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case7.click else unselect_color, case7.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case8.click else unselect_color, case8.rect, 5, border_radius=14)

        pygame.draw.rect(screen, select_color if case11.click else unselect_color, case11.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case12.click else unselect_color, case12.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case13.click else unselect_color, case13.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case14.click else unselect_color, case14.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case15.click else unselect_color, case15.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case16.click else unselect_color, case16.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case17.click else unselect_color, case17.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case18.click else unselect_color, case18.rect, 5, border_radius=14)


        #  Cases main du joueur

        pygame.draw.rect(screen, select_color if case1_main.click else unselect_color, case1_main.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case2_main.click else unselect_color, case2_main.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case3_main.click else unselect_color, case3_main.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case4_main.click else unselect_color, case4_main.rect, 5, border_radius=14)
        pygame.draw.rect(screen, select_color if case5_main.click else unselect_color, case5_main.rect, 5, border_radius=14)
        
        
        
        
        
        
        
        # Coord des cartes ---------------------------------------------------------------------------------------- 


        for i in range(16):
            if cartes_small[i] is not None:
                screen.blit(cartes_small[i],tab_coord[i])

        for i in range(5):
            if cartes_main_small[i] is not None:
                screen.blit(cartes_main_small[i],tab_coord_main[i])
        

        # Affichage carte en grand =========================================

        Mouse_hover_x,Mouse_hover_y = pygame.mouse.get_pos()
        if 410 <= Mouse_hover_x <= 590 and 50 <= Mouse_hover_y <= 200:
            if case1.carte_posee is not None:
                screen.blit(cartes[0], [0, 200])
        elif 615 <= Mouse_hover_x <= 795 and 50 <= Mouse_hover_y <= 200:
            if case2.carte_posee is not None:
                screen.blit(cartes[1], [0, 200])
        elif 825 <= Mouse_hover_x <= 1005 and 50 <= Mouse_hover_y <= 200:
            if case3.carte_posee is not None:
                screen.blit(cartes[2], [0, 200])
        elif 1035 <= Mouse_hover_x <= 1215 and 50 <= Mouse_hover_y <= 200:
            if case4.carte_posee is not None:
                screen.blit(cartes[3], [0, 200])
        elif 410 <= Mouse_hover_x <= 590 and 205 <= Mouse_hover_y <= 355:
            if case5.carte_posee is not None:
                screen.blit(cartes[4], [0, 200])
        elif 615 <= Mouse_hover_x <= 795 and 205 <= Mouse_hover_y <= 355:
            if case6.carte_posee is not None:
                screen.blit(cartes[5], [0, 200])
        elif 825 <= Mouse_hover_x <= 1005 and 205 <= Mouse_hover_y <= 355:
            if case7.carte_posee is not None:
                screen.blit(cartes[6], [0, 200])
        elif 1035 <= Mouse_hover_x <= 1215 and 205 <= Mouse_hover_y <= 355:
            if case8.carte_posee is not None:
                screen.blit(cartes[7], [0, 200])
        elif 410 <= Mouse_hover_x <= 590 and 590 <= Mouse_hover_y <= 740:
            if case11.carte_posee is not None:
                screen.blit(cartes[8], [0, 200])
        elif 615 <= Mouse_hover_x <= 795 and 590 <= Mouse_hover_y <= 740:
            if case12.carte_posee is not None:
                screen.blit(cartes[9], [0, 200])
        elif 825 <= Mouse_hover_x <= 1005 and 590 <= Mouse_hover_y <= 740:
            if case13.carte_posee is not None:
                screen.blit(cartes[10], [0, 200])
        elif 1035 <= Mouse_hover_x <= 1215 and 590 <= Mouse_hover_y <= 740:
            if case14.carte_posee is not None:
                screen.blit(cartes[11], [0, 200])
        elif 410 <= Mouse_hover_x <= 590 and 750 <= Mouse_hover_y <= 900:
            if case15.carte_posee is not None:
                screen.blit(cartes[12], [0, 200])
        elif 615 <= Mouse_hover_x <= 795 and 750 <= Mouse_hover_y <= 900:
            if case16.carte_posee is not None:
                screen.blit(cartes[13], [0, 200])
        elif 825 <= Mouse_hover_x <= 1005 and 750 <= Mouse_hover_y <= 900:
            if case17.carte_posee is not None:
                screen.blit(cartes[14], [0, 200])
        elif 1035 <= Mouse_hover_x <= 1215 and 750 <= Mouse_hover_y <= 900:
            if case18.carte_posee is not None:
                screen.blit(cartes[15], [0, 200])

        # Carte en main   

        elif 1300 <= Mouse_hover_x <= 1490 and 90 <= Mouse_hover_y <= 250:
            if case1_main.carte_posee is not None:
                screen.blit(cartes_main[0], [0, 200])
        elif 1300 <= Mouse_hover_x <= 1490 and 260 <= Mouse_hover_y <= 420:
            if case2_main.carte_posee is not None:
                screen.blit(cartes_main[1], [0, 200])
        elif 1300 <= Mouse_hover_x <= 1490 and 430 <= Mouse_hover_y <= 590:
            if case3_main.carte_posee is not None:
                screen.blit(cartes_main[2], [0, 200])
        elif 1300 <= Mouse_hover_x <= 1490 and 600 <= Mouse_hover_y <= 760:
            if case4_main.carte_posee is not None:
                screen.blit(cartes_main[3], [0, 200])
        elif 1300 <= Mouse_hover_x <= 1490 and 770 <= Mouse_hover_y <= 930:
            if case5_main.carte_posee is not None:
                screen.blit(cartes_main[4], [0, 200])
                


        pygame.display.flip()

    pygame.quit()



cartes_Sasouke = [
    [5,23,None,14],
    [1,None,50,53]
]
# cartes_Narouto = [
#     [55,45,16,44],
#     [9,0,2,28]
# ]

cartes_Narouto = [
    [None,None,None,None],
    [None,None,None,None]
]

main_Sasouke = [None,None,None,None,None]
main_Narouto = [21,None,43,35,42]

cartes = []
cartes_small = []
cartes_main = []
cartes_main_small = []

afficher_jeu()
