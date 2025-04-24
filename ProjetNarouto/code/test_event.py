import pygame 



for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            click_x, click_y = pygame.mouse.get_pos()

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