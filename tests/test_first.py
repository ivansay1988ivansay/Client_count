
from wsgiref.validate import assert_

from mypyc.primitives.float_ops import pow_op
import pytest


from src.masks import get_mask_card_number
from src.garbage import divide, reverse_lst

pooop = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

from src.processing import sort_by_date

poop2 = 'Отфильтрованный список операций по дате ', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# print(sort_by_date(pooop))

def test_sort():
    assert sort_by_date(pooop) == poop2

def test_main():
    assert get_mask_card_number('5999414228426353') == '5999 41** **** 6353'



def test_divide_by_zero():
    with pytest.raises(ValueError) as exc_info:  # Говорим: "Здесь должна быть ошибка!"
        divide(10, 0)  # Пробуем поделить 10 на 0 (так нельзя!)

    # Проверяем, что текст ошибки правильный
    assert str(exc_info.value) == "На ноль делить нельзя!"


@pytest.mark.parametrize("poz, neg",[
    ("flow", "wolf"),
    ("one", "eno"),
    ("stop", "pots")
] )
def test_reverse_lst(poz, neg):
    assert reverse_lst(poz) == neg