import sqlite3


connection = sqlite3.connect('initiate_db.db')
cursor = connection.cursor()
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMERY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
)
''')


# for a in range(1, 5):
#     cursor.execute('INSERT INTO Products(id, title, description, price) VALUES (?, ?, ?, ?)',
#                    (a, f'Продукт {a}', f'Описание {a}', f'{a * 100}'))
# connection.commit()
def get_all_products():
    cursor.execute('SELECT * FROM Products;')
    result = cursor.fetchall()
    connection.commit()
    return result

# pruds = get_all_products()
# for prod in pruds:
#     print(prod)
