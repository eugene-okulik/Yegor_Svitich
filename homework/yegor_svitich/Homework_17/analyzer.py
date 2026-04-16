import os
import argparse
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(description='Find logs by text')
    parser.add_argument('path', help='Full path to the directory or file with logs')
    parser.add_argument('-t', '--text', required=True, help='Text to find in logs')
    return parser.parse_args()


def get_date_from_line(line_content):
    # Извлечение даты в начале строки, если она там есть
    if len(line_content) >= 23:
        date_candidate = line_content[:23]
        try:
            # Распознавание даты (формат ISO, например 2026-04-15 13:03:00)
            datetime.fromisoformat(date_candidate.replace(',', '.'))  # замена для поддержки разных форматов
            return date_candidate
        except ValueError:
            pass
    return None


def get_context(text, word, words_quantity=5):
    # Нахождение слова и возвращение 5 слов до и 5 после
    words = text.split()
    if word not in words:
        try:
            idx = next(i for i, w in enumerate(words) if word in w)
        except StopIteration:
            return text[:50] + "..."
    else:
        idx = words.index(word)

    start = max(0, idx - words_quantity)
    end = min(len(words), idx + words_quantity + 1)
    return " ".join(words[start:end])


def main():
    args = parse_args()
    file_path = args.path
    word_to_find = args.text

    # Формирование списка файлов
    if os.path.isdir(file_path):
        files = [os.path.join(file_path, file_name) for file_name in os.listdir(file_path)
                 if file_name.endswith('.log')]
        files.sort()
    elif os.path.isfile(file_path):
        files = [file_path]
    else:
        print(f"Ошибка: Путь {file_path} не найден.")
        return

    for file in files:
        data = {}
        current_date_key = None

        try:
            with open(file, encoding='utf-8') as log_file:
                for line in log_file:
                    line_date = get_date_from_line(line)

                    if line_date:
                        current_date_key = line_date
                        data[current_date_key] = line.strip()
                    elif current_date_key:
                        data[current_date_key] += " " + line.strip()

            # Анализ собранных логов в файле
            for key, entry in data.items():
                if word_to_find in entry:
                    context = get_context(entry, word_to_find)
                    filename = os.path.basename(file)
                    print(f"[{filename}] | Время: {key}")
                    print(f"Фрагмент: ...{context}...")
                    print("-" * 40)

        except Exception as e:
            print(f"Не удалось прочитать файл {file}: {e}")


if __name__ == "__main__":
    main()
