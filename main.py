from data import transactions, operation
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card, get_date
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

print(mask_account_card("Visa Gold 5999414228426300"))

print(get_date("2024-03-11T02:26:18.671407"))

print(filter_by_state(operation))

print(sort_by_date(operation))

usd_transactions = filter_by_currency(transactions, "USD")
descriptions = transaction_descriptions(transactions)

if __name__ == "__main__":

    for _ in range(2):
        print(next(usd_transactions))


    for _ in range(5):
        print(next(descriptions))

    for card in card_number_generator(1, 100):
        print(card)