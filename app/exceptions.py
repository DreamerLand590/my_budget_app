"""Власні винятки програми. Одна назва = один тип проблеми."""


class ReportError(Exception):
    """Базова помилка нашої програми."""


class DataFileError(ReportError):
    """Файл з даними не знайдено або його не можна прочитати."""


class InvalidRowError(ReportError):
    """Рядок даних має неправильний формат."""
