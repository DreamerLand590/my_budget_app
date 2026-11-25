"""Тести живуть окремо від коду. Запуск з кореня проєкту: python -m pytest -q"""
import pytest

from app.models import Expense
from app.services import calculate_total, group_by_category, biggest_category

def test_calculate_total():
    
    expenses = [
        Expense("2026-11-01", "Їжа", 100.0), 
        Expense("2026-11-02", "Транспорт", 50.0)
    ]
    
    assert calculate_total(expenses) == 150.0

def test_group_by_category():
    
    expenses = [
        Expense("2026-11-01", "Їжа", 100.0), 
        Expense("2026-11-02", "Їжа", 50.0),
        Expense("2026-11-03", "Транспорт", 20.0)
    ]
    
    expected = {"Їжа": 150.0, "Транспорт": 20.0}
    assert group_by_category(expenses) == expected

def test_biggest_category():
    
    totals = {"Їжа": 150.0, "Транспорт": 50.0, "Розваги": 200.0}
    assert biggest_category(totals) == "Розваги"