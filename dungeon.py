from room import Room
from constants import *
from monster_factory import MonsterFactory
import random
from queue import Queue


class Dungeon:
    """Class representing the dungeon."""

    def __init__(self, size_x, size_y, dbFile):
        """
        Initialize the Dungeon object.

        Args:
            size_x (int): The width of the dungeon.
            size_y (int): The height of the dungeon.
            dbFile (str): The path to the database file for monster generation.
        """
        self.size_x = size_x
        self.size_y = size_y
        self.rooms = [[Room(y * size_x + x) for x in range(size_x)] for y in range(size_y)]
        self.entrance_x = None
        self.entrance_y = None
        self.exit_x = None
        self.exit_y = None
        self.monsterFactory = MonsterFactory(dbFile)
        self.prepare_dungeon()

    def prepare_dungeon(self):
        """Prepare the dungeon."""
        # Step 1: connect all the rooms to each other
        self.connect_rooms_with_no_dead_ends()

        # Step 2: set entrance and exit
        self.set_entrance_and_exit()

        # Step 3: generate dungeon items/scenes
        self.generate_dungeon_items()

        # Step 4: set pillars of oo
        self.set_pillars_of_oo()

        # Step 5: generate dead-ends
        self.generate_dead_ends()

        # Step 6: make sure the dungeon is traversable and if not regenerate dead-ends
        while not self.is_dungeon_traversable():
            self.connect_rooms_with_no_dead_ends()
            self.generate_dead_ends()

        # Step 7: Place monsters
        self.place_monsters()

    def connect_rooms_with_no_dead_ends(self):
        """Connect rooms with no dead ends."""
        for y in range(self.size_y):
            for x in range(self.size_x):
                room = self.rooms[y][x]
                room.is_dead_end = False
                if y > 0:
                    room.neighbors[NORTH] = self.rooms[y - 1][x]
                if y < self.size_y - 1:
                    room.neighbors[SOUTH] = self.rooms[y + 1][x]
                if x > 0:
                    room.neighbors[WEST] = self.rooms[y][x - 1]
                if x < self.size_x - 1:
                    room.neighbors[EAST] = self.rooms[y][x + 1]

    def set_entrance_and_exit(self):
        """Set the entrance and exit of the dungeon."""
        self.entrance_x = random.randint(0, self.size_x - 1)
        self.entrance_y = random.randint(0, self.size_y - 1)
        self.exit_x = random.randint(0, self.size_x - 1)
        self.exit_y = random.randint(0, self.size_y - 1)
        while (self.exit_x == self.entrance_x) and (self.exit_y == self.entrance_y):
            self.exit_x = random.randint(0, self.size_x - 1)
            self.exit_y = random.randint(0, self.size_y - 1)
        self.rooms[self.entrance_y][self.entrance_x].is_entrance = True
        self.rooms[self.exit_y][self.exit_x].is_exit = True

    def set_pillars_of_oo(self):
        """Set the pillars of object-oriented programming in the dungeon."""
        for pillar in PILLARS_OF_OO:
            pillar_x = random.randint(0, self.size_x - 1)
            pillar_y = random.randint(0, self.size_y - 1)
            room = self.rooms[pillar_y][pillar_x]
            while (room.pillar_of_oo is not None) or room.is_entrance_or_exit():
                pillar_x = random.randint(0, self.size_x - 1)
                pillar_y = random.randint(0, self.size_y - 1)
                room = self.rooms[pillar_y][pillar_x]
            room.pillar_of_oo = pillar

    def get_dungeon_entrance(self):
        """Get the room representing the dungeon entrance."""
        if self.entrance_x is not None or self.entrance_y is not None:
            return self.rooms[self.entrance_y][self.entrance_x]
        return None

    def get_dungeon_exit(self):
        """Get the room representing the dungeon exit."""
        if self.exit_x is not None or self.exit_y is not None:
            return self.rooms[self.exit_y][self.exit_x]
        return None

    def generate_dungeon_items(self):
        """Generate items/scenes in the dungeon rooms."""
        for row in self.rooms:
            for room in row:
                room.generate_items()

    def generate_dead_ends(self):
        """Generate dead ends in the dungeon."""
        for row in self.rooms:
            for room in row:
                if random.random() < 0.1:
                    room.make_room_dead_end()

    def is_dungeon_traversable(self):
        """Check if the dungeon is traversable."""
        return self.is_dungeon_traversable_to_pillars_before_exit() and self.is_dungeon_traversable_to_an_exit()

    def is_dungeon_traversable_to_pillars_before_exit(self):
        """Check if the dungeon is traversable to pillars before reaching the exit."""
        visited = {}
        for row in self.rooms:
            for room in row:
                visited[room.room_id] = False
        found = {}
        for pillar in PILLARS_OF_OO:
            found[pillar] = False

        queue = Queue()
        entrance_room = self.rooms[self.entrance_y][self.entrance_x]
        queue.put(entrance_room)
        while not queue.empty():
            room = queue.get()
            visited[room.room_id] = True
            if room.pillar_of_oo is not None:
                found[room.pillar_of_oo] = True
            if False not in found.values():
                return True

            current_neighbors = room.get_open_doors()
            for direction in current_neighbors:
                neighbor = room.neighbors[direction]
                if (not visited[neighbor.room_id]) and (not neighbor.is_exit):
                    queue.put(neighbor)
        return False not in found.values()

    def is_dungeon_traversable_to_an_exit(self):
        """Check if the dungeon is traversable to any exit."""
        visited = {}
        for row in self.rooms:
            for room in row:
                visited[room.room_id] = False

        queue = Queue()
        entrance_room = self.rooms[self.entrance_y][self.entrance_x]
        queue.put(entrance_room)
        while not queue.empty():
            room = queue.get()
            visited[room.room_id] = True
            if room.is_exit:
                return True

            current_neighbors = room.get_open_doors()
            for direction in current_neighbors:
                neighbor = room.neighbors[direction]
                if (not visited[neighbor.room_id]):
                    queue.put(neighbor)
        return False

    def place_monsters(self):
        """Place monsters in the dungeon."""
        for row in self.rooms:
            for room in row:
                if (not room.is_entrance_or_exit()) and (room.pillar_of_oo is not None):
                    if random.random() < 0.5:
                        monster_type = random.choice(MONSTERS)
                        room.monster = self.monsterFactory.create_monster(monster_type)
                elif not room.is_entrance_or_exit():
                    if random.random() < 0.1:
                        monster_type = random.choice(MONSTERS)
                        room.monster = self.monsterFactory.create_monster(monster_type)

    def __str__(self):
        """Return the string representation of the dungeon."""
        dungeon_str = ""
        space = ' '
        for row in self.rooms:
            for i in range(5):
                for room in row:
                    if i == 0:
                        dungeon_str += room.north_side_as_str()
                    if i == 1:
                        dungeon_str += f"{room.west_side_as_str()}{space:^{room.width}}{room.east_side_as_str()}"
                    if i == 2:
                        dungeon_str += f"{room.west_side_as_str()}{room.content_as_str():^{room.width}}{room.east_side_as_str()}"
                    if i == 3:
                        dungeon_str += f"{room.west_side_as_str()}{space:^{room.width}}{room.east_side_as_str()}"
                    if i == 4:
                        dungeon_str += room.south_side_as_str()
                dungeon_str += "\n"
        return dungeon_str

# dbFile = 'database/monsters.db'
# dungeon = Dungeon(5, 5, dbFile)
# print(dungeon)

# surrounding_info = dungeon.get_dungeon_entrance().get_surrounding_rooms_info()
# info_str = '\n'.join([f"{key} :\n{value}" for key, value in surrounding_info.items()])
# print(f"Used and got the following info:\n{info_str}")