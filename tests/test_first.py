
import pytest

from src.masks import get_mask_card_number, get_mask_account

from src.processing import sort_by_date, operation
from src.widget import mask_account_card

sorted_operation = 'Отфильтрованный список операций по дате ', [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]


def test_sort_by_date(list_of_operations):
    '''Базовый тест на работу функции'''
    assert sort_by_date(list_of_operations) == sorted_operation


def test_sort_by_date_missing_key():
    """Тест с операцией без ключа date"""
    invalid_ops = operation + [{"id": 1, "state": "EXECUTED"}]
    with pytest.raises(KeyError):
        sort_by_date(invalid_ops)


@pytest.mark.parametrize("card_number, expected", [
    (5999414228426353, "5999 41** **** 6353"),
    (36159852478526, "3615 98** **85 26"),
    (12345678901234567890, "1234 56** **** **** 7890")
])
def test_parametrize_get_mask_card_number(card_number, expected):
    '''Тест на работу функции с разной длинной карты'''
    assert get_mask_card_number(card_number) == expected

def test_short_card_number():
    '''Тест на обработку слишком короткого номера карты'''
    with pytest.raises(ValueError, match="Номер карты должен содержать минимум 10 цифр"):
        get_mask_card_number(12345678)


@pytest.mark.parametrize("account_number, expected", [
    # Стандартные проверки
    (1234567890123456, "**3456"),
    (9999999999999999, "**9999"),
    (1000000000000004, "**0004"),
    # Проверки счёта разной длины
    (123467, "**3467"),
    (123455567890, "**7890"),
    (12345678901234567890, "**7890")
])

def test_parametrize_valid_account_numbers(account_number, expected):
    """Параметризованное тестирование правильности маскирования номера счета"""
    assert get_mask_account(account_number) == expected

def test_mask_account_card(mask_account_name_card, mask_account_name_check):
    '''Стандартное тестирование mask_account_card'''
    assert mask_account_card(mask_account_name_card) == "Maestro 7000 79** **** 6361"
    assert mask_account_card(mask_account_name_check) == "Счет **4305"


@pytest.mark.parametrize("account_number, expected", [
    # Стандартные проверки карт
    ('Visa Platinum 7000792289606361', "Visa Platinum 7000 79** **** 6361"),
    ('Maestro 7000792289606361', "Maestro 7000 79** **** 6361"),
    # Стандартные проверки номера счета
    ('Счет 73654108430135874305', "Счет **4305"),
    ('Счет 14569875632145698759', "Счет **8759")
])

def test_parametrize_mask_account_card(account_number, expected):
    '''Параметризованное тестирование mask_account_card'''
    assert mask_account_card(account_number) == expected
