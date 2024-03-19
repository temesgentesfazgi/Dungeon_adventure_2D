import sqlite3
from constants import MONSTER_CONFIGS, NAME


class SQLHelper:
    """A class to handle SQLite database operations."""

    def __init__(self, dbFile):
        """
        Initialize the SQLHelper object.

        :param dbFile: Path to the SQLite database file.
        """
        self.dbFile = dbFile

    def __create_connection(self):
        """
        Create a connection to the SQLite database.

        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(self.dbFile)
        except Exception as e:
            print(e)

        return conn

    def create_monsters_table(self):
        """
        Create the Monsters table in the database if it doesn't exist.
        """
        conn = None
        try:
            conn = self.__create_connection()
            cursor = conn.cursor()

            # Check if Monsters table already exists
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Monsters'")

            if not cursor.fetchone():
                # Table does not exist, create it
                cursor.execute('''CREATE TABLE Monsters (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT,
                                    hit_points INTEGER,
                                    attack_speed REAL,
                                    chance_to_hit REAL,
                                    min_damage INTEGER,
                                    max_damage INTEGER,
                                    chance_to_heal REAL,
                                    min_heal_points INTEGER,
                                    max_heal_points INTEGER
                                )''')

                # Commit changes
                conn.commit()

                print("Monsters table created successfully.")
            else:
                print("Monsters table already exists.")

        except sqlite3.Error as e:
            print("Error creating Monsters table:", e)
        finally:
            if conn:
                conn.close()

    def load_monster_configs_from_db(self):
        """
        Load monster configurations from the Monsters table in the database.

        :return: Dictionary containing monster configurations.
        """
        monsters = {}
        conn = None
        try:
            conn = self.__create_connection()
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Monsters")
            rows = cursor.fetchall()
            for row in rows:
                # Convert each sqlite3.Row object to a dictionary to avoid pickle errors
                dict_row = dict(row)
                monsters[row[NAME]] = dict_row
        except sqlite3.Error as e:
            print("Error fetching monsters:", e)
        finally:
            if conn:
                conn.close()
        return monsters

    def insert_all_monster_configs_to_db(self):
        """
        Insert all monster configurations into the Monsters table in the database.
        """
        conn = None
        try:
            table = "Monsters"
            conn = self.__create_connection()
            cursor = conn.cursor()
            for configDict in MONSTER_CONFIGS:
                placeholders = ', '.join(['?'] * len(configDict))
                columns = ', '.join(configDict.keys())
                sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table, columns, placeholders)
                cursor.execute(sql, list(configDict.values()))
                conn.commit()
        except Exception as e:
            print("Error inserting monsters:", e)
        finally:
            if conn:
                conn.close()
