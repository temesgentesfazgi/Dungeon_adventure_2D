from dungeon import Dungeon
from gui_view import GuiView


if __name__ == "__main__":
    dbFile = 'database/monsters.db'
    dungeon = Dungeon(5, 5, dbFile)
    view = GuiView(dungeon)
    view.draw_loop()