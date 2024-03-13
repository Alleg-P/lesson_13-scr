# Задание 5: Авторизация доступа к персональным данным клиентов

def authentication_required(func):
    def wrapper(username, password):
        if username == 'Роман' and password == 'correctpassword':
            print('Доступ получен. Данные: ...')
            return func(username, password)
        else:
            print('В доступе отказано!')
    return wrapper

@authentication_required
def access_client_data(username, password):
    pass
access_client_data('Роман', 'correctpassword')

access_client_data('Олег', 'wrongpassword')
