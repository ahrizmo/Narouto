import pygame

pygame.init()
clock = pygame.time.Clock()


WIDTH, HEIGHT = 1900, 1200 #Résolution écran

# Les couleurs -----------------------------------------------------------------------------------
blue_color = (0,0,250)
red_color = (250,0,0)
unselect_color = (2,209,195)
select_color = (240,9,181)
black_color = (0,0,0)

# Setup ----------------------------------------------------------------------------------------

screen = pygame.display.set_mode((0,0),pygame.NOFRAME)
running = True

from card_image import * #Chargement des cartes

from map_image import * #Chargement de la map








#from card_image import *


# Gestion des cases ----------------------------------------------------------------------------------

def mise_a_false(b1,b2,b3,b4,b5,b6,b7):
    return False, False, False, False, False, False, False

def deselect_all_upper():
    global TC1, TC2, TC3, TC4, TC5, TC6, TC7, TC8
    TC1 = TC2 = TC3 = TC4 = TC5 = TC6 = TC7 = TC8 = False

def deselect_all_lower():
    global TC11, TC12, TC13, TC14, TC15, TC16, TC17, TC18
    TC11 = TC12 = TC13 = TC14 = TC15 = TC16 = TC17 = TC18 = False

def attack_thrown():
    global upper_case_select, lower_case_select
    if upper_case_select and lower_case_select:
        deselect_all_lower(); deselect_all_upper()
        upper_case_select = lower_case_select = False


from create_case import *



# Lancement du jeu ----------------------------------------------------------------------------------------

while running :
    screen.blit(fond,[0,0])
    screen.blit(fondParchemin,[1230,0])
    screen.blit(carteHeroS_small,[0,0])   
    screen.blit(carteHeroN_small,[0,662])
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            click_x, click_y = pygame.mouse.get_pos()

            mouse_pos = event.pos
            # Vérifie si on clique sur une image


            #Test case haut
            if 410 <= click_x <= 590 and 50 <= click_y <= 200:
                TC1 = not TC1
                TC2,TC3,TC4,TC5,TC6,TC7,TC8 = mise_a_false(TC2,TC3,TC4,TC5,TC6,TC7,TC8)
                pygame.draw.rect(screen, select_color,rect1,5)
                upper_case_select = True

            elif 615 <= click_x <= 795 and 50 <= click_y <= 200:
                TC2 = not TC2
                TC1,TC3,TC4,TC5,TC6,TC7,TC8 = mise_a_false(TC1,TC3,TC4,TC5,TC6,TC7,TC8)
                pygame.draw.rect(screen, select_color,rect2,5)
                upper_case_select = True
            elif 825 <= click_x <= 1005 and 50 <= click_y <= 200:
                TC3 = not TC3
                TC1,TC2,TC4,TC5,TC6,TC7,TC8 = mise_a_false(TC1,TC2,TC4,TC5,TC6,TC7,TC8)
                pygame.draw.rect(screen, select_color,rect3,5)
                upper_case_select = True
            elif 1035 <= click_x <= 1215 and 50 <= click_y <= 200:
                TC4 = not TC4
                TC1,TC2,TC3,TC5,TC6,TC7,TC8 = mise_a_false(TC1,TC2,TC3,TC5,TC6,TC7,TC8)
                pygame.draw.rect(screen, select_color,rect4,5)
                upper_case_select = True
            elif 410 <= click_x <= 590 and 205 <= click_y <= 355:
                TC5 = not TC5
                TC1,TC2,TC4,TC3,TC6,TC7,TC8 = mise_a_false(TC1,TC2,TC4,TC3,TC6,TC7,TC8)
                pygame.draw.rect(screen, select_color,rect5,5)
                upper_case_select = True
            elif 615 <= click_x <= 795 and 205 <= click_y <= 355:
                TC6 = not TC6
                TC1,TC2,TC4,TC5,TC3,TC7,TC8 = mise_a_false(TC1,TC2,TC4,TC5,TC3,TC7,TC8)
                pygame.draw.rect(screen, select_color,rect6,5)
                upper_case_select = True
            elif 825 <= click_x <= 1005 and 205 <= click_y <= 355:
                TC7 = not TC7
                TC1,TC2,TC4,TC5,TC6,TC3,TC8 = mise_a_false(TC1,TC2,TC4,TC5,TC6,TC3,TC8)
                pygame.draw.rect(screen, select_color,rect7,5)
                upper_case_select = True
            elif 1035 <= click_x <= 1215 and 205 <= click_y <= 355:
                TC8 = not TC8
                TC1,TC2,TC4,TC5,TC6,TC7,TC3 = mise_a_false(TC1,TC2,TC4,TC5,TC6,TC7,TC3)
                pygame.draw.rect(screen, select_color,rect8,5)
                upper_case_select = True
            else:
                TC1=TC2=TC3=TC4=TC5=TC6=TC7=TC8 = False



            #Test case bas

            if 410 <= click_x <= 590 and 590 <= click_y <= 740:
                TC11 = not TC11
                TC12,TC13,TC14,TC15,TC16,TC17,TC18 = mise_a_false(TC12,TC13,TC14,TC15,TC16,TC17,TC18)
                pygame.draw.rect(screen, select_color, rect11, 5)
                lower_case_select = True
            elif 615 <= click_x <= 795 and 590 <= click_y <= 740:
                TC12 = not TC12
                TC11,TC13,TC14,TC15,TC16,TC17,TC18 = mise_a_false(TC11,TC13,TC14,TC15,TC16,TC17,TC18)
                pygame.draw.rect(screen, select_color, rect12, 5)
                lower_case_select = True
            elif 825 <= click_x <= 1005 and 590 <= click_y <= 740:
                TC13 = not TC13
                TC11,TC12,TC14,TC15,TC16,TC17,TC18 = mise_a_false(TC11,TC12,TC14,TC15,TC16,TC17,TC18)
                pygame.draw.rect(screen, select_color, rect13, 5)
                lower_case_select = True
            elif 1035 <= click_x <= 1215 and 590 <= click_y <= 740:
                TC14 = not TC14
                TC11,TC12,TC13,TC15,TC16,TC17,TC18 = mise_a_false(TC11,TC12,TC13,TC15,TC16,TC17,TC18)
                pygame.draw.rect(screen, select_color, rect14, 5)
                lower_case_select = True
            elif 410 <= click_x <= 590 and 750 <= click_y <= 900:
                TC15 = not TC15
                TC11,TC12,TC14,TC13,TC16,TC17,TC18 = mise_a_false(TC11,TC12,TC14,TC13,TC16,TC17,TC18)
                pygame.draw.rect(screen, select_color, rect15, 5)
                lower_case_select = True
            elif 615 <= click_x <= 795 and 750 <= click_y <= 900:
                TC16 = not TC16
                TC11,TC12,TC14,TC15,TC13,TC17,TC18 = mise_a_false(TC11,TC12,TC14,TC15,TC13,TC17,TC18)
                pygame.draw.rect(screen, select_color, rect16, 5)
                lower_case_select = True
            elif 825 <= click_x <= 1005 and 750 <= click_y <= 900:
                TC17 = not TC17
                TC11,TC12,TC14,TC15,TC16,TC13,TC18 = mise_a_false(TC11,TC12,TC14,TC15,TC16,TC13,TC18)
                pygame.draw.rect(screen, select_color, rect17, 5)
                lower_case_select = True
            elif 1035 <= click_x <= 1215 and 750 <= click_y <= 900:
                TC18 = not TC18
                TC11,TC12,TC14,TC15,TC16,TC17,TC13 = mise_a_false(TC11,TC12,TC14,TC15,TC16,TC17,TC13)
                pygame.draw.rect(screen, select_color, rect18, 5)
                lower_case_select = True
            else:
                TC11=TC12=TC13=TC14=TC15=TC16=TC17=TC18 = False

            attack_thrown()


        if pygame.mouse.get_pressed()[2]:  # bouton droit


                Mouse_hover_x, Mouse_hover_y = pygame.mouse.get_pos()

                if 410 <= Mouse_hover_x <= 600:
                    if 50 <= Mouse_hover_y <= 200:
                        screen.blit(carte, [500, 200])






   # Coord des cartes ----------------------------------------------------------------------------------------

    #Haut ----------------------------------

    screen.blit(cartes_small[0],[410,50])
    screen.blit(cartes_small[1],[620,50])
    screen.blit(cartes_small[2],[830,50])
    screen.blit(cartes_small[3],[1040,50])

    screen.blit(cartes_small[4],[410,210])
    screen.blit(cartes_small[5],[620,210])
    screen.blit(cartes_small[6],[830,210])
    screen.blit(cartes_small[7],[1040,210])
  
    

    #BAS ----------------------------------
  
    screen.blit(cartes_small[8],[410,590])
    screen.blit(cartes_small[9],[620,590])
    screen.blit(cartes_small[10],[830,590])
    screen.blit(cartes_small[11],[1040,590])

    screen.blit(cartes_small[12],[410,750])
    screen.blit(cartes_small[13],[620,750])
    screen.blit(cartes_small[14],[830,750])
    screen.blit(cartes_small[15],[1040,750])
    
    pygame.draw.rect(screen,select_color if TC1 else unselect_color,rect1,5, border_radius=14)
    pygame.draw.rect(screen,select_color if TC2 else unselect_color,rect2,5, border_radius=14)
    pygame.draw.rect(screen,select_color if TC3 else unselect_color,rect3,5, border_radius=14)
    pygame.draw.rect(screen,select_color if TC4 else unselect_color,rect4,5, border_radius=14)
    pygame.draw.rect(screen,select_color if TC5 else unselect_color,rect5,5, border_radius=14)
    pygame.draw.rect(screen,select_color if TC6 else unselect_color,rect6,5, border_radius=14)
    pygame.draw.rect(screen,select_color if TC7 else unselect_color,rect7,5, border_radius=14)
    pygame.draw.rect(screen,select_color if TC8 else unselect_color,rect8,5, border_radius=14)

    pygame.draw.rect(screen,select_color if TC11 else unselect_color,rect11,5, border_radius=14)
    pygame.draw.rect(screen,select_color if TC12 else unselect_color,rect12,5, border_radius=14)
    pygame.draw.rect(screen,select_color if TC13 else unselect_color,rect13,5, border_radius=14)
    pygame.draw.rect(screen,select_color if TC14 else unselect_color,rect14,5, border_radius=14)
    pygame.draw.rect(screen,select_color if TC15 else unselect_color,rect15,5, border_radius=14)
    pygame.draw.rect(screen,select_color if TC16 else unselect_color,rect16,5, border_radius=14)
    pygame.draw.rect(screen,select_color if TC17 else unselect_color,rect17,5, border_radius=14)
    pygame.draw.rect(screen,select_color if TC18 else unselect_color,rect18,5, border_radius=14)
    
  
   
    



    pygame.display.flip()
    clock.tick(60)


pygame.quit()


# matriceHaut=[
#     [-1,-1,-1,-1],
#     [-1,-1,-1,-1]
# ]

# matriceBas=[
#     [-1,-1,-1,-1],
#     [-1,-1,-1,-1]
# ]


