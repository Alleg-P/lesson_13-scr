# Задание 1: Логирование изменений стоимости товаров

def log_price_change(func):
    def wrapper(item, old_price, new_price):
        result = func(item, old_price, new_price)
        print(f"Цена на {item} изменилась! {old_price} > {new_price}")
        return result
    return wrapper

@log_price_change
def change_price(item, old_price, new_price):
    return (item, new_price)

change_price('Кресло', 5000, 4500)
change_price('Стол', 8000, 7600)
