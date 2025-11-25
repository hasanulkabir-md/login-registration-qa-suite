# db-validation/tests_db_validation.py
import sqlite3

def test_user_present_in_db():
    # Change this path to your real database file
    conn = sqlite3.connect("data/users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT email FROM users WHERE email = ?", ("user@example.com",))
    row = cursor.fetchone()

    conn.close()

    assert row is not None
