import pytest


@pytest.fixture
def card_number():      # подставляет номер карты
    return 7000792289606361

@pytest.fixture
def mask_account():     # подставляет номер счёта
    return 73654108430135874305