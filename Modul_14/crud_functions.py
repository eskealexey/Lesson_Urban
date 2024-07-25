import sqlite3


connection = sqlite3.connect('initiate_db.db')
cursor = connection.cursor()
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
)
''')


# for a in range(1, 5):
#     cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
#                    (f'Продукт {a}', f'Описание {a}', f'{a * 100}'))
# connection.commit()
def get_all_products():
    cursor.execute('SELECT * FROM Products;')
    result = cursor.fetchall()
    connection.commit()
    return result


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT,
    age INTEGER,
    balance INTEGER DEFAULT 1000
)
    ''')
    connection.commit()


def is_included(username):
    cursor.execute('SELECT COUNT(username) FROM Users WHERE username = ?', (username,))
    count = cursor.fetchone()
    if count[0] > 0:
        return True
    else:
        return False


def add_user(username, email, age):
    if not is_included(username):
        cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', (username, email, age))
        connection.commit()


initiate_db()
