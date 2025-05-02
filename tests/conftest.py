import pytest


@pytest.fixture
def card_number():      # подставляет номер карты
    return 7000792289606361

@pytest.fixture
def mask_account_name_card():
    return 'Maestro 7000792289606361'

@pytest.fixture
def mask_account_name_check():
    return 'Счет 73654108430135874305'

@pytest.fixture
def mask_account():     # подставляет номер счёта
    return 73654108430135874305

@pytest.fixture
def list_of_operations():
    return [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]