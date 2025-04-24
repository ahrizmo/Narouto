import pygame

pygame.init


WIDTH, HEIGHT = 1900, 1200
color_blue = (0,0,250)
screen = pygame.display.set_mode([WIDTH, HEIGHT],pygame.FULLSCREEN)
running = True

logo = pygame.image.load("imgTest.png")
logo.convert()

carte = pygame.image.load("CarteNarutoExemple.png")
carte.convert()

map = pygame.image.load("Map1.jpg")
map.convert()
fond = pygame.transform.scale(map, (1250, 980))
IMAGE_SMALL = pygame.transform.scale(logo, (180, 150))

#rect = [50,50,100,100]
#pygame.draw.rect()
while running :
    screen.blit(fond,[0,0])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False

    
            

    
    
    
    


    
    screen.blit(IMAGE_SMALL,[310,50])
    screen.blit(IMAGE_SMALL,[520,50])
    screen.blit(IMAGE_SMALL,[730,50])
    screen.blit(IMAGE_SMALL,[940,50])


    screen.blit(IMAGE_SMALL,[310,210])
    screen.blit(IMAGE_SMALL,[520,210])
    screen.blit(IMAGE_SMALL,[730,210])
    screen.blit(IMAGE_SMALL,[940,210])
  
    screen.blit(IMAGE_SMALL,[1340,210])

#BAS

    
    screen.blit(IMAGE_SMALL,[310,590])
    screen.blit(IMAGE_SMALL,[520,590])
    screen.blit(IMAGE_SMALL,[730,590])
    screen.blit(IMAGE_SMALL,[940,590])


    screen.blit(IMAGE_SMALL,[310,750])
    screen.blit(IMAGE_SMALL,[520,750])
    screen.blit(IMAGE_SMALL,[730,750])
    screen.blit(IMAGE_SMALL,[940,750])
    
   
    

    x,y = pygame.mouse.get_pos()

    if x >= 310 and x <= 500:
        if y >= 50 and y <= 200:
            print("{}".format(event.pos))
            screen.blit(carte,[500,200])

    pygame.display.flip()
