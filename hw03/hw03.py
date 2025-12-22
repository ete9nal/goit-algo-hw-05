import sys
from collections import defaultdict


def parse_log_line(line: str) -> dict:
    '''
    Функція парсить строчку файлу з логами
    та ділить її на частини для обробки.
    '''
    parts = line.strip().split(" ", 3)
    # якщо строку логу в неправильному форматі - видає помилку
    if len(parts) < 4:
        raise ValueError("Invalid log format")

    # добавляє частини списку у словник за відповідними ключами
    date, time, level, message = parts
    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message
    }


def load_logs(file_path: str) -> list:
    '''
    Функція обробляє файл і використовує функцію парсингу строк
    для додавання інформації у список словників.
    '''
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    '''
    Функція фільтрує список словників та повертає список словників
    відфільтрований за рівнем помилки.
    '''
    level = level.upper()
    return list(filter(lambda log: log["level"] == level, logs))


def count_logs_by_level(logs: list) -> dict:
    '''
    Функція підраховує кількість логів за помилками та повертає словник,
    де ключ - тип помилки, а значення - кількість таких помилок у файлі логів.
    '''
    # створюємо спеціальний словник, який автоматично створює значення за ключем
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return dict(counts)


def display_log_counts(counts: dict):
    '''
    Функція виводить структуру для прінта помилок.
    '''
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def main():
    # якщо аргументів менше двух - видає помилку та виходить
    if len(sys.argv) < 2:
        print("Usage: python hw03.py <logfile> [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    if len(sys.argv) > 2:
        level = sys.argv[2]
    else:
        level = None

    logs = load_logs(file_path)

    counts = count_logs_by_level(logs)
    display_log_counts(counts)
    
    if level:
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
