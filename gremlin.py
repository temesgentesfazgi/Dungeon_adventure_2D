from monster import Monster
import random


class Gremlin(Monster):
    """Class representing a Gremlin monster."""

    def __init__(self, name, hit_points, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal,
                 min_heal_points, max_heal_points):
        """
        Initialize the Gremlin object.

        :param name: The name of the Gremlin.
        :param hit_points: The hit points of the Gremlin.
        :param min_damage: The minimum damage the Gremlin can inflict.
        :param max_damage: The maximum damage the Gremlin can inflict.
        :param attack_speed: The attack speed of the Gremlin.
        :param chance_to_hit: The chance of the Gremlin hitting its opponent.
        :param chance_to_heal: The chance of the Gremlin healing itself.
        :param min_heal_points: The minimum hit points the Gremlin can heal.
        :param max_heal_points: The maximum hit points the Gremlin can heal.
        """
        super().__init__(name, hit_points, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal,
                         min_heal_points, max_heal_points)
