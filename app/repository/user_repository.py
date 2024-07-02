from app.extensions import get_db

class UserRepository:

    @staticmethod
    def find_by_username(username):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT id, username, password_hash FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()
        if user:
            return {'id': user[0], 'username': user[1], 'password_hash': user[2]}
        return None

    @staticmethod
    def save(username, password_hash):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING id", (username, password_hash))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        return user_id
