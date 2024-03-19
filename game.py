from dungeon import Dungeon
from warrior import Warrior
from priestess import Priestess
from thief import Thief
from constants import *
import pickle
import os
from enum import Enum


class Difficulty(Enum):
    """Enum class representing different difficulty levels."""
    EASY = 1
    MEDIUM = 2
    HARD = 3


class Game:
    """Class representing the game logic."""

    def __init__(self):
        """Initialize the game."""
        self.player = None
        self.dungeon = None
        self.is_game_over = False
        self.game_won = False
        self.difficulty = None

        self.total_games_played = 0
        self.num_games_lost = 0
        self.num_games_won = 0
        self.current_room = None

        # Game constants
        self.dungeon_xsize = 5
        self.dungeon_ysize = 5
        self.dbFile = 'database/monsters.db'

        # Define default parameters for each difficulty level
        self.difficulty_parameters = {
            Difficulty.EASY: {
                'player_hit_points': 100,
                'player_min_damage': 10,
                'player_max_damage': 20,
            },
            Difficulty.MEDIUM: {
                'player_hit_points': 75,
                'player_min_damage': 20,
                'player_max_damage': 40,
                # Add more parameters as needed...
            },
            Difficulty.HARD: {
                'player_hit_points': 50,
                'player_min_damage': 30,
                'player_max_damage': 60,
                # Add more parameters as needed...
            }
        }

        # start game
        self.start_outer_game_loop()

    def start_outer_game_loop(self):
        """Start the main game loop."""
        while True:
            choice = self.get_input_to_start_game()
            # Start new game
            if choice == "1" or choice == "2" or choice == "3":
                # initialize new game
                self.initialize_new_game()

                # play game
                self.play_game()
            elif choice == "4":
                # load saved game
                load_file = self.load_game()

                # play game
                if load_file is not None:
                    self.play_game()
                    if self.game_won or self.is_game_over:
                        self.delete_saved_game(load_file)
            elif choice == "5":
                # see stats
                print("\nStats:")
                print(f"Total Games Started: {self.total_games_played}")
                print(f"Games Won: {self.num_games_won}")
                print(f"Games Lost: {self.num_games_lost}")
            elif choice == "6":
                print("\nExiting Game. Bye!")
                break

    def get_input_to_start_game(self):
        """Get user input to start a game."""
        print("\nOptions:")
        print("1. Start New Game (Easy)")
        print("2. Start New Game (Medium)")
        print("3. Start New Game (Hard)")
        print("4. Load Game")
        print("5. See Stats")
        print("6. Exit")
        choice = input("Enter your choice: ")
        while choice not in {'1', '2', '3', '4', '5', '6'}:
            print("Invalid choice. Please choose among 1, 2, 3, 4, 5, 6")
            choice = input("Enter your choice: ")
        if choice in {'1', '2', '3'}:
            self.set_difficulty(choice)  # Pass the choice directly
        return choice

    def introduce_game(self):
        """Introduce the game to the player."""
        print(
            '''
*************************************************************************
Welcome to the Dungeon Adventure!
You find yourself in a mysterious dungeon full of dangers and treasures.
Your goal is to navigate through the dungeon, collect all pillars of
    object-oriented programming, along the way avoid pitfalls and destroy
    monsters and find the exit.
Along the way, you may discover healing potions to restore your health
    and vision potions to see through the surrounding.
Use your wits to survive and emerge victorious!
*************************************************************************
'''
        )

    def initialize_new_game(self):
        """Initialize a new game."""
        self.introduce_game()
        self.dungeon = Dungeon(self.dungeon_xsize, self.dungeon_ysize, self.dbFile)
        self.choose_hero()
        self.adjust_game_parameters()  # Move this line here
        self.total_games_played += 1
        self.current_room = self.dungeon.get_dungeon_entrance()
        self.current_room.player_is_in_room = True
        self.is_game_over = False
        self.game_won = False

    def choose_hero(self):
        """Let the player choose their hero."""
        print("\nChoose your hero: Warrior, Priestess, or Thief")
        hero_choice = input("Enter the name of your hero: ").lower()
        if hero_choice == "warrior":
            self.player = Warrior()
            print(f"\nYour hero is {hero_choice.capitalize()}")
        elif hero_choice == "priestess":
            self.player = Priestess()
            print(f"\nYour hero is {hero_choice.capitalize()}")
        elif hero_choice == "thief":
            self.player = Thief()
            print(f"\nYour hero is {hero_choice.capitalize()}")
        else:
            print("Invalid choice. Please choose Warrior, Priestess, or Thief.")
            self.choose_hero()  # Call recursively until a valid hero choice is made

    def set_difficulty(self, choice):
        """Set the game difficulty based on player's choice."""
        if choice == '1':
            self.difficulty = Difficulty.EASY
        elif choice == '2':
            self.difficulty = Difficulty.MEDIUM
        elif choice == '3':
            self.difficulty = Difficulty.HARD
        else:
            print("Invalid choice. Select difficulty.")

        self.adjust_game_parameters()

    def adjust_game_parameters(self):
        """Adjust game parameters based on selected difficulty."""
        if self.player is not None:
            parameters = self.difficulty_parameters.get(self.difficulty, {})
            if parameters:
                # Update game parameters based on the selected difficulty level
                self.player.hit_points = parameters.get('player_hit_points', self.player.hit_points)
                self.player.min_damage = parameters.get('player_min_damage', self.player.min_damage)
                self.player.max_damage = parameters.get('player_max_damage', self.player.max_damage)
        else:
            print("Error: Player has not been properly initialized.")

    def get_user_input_to_play_game(self):
        """Get user input to play the game."""
        print("\nOptions:")
        print("1. Move (N, S, E, W)")
        print("2. Use Healing Potion")
        print("3. Use Vision Potion")
        print("4. Save game")
        print("5. Exit game")
        print("6. View Dungeon (Hidden Test Option)")
        print("7. Cheat Sheet: Win Game")
        print("8. Cheat Sheet: Lose Game")
        print("9. Cheat Sheet: Identify Rooms with Monsters")
        choice = input("Enter your choice: ")
        return choice

    def play_game(self):
        """Main game loop."""
        # Step 1. Print status of player
        stop_game = False
        while (not self.is_game_over) and (not stop_game):
            print("\nCurrent Hero Status:")
            print(self.player)

            # Get user input
            choice = self.get_user_input_to_play_game()
            while (choice != '1') and (choice != '2') and (choice != '3') and (choice != '4') and (choice != '5') and (
                    choice != '6') and (choice != '7') and (choice != '8') and (choice != '9'):
                print("Invalid choice. Please choose among 1, 2, 3, 4, 5, 6, 7, 8, 9")
                choice = self.get_user_input_to_play_game()

            if choice == '1':
                direction = input("Enter the direction to move (N, S, E, W): ").upper()
                while (direction != 'N') and (direction != 'S') and (direction != 'E') and (direction != 'W'):
                    print("Invalid choice. Please choose among (N, S, E, W) to move")
                    direction = input("Enter the direction to move (N, S, E, W): ").upper()

                next_room = self.player.move(direction, self.current_room)
                if next_room is None:
                    print(f"Hero can't move to {direction} as there is a wall. Please choose another direction")
                    continue
                else:
                    self.current_room = next_room
                    print("\nCurrent Room:\n")
                    print(self.current_room)
                    # explore room - collect potions and/or fight monsters
                    self.player.explore_room(self.current_room)
                    game_status = self.check_game_status()
                    if game_status > 0:
                        print("\nCongrats!! You Have Won!")
                        print(self.player)
                        print(self.current_room)
                        stop_game = True
                        self.game_won = True
                    elif game_status < 0:
                        print("\nGame Over!! You Have Lost!")
                        print(self.player)
                        print(self.current_room)
                        stop_game = True
                        self.is_game_over = True
                    else:
                        continue

            elif choice == '2':
                result = self.player.use_potions(HEALING_POTION, self.current_room)
                print(f"\n{result}")
                print("\nCurrent Room:\n")
                print(self.current_room)

            elif choice == '3':
                result = self.player.use_potions(VISION_POTION, self.current_room)
                print(f"\n{result}")
                print("\nCurrent Room:\n")
                print(self.current_room)

            elif choice == '4':
                self.save_game()
                stop_game = True

            elif choice == '5':
                stop_game = True

            elif choice == '6':  # Hidden test option to view the entire dungeon
                print("\nHidden Test Option: View Entire Dungeon")
                print(self.dungeon)

            elif choice == '7':
                print("\nCheat Sheet: Win Game")
                self.cheat_win_game()

            elif choice == '8':
                print("\nCheat Sheet: Lose Game")
                self.cheat_loose_game()

            elif choice == '9':
                print("\nCheat Sheet: Identify Rooms with Monsters")
                self.cheat_identify_monsters()

        if self.game_won:
            self.num_games_won += 1
        elif self.is_game_over:
            self.num_games_lost += 1

    def check_game_status(self):
        """Check the status of the game."""
        player_in_exit = self.dungeon.get_dungeon_exit() == self.current_room
        if player_in_exit and len(self.player.pillars_found) == 4:
            return 1
        elif not self.player.is_alive():
            return -1
        else:
            return 0

    def save_game(self):
        """Save the current game state."""
        file_name = input("Enter the file name to save the game state: ")
        game_state = {
            "player": self.player,
            "dungeon": self.dungeon,
            "is_game_over": self.is_game_over,
            "game_won": self.game_won,
            "total_games_played": self.total_games_played,
            "num_games_lost": self.num_games_lost,
            "num_games_won": self.num_games_won,
            "current_room": self.current_room,
        }
        with open(file_name, "wb") as file:
            pickle.dump(game_state, file)
        print("Game state saved successfully.")

    def load_game(self):
        """Load a saved game state."""
        file_name = input("Enter the file name to load the game state: ")
        try:
            with open(file_name, "rb") as file:
                game_state = pickle.load(file)
            self.player = game_state["player"]
            self.dungeon = game_state["dungeon"]
            self.is_game_over = game_state["is_game_over"]
            self.game_won = game_state["game_won"]
            self.total_games_played = game_state["total_games_played"]
            self.num_games_lost = game_state["num_games_lost"]
            self.num_games_won = game_state["num_games_won"]
            self.current_room = game_state["current_room"]
            print("Game state loaded successfully.")
            return file_name
        except FileNotFoundError:
            print("\nFile not found. Unable to load game state.")
        except Exception as e:
            print("\nAn error occurred while loading the game state:", e)
        return None

    def delete_saved_game(self, file_path):
        """Delete a saved game file."""
        # Check if the file exists before attempting to delete it
        if os.path.exists(file_path):
            # Attempt to delete the file
            os.remove(file_path)
            print(f"Saved game in '{file_path}' file has been successfully deleted.")
        else:
            print(f"Trying to delete saved game but '{file_path}' file does not exist.")

    def cheat_win_game(self):
        """Cheat to simulate winning the game."""
        print("\nCheat Sheet: Simulating winning the game...")
        # Simulate winning scenario
        self.player.pillars_found = [PILLAR_ONE, PILLAR_TWO, PILLAR_THREE, PILLAR_FOUR]
        self.game_won = True

    def cheat_loose_game(self):
        """Cheat to simulate losing the game."""
        print("\nCheat Sheet: Simulating losing the game...")
        # Reduce player's hit points to zero
        self.player.hit_points = 0
        # Check game status
        game_status = self.check_game_status()
        # If player has lost
        if game_status < 0:
            print("\nGame Over!! You Have Lost!")
            print("\nStats:")
            print(f"Total Games Started: {self.total_games_played}")
            print(f"Games Won: {self.num_games_won}")
            print(f"Games Lost: {self.num_games_lost + 1}")  # Increment lost game count
            self.num_games_lost += 1  # Update lost game count
            print(self.player)
            print(self.current_room)
            self.is_game_over = True  # Set game over flag
        else:
            print("Game not lost. Continue playing...")

    def cheat_identify_monsters(self):
        """Cheat to identify rooms with monsters."""
        if self.dungeon and self.player:
            print("\nCheat Sheet: Identify Rooms with Monsters\n")
            current_room_id = self.current_room.room_id if self.current_room else None
            for y in range(self.dungeon.size_y):
                for x in range(self.dungeon.size_x):
                    room = self.dungeon.rooms[y][x]
                    if room.monster:
                        print("M", end=" ")  # Print M for room with monster
                    elif room.room_id == current_room_id:
                        print(self.player.name[0].upper(),
                              end=" ")  # Print first letter of player's name for current room
                    else:
                        print(".", end=" ")  # Print . for empty room
                print()  # New line after each row
            print(
                "\nLegend: M - Room with Monster, First letter of hero's name - Player's Current Room, . - Empty Room\n")
        else:
            print("No dungeon loaded or player not selected. Start a new game, choose a hero, or load a saved one.")


game = Game()
