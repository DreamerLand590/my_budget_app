"""МОДЕЛЬ: як виглядає один запис у нашій програмі."""
from dataclasses import dataclass


@dataclass
class Expense:
    date: str
    category: str
    amount: float
