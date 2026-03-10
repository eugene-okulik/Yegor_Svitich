class Book:
    page_material = "бумага"
    has_text = True

    def __init__(self, title, author, page_count, isbn, is_reserved=False):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.is_reserved = is_reserved

    def get_details(self):
        details = (f"Название: {self.title}, автор: {self.author}, страниц: {self.page_count}, "
                   f"материал: {self.page_material}")
        if self.is_reserved:
            details += ", зарезервирована"
        return details

class SchoolBook(Book):
    def __init__(self, title, author, page_count, subject, grade, has_tasks=False, is_reserved=False):
        super().__init__(title, author, page_count, isbn=None, is_reserved=is_reserved)
        self.subject = subject
        self.grade = grade
        self.has_tasks = has_tasks

    def get_details(self):
        details = (f"Название: {self.title}, автор: {self.author}, страниц: {self.page_count}, "
                   f"предмет: {self.subject}, класс: {self.grade}")
        if self.is_reserved:
            details += ", зарезервирована"
        return details

books = [
    Book("Идиот", "Достоевский", 500, "978-5-389-04715-0"),
    Book("Мастер и Маргарита", "Булгаков", 480, "978-5-17-083049-7"),
    Book("1984", "Оруэлл", 320, "978-5-17-080085-8"),
    Book("Ведьмак", "Сапковский", 350, "978-5-17-080982-0"),
    Book("Маленький принц", "Экзюпери", 120, "978-5-699-52854-7")
]

books[3].is_reserved = True

print("--- Список художественных книг ---")
for book in books:
    print(book.get_details())

schoolbooks = [
    SchoolBook("Алгебра", "Иванов", 200, "математика", 9, True),
    SchoolBook("История нового времени", "Петров", 350, "история",
               10, False),
    SchoolBook("Физика", "Сидоров", 250, "физика", 8, True)
]

schoolbooks[1].is_reserved = True

print("\n--- Список учебников ---")
for schoolbook in schoolbooks:
    print(schoolbook.get_details())
