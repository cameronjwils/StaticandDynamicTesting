import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card_game = CardGame()
        self.card1 = Card('Spade', 3)
        self.card2 = Card('Spade', 1)
        self.cards = [self.card1, self.card2]
    
    def test_cards_have_ace(self):
        self.card_game.check_for_ace(self.card2)
        self.assertEqual(True, self.card_game.check_for_ace(self.card2))

    def test_highest_card(self):
        self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card1, self.card_game.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 4", self.card_game.cards_total(self.cards))