import unittest
from unittest.mock import patch
from io import StringIO
from room import Room
from dungeon import Dungeon
from constants import *
from monster_factory import MonsterFactory
from ogre import Ogre
from gremlin import Gremlin
from skeleton import Skeleton


class TestDungeon(unittest.TestCase):
    """A test suite for the Dungeon class."""

    def setUp(self):
        """Set up a Dungeon instance for testing."""
        self.dungeon = Dungeon(5, 5, 'database/monsters.db')

    def test_prepare_dungeon(self):
        """Test preparing the dungeon."""
        self.assertIsNotNone(self.dungeon.rooms)
        self.assertIsNotNone(self.dungeon.monsterFactory)
        self.assertIsNotNone(self.dungeon.entrance_x)
        self.assertIsNotNone(self.dungeon.entrance_y)
        self.assertIsNotNone(self.dungeon.exit_x)
        self.assertIsNotNone(self.dungeon.exit_y)

    def test_connect_rooms_with_no_dead_ends(self):
        """Test connecting rooms without dead ends."""
        self.dungeon.connect_rooms_with_no_dead_ends()
        # Check if all rooms have neighbors
        for y in range(self.dungeon.size_y):
            for x in range(self.dungeon.size_x):
                room = self.dungeon.rooms[y][x]
                self.assertTrue(all(neighbor is not None for neighbor in room.neighbors.values()))

    def test_set_entrance_and_exit(self):
        """Test setting the entrance and exit."""
        self.assertIsNotNone(self.dungeon.entrance_x)
        self.assertIsNotNone(self.dungeon.entrance_y)
        self.assertIsNotNone(self.dungeon.exit_x)
        self.assertIsNotNone(self.dungeon.exit_y)
        self.assertNotEqual((self.dungeon.entrance_x, self.dungeon.entrance_y), (self.dungeon.exit_x, self.dungeon.exit_y))

    def set_pillars_of_oo(self):
<<<<<<< HEAD
        """Set the pillars of object-oriented programming."""
=======
>>>>>>> 523f50714d35007a90dac8de3a3ffb54debf5c40
        # Initialize a set to keep track of assigned pillars
        assigned_pillars = set()

        for row in self.rooms:
            for room in row:
                # Iterate through the pillars until a unique one is found
                for pillar in PILLARS_OF_OO:
                    if pillar not in assigned_pillars:
                        room.pillar_of_oo = pillar
                        assigned_pillars.add(pillar)
                        break

    def test_get_dungeon_entrance(self):
        """Test getting the dungeon entrance."""
        entrance_room = self.dungeon.get_dungeon_entrance()
        self.assertIsNotNone(entrance_room)
        self.assertTrue(entrance_room.is_entrance)

    def test_get_dungeon_exit(self):
        """Test getting the dungeon exit."""
        exit_room = self.dungeon.get_dungeon_exit()
        self.assertIsNotNone(exit_room)
        self.assertTrue(exit_room.is_exit)

    def test_generate_dungeon_items(self):
        """Test generating dungeon items."""
        self.dungeon.generate_dungeon_items()
        # Check if all rooms have items generated
        for row in self.dungeon.rooms:
            for room in row:
                self.assertTrue(room.items)

    def test_generate_dead_ends(self):
        """Test generating dead ends."""
        self.dungeon.generate_dead_ends()
        # Check if some rooms are dead ends
        dead_ends = sum(room.is_dead_end for row in self.dungeon.rooms for room in row)
        self.assertGreater(dead_ends, 0)

    def test_is_dungeon_traversable(self):
        """Test checking if the dungeon is traversable."""
        traversable = self.dungeon.is_dungeon_traversable()
        self.assertTrue(traversable)

    def test_place_monsters(self):
        """Test placing monsters in the dungeon."""
        self.dungeon.place_monsters()
        # Check if some rooms have monsters
        monsters_placed = sum(1 for row in self.dungeon.rooms for room in row if room.monster is not None)
        self.assertGreater(monsters_placed, 0)

# if __name__ == '__main__':
#     unittest.main()
