# Задание 2: Отслеживание времени выполнения дизайн-проектов

import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Execution: {end_time - start_time:.3} seconds')
        return result
    return wrapper

@execution_time
def create_design(task, pause):
    return time.sleep(pause)

task1 = 'Логотип Васильевский рынок'
task2 = 'Макет сайта Логомашины'

create_design(task1, 2.45)
create_design(task2, 4.30)
