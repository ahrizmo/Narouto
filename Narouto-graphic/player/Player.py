from collections import deque
from card import Card # Import de la classe Card
from enumeration import TypeCard
import random
import pygame

class Player:
    def __init__(self, name: str, pv: int, chakra: int,img_rect):
        self.name = name
        self.PV = pv
        self.chakra = chakra
        self.deck = deque()  # Pile de cartes
        self.hand = []  # Liste de cartes en main
        self.board = [[None for _ in range(4)] for _ in range(2)]  # Matrice 2x4
        self.img_rect = img_rect

    def add_in_deck(self, carte: Card):
        """Ajoute une carte à la pile (deck)."""
        self.deck.append(carte)

    def set_chakra(self, chakra: int):
        self.chakra = chakra

    def set_deck(self, deck):
        self.deck = deque(deck)
        random.shuffle(self.deck)

    def draw(self):
        """Pioche une carte du deck (dernier entré, premier sorti) et l'ajoute à la main."""
        if self.deck:
            drawed_card = self.deck.pop()
            self.hand.append(drawed_card)
            print(f"{drawed_card.name} a été piochée et ajoutée à la main.")
        else:
            print("Le deck est vide, impossible de piocher.")

    def verifElementBonus(self,row,col):
        #vérification de la ligne
        pvBonus = True
        for i in range(4):
            if self.board[row][i] == None or self.board[row][i].type != self.board[row][col]:
                pvBonus = False
                break
        #vérification de la colonne
        attBonus = True
        for i in range(2):
            if self.board[i][col] == None or self.board[i][col].type != self.board[row][col]:
                attBonus = False
                break
        if pvBonus:
            for i in range(4):
                self.board[row][i].pvMax[1] = 1
                self.board[row][i].PV += 1
        else:
            for i in range(4):
                if self.board[row][i] != None:
                    self.board[row][i].pvMax[1] = 1
                    self.board[row][i].PV += 1

        if attBonus:
            for i in range(2):
                self.board[i][col].att[1] = 1
        else:
            for i in range(2):
                if self.board[i][col] != None:
                    self.board[i][col].att[1] = 0





    def play_card(self, card, row: int, col: int, player: "Player"):
        """
        Joue une carte de la main et la place sur le board à la position donnée.
        La carte est retirée de la main après avoir été placée.
        """
        if card not in self.hand:
            print(f"{card.nom} n'est pas dans votre main !")
            return

        if card.type == TypeCard.Ninja:
            if card.cost <= self.chakra:
                if 0 <= row < 2 and 0 <= col < 4 and self.board[row][col] is None:
                    self.board[row][col] = card
                    self.hand.remove(card)  # Retire la carte de la main après l'avoir jouée
                    self.chakra -= card.cost
                    print(f"{card.name} a été placé en ({row}, {col}).")
                    self.verifElementBonus(row, col)
                    self.board[row][col].turnAttack = True
                else:
                    print("Position invalide ou déjà occupée !")
            else:
                print("pas assez de chakra")

        elif card.type == TypeCard.Spell:
            if card.cost <= self.chakra:
                card.cast(player.board[row][col],self,player)
                self.chakra -= card.cost
                self.hand.remove(card)
                self.verifElementBonus(row,col)

    def new_turn(self):
        for i in range(2):  # Parcourt les lignes
            for j in range(4):
                card = self.board[i][j]
                if card is not None:
                    card.hasAttacked = False


    def afficher_main(self):
        """Affiche les cartes en main."""
        if self.hand:
            print("Cartes en main :", self.hand)
        else:
            print("La main est vide.")

    def draw_hand(self):
        if self.hand:
            col=0
            row=1250
            for card in self.hand:
                pygame.blit(card.img,pygame.Rect(col, row, 250, 250))
                col += 300



    def afficher_deck(self):
        """Affiche les cartes du deck."""
        if self.deck:
            print("Cartes dans le deck :", list(self.deck))
        else:
            print("Le deck est vide.")

    def show_board(self):
        print(f"Board de {self.name} :")
        for i in range(2):  # Parcourt les lignes
            for j in range(4):  # Parcourt les colonnes
                card = self.board[i][j]
                print(f"[{card.name if card else 'Vide'}]", end=" ")  # Affichage en ligne
            print()  # Nouvelle ligne après chaque rangée
        print("-" * 30)  # Séparateur visuel

    def draw_board(self,screen):
        for i in range(2):
            for j in range(4):
                card = self.board[i][j]
                if card is not None:
                    screen.blit(card.img,self.img_rect[2][4])