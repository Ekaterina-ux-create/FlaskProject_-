import sqlite3

# Подключаемся или создаем базу данных
conn = sqlite3.connect('gifts.db')
cursor = conn.cursor()

# Создаём таблицу
cursor.execute('''
CREATE TABLE IF NOT EXISTS gifts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    gift_name TEXT NOT NULL,
    price REAL NOT NULL,
    status TEXT NOT NULL
)
''')

# Вставляем данные
gifts_data = [
    ('Иванов Иван Иванович', 'Носки', 500, 'Куплен'),
    ('Петров Петр Петрович', 'Книга', 1500, 'Не куплен'),
    ('Сидоров Сидор Сидорович', 'Чашка', 700, 'Куплен'),
    ('Кузнецов Алексей', 'Пенджак', 3000, 'Не куплен'),
    ('Смирнова Анна', 'Вино', 1200, 'Куплен'),
    ('Морозова Ирина', 'Подарочная карта', 2000, 'Не куплен'),
    ('Лебедев Олег', 'Флешка', 800, 'Куплен'),
    ('Зайцева Настя', 'Косметика', 2500, 'Не куплен'),
    ('Николаев Михаил', 'Пазлы', 600, 'Куплен'),
    ('Тихонов Сергей', 'Игрушка', 900, 'Не куплен')
]

cursor.executemany('INSERT INTO gifts (name, gift_name, price, status) VALUES (?, ?, ?, ?)', gifts_data)

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()