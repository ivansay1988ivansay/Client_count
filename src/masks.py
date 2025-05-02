
def get_mask_card_number(card_number: int) -> str:
    """
       Маскирует номер карты, оставляя первые 6 и последние 4 цифры
       Форматирует результат в группы по 4 цифры, разделенные пробелами

    """
    str_card = str(card_number)
    if len(str_card) < 10:
        raise ValueError("Номер карты должен содержать минимум 10 цифр")

    masked = str_card[:6] + '*' * (len(str_card) - 10) + str_card[-4:]
    # Разбиваем на группы по 4 цифры
    parts = [masked[i:i + 4] for i in range(0, len(masked), 4)]
    return ' '.join(parts)

def get_mask_account(account_number: int) -> str:
    """Функция маскирует номер счёта, оставляя только последние 4 цифры"""

    str_account_number = str(account_number)
    new_account = "**" + str_account_number[-4:]
    return new_account


if __name__ == "__main__":
     print(get_mask_card_number(1234561234567896))