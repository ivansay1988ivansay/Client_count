operation = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(operation: list[dict], operation_state: str = "EXECUTED") -> list[dict]:
    """функция принимает список словарей + статус операции, и фильтрует по заданному статусу"""
    operation_list = []
    for operation_dict in operation:
        if operation_dict.get("state") == operation_state:
            operation_list.append(operation_dict)
    return operation_list


def sort_by_date(operation: list[dict], sorted_by=None) -> list[dict]:
    """Функция принимает список словарей, и возвращает новый отсортированный по ключу date"""

    if sorted_by == None:
        sorted_operation = sorted(operation, key=lambda oper: oper["date"], reverse=True)
    else:
        sorted_operation = sorted(operation, key=lambda oper: oper["date"])

    return sorted_operation


if __name__ == "__main__":
    print(filter_by_state(operation))
    print(sort_by_date(operation))
