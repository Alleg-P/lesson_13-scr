# Задание 4: Валидация входных данных для расчёта сроков

def check_arguments(func):
    def wrapper(*args):
        if len(args) != 2:
            return 'Ошибка: Неверное количество аргументов!'
        if not isinstance(args[0], str):
            return 'Ошибка: Первый аргумент не строка!'
        if not isinstance(args[1], int):
            return 'Ошибка: Второй аргумент не число!'
        return func(*args)
    return wrapper

@check_arguments
def estimate_time(project_name, num_tasks):
    return 'Estimated time calculated successfully.'

print(estimate_time('Веб-сайт', 'пять'))
print(estimate_time('Визитка', 10))
