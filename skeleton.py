from monster import Monster
import random

class Skeleton(Monster):
    """
            Initialize a Skeleton monster.

            :param name: The name of the Skeleton.
            :param hit_points: The hit points of the Skeleton.
            :param min_damage: The minimum damage the Skeleton can inflict.
            :param max_damage: The maximum damage the Skeleton can inflict.
            :param attack_speed: The attack speed of the Skeleton.
            :param chance_to_hit: The chance to hit of the Skeleton.
            :param chance_to_heal: The chance to heal of the Skeleton.
            :param min_heal_points: The minimum heal points of the Skeleton.
            :param max_heal_points: The maximum heal points of the Skeleton.
            """
    def __init__(self, name, hit_points, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal,
                 min_heal_points, max_heal_points):
        super().__init__(name, hit_points, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal,
                 min_heal_points, max_heal_points)
        
    