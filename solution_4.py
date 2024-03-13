# Задание 4: Валидация входных данных для расчёта сроков

import sys
def estimate_time(project_name, num_tasks):
    if len(sys.argv) != 1:
        return 'Ошибка: Неверное количество аргументов!'
    if not isinstance(project_name, str):
        return 'Ошибка: Первый аргумент не строка!'
    if not isinstance(num_tasks, int):
        return 'Ошибка: Второй аргумент не число!'
    return 'Estimated time calculated successfully.'

print(estimate_time('Веб-сайт', 'пять'))
print(estimate_time('Визитка', 10))
