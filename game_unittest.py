import unittest
from unittest.mock import patch
from game import Game
from dungeon import Dungeon
from warrior import Warrior
from priestess import Priestess
from thief import Thief
from constants import Difficulty

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def tearDown(self):
        # Clean up any resources used during testing
        del self.game

    @patch('builtins.input', side_effect=['warrior'])
    def test_choose_hero_warrior(self, mock_input):
        self.game.choose_hero()
        self.assertIsInstance(self.game.player, Warrior)

    @patch('builtins.input', side_effect=['priestess'])
    def test_choose_hero_priestess(self, mock_input):
        self.game.choose_hero()
        self.assertIsInstance(self.game.player, Priestess)

    @patch('builtins.input', side_effect=['thief'])
    def test_choose_hero_thief(self, mock_input):
        self.game.choose_hero()
        self.assertIsInstance(self.game.player, Thief)

    @patch('builtins.input', side_effect=['1'])
    def test_set_difficulty_easy(self, mock_input):
        self.game.set_difficulty('1')
        self.assertEqual(self.game.difficulty, Difficulty.EASY)

    @patch('builtins.input', side_effect=['2'])
    def test_set_difficulty_medium(self, mock_input):
        self.game.set_difficulty('2')
        self.assertEqual(self.game.difficulty, Difficulty.MEDIUM)

    @patch('builtins.input', side_effect=['3'])
    def test_set_difficulty_hard(self, mock_input):
        self.game.set_difficulty('3')
        self.assertEqual(self.game.difficulty, Difficulty.HARD)

    # Add more test methods to cover other functionalities of your Game class

    def test_game_initialization(self):
        self.assertIsNotNone(self.game.player)
        self.assertIsNone(self.game.dungeon)
        self.assertFalse(self.game.is_game_over)
        self.assertFalse(self.game.game_won)
        self.assertIsNone(self.game.difficulty)
        self.assertEqual(self.game.total_games_played, 0)
        self.assertEqual(self.game.num_games_lost, 0)
        self.assertEqual(self.game.num_games_won, 0)
        self.assertIsNone(self.game.current_room)

if __name__ == '__main__':
    unittest.main()
