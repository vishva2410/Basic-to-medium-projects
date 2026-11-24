import sqlite3

def create_connection():
    conn = sqlite3.connect('theatre_ranking.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            scope TEXT,
            seat_comfort REAL,
            ac_quality REAL,
            availability REAL,
            projection_quality INTEGER CHECK (projection_quality IN (2, 4, 8)),
            type TEXT,
            rating REAL NOT NULL
        );
    ''')

    conn.commit()
    conn.close()

def add(name, scope, seat_comfort, ac_quality, availability, projection_quality, type, rating):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO movies (name, scope, seat_comfort, ac_quality, availability, projection_quality, type, rating)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    ''', (name, scope, seat_comfort, ac_quality, availability, projection_quality, type, rating))

    conn.commit()
    conn.close()

def delete(name):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM movies WHERE name = ?;
    ''', (name,))

    conn.commit()
    conn.close()

def best_theatre():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT name, rating FROM movies ORDER BY rating DESC LIMIT 1;
    ''')

    result = cursor.fetchone()
    conn.close()
    return result

def best_theatre_by_type(theatre_type):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT name, rating FROM movies WHERE type = ? ORDER BY rating DESC LIMIT 1;
    ''', (theatre_type,))

    result = cursor.fetchone()
    conn.close()
    return result

def best_theatre_by_projection_quality(projection_quality):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT name, rating FROM movies WHERE projection_quality = ? ORDER BY rating DESC LIMIT 1;
    ''', (projection_quality,))

    result = cursor.fetchone()
    conn.close()
    return result   

def largest_theatre():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT name, scope FROM movies ORDER BY scope DESC LIMIT 1;
    ''')

    result = cursor.fetchone()
    conn.close()
    return result

def largest_theatre_by_type(theatre_type):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT name, scope FROM movies WHERE type = ? ORDER BY scope DESC LIMIT 1;
    ''', (theatre_type,))

    result = cursor.fetchone()
    conn.close()
    return result

def avoid_theatre():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT name, rating FROM movies where rating < 2 ORDER BY rating ASC LIMIT 1;
    ''')

    result = cursor.fetchone()
    conn.close()
    return result

def imax_screens():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT name from movies where type = 'imax' ORDER BY rating DESC;
    ''')

    result = cursor.fetchall()
    conn.close()
    return result

def view_rankings():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM movies ORDER BY rating DESC;
    ''')

    result = cursor.fetchall()
    conn.close()

    if result:
        for movie in result:
            print(movie)
    else:
        print("No theatres found.")

