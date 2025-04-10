from sympy.physics.units import joule

from player import Player
from deck import deck1, deck2, deck3, deck4
import pygame

img_rect_p1 = [2][4]
img_rect_p2 = [2][4]
y = 45
x = 405
for i in range(2):
    for j in range(4):
        img_rect_p1[i][j] = pygame.Rect(x+j*210,y+i*160)

y = 585
x = 405
for i in range(2):
    for j in range(4):
        img_rect_p2[i][j] = pygame.Rect(x+j*210,y+i*160)

# Création des joueurs1
joueur1 = Player("J1",20, 1,img_rect_p1)
joueur2 = Player( "J2",20, 1,img_rect_p1)

# Attribution des decks aux joueurs
joueur1.set_deck(deck4)
joueur2.set_deck(deck4)

# Affichage des decks des joueurs
print("\nDeck du Joueur 1 :")

joueur1.afficher_deck()

print("\nDeck du Joueur 2 :")
joueur2.afficher_deck()

screen = pygame.display.set_mode((0,0),pygame.NOFRAME)

def main():
    current_player = joueur1
    opponent = joueur2
    chakra = 1
    tour = 0
    while current_player.PV > 0 and opponent.PV > 0:
        current_player.new_turn()
        print((tour/2)+1)

        print(f"{current_player.name} - PV: {current_player.PV} | {opponent.name} - PV: {opponent.PV}")
        print(f"\n{current_player.name}, c'est votre tour !")

        print(f"\n{opponent.name}: ")
        opponent.show_board()
        print(f"\n{current_player.name}: ")
        current_player.show_board()

        current_player.set_chakra(chakra)
        print(f"chakra: {current_player.chakra}")

        current_player.draw()
        current_player.afficher_main()

        nbr_play = -1
        while nbr_play != 0:


            nbr_play = int(input(f"\n{current_player.name}: Choississez la carte que vous voulez jouer dans la main (avec le nombre de l'index),si vous voulez attacker tapez -1 ou sinon tapez 0 pour passez votre tour? "))
            if nbr_play != 0:
                if nbr_play != -1:
                    row = int(input("chossissez dans quelles ligne ou vous voulez la posez (1 ou 2)" ))
                    row -= 1
                    col = int(input("chossissez dans quelles colonnes ou vous voulez la posez (1-4)" ))
                    col -= 1

                    current_player.play_card(current_player.hand[nbr_play-1], row, col,current_player)
                    print(f"\n{opponent.name}: ")
                    opponent.draw_board()
                    print(f"\n{current_player.name}: ")
                    current_player.draw_board()

                    current_player.draw_hand()

                    print(f"chakra: {current_player.chakra}")
                else:
                    att = int(input("si vous voulez attaquez le joueur tapez 1, 0 sinon"))
                    if att == 1:
                        i = int(input("ligne de la carte que vous voulez jouer(1-2)"))-1
                        j = int(input("colonne de la carte que voulez voulez(1-4)"))-1
                        bool = current_player.board[i][j].attackPLayer(opponent)
                        if bool == True:
                            nbr_play = 0
                        print(f"{current_player.name} - PV: {current_player.PV} | {opponent.name} - PV: {opponent.PV}")
                    elif att == 0:

                        i = int(input("ligne de la carte que vous voulez jouer(1-2)"))-1
                        j = int(input("colonne de la carte que voulez voulez(1-4)"))-1

                        i2 = int(input("ligne de la carte que vous voulez attaquez(1-2)"))-1
                        j2 = int(input("colonne de la carte que voulez attaquez(1-4)"))-1

                        if current_player.board[i][j] != None and opponent.board[i][j] != None:
                            current_player.board[i][j].attack(opponent.board[i][j], current_player.board, opponent.board)
                            current_player.verifElementBonus(i,j)
                            opponent.verifElementBonus(i2,j2)
                        elif current_player.board[i][j] == None or opponent.board[i][j] == None:
                            print("pas de carte à cette position")
                            print(current_player.board[i][j].name)
                    print(f"\n{opponent.name}: ")
                    opponent.draw_board()
                    print(f"\n{current_player.name}: ")
                    current_player.draw_board()
        current_player, opponent = opponent, current_player
        tour += 1
        if tour%2 == 0:
            chakra += 1
    if current_player.PV < 0:
        print(f"\n{opponent.name} a gagné !")
    else:
        print(f"\n{current_player.name} a gagné !")

if __name__ == "__main__":
    main()