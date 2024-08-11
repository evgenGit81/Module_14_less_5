import sqlite3


def initiate_db():
    connection = sqlite3.connect("botdb.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)
    """)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_title ON Products (title)")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY, 
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL)    
    """)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
    connection.commit()
    connection.close()

def add_user(username, email, age, balance):
    connection = sqlite3.connect("botdb.db")
    cursor = connection.cursor()
    # balance = 1000
    cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES (? , ? , ?, ?)",
                   (username, email, age, balance))
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect("botdb.db")
    cursor = connection.cursor()
    chuser = cursor.execute(f"SELECT username FROM Users WHERE username=?", (username, )).fetchone()
    if chuser is None:
        chuser = False
    else:
        chuser = True
    connection.commit()
    connection.close()
    return chuser

def get_all_products():
    connection = sqlite3.connect("botdb.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    total = cursor.fetchall()
    connection.commit()
    connection.close()
    return total

initiate_db()
# print(is_included('evgen'))
# add_user('evgen', 'evgen@mail.ru', 23)