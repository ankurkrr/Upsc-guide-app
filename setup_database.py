import sqlite3

def create_database():
    conn = sqlite3.connect("upsc_study_tracker.db")
    cursor = conn.cursor()

    # Table for syllabus topics
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS syllabus (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT,
        completed BOOLEAN
    )
    """)

    # Table for tracking study progress
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS study_progress (
        date TEXT,
        hours_studied REAL
    )
    """)

    # Table for UPSC questions
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT,
        question TEXT
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
