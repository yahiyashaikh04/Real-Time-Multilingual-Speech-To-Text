
import sqlite3
import os

DB_PATH = "instance/speech.db"


def get_connection():
    os.makedirs("instance", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS transcriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_transcription(text):
    conn = get_connection()

    conn.execute(
        "INSERT INTO transcriptions (text) VALUES (?)",
        (text,)
    )

    conn.commit()
    conn.close()


def get_transcriptions():
    conn = get_connection()

    records = conn.execute(
        "SELECT * FROM transcriptions ORDER BY id DESC"
    ).fetchall()

    conn.close()
    return records


def update_transcription(record_id, text):

    conn = get_connection()

    cursor = conn.execute(
        "UPDATE transcriptions SET text = ? WHERE id = ?",
        (text, record_id)
    )

    conn.commit()

    print("ROWS UPDATED:", cursor.rowcount)

    conn.close()


def delete_transcription(record_id):
    conn = get_connection()

    conn.execute(
        "DELETE FROM transcriptions WHERE id = ?",
        (record_id,)
    )

    conn.commit()
    conn.close()
