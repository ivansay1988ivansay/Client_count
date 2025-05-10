
# Банковские транзакции - обработка данных

Проект предоставляет набор инструментов для работы с банковскими транзакциями:

## Функционал

### 1. Генераторы (`generators.py`)
- `filter_by_currency(transactions, currency)` - фильтрует транзакции по валюте (USD/RUB)
- `transaction_descriptions(transactions)` - извлекает описания транзакций
- `card_number_generator(start, end)` - генерирует номера карт в формате "XXXX XXXX XXXX XXXX"

### 2. Обработка данных (`processing.py`)
- `filter_by_state(operations, state)` - фильтрует операции по статусу (EXECUTED/CANCELED)
- `sort_by_date(operations, reverse)` - сортирует операции по дате

### 3. Утилиты (`widget.py`)
- `mask_account_card(data)` - маскирует номера карт/счетов
- `get_date(date_str)` - форматирует дату в вид DD.MM.YYYY