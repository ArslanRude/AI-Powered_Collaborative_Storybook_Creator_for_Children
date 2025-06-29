import sqlite3

class UserManager:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Create users table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
            (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             age INTEGER,
             preferences TEXT)''')
        
        # Create stories table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS stories
            (story_id INTEGER PRIMARY KEY AUTOINCREMENT,
             user_id INTEGER,
             story_text TEXT,
             created_at TEXT)''')
        
        self.conn.commit()

    def save_story(self, story_data):
        # Insert story into database
        self.cursor.execute('INSERT INTO stories (user_id, story_text, created_at)
                           VALUES (?, ?, CURRENT_TIMESTAMP)',
                           (story_data['user_id'], story_data['story_text']))
        self.conn.commit()

    def get_user_preferences(self, user_id):
        # Retrieve user preferences
        self.cursor.execute('SELECT preferences FROM users WHERE user_id = ?', (user_id,))
        preferences = self.cursor.fetchone()[0]
        
        return preferences

    def close_connection(self):
        self.conn.close()