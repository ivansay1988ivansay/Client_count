from data import transactions


def filter_by_currency(transactions_list, currency):
    '''Функция возвращает список транзакций, с указанным типом валюты в запросе'''
    for transaction in transactions_list:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield 'Транзакция по запросу',  transaction


# print(next(filter_by_currency(transactions, 'USD')))

def transaction_descriptions(transactions_list):
    '''Функция по запросу возвращает описание одной транзакции за один запрос'''
    for transaction in transactions_list:
        yield transaction["description"]


def card_number_generator(start, end):
    '''Функция-генератор, для создания номеров карт, разделенных по блокам из 4 символов'''
    counter = start
    while counter <= end:
        number_str = str(counter)
        full_number = '0' * (16 - len(number_str)) + number_str
        divided_number = ' '.join([full_number[i:i+4] for i in range(0, 16, 4)])
        yield divided_number
        counter += 1


for card in card_number_generator(1, 100):
    print(card)


if __name__ == "__main__":
    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
        print(next(descriptions))

print(card_number_generator(1, 7))