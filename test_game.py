import unittest
from unittest.mock import patch
from io import StringIO
from game import Game
from warrior import Warrior
from dungeon import Dungeon


class TestGame(unittest.TestCase):
    """A test suite for the Game class."""

    def test_initialize_new_game(self):
        """Test the initialization of a new game instance."""
        game = Game()
        self.assertIsNone(game.player)
        self.assertIsNone(game.dungeon)
        self.assertFalse(game.is_game_over)
        self.assertFalse(game.game_won)
        self.assertEqual(game.total_games_played, 0)
        self.assertEqual(game.num_games_lost, 0)
        self.assertEqual(game.num_games_won, 0)
        self.assertIsNone(game.current_room)

    @patch('builtins.input', side_effect=['1', 'Warrior', 'N', '5', '2', 'N'])
    def test_start_outer_game_loop(self, mock_input):
        """Test starting the outer game loop."""
        game = Game()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            game.start_outer_game_loop()
            output = fake_out.getvalue()
            self.assertIn("Current Hero Status:", output)

    @patch('builtins.input', side_effect=['invalid', '1'])
    def test_get_input_to_start_game(self, mock_input):
        """Test getting input to start the game."""
        game = Game()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            choice = game.get_input_to_start_game()
            self.assertEqual(choice, '1')

    def test_choose_hero(self):
        """Test choosing a hero for the game."""
        game = Game()
        with patch('builtins.input', side_effect=['Warrior']):
            game.choose_hero()
            self.assertIsInstance(game.player, Warrior)

    def test_check_game_status(self):
        """Test checking the game status."""
        game = Game()
        game.dungeon = Dungeon(5, 5, 'database/monsters.db')
        game.player = Warrior()
        game.current_room = game.dungeon.get_dungeon_exit()
        game.player.pillars_found = [1, 2, 3, 4]
        self.assertEqual(game.check_game_status(), 1)

    def test_delete_saved_game(self):
        """Test deleting a saved game."""
        game = Game()
        with patch('os.path.exists', return_value=True), \
             patch('os.remove') as mock_remove:
            game.delete_saved_game('test_file')
            mock_remove.assert_called_once_with('test_file')


if __name__ == '__main__':
    unittest.main()
