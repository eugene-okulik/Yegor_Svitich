import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()

# 1. Добавление студента
cursor.execute("INSERT INTO students (name, second_name) VALUES (%s, %s)", ('Егор', 'Свитич'))
student_id = cursor.lastrowid
print(f"Создан студент с ID: {student_id}")

# 2. Добавление группы
cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
    ('Курс по автоматизации', 'январь 2026', 'август 2026')
)
group_id = cursor.lastrowid
print(f"Создана группа с ID: {group_id}")

# 3. Обновление группы у студента с использованием полученных id
cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))

# 4. Добавление книг студенту
books = [('1984 (Оруэлл)',), ('Ведьмак (Сапковский)',), ('Мастер и Маргарита (Булгаков)',)]
for book in books:
    cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
                   (book[0], student_id))

# 5. Добавление предметов и сохранение их id в словарь
subjects = ['Python', 'SQL', 'Automation']
subject_ids = {}
for subject in subjects:
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", (subject,))
    subject_ids[subject] = cursor.lastrowid

# 6. Добавление уроков и привязывание их к предметам
lessons_to_add = [
    ('Классы в Python', subject_ids['Python']),
    ('ОПП в Python', subject_ids['Python']),
    ('SQL', subject_ids['SQL']),
    ('Работа с базами данных в Python', subject_ids['SQL']),
    ('Введение в автоматизацию тестирования', subject_ids['Automation']),
    ('Работа с API', subject_ids['Automation'])
]

lesson_ids = []
for title, subject_id in lessons_to_add:
    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", (title, subject_id))
    lesson_ids.append(cursor.lastrowid)

# 7. Выставление оценок за уроки (8, 8, 9, 8, 9, 8)
marks_values = [8, 8, 9, 8, 9, 8]
for value, lesson_id in zip(marks_values, lesson_ids):
    cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
                   (value, lesson_id, student_id))

db.commit()

print("\n--- Все оценки студента ---")
query = """
    SELECT m.value, l.title FROM marks m INNER JOIN lessons l
    ON m.lesson_id = l.id
    WHERE m.student_id = %s
"""
cursor.execute(query, (student_id,))

for result in cursor.fetchall():
    print(f"Оценка: {result[0]} | Урок: {result[1]}")

print("\n--- Все книги студента ---")
cursor.execute("SELECT title FROM books WHERE taken_by_student_id = %s", (student_id,))
for (title,) in cursor.fetchall():
    print(f"Книга: {title}")

print("\n--- Полная информация о студенте (одним запросом) ---")
query = """
    SELECT st.name, st.second_name, st.group_id, g.title, g.start_date, g.end_date, b.title, m.value, l.title, s.title 
    FROM students st
    INNER JOIN `groups` g
    ON st.group_id = g.id
    INNER JOIN books b
    ON st.id = b.taken_by_student_id
    INNER JOIN marks m
    ON m.student_id  = st.id
    INNER JOIN lessons l
    ON m.lesson_id = l.id
    INNER JOIN subjects s
    ON l.subject_id = s.id
    WHERE st.id = %s
"""
cursor.execute(query, (student_id,))

for result in cursor.fetchall():
    print(f"Студент: {result[0]} {result[1]} | Группа: {result[2]} '{result[3]}', {result[4]} - {result[5]} | "
          f"Книга: {result[6]} | Оценка: {result[7]} | Урок: {result[8]} | Предмет: {result[9]}")

db.close()
