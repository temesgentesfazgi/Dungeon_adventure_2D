from monster import Monster
import random

class Ogre(Monster):
    """A class representing an Ogre monster."""

    def __init__(self, name, hit_points, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal,
                 min_heal_points, max_heal_points):
        """
        Initialize an Ogre monster with specific attributes.

        :param name: The name of the Ogre.
        :param hit_points: The hit points of the Ogre.
        :param min_damage: The minimum damage the Ogre can deal.
        :param max_damage: The maximum damage the Ogre can deal.
        :param attack_speed: The attack speed of the Ogre.
        :param chance_to_hit: The chance for the Ogre to successfully hit its target.
        :param chance_to_heal: The chance for the Ogre to heal itself.
        :param min_heal_points: The minimum amount of hit points the Ogre can heal.
        :param max_heal_points: The maximum amount of hit points the Ogre can heal.
        """
        super().__init__(name, hit_points, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal,
                 min_heal_points, max_heal_points)
