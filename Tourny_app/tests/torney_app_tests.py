import unittest

from models.player import *
from models.match import *


class TestTourny(unittest.TestCase):

    def setUp(self):
        self.player1 = Player('Christopher', 'Mario')
        self.player2 = Player('Stephen', 'Peach')

        self.match1 = Match(self.player1.id, self.player2.id)

    def test_player_has_name(self):
        self.assertEqual("Christopher", self.player1.name)

    def test_player_has_character(self):
        self.assertEqual("Peach", self.player2.character)

    def test_player_has_id(self):
        self.assertEqual(None , self.player1.id)

    def test_match_class(self):
        self.assertEqual(None, self.match1.player1_id)
        self.assertEqual(None, self.match1.player2_id)
        self.assertEqual(None, self.match1.id)
        self.assertEqual(None, self.match1.result)

