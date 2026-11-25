"""Точка входу. Запуск з кореня проєкту: python main.py
main.py лише з'єднує шари (дані -> логіка -> показ) і ловить помилки."""
import sys

from app import config
from app.data_loader import load_expenses
from app.exceptions import DataFileError
from app.report import format_report
from app.services import calculate_total, group_by_category, biggest_category

def main() -> int:
    try:
        
        expenses, warnings = load_expenses(config.DATA_FILE)
        
        
        total = calculate_total(expenses)
        categories = group_by_category(expenses)
        top_category = biggest_category(categories)
        
    except DataFileError as error:
        print(f"Помилка: {error}")
        return 1
    except ValueError as error:
        print(f"Не вдалося порахувати: {error}")
        return 1

    if not expenses:
        print("Немає даних для аналізу (всі рядки помилкові).")
        return 0

    
    text = format_report(total, categories, top_category, warnings)
    print(text)
    
    
    config.REPORT_FILE.parent.mkdir(exist_ok=True)
    config.REPORT_FILE.write_text(text, encoding="utf-8")
    
    
    print(f"\nЗвіт збережено: {config.REPORT_FILE.relative_to(config.BASE_DIR)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())