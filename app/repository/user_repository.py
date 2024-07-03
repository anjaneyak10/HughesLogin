from app.extensions import get_db

class UserRepository:

    @staticmethod
    def find_by_username(username):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT email, name, username, role, function, hashedpassword
            FROM usermaster WHERE username = %s
        """, (username,)) #
        user = cur.fetchone()
        cur.close()
        if user:
            return {
                'email': user[0],
                'name': user[1],
                'username': user[2],
                'role': user[3],
                'function': user[4],
                'password_hash': user[5]

            }
        return None

    @staticmethod
    def save(email, name, username, role, function,password_hash):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO usermaster (email, name, username, role, function, hashedpassword)
            VALUES (%s, %s, %s, %s, %s,%s ) RETURNING email
        """, (email, name, username, role, function, password_hash))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        return user_id
