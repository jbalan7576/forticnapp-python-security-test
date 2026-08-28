import sqlite3

DATABASE = "users.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT,
            password TEXT
        )
    """)

    connection.execute(
        "INSERT OR IGNORE INTO users VALUES ('admin', 'admin')"
    )

    connection.commit()
    connection.close()


def find_user(username):
    connection = get_connection()

    # INTENTIONALLY VULNERABLE: CWE-89 SQL Injection
    query = "SELECT username, password FROM users WHERE username = '" + username + "'"

    cursor = connection.execute(query)
    result = cursor.fetchone()

    connection.close()

    return result