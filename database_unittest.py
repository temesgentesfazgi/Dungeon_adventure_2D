import unittest
import sqlite3

class TestDatabase(unittest.TestCase):
<<<<<<< HEAD
    """Test case for the database."""

    def setUp(self):
        """Set up the test environment."""
=======
    def setUp(self):
>>>>>>> 523f50714d35007a90dac8de3a3ffb54debf5c40
        # Connect to the testing database
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

        # Create tables and insert test data
        self.cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
        self.cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
        self.cursor.execute("INSERT INTO users (name) VALUES ('Bob')")
        self.conn.commit()

    def tearDown(self):
<<<<<<< HEAD
        """Tear down the test environment."""
=======
>>>>>>> 523f50714d35007a90dac8de3a3ffb54debf5c40
        # Close the connection and clean up
        self.cursor.close()
        self.conn.close()

    def test_user_count(self):
<<<<<<< HEAD
        """Test the count of users in the database."""
=======
>>>>>>> 523f50714d35007a90dac8de3a3ffb54debf5c40
        # Check the number of users in the database
        self.cursor.execute('SELECT COUNT(*) FROM users')
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 2)

    def test_user_names(self):
<<<<<<< HEAD
        """Test the names of specific users."""
=======
>>>>>>> 523f50714d35007a90dac8de3a3ffb54debf5c40
        # Check if specific users exist in the database
        self.cursor.execute("SELECT name FROM users WHERE id = 1")
        user1 = self.cursor.fetchone()[0]
        self.assertEqual(user1, 'Alice')

        self.cursor.execute("SELECT name FROM users WHERE id = 2")
        user2 = self.cursor.fetchone()[0]
        self.assertEqual(user2, 'Bob')

<<<<<<< HEAD

=======
>>>>>>> 523f50714d35007a90dac8de3a3ffb54debf5c40
if __name__ == '__main__':
    unittest.main()
