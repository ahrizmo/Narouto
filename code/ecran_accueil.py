import pygame
import time

orange_color = (255,128,0)
black_color = (0,0,0)
dark_blue_color = (9,61,124)
WIDTH, HEIGHT = 1900,1200

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("musiques/lancement.mp3")
titre = pygame.image.load("../titre.png")
sasouke = pygame.image.load("../HeroS.png")
narouto = pygame.image.load("../HeroN.png")
logo = pygame.image.load("../LogoJeu.png")

titre = pygame.transform.scale(titre,(1396,200))
narouto = pygame.transform.scale(narouto,(300,500))
sasouke = pygame.transform.scale(sasouke,(300,500))
logo = pygame.transform.scale(logo,(600,300))

screen = pygame.display.set_mode([WIDTH, HEIGHT],pygame.FULLSCREEN)
pygame.mixer.music.play(-1)





running = True

start_time = pygame.time.get_ticks()
narouto_appeared = False
sasouke_appeared = False
last = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                if last:
                    click_x, click_y = pygame.mouse.get_pos()
                    if 518 <= click_x <= 1018 and 250 <= click_y <= 400:
                        # Code pour lancer une partie en 1v1
                        print("Jcj")
                    elif 518 <= click_x <= 1018 and 450 <= click_y <= 600:
                        # Code pour lancer une partie contre ia
                        print("JcI")
                    elif 518 <= click_x <= 1018 and 650 <= click_y <= 800:
                        # Code pour voir les règles
                        print("Regles")

    
    screen.fill(orange_color)
    # screen.blit(titre,(75,0))
    pygame.draw.rect(screen,black_color,(0,0,20,960))
    pygame.draw.rect(screen,black_color,(30,0,20,960))
    pygame.draw.rect(screen,black_color,(60,0,20,960))

    pygame.draw.rect(screen,black_color,(1516,0,20,960))
    pygame.draw.rect(screen,black_color,(1486,0,20,960))
    pygame.draw.rect(screen,black_color,(1456,0,20,960))

    font = pygame.font.SysFont("Permanent Marker", 60)

    versus = font.render("Joueur contre Joueur",True,orange_color)
    contreIa = font.render("Joueur contre IA",True, orange_color)
    regles = font.render("Regles du jeu",True,orange_color)

    




    

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= 5000 and sasouke_appeared == False:
        screen.fill(black_color)
        pygame.display.flip()
        pygame.time.delay(150)
        screen.fill(orange_color)
        screen.blit(sasouke,(1156,460))
        pygame.draw.rect(screen,black_color,(0,0,20,960))
        pygame.draw.rect(screen,black_color,(30,0,20,960))
        pygame.draw.rect(screen,black_color,(60,0,20,960))

        pygame.draw.rect(screen,black_color,(1516,0,20,960))
        pygame.draw.rect(screen,black_color,(1486,0,20,960))
        pygame.draw.rect(screen,black_color,(1456,0,20,960))
        sasouke_appeared = True
    if current_time - start_time >= 7500 and narouto_appeared == False:
        screen.fill(black_color)
        pygame.display.flip()
        pygame.time.delay(150)
        screen.fill(orange_color)
        screen.blit(narouto,(80,460))
        screen.blit(sasouke,(1156,460))
        pygame.draw.rect(screen,black_color,(0,0,20,960))
        pygame.draw.rect(screen,black_color,(30,0,20,960))
        pygame.draw.rect(screen,black_color,(60,0,20,960))

        pygame.draw.rect(screen,black_color,(1516,0,20,960))
        pygame.draw.rect(screen,black_color,(1486,0,20,960))
        pygame.draw.rect(screen,black_color,(1456,0,20,960))
        narouto_appeared = True

    if current_time - start_time >= 13000:
        screen.blit(titre,(75,0))

    if current_time - start_time >= 15500:
        screen.blit(logo, (455,300) )

    
    if current_time - start_time >= 20500 and last == False:
        screen.fill(black_color)
        pygame.display.flip()
        pygame.time.delay(150)

        screen.fill(orange_color)
        screen.blit(titre,(75,0))
        screen.blit(narouto,(80,460))
        screen.blit(sasouke,(1156,460))
        pygame.draw.rect(screen,black_color,(0,0,20,960))
        pygame.draw.rect(screen,black_color,(30,0,20,960))
        pygame.draw.rect(screen,black_color,(60,0,20,960))

        pygame.draw.rect(screen,black_color,(1516,0,20,960))
        pygame.draw.rect(screen,black_color,(1486,0,20,960))
        pygame.draw.rect(screen,black_color,(1456,0,20,960))


        pygame.draw.rect(screen, black_color,(518,250,500,150))
        pygame.draw.rect(screen, dark_blue_color,(520,252,495,145))


        pygame.draw.rect(screen, black_color,(518,450,500,150))
        pygame.draw.rect(screen, dark_blue_color,(520,452,495,145))

        pygame.draw.rect(screen, black_color,(518,650,500,150))
        pygame.draw.rect(screen, dark_blue_color,(520,652,495,145))

        screen.blit(versus,(545,310))
        screen.blit(contreIa,(600,510))
        screen.blit(regles,(620,710))
        last = True


    if sasouke_appeared:
        screen.blit(sasouke, (1156, 460))

    if narouto_appeared:
        screen.blit(narouto,(80,460))

    if last:


        screen.fill(orange_color)
        screen.blit(titre,(75,0))
        screen.blit(narouto,(80,460))
        screen.blit(sasouke,(1156,460))
        pygame.draw.rect(screen,black_color,(0,0,20,960))
        pygame.draw.rect(screen,black_color,(30,0,20,960))
        pygame.draw.rect(screen,black_color,(60,0,20,960))

        pygame.draw.rect(screen,black_color,(1516,0,20,960))
        pygame.draw.rect(screen,black_color,(1486,0,20,960))
        pygame.draw.rect(screen,black_color,(1456,0,20,960))


        pygame.draw.rect(screen, black_color,(518,250,500,150))
        pygame.draw.rect(screen, dark_blue_color,(520,252,495,145))


        pygame.draw.rect(screen, black_color,(518,450,500,150))
        pygame.draw.rect(screen, dark_blue_color,(520,452,495,145))

        pygame.draw.rect(screen, black_color,(518,650,500,150))
        pygame.draw.rect(screen, dark_blue_color,(520,652,495,145))

        screen.blit(versus,(545,310))
        screen.blit(contreIa,(600,510))
        screen.blit(regles,(620,710))

        



    
    
    

    pygame.display.flip()
    

pygame.quit()











