INSERT INTO students (name, second_name) VALUES ('Егор', 'Свитич');

INSERT INTO books (title, taken_by_student_id) VALUES 
('1984 (Оруэлл)', 22514),
('Ведьмак (Сапковский)', 22514),
('Мастер и Маргарита (Булгаков)', 22514);

INSERT INTO `groups` (title, start_date, end_date) VALUES ('Курс по автоматизации', 'январь 2026', 'август 2026');
UPDATE students SET group_id = 22200 WHERE id = 22514;

INSERT INTO subjects (title) VALUES ('Python'), ('SQL'), ('Automation');

INSERT INTO lessons (title, subject_id) VALUES 
('Классы в Python', 14242), ('ОПП в Python', 14242),
('SQL', 14243), ('Работа с базами данных в Python', 14243),
('Введение в автоматизацию тестирования', 14244), ('Работа с API', 14244);

INSERT INTO marks (value, lesson_id, student_id) VALUES 
(8, 75613, 22514), (8, 75614, 22514),
(9, 75615, 22514), (8, 75616, 22514),
(9, 75617, 22514), (8, 75618, 22514);


SELECT m.value, l.title FROM marks m INNER JOIN lessons l
ON m.lesson_id = l.id 
WHERE m.student_id = 22514; -- все оценки студента

SELECT title FROM books WHERE taken_by_student_id = 22514; -- все книги студента

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
WHERE st.id = 22514; -- полная информация о студенте (одним запросом)