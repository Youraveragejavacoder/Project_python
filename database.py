import hashlib

# Add this function to hash passwords securely (simple example):
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

class Database:
    # ... your existing code ...

    def create_tables(self):
        cursor = self.conn.cursor()
        # existing tables here ...

        # New table for user credentials
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id_number TEXT PRIMARY KEY,
                password_hash TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def user_exists(self, id_number):
        cursor = self.conn.cursor()
        cursor.execute('SELECT 1 FROM users WHERE id_number = ?', (id_number,))
        return cursor.fetchone() is not None

    def add_user(self, id_number, password):
        password_hash = hash_password(password)
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO users (id_number, password_hash) VALUES (?, ?)', (id_number, password_hash))
        self.conn.commit()

    def validate_user(self, id_number, password):
        password_hash = hash_password(password)
        cursor = self.conn.cursor()
        cursor.execute('SELECT password_hash FROM users WHERE id_number = ?', (id_number,))
        row = cursor.fetchone()
        if row is None:
            return False
        return row[0] == password_hash
