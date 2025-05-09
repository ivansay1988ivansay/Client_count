from data import transactions


def filter_by_currency(transactions_list, currency):
    for transaction in transactions_list:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield 'Транзакция по запросу',  transaction


# print(next(filter_by_currency(transactions, 'USD')))

def transaction_descriptions(transactions_list):
    for transaction in transactions_list:
        yield transaction["description"]

if __name__ == "__main__":
    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
        print(next(descriptions))