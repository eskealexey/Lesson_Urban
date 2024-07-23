import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMERY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

for x in range(1, 11):
    cursor.execute('INSERT INTO Users(id, username, email, age, balance) VALUES (?, ?, ?, ?, ?)',
                   (x, f'User{x}', f'example{x}@gmail.com', f'{x * 10}', f'1000'))

for x in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, x))

for x in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (x,))

cursor.execute('SELECT * FROM Users WHERE age != ?', (60,))
results = cursor.fetchall()
for result in results:
    print(f"Имя: {result[1]} | Почта: {result[2]} | Возраст: {result[3]} | Баланс: {result[4]}")

connection.commit()
connection.close()
