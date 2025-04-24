from caseClass import Case
# Gestion des cases ----------------------------------------------------------------------------------

#Cases du haut

rect1 = [405,45,190,160];    rect2 = [615,45,190,160];    rect3 = [825,45,190,160];    rect4 = [1035,45,190,160]
rect5 = [405,205,190,160];   rect6 = [615,205,190,160];   rect7 = [825,205,190,160];   rect8 = [1035,205,190,160]

case1 = Case();case2 = Case();case3 = Case();case4 = Case()
case5 = Case();case6 = Case();case7 = Case();case8 = Case()

case1.rect = rect1; case2.rect = rect2; case3.rect = rect3; case4.rect = rect4
case5.rect = rect5; case6.rect = rect6; case7.rect = rect7; case8.rect = rect8


#Cases du bas

rect11 = [405,585,190,160];    rect12 = [615,585,190,160];    rect13 = [825,585,190,160];    rect14 = [1035,585,190,160]
rect15 = [405,745,190,160];    rect16 = [615,745,190,160];    rect17 = [825,745,190,160];    rect18 = [1035,745,190,160]

case11 = Case();case12 = Case();case13 = Case();case14 = Case()
case15 = Case();case16 = Case();case17 = Case();case18 = Case()

case11.rect = rect11; case12.rect = rect12; case13.rect = rect13; case14.rect = rect14
case15.rect = rect15; case16.rect = rect16; case17.rect = rect17; case18.rect = rect18

#  Cases main

rect1_main = [1300,90,190,160];     rect2_main = [1300,260,190,160];     rect3_main = [1300,430,190,160];     rect4_main = [1300,600,190,160];     rect5_main = [1300,770,190,160]
# rect11_main = [0,0,190,160];     rect12_main = [0,0,190,160];     rect13_main = [0,0,190,160];     rect14_main = [0,0,190,160];     rect15_main = [0,0,190,160]

case1_main = Case();case2_main = Case();case3_main = Case();case4_main = Case();case5_main = Case()
case1_main.rect = rect1_main; case2_main.rect = rect2_main; case3_main.rect = rect3_main; case4_main.rect = rect4_main; case5_main.rect = rect5_main

upper_case_select = False
lower_case_select = False
hand_case_select = False









