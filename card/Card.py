from enumeration import ElementalChakra, TypeCard
from player import Player
from typing import List, Callable

class Card:
    def __init__(self, name: str, type: TypeCard, pv: List[int], att: List[int], nature: ElementalChakra, cost: int):#, passif: List[Callable]):
        self.name = name
        self.type = type
        self.pvMax = pv
        self.PV = sum(self.pvMax)
        self.att = att
        self.nature = nature
        self.cost = cost
        self.hasAttacked = False
        self.turnAttack = False
        #self.passif = passif

    def attack(self, cible, board_attack, board_defense):
        if not self.hasAttacked:
            """Attaque une autre carte et gère sa destruction si ses PV tombent à 0."""
            if cible is None:
                print(f"{self.name} attaque, mais il n'y a pas de cible !")
                return

            print(f"{self.name} attaque {cible.name} !")

            # Les deux cartes se font des dégâts mutuels
            self.PV -= sum(cible.att)
            cible.PV -= sum(self.att)

            self.hasAttacked = True
            # Vérifier si une carte est détruite
            if self.PV <= 0:
                self.remove_from_board(board_attack)
                print(f"{self.name} a été détruite !")
                board_attack.verifElementBonus()

            if cible.PV <= 0:
                cible.remove_from_board(board_defense)
                print(f"{cible.name} a été détruite !")
        else:
            print("cette carte a déjà attaqué")



    def attackPLayer(self, player: Player):
        if not self.hasAttacked:
            player.PV -= sum(self.att)
            self.hasAttacked = True
            if player.PV <= 0:
                return True
            else:
                return False
        else:
            print("cette carte a déjà attaqué")
    def cast(self, target, player, opponent):
        if self.type == TypeCard.Spell:
            if sum(self.att) > 0:
                # Si le Spell inflige des dégâts
                if player != opponent:
                    target.PV -= sum(self.att)
                    if target.PV <= 0:
                        target.remove_from_board(opponent.board)
            elif self.PV > 0:
                if player == opponent:
                    target.PV = min(target.PV + self.PV, target.pvMax)
                # Si le Spell soigne

    def remove_from_board(self, board):
        """Supprime la carte du board après destruction."""
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == self:
                    board[i][j] = None
                    return

    def __repr__(self):
        return f"Card(name={self.name}, type={self.type}, PV={self.PV}, att={sum(self.att)}, nature={self.nature}, coût={self.cost})"

