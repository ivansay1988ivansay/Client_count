from datetime import datetime




def log(filename=None):
    def get_function(fun):
        def inner(*args, **kwargs):
            print("Внутри inner")
            start_time = datetime.now()
            try:
                result = fun(*args, **kwargs)
                end_time = datetime.now()
                message_to_log = (f'Название запущенной функции: {fun.__name__}\n'
                            f'Время запуска функции: {start_time.time()}\n'
                            f'Функция работала {end_time - start_time} секунд\n'
                            f'Окончание работы функции: {end_time.time()}\n'
                            f'Результат работы функции: {result}\n'
                            "===============================\n"
                        )
                if filename:
                    with open("log_file.txt", 'a', encoding="utf-8") as file:
                        file.write(message_to_log)
                else:
                    print(f'А файла то нет, но вот что я бы туда записал {message_to_log}')

                return result
            except Exception as e:
                end_time = datetime.now()
                error_message_to_log =(f'Название функции: {fun.__name__}\n'
                                    f'Ошибка: {start_time.time()}\n'
                                    f"Ошибка: {type(e).__name__}\n"
                                    f'Окончание работы функции: {end_time.time()}\n'
                                    "===============================\n"
                        )
                if filename:
                    with open("log_file.txt", 'a', encoding="utf-8") as file:
                        file.write(error_message_to_log)
                else:
                    print(f'А файла то нет, но вот что я бы туда записал {error_message_to_log}')
                raise "Ошибка"

        return inner
    return get_function

@log(filename='log_file.txt')
def puts(a, b):
    return a / b

print(puts(2, 1))