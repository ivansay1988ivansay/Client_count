import pytest

from data import transactions
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_card_number, get_mask_account
from src.processing import sort_by_date, operation, filter_by_state
from src.widget import mask_account_card, get_date
from тренеровочка import fuf, add


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (5999414228426353, "5999 41** **** 6353"),
        (36159852478526, "3615 98** **85 26"),
        (12345678901234567890, "1234 56** **** **** 7890"),
    ],
)
def test_parametrize_get_mask_card_number(card_number, expected):
    """Тест на работу функции с разной длинной карты"""
    assert get_mask_card_number(card_number) == expected


def test_short_card_number():
    """Тест на обработку слишком короткого номера карты"""
    with pytest.raises(ValueError, match="Номер карты должен содержать минимум 10 цифр"):
        get_mask_card_number(12345678)


@pytest.mark.parametrize(
    "account_number, expected",
    [
        # Стандартные проверки
        (1234567890123456, "**3456"),
        (9999999999999999, "**9999"),
        (1000000000000004, "**0004"),
        # Проверки счёта разной длины
        (123467, "**3467"),
        (123455567890, "**7890"),
        (12345678901234567890, "**7890"),
    ],
)
def test_parametrize_valid_account_numbers(account_number, expected):
    """Параметризованное тестирование правильности маскирования номера счета"""
    assert get_mask_account(account_number) == expected


def test_mask_account_card(mask_account_name_card, mask_account_name_check):
    """Стандартное тестирование mask_account_card"""
    assert mask_account_card(mask_account_name_card) == "Maestro 7000 79** **** 6361"
    assert mask_account_card(mask_account_name_check) == "Счет **4305"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        # Стандартные проверки карт
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        # Стандартные проверки номера счета
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 14569875632145698759", "Счет **8759"),
    ],
)
def test_parametrize_mask_account_card(account_number, expected):
    """Параметризованное тестирование mask_account_card"""
    assert mask_account_card(account_number) == expected


def test_mask_account_card_letters(card_number):
    assert mask_account_card(card_number) == "Название карты/счета не может начинаться с цифры"


def test_sort_by_date(list_of_operations, sorted_operation, sorted_operation_reverse):
    """Базовый тест на работу функции"""
    assert sort_by_date(list_of_operations) == sorted_operation


def test_sort_by_date_rev(not_sorted_operation, sorted_operation_reverse):
    assert sort_by_date(not_sorted_operation, False) == sorted_operation_reverse


def test_sort_by_date_missing_key():
    """Тест с операцией без ключа date"""
    invalid_ops = operation + [{"id": 1, "state": "EXECUTED"}]
    with pytest.raises(KeyError):
        sort_by_date(invalid_ops)


def test_get_date(get_date_test):
    """Базовый тест на проверку преобразования даты"""
    assert get_date(get_date_test) == "11.03.2024"


@pytest.mark.parametrize(
    "date, expected",
    [
        # Проверка граничных случаев дат
        ("2023-01-01T00:00:00.000000", "01.01.2023"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
        # Проверка нестандартных, но допустимых строк с датой
        ("2024/03/11-02/26/18", "11.03.2024"),
        ("2024/03/11", "11.03.2024"),
        # Проверка недопустимых дат
        ("1999/05", "Введите корректную дату"),
        ("wtf", "Введите корректную дату"),
    ],
)
def test_get_date_not_standard(date, expected):
    """Проверка нестандартных случаев"""
    assert get_date(date) == expected


def test_filter_by_state(list_of_operations, list_sort_by_state):
    """Базовый тест на сортировку по статусу"""
    assert filter_by_state(list_of_operations) == list_sort_by_state


def test_filter_not_state(list_not_state):
    """Тест на отсутствующий статус"""
    assert filter_by_state(list_not_state) == "Операций со статусом 'EXECUTED' не найдено."


def test_filters_by_currency_code():
    """Проверяем, что функция отбирает транзакции по коду валюты"""
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 3, "Должна быть только одна USD транзакция"


def test_card_number_generator(expected_results):
    '''Тест на создание генератором номеров карт в заданном диапазоне'''
    generator = card_number_generator(1, 5)
    actual_results = list(generator)
    assert actual_results == expected_results


def test_transaction_descriptions():
    """Проверяем, что функция корректно извлекает описания транзакций"""
    desc_gen = transaction_descriptions(transactions)
    assert next(desc_gen) == "Перевод организации"
    assert next(desc_gen) == "Перевод со счета на счет"
    assert next(desc_gen) == "Перевод со счета на счет"
    assert next(desc_gen) == "Перевод с карты на карту"
    assert next(desc_gen) == "Перевод организации"

