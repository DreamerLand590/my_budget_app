"""ШАР ПОКАЗУ (presentation): як результат бачить людина."""

def format_report(total: float, categories: dict[str, float], top_category: str, warnings: list[str]) -> str:
    lines = ["Звіт про витрати домашнього бюджету", "-" * 35]
    
    
    lines.append(f"Загальна сума витрат: {total:.2f} грн\n")
    
    
    lines.append("Витрати за категоріями:")
    for category, amount in sorted(categories.items()):
        lines.append(f"{category:<15} {amount:>8.2f} грн")
        
    
    lines.append(f"\nНайбільше грошей пішло на: {top_category}")
    
    
    if warnings:
        lines.append("\nПопередження (пропущені рядки):")
        lines.extend(f" - {w}" for w in warnings)
        
    return "\n".join(lines)