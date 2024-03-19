from abc import ABC, abstractmethod
import random

class DungeonCharacter(ABC):
    """Abstract base class representing a character in the dungeon."""

    def __init__(self, name, hit_points, min_damage, max_damage, attack_speed, chance_to_hit):
        """
        Initialize a DungeonCharacter object.

        Args:
            name (str): The name of the character.
            hit_points (int): The hit points of the character.
            min_damage (int): The minimum damage the character can deal.
            max_damage (int): The maximum damage the character can deal.
            attack_speed (float): The attack speed of the character.
            chance_to_hit (float): The chance of the character hitting the opponent.
        """
        self.name = name
        self.hit_points = hit_points
        self.hit_points_max = hit_points
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.attack_speed = attack_speed
        self.chance_to_hit = chance_to_hit

    @abstractmethod
    def attack(self, opponent, num_attacks):
        """
        Perform an attack on the opponent.

        Args:
            opponent (DungeonCharacter): The opponent character to attack.
            num_attacks (int): The number of attacks to perform.
        """
        pass

    def multiple_attacks(self, opponent):
        """
        Perform multiple attacks on the opponent.

        Args:
            opponent (DungeonCharacter): The opponent character to attack.
        """
        num_attacks = max(1, round(self.attack_speed / opponent.attack_speed))
        for _ in range(num_attacks):
            if self.chance_to_hit >= random.random():
                damage = random.randint(self.min_damage, self.max_damage)
                opponent.hit_points = max(0, opponent.hit_points - damage)
                print(f"{self.name} hits {opponent.name} for {damage} damage.")
            else:
                print(f"{self.name}'s attack missed {opponent.name}.")

    def report_status(self):
        """Report the current status of the character."""
        print(f"{self.name}: HP={self.hit_points}")

    def is_alive(self):
        """Check if the character is alive."""
        return self.hit_points > 0
