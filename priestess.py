from hero import Hero
import random


class Priestess(Hero):
    """A class representing a Priestess hero."""

    def __init__(self):
        """
        Initialize a Priestess hero with specific attributes.

        - Name: Priestess
        - Hit Points: 75
        - Min Damage: 25
        - Max Damage: 45
        - Attack Speed: 5
        - Chance to Hit: 0.7
        - Chance to Heal: 0.3
        """
        super().__init__("Priestess", 75, 25, 45, 5, 0.7, 0.3)
        self.special_heal_max = 60
        self.special_heal_min = 30

    def try_special_skill(self, monster, num_attacks):
        """
        Attempt to use the Priestess's special healing skill.

        If successful, the Priestess heals a random amount of hit points within a specific range.
        If unsuccessful, the Priestess fails to use the special skill and resorts to a normal attack.

        :param monster: The monster to attack.
        :param num_attacks: The number of attacks to perform.
        """
        chance = random.random()
        if chance <= 0.4:
            print(f"{self.name} activated a special skill - healing.")
            heal_amount = random.randint(self.special_heal_min, self.special_heal_max)
            self.hit_points = min(self.hit_points_max, self.hit_points + heal_amount)
            print(f"{self.name} healed {heal_amount} hit points.")
        else:
            # normal attack
            # self.attack(monster, num_attacks)
            print(f"{self.name} failed to heal using special skill.")
