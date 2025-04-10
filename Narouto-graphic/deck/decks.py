from card import Card
from enumeration import *
# Création des cartes
c1 = Card("Dragon de feu", TypeCard.Ninja, [6,0,0], [8,0,0], ElementalChakra.Fire, 5)
c2 = Card("Chevalier", TypeCard.Ninja, [4,0,0], [2,0,0], ElementalChakra.Earth, 3)
c3 = Card("Mage de glace", TypeCard.Ninja, [4,0,0], [5,0,0], ElementalChakra.Water, 4)
c4 = Card("Mercenaire", TypeCard.Ninja, [2,0,0], [2,0,0], ElementalChakra.Lightning, 2)
c5 = Card("soldat", TypeCard.Ninja, [1,0,0], [1,0,0], ElementalChakra.Wind, 1)

# Decks prédéfinis pour les joueurs
deck1 = [c1, c2,c3,c4,c5]
deck2 = [c3, c2]
deck3 = [c1, c2, c3]
deck4 = [c5,c5]