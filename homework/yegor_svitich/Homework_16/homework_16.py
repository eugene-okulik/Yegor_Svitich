import os
import csv
import mysql.connector as mysql
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor()

base_path = os.path.dirname(__file__)
print(base_path)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
print(eugene_file_path)

with open(eugene_file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    for row in file_data:
        query = """
            SELECT st.name, st.second_name, g.title, b.title, s.title, l.title, m.value
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
            WHERE st.name = %s AND second_name = %s
            AND g.title = %s AND b.title = %s
            AND s.title = %s
            AND l.title = %s AND m.value = %s;
        """
        values = (
            row['name'], row['second_name'], row['group_title'],
            row['book_title'], row['subject_title'],
            row['lesson_title'], row['mark_value']
        )
        cursor.execute(query, values)
        result = cursor.fetchone()
        if result is None:  # данных в базе нету
            value = list(row.values())
            print(f"Данных не хватает в базе:\nСтудент: {value[0]} {value[1]} | Группа: {value[2]} | "
                  f"Книга: {value[3]} | Предмет: {value[4]} | Урок: {value[5]} | Оценка: {value[6]}")

db.close()
