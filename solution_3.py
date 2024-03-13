# Задание 3: Кеширование результатов расчёта стоимости проектов

cache = {}

def calculate_project_cost(project_type, business_size):
    key = (project_type, business_size)
    
    if key in cache:
        result = cache[key]
        return f'Загрузили из кеша: {result}'
    
    if project_type == 'Логотип' and business_size == 'малый бизнес':
        cost = 3000
    else:
        cost = None
    
    cache[key] = cost
    
    return f'Посчитали цену: {cost}'

print(calculate_project_cost('Логотип', 'малый бизнес'))
print(calculate_project_cost('Логотип', 'малый бизнес'))
