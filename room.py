import random
from constants import *


class Room:
    """A class representing a room in the dungeon."""

    def __init__(self, room_id):
        """
        Initialize a room with the given ID.

        :param room_id: The ID of the room.
        """
        self.room_id = room_id
        self.neighbors = {
            NORTH: WALL,
            SOUTH: WALL,
            EAST: WALL,
            WEST: WALL
        }
        self.pillar_of_oo = None
        self.is_entrance = False
        self.is_exit = False
        self.items = {
            HEALING_POTION: None,
            VISION_POTION: None,
            PIT: None
        }
        self.monster = None
        self.is_dead_end = False
        self.player_is_in_room = False

        self.width = 10
        self.horizontal_wall = "*" * (self.width + 2)
        self.horizontal_door = "*" + ("-" * self.width) + "*"
        self.vertical_wall = "*"

    def generate_items(self):
        """Generate items in the room."""
        if not self.is_entrance_or_exit():
            # Healing potion, vision potion, and pit with 10% probability each
            if random.random() < 0.1:
                self.generate_healing_potion()
            if random.random() < 0.1:
                self.generate_vision_potion()
            if random.random() < 0.1:
                self.generate_pit()

    def generate_healing_potion(self):
        """Generate a healing potion."""
        # Healing potion heals 5-15 hit points
        healing_amount = random.randint(5, 15)
        self.items[HEALING_POTION] = healing_amount

    def generate_vision_potion(self):
        """Generate a vision potion."""
        # Vision potion allows the user to see surrounding rooms
        vision_info = self.get_surrounding_rooms_info()
        self.items[VISION_POTION] = vision_info

    def generate_pit(self):
        """Generate a pit."""
        # Pit damage is from 1-20 hit points
        pit_damage = random.randint(1, 20)
        self.items[PIT] = pit_damage

    def make_room_dead_end(self):
        """Make the room a dead-end."""
        if self.is_dead_end:
            print(f"Room: {self.room_id} is already a dead-end")
        current_doors = self.get_open_doors()

        if len(current_doors) == 0:
            print(f"Room: {self.room_id} has wrong dead-end configuration")
            return 0

        if self.is_entrance_or_exit():
            return

        if len(current_doors) == 1 and not self.is_dead_end:
            self.is_dead_end = True
        else:
            door = current_doors[random.randint(0, len(current_doors) - 1)]
            current_doors.remove(door)
            for direction in current_doors:
                neighbor = self.neighbors[direction]
                neighbors_open_doors = neighbor.get_open_doors()

                if neighbor.check_dead_end() and (neighbors_open_doors[0] == OPPOSITE_DIRECTION[direction]):
                    return
                self.neighbors[direction] = WALL
                self.is_dead_end = True
                neighbor.neighbors[OPPOSITE_DIRECTION[direction]] = WALL

    def get_open_doors(self):
        """Get the directions of the open doors in the room."""
        return [direction for direction, room in self.neighbors.items() if room != WALL]

    def check_dead_end(self):
        """Check if the room is a dead-end."""
        if self.is_dead_end:
            return True
        else:
            current_doors = self.get_open_doors()
            return len(current_doors) == 1

    def has_any_items(self):
        """Check if the room has any items."""
        return any(value != None for _, value in self.items.items())

    def is_entrance_or_exit(self):
        """Check if the room is an entrance or exit."""
        return self.is_entrance or self.is_exit

    def get_surrounding_rooms_info(self):
        """Get information about surrounding rooms."""
        surrounding_rooms = {}
        for direction, room in self.neighbors.items():
            if room:
                surrounding_rooms[direction] = room
        return surrounding_rooms

    def display_info(self):
        """Display information about the room."""
        print(
            f"Room {self.room_id} - Doors: {', '.join([key for key, value in self.neighbors.items() if value != WALL])}")
        if self.items:
            for item_name, item_value in self.items.items():
                if item_name == VISION_POTION:
                    print(f"{item_name}: {item_value}")
                else:
                    print(f"{item_name}: {item_value} hit points")
        if self.is_entrance:
            print("Entrance")
        if self.is_exit:
            print("Exit")
        if self.pillar_of_oo:
            print(f"Pillar of OO: {self.pillar_of_oo}")
        print("\n")

    def north_side_as_str(self):
        """Return the string representation of the north side of the room."""
        return self.horizontal_door if self.neighbors[NORTH] != WALL else self.horizontal_wall

    def south_side_as_str(self):
        """Return the string representation of the south side of the room."""
        return self.horizontal_door if self.neighbors[SOUTH] != WALL else self.horizontal_wall

    def west_side_as_str(self):
        """Return the string representation of the west side of the room."""
        return "|" if self.neighbors[WEST] != WALL else self.vertical_wall

    def east_side_as_str(self):
        """Return the string representation of the east side of the room."""
        return "|" if self.neighbors[EAST] != WALL else self.vertical_wall

    def content_as_str(self):
        """Return the string representation of the content of the room."""
        center_content = []  # Default is an empty room

        if self.is_entrance:
            center_content.append('<i>')
        elif self.is_exit:
            center_content.append('^O^')
        else:
            if self.pillar_of_oo:
                center_content.append('$' + self.pillar_of_oo[0])
            if self.items[VISION_POTION]:
                center_content.append('V')
            if self.items[HEALING_POTION]:
                center_content.append('H')
            if self.items[PIT]:
                center_content.append('X')
            if self.is_dead_end:
                center_content.append('#')
            if self.monster is not None:
                if self.monster.name == OGRE:
                    center_content.append('m_O')
                elif self.monster.name == GREMLIN:
                    center_content.append('m_G')
                else:
                    center_content.append('m_S')
        if self.player_is_in_room:
            center_content.append(':)')

        return ",".join(center_content)

    def __str__(self):
        """Return the string representation of the room."""
        return f"{self.north_side_as_str()}\n{self.west_side_as_str()}{self.content_as_str():^{self.width}}\
{self.east_side_as_str()}\n{self.south_side_as_str()}"

# room = Room(2)
# room.generate_items()
# print(room)
