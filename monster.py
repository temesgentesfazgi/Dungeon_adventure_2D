from abc import ABC, abstractmethod
from dungeon_character import DungeonCharacter
import random


class Monster(DungeonCharacter, ABC):
    """Abstract base class representing a monster in the dungeon."""

    def __init__(self, name, hit_points, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal,
                 min_heal_points, max_heal_points):
        """
        Initialize the Monster object.

        :param name: The name of the monster.
        :param hit_points: The hit points of the monster.
        :param min_damage: The minimum damage the monster can inflict.
        :param max_damage: The maximum damage the monster can inflict.
        :param attack_speed: The attack speed of the monster.
        :param chance_to_hit: The chance of the monster hitting its opponent.
        :param chance_to_heal: The chance of the monster healing itself.
        :param min_heal_points: The minimum amount of healing points.
        :param max_heal_points: The maximum amount of healing points.
        """
        super().__init__(name, hit_points, min_damage, max_damage, attack_speed, chance_to_hit)
        self.chance_to_heal = chance_to_heal
        self.min_heal_points = min_heal_points
        self.max_heal_points = max_heal_points

    def heal(self):
        """
        Perform healing for the monster.

        Randomly determines if the monster will heal itself based on chance_to_heal.
        """
        if random.random() <= self.chance_to_heal:
            heal_amount = random.randint(self.min_heal_points, self.max_heal_points)
            self.hit_points = min(self.hit_points_max, self.hit_points + heal_amount)
            print(f"{self.name} healed to reach {self.hit_points} total hit points.")
        else:
            print(f"{self.name} did not heal.")

    def attack(self, opponent, num_attacks):
        """
        Attack the opponent.

        Randomly determines if the monster's attack hits the opponent based on chance_to_hit.
        If the attack hits, damage is inflicted on the opponent.

        :param opponent: The opponent to attack.
        :param num_attacks: The number of attacks to perform.
        """
        for _ in range(num_attacks):
            if random.random() <= self.chance_to_hit:
                if not (random.random() < opponent.chance_to_block):
                    print(f"{opponent.name} fails to block {self.name}'s attack.")
                    damage = random.randint(self.min_damage, self.max_damage)
                    opponent.hit_points = max(0, opponent.hit_points - damage)
                    print(f"{self.name} hits {opponent.name} causing {damage} hitpoints damage.")
                else:
                    print(f"{opponent.name} successfully blocks {self.name}'s attack.")

            else:
                print(f"{self.name}'s attack missed {opponent.name}.")
