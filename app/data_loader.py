"""ШАР ДАНИХ: читає файл і перетворює рядки на об'єкти Request.
Тільки тут програма знає, що дані лежать саме в CSV."""
"""ЗАВАНТАЖЕННЯ ДАНИХ: читає файл і перетворює рядки на об'єкти Expense."""
import csv
from pathlib import Path

from app.exceptions import DataFileError, InvalidRowError
from app.models import Expense 


def parse_row(row: dict) -> Expense:
    """Один рядок CSV -> Expense. Якщо щось не так, піднімаємо InvalidRowError."""
    try:
        
        amount = float(row["amount"])
    except KeyError as error:
        raise InvalidRowError("немає стовпця amount") from error
    except ValueError as error:
        raise InvalidRowError(f"amount не число: {row['amount']!r}") from error

    
    if amount < 0:
        raise InvalidRowError(f"від'ємна сума витрат: {amount}")

    
    return Expense(
        date=row["date"],
        category=row["category"],
        amount=amount
    )


def load_expenses(path: Path) -> tuple[list[Expense], list[str]]:
    """Повертає (добрі записи, попередження про пропущені рядки)."""
    try:
        with open(path, encoding="utf-8", newline="") as file:
            rows = list(csv.DictReader(file))
    except FileNotFoundError as error:
        
        raise DataFileError(f"Файл не знайдено: {path}") from error

    expenses, warnings = [], []
    for line_number, row in enumerate(rows, start=2):  
        try:
            expenses.append(parse_row(row))
        except InvalidRowError as error:
            warnings.append(f"рядок {line_number}: {error}, пропущено")
            
    return expenses, warnings