from enum import Enum


class Difficulty(Enum):
    """Enumeration of difficulty levels."""
    EASY = 'EASY'
    MEDIUM = 'MEDIUM'
    HARD = 'HARD'


OGRE = "Ogre"
GREMLIN = "Gremlin"
SKELETON = "Skeleton"

MONSTERS = [OGRE, GREMLIN, SKELETON]

NAME = 'name'
HIT_POINTS = 'hit_points'
MIN_DAMAGE = 'min_damage'
MAX_DAMAGE = 'max_damage'
ATTACK_SPEED = 'attack_speed'
CHANCE_TO_HIT = 'chance_to_hit'
CHANCE_TO_HEAL = 'chance_to_heal'
MIN_HEAL_POINTS = 'min_heal_points'
MAX_HEAL_POINTS = 'max_heal_points'
CHANCE_FOR_SPECIAL_SKILL = 'chance_for_special_skill'

ABSTRACTION = 'Abstraction'
ENCAPSULATION = 'Encapsulation'
INHERITANCE = 'Inheritance'
POLYMORPHISM = 'Polymorphism'
PILLARS_OF_OO = [ABSTRACTION, ENCAPSULATION, INHERITANCE, POLYMORPHISM]

WALL = 'Wall'
HEALING_POTION = 'Healing Potion'
VISION_POTION = 'Vision Potion'
PIT = 'Pit'

NORTH = 'North'
SOUTH = 'South'
WEST = 'West'
EAST = 'East'
OPPOSITE_DIRECTION = {
    NORTH: SOUTH,
    SOUTH: NORTH,
    WEST: EAST,
    EAST: WEST
}

EXIT = 'Exit'

# Configs
OGRE_CONFIGURATIONS = {
    NAME: OGRE,
    HIT_POINTS: 200,
    MIN_DAMAGE: 30,
    MAX_DAMAGE: 60,
    ATTACK_SPEED: 2,
    CHANCE_TO_HIT: 0.6,
    CHANCE_TO_HEAL: 0.1,
    MIN_HEAL_POINTS: 30,
    MAX_HEAL_POINTS: 60
}

GREMLIN_CONFIGURATIONS = {
    NAME: GREMLIN,
    HIT_POINTS: 70,
    MIN_DAMAGE: 15,
    MAX_DAMAGE: 30,
    ATTACK_SPEED: 5,
    CHANCE_TO_HIT: 0.8,
    CHANCE_TO_HEAL: 0.4,
    MIN_HEAL_POINTS: 20,
    MAX_HEAL_POINTS: 40
}

SKELETON_CONFIGURATIONS = {
    NAME: SKELETON,
    HIT_POINTS: 100,
    MIN_DAMAGE: 30,
    MAX_DAMAGE: 50,
    ATTACK_SPEED: 3,
    CHANCE_TO_HIT: 0.8,
    CHANCE_TO_HEAL: 0.3,
    MIN_HEAL_POINTS: 30,
    MAX_HEAL_POINTS: 50
}

MONSTER_CONFIGS = [OGRE_CONFIGURATIONS, GREMLIN_CONFIGURATIONS, SKELETON_CONFIGURATIONS]

THIEF = "Thief"
WARRIOR = "Warrior"
PRIESTESS = "Priestess"

PILLAR_ONE = "Abstraction"
PILLAR_TWO = "Encapsulation"
PILLAR_THREE = "Inheritance"
PILLAR_FOUR = "Polymorphism"
