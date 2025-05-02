# # import pytest
# #
# #
# # def divide(a, b):
# #     if b == 0:
# #         raise ValueError("На ноль делить нельзя!")
# #     return a / b
# #
# # # print(divide(2, 0))
# #
# #
# # def test_divide_by_zero():
# #     with pytest.raises(ValueError) as exc_info:  # Говорим: "Здесь должна быть ошибка!"
# #         divide(10, 0)  # Пробуем поделить 10 на 0 (так нельзя!)
# #
# #     # Проверяем, что текст ошибки правильный
# #     assert str(exc_info.value) == "На ноль делить нельзя!"
# #
# #

#
# lst_num = [1, 3, 9, 9, 0, 45, 8]
#
#
# # def max_num(ln: list) -> int:
# #     return max(ln)
# #
# # # print(max_num(lst_num))
# #
# # def revers_num(num: int) -> int:
# #     return int(str(num)[::-1])
# #
# # print(revers_num(max_num))
#
# # assert max_num(lst_num) == 45
# # assert revers_num(max_num) == 54
#
# lst_num = [1, 3, 9, 9, 0, 45, 8]
#
# def max_num(ln: list) -> int:
#     return max(ln)
#
# def revers_num(num: int) -> int:
#     # Преобразуем число в строку, разворачиваем, затем обратно в число
#     return int(str(num)[::-1])
#
# # Получаем максимальное число
# max_number = max_num(lst_num)
# # Разворачиваем его
# reversed_number = revers_num(max_number)
#
# print(f"Максимальное число: {max_number}")
# print(f"Развёрнутое число: {reversed_number}")
#
# assert max_num(lst_num) == 45
# assert revers_num(max_num) == 54