import sqlite3

# Подключаемся к базе данных (файл practice.db создастся автоматически)
conn = sqlite3.connect('practice.db')
cursor = conn.cursor()

# Создаём таблицу вакансий
cursor.execute('''
CREATE TABLE IF NOT EXISTS vacancies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    course TEXT NOT NULL,
    direction TEXT NOT NULL,
    contact TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Добавляем тестовые данные
test_vacancies = [
    ('Яндекс', 'Стажёр-разработчик Python', 'Работа над backend-сервисами. Требуется знание Python, SQL.', '3-4 курс', 'Программирование', 'ivan@yandex.ru'),
    ('Сбер', 'Аналитик данных', 'Работа с большими данными, SQL, Python. Опыт приветствуется.', '4 курс, магистр', 'Аналитика', 'petr@sber.ru'),
    ('Google', 'Маркетолог-стажёр', 'Помощь в запуске рекламных кампаний. Английский от B2.', '3 курс', 'Маркетинг', 'maria@google.com'),
    ('Тинькофф', 'Java-разработчик', 'Разработка микросервисов. Знание Java, Spring.', '3-4 курс', 'Программирование', 'alex@tinkoff.ru'),
    ('ВК', 'Продуктовый аналитик', 'Анализ пользовательского поведения. SQL, Tableau.', '4 курс, магистр', 'Аналитика', 'olga@vk.com'),
]

cursor.executemany('''
INSERT INTO vacancies (company, title, description, course, direction, contact)
VALUES (?, ?, ?, ?, ?, ?)
''', test_vacancies)

conn.commit()
conn.close()

print("База данных создана! Добавлено", len(test_vacancies), "тестовых вакансий.")