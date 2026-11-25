"""ШАР ЛОГІКИ: рахує. Не знає ні про файли, ні про print.
Тому цю саму функцію можна викликати з консолі, зі Streamlit чи з API."""
from collections import defaultdict

from app.models import Expense

def calculate_total(expenses: list[Expense]) -> float:
    """Рахує загальну суму всіх витрат."""
    return sum(item.amount for item in expenses)

def group_by_category(expenses: list[Expense]) -> dict[str, float]:
    """Групує витрати за категоріями і рахує суму для кожної."""
    groups = defaultdict(float)
    for item in expenses:
        groups[item.category] += item.amount
    return dict(groups)

def biggest_category(totals: dict[str, float]) -> str:
    """Знаходить категорію з найбільшими витратами."""
    if not totals:
        
        raise ValueError("немає даних для аналізу категорій")
    return max(totals, key=totals.get)