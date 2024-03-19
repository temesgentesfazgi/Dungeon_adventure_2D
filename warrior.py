from hero import Hero
import random

class Warrior(Hero):
    """A class representing a Warrior hero.

    Inherits from the Hero class and provides specific attributes and methods
    for the Warrior hero type.
    """

    def __init__(self):
        """Initialize the Warrior with specific attributes."""
        super().__init__("Warrior", 125, 35, 60, 4, 0.8, 0.2)
        self.chance_for_special_skill = 0.4
        self.special_damage_min = 75
        self.special_damage_max = 175

    def try_special_skill(self, monster, num_attacks):
        """Attempt to use the Warrior's special skill on a monster.

        Args:
            monster (Monster): The monster to attack.
            num_attacks (int): The number of attacks to attempt.

        Returns:
            None

        Prints a message indicating whether the special skill was activated
        and its effect on the monster's hit points.
        """
        for _ in range(num_attacks):
            chance = random.random()
            if chance <= 0.4:
                print(f"{self.name} activated a special skill - crushing blow.")
                damage = random.randint(self.special_damage_min, self.special_damage_max)
                monster.hit_points = max(0, monster.hit_points - damage)
                print(f"{self.name} unleashed a crushing blow causing {damage} hitpoints damage.")
            else:
                print(f"{self.name} failed to land the crushing blow.")
