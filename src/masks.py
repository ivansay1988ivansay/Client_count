def get_mask_card_number(cart_number: int) -> str:
    """Функция маскирует номер карты клиента, за исключением первых шести, и последних четырех цифр"""
    count = []

    str_cart_number = str(cart_number)
    disguise_cart_number = str_cart_number[:6] + "*" * (len(str_cart_number) - 10) + str_cart_number[-4:]

    for num in range(0, len(disguise_cart_number), 4):
        count.append(disguise_cart_number[num : num + 4])

    return " ".join(count)


def get_mask_account(account_number: int) -> str:
    """Функция маскирует номер счёта, оставляя только последние 4 цифры"""

    str_account_number = str(account_number)
    new_account = "**" + str_account_number[-4:]
    return new_account
