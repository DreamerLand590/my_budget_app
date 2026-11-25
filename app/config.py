"""Налаштування та шляхи. Усі шляхи будуємо від місця, де лежить проєкт,
тому програма працює, звідки б її не запустили."""
from pathlib import Path

# config.py лежить у app/, тож корінь проєкту на рівень вище
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "expenses.csv"
REPORT_FILE = BASE_DIR / "output" / "report.txt"

(BASE_DIR / "output").mkdir(exist_ok=True)