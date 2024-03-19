from hero import Hero
import random

class Thief(Hero):
    """A class representing a Thief hero.

    Inherits from the Hero class and provides specific attributes and methods
    for the Thief hero type.
    """

    def __init__(self):
        """Initialize the Thief with specific attributes."""
        super().__init__("Thief", 75, 20, 40, 6, 0.8, 0.4)

    def try_special_skill(self, monster, num_attacks):
        """Attempt to use the Thief's special skill on a monster.

        Args:
            monster (Monster): The monster to attack.
            num_attacks (int): The number of attacks to attempt.

        Returns:
            None

        Prints a message indicating whether the special skill was activated
        and its effect on the monster's hit points. If the special skill is
        successful, an additional attack is performed.
        """
        for _ in range(num_attacks):
            chance = random.random()
            if chance <= 0.4:
                print(f"{self.name} activated a special skill - surprise attack.")
                damage = random.randint(20, 40)
                monster.hit_points = max(0, monster.hit_points - damage)
                print(f"{self.name} unleashed a surprise Attack causing {damage} hitpoints damage.")
                print(f"{self.name} gets one extra attack for the successful surprise")
                self.attack(monster, 1)
            elif chance > 0.4 and chance <= 0.6:
                print("Surprise Attack failed and Thief got caught. Lesson Learned - don't be a thief")
            else:
                self.attack(monster, 1)  # normal attack
