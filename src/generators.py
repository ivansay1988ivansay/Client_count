from data import transactions


def filter_by_currency(transactions_list, currency):
    for transaction in transactions_list:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield 'Транзакция по запросу',  transaction


print(next(filter_by_currency(transactions, 'USD')))