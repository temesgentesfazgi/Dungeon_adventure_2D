from dungeon_character import DungeonCharacter
from abc import ABC, abstractmethod
from constants import *
import random


class Hero(DungeonCharacter, ABC):
    """Abstract base class representing a hero character."""

    def __init__(self, name, hit_points, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_block):
        """
        Initialize the Hero object.

        :param name: The name of the hero.
        :param hit_points: The hit points of the hero.
        :param min_damage: The minimum damage the hero can inflict.
        :param max_damage: The maximum damage the hero can inflict.
        :param attack_speed: The attack speed of the hero.
        :param chance_to_hit: The chance of the hero hitting its opponent.
        :param chance_to_block: The chance of the hero blocking an opponent's attack.
        """
        super().__init__(name, hit_points, min_damage, max_damage, attack_speed, chance_to_hit)
        self.chance_to_block = chance_to_block
        self.healing_potions = []
        self.vision_potions = 0
        self.pillars_found = []
        self.chance_to_try_special_skill = 0.5

    @abstractmethod
    def try_special_skill(self, opponent, num_attacks):
        """
        Abstract method for the hero to attempt a special skill.

        :param opponent: The opponent to use the special skill against.
        :param num_attacks: The number of attacks to perform.
        """
        pass

    def attack(self, opponent, num_attacks):
        """
        Perform an attack on the opponent.

        :param opponent: The opponent to attack.
        :param num_attacks: The number of attacks to perform.
        """
        for _ in range(num_attacks):
            if random.random() <= self.chance_to_hit:
                damage = random.randint(self.min_damage, self.max_damage)
                opponent.hit_points = max(0, opponent.hit_points - damage)
                print(f"{self.name} hits {opponent.name} causing {damage} hitpoints damage.")
            else:
                print(f"{self.name}'s attack missed {opponent.name}.")

    def get_hero_input(self, battle_round):
        """
        Get the hero's input for selecting attack type.

        :param battle_round: The current round of battle.
        :return: The hero's choice of attack type (Normal or Special).
        """
        print(f"\nChoose between two types of attack for Round: {battle_round}")
        print("N. Normal Attack")
        print("Q. Special Skill Attack")
        choice = input("Enter your choice(N or Q): ").upper()
        while choice not in ['N', 'Q']:
            print("Invalid choice. Please choose between N, Q")
            choice = input("Enter your choice(N or Q): ").upper()
        return choice

    def battle_monster(self, monster, current_room):
        """
        Battle a monster in the current room.

        :param monster: The monster to battle.
        :param current_room: The current room where the battle takes place.
        """
        battle_round = 0
        print(f"\nAttention!! There is a monster named {monster.name} in the room!! Battle!!")
        while self.is_alive() and monster.is_alive():
            battle_round += 1
            print(f"\nRound: {battle_round}\n")
            print(self)

            if self.attack_speed >= monster.attack_speed:
                hero_num_attacks = max(1, round(self.attack_speed / monster.attack_speed))
                hero_attack_type = self.get_hero_input(battle_round)
                if hero_attack_type == "Q":
                    print(f"{self.name} is trying to use a special skill.")
                    self.try_special_skill(monster, hero_num_attacks)
                else:
                    self.attack(monster, hero_num_attacks)

                if monster.is_alive():
                    if monster.hit_points < monster.hit_points_max:
                        print(f"{monster.name} is damaged so is trying to heal.")
                        monster.heal()
                    monster.attack(self, 1)
            else:
                monster_num_attacks = max(1, round(monster.attack_speed / self.attack_speed))
                monster.attack(self, monster_num_attacks)

                if self.is_alive():
                    hero_attack_type = self.get_hero_input(battle_round)
                    if hero_attack_type == "Q":
                        print(f"{self.name} is trying to use a special skill.")
                        self.try_special_skill(monster, 1)
                    else:
                        self.attack(monster, 1)
                if monster.is_alive():
                    monster.heal()

        if self.is_alive():
            print(f"Yay! The {monster.name} monster is DEAD!!")
            current_room.monster = None
        else:
            print(f"Your hero {self.name} is DEAD!! Game Over!!")

    def move(self, direction, current_room):
        """
        Move the hero to the adjacent room in the specified direction.

        :param direction: The direction to move (N, S, E, W).
        :param current_room: The current room where the hero is located.
        :return: The next room if movement is possible, otherwise None.
        """
        available_doors = current_room.get_open_doors()
        next_room = None
        if direction == 'N':
            if NORTH in available_doors:
                next_room = current_room.neighbors[NORTH]
            else:
                return None
        elif direction == 'S':
            if SOUTH in available_doors:
                next_room = current_room.neighbors[SOUTH]
            else:
                return None
        elif direction == 'E':
            if EAST in available_doors:
                next_room = current_room.neighbors[EAST]
            else:
                return None
        else:
            if WEST in available_doors:
                next_room = current_room.neighbors[WEST]
            else:
                return None
        current_room.player_is_in_room = False
        next_room.player_is_in_room = True
        return next_room

    def explore_room(self, current_room):
        """
        Explore the items and monster in the current room.

        :param current_room: The current room to explore.
        """
        if current_room.monster is not None:
            self.battle_monster(current_room.monster, current_room)

        if self.is_alive():
            if current_room.items[PIT] is not None:
                self.hit_points -= current_room.items[PIT]
                current_room.items[PIT] = None

            if current_room.items[HEALING_POTION] is not None:
                self.healing_potions.append(current_room.items[HEALING_POTION])
                current_room.items[HEALING_POTION] = None

            if current_room.items[VISION_POTION] is not None:
                self.vision_potions += 1
                current_room.items[VISION_POTION] = None

            if current_room.pillar_of_oo is not None:
                self.pillars_found.append(current_room.pillar_of_oo)
                current_room.pillar_of_oo = None

    def use_potions(self, potion, current_room):
        """
        Use a potion in the current room.

        :param potion: The type of potion to use.
        :param current_room: The current room where the potion is used.
        :return: A message indicating the result of using the potion.
        """
        if potion == HEALING_POTION:
            if len(self.healing_potions) > 0:
                self.hit_points = min(self.hit_points_max, self.hit_points + self.healing_potions.pop(0))
                return f"Used {potion} and hit points is now {self.hit_points}"
            else:
                return f"No {potion} available."
        elif potion == VISION_POTION:
            if self.vision_potions > 0:
                self.vision_potions -= 1
                surrounding_info = current_room.get_surrounding_rooms_info()
                info_str = '\n'.join([f"{key} :\n{value}" for key, value in surrounding_info.items()])
                return f"Used {potion} and got the following info:\n{info_str}"
            else:
                return f"No {potion} available."

    def __str__(self):
        """
        Return a string representation of the hero.

        :return: A string containing the hero's name, hit points, and collected items.
        """
        return f"\nName: {self.name}\nHit Points: {self.hit_points}\nPillars Found: {self.pillars_found}\n" + \
            f"Healing Potions: {self.healing_potions}\nVision Potions: {self.vision_potions}"
