from data import operation


def filter_by_state(operation: list[dict], operation_state: str = "EXECUTED") -> str | tuple[str, list[dict]]:
    """функция принимает список словарей + статус операции, и фильтрует по заданному статусу"""
    operation_list = []
    for operation_dict in operation:
        if operation_dict.get("state", "В этом словаре нет статуса операций") == operation_state:
            operation_list.append(operation_dict)

    if not operation_list:
        return f"Операций со статусом '{operation_state}' не найдено."

    message = "Отфильтрованный список операций по статусу "
    return message, operation_list


def sort_by_date(operation: list[dict], sorted_by: bool = True) -> tuple[str, list[dict]]:
    """Функция принимает список словарей, и возвращает новый отсортированный по ключу date"""

    if sorted_by:
        sorted_operation = sorted(operation, key=lambda oper: oper["date"], reverse=True)
    else:
        sorted_operation = sorted(operation, key=lambda oper: oper["date"])
    message = "Отфильтрованный список операций по дате "
    return message, sorted_operation


if __name__ == "__main__":
    print(filter_by_state(operation))
    # print(sort_by_date(operation, False))
