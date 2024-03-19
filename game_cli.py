from dungeon import Dungeon
from warrior import Warrior
from priestess import Priestess
from thief import Thief
from constants import *
import pickle
import os


class Game:
    def __init__(self):
        self.player = None
        self.dungeon = None
        self.is_game_over = False
        self.game_won = False

        self.total_games_played = 0
        self.num_games_lost = 0
        self.num_games_won = 0
        self.current_room = None

        # Game constants
        self.dungeon_xsize = 5
        self.dungeon_ysize = 5
        self.dbFile = 'database/monsters.db'

        # start game
        self.start_outer_game_loop()


    def start_outer_game_loop(self): 
        while True:
            choice = self.get_input_to_start_game()
            # Start new game
            if choice == "1":
                # initialize new game 
                self.initialize_new_game()

                # play game
                self.play_game()
            elif choice == "2":
                # load saved game
                load_file = self.load_game()

                # play game
                if load_file is not None:
                    self.play_game()
                    if self.game_won or self.is_game_over:
                        self.delete_saved_game(load_file)
            elif choice == "3":
                # see stats
                print("\nStats:")
                print(f"Total Games Started: {self.total_games_played}")
                print(f"Games Won: {self.num_games_won}")
                print(f"Games Lost: {self.num_games_lost}")
            else:
                print("\nExiting Game. Bye!")
                break

    def get_input_to_start_game(self):
        print("\nOptions:")
        print("1. Start New Game")
        print("2. Load Game")
        print("3. See Stats")
        print("4. Exit")
        choice = input("Enter your choice: ")
        while (choice != '1') and (choice != '2') and (choice != '3') and (choice != '4'):
            print("Invalid choice. Please choose among 1, 2, 3, 4")
            choice = input("Enter your choice: ")
        return choice


    def introduce_game(self):
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
        self.introduce_game()
        self.dungeon = Dungeon(self.dungeon_xsize, self.dungeon_ysize, self.dbFile)
        self.choose_hero()
        self.total_games_played += 1
        self.current_room = self.dungeon.get_dungeon_entrance()
        self.current_room.player_is_in_room = True
        self.is_game_over = False
        self.game_won = False

    def choose_hero(self):
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
            self.choose_hero()
    
    def get_user_input_to_play_game(self):
        print("\nOptions:")
        print("1. Move (N, S, E, W)")
        print("2. Use Healing Potion")
        print("3. Use Vision Potion")
        print("4. Save game")
        print("5. Exit game")
        print("6. View Dungeon (Hidden Test Option)")
        choice = input("Enter your choice: ")
        return choice

    def play_game(self):
        # Step 1. Print status of player
        stop_game = False
        while (not self.is_game_over) and (not stop_game):
            print("\nCurrent Hero Status:")
            print(self.player)            


            # Get user input
            choice = self.get_user_input_to_play_game()
            while (choice != '1') and (choice != '2') and (choice != '3') and (choice != '4') and (choice != '5') and (choice != '6'):
                print("Invalid choice. Please choose among 1, 2, 3, 4, 5, 6")
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
        
        if self.game_won:
            self.num_games_won += 1
        elif self.is_game_over:
            self.num_games_lost += 1
    

    def check_game_status(self):
        player_in_exit = self.dungeon.get_dungeon_exit() == self.current_room
        if player_in_exit and len(self.player.pillars_found) == 4:
            return 1
        elif not self.player.is_alive():
            return -1
        else:
            return 0
    
    def save_game(self):
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
        # Check if the file exists before attempting to delete it
        if os.path.exists(file_path):
            # Attempt to delete the file
            os.remove(file_path)
            print(f"Saved game in '{file_path}' file has been successfully deleted.")
        else:
            print(f"Trying to delete saved game but '{file_path}' file does not exist.")


game = Game()
# print(game.dungeon)
