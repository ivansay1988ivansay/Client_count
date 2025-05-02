from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(client_data: str) -> str:
    '''Функция маскирует номер карты клиента'''
    client_data_divided = client_data.rsplit(" ", 1)
    if client_data_divided[0].startswith("Счет"):
        return client_data_divided[0] + " " + get_mask_account(client_data_divided[1])
    else:
        return client_data_divided[0] + " " + get_mask_card_number(client_data_divided[1])


def get_date(date: str) -> str:
    '''Функция преобразует дату проведения операции'''
    date = "2024-03-11T02:26:18.671407"
    modif_date = date[:10]
    return modif_date[8:10] + "." + modif_date[5:7] + "." + modif_date[0:4]

if __name__ == "__main__":
    print(mask_account_card("Visa Gold 5999414228426300"))
    print(mask_account_card("Счет 73654108430135874305"))