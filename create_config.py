import requests

def get_random_hash(phone_number):
    url = "https://my.telegram.org/auth/send_password"
    payload = {'phone': phone_number}
    response = requests.post(url, data=payload)
    if response.status_code == 200 and 'Sorry, too many tries' not in response.text:
        return response.json()['random_hash']
    else:
        print('Слишком много попыток. Пожалуйста, попробуйте позже.')
        return None

def authenticate(phone_number, random_hash, password):
    url = "https://my.telegram.org/auth/login"
    payload = {'phone': phone_number, 'random_hash': random_hash, 'password': password}
    response = requests.post(url, data=payload)
    response.raise_for_status()
    return response.cookies

def create_telegram_app(cookies, app_title, short_name):
    url = "https://my.telegram.org/apps/create"
    payload = {
        'app_title': app_title,
        'app_shortname': short_name,
        'app_url': '',
        'app_platform': 'web',
        'app_desc': ''
    }
    response = requests.post(url, cookies=cookies, data=payload)
    try:
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f'Ошибка создания приложения: {e}')
        print(f'Status Code: {response.status_code}')
        print(f'Ответ сервера: {response.text}')
        return None

def create_config():
    phone_number = input("Введите ваш номер телефона в формате +1234567890: ")
    random_hash = get_random_hash(phone_number)
    if random_hash is None:
        print("Не удалось получить random_hash. Попробуйте снова позже.")
        return

    password = input("Введите код подтверждения, который пришел в Telegram: ")

    try:
        cookies = authenticate(phone_number, random_hash, password)
    except Exception as e:
        print(f'Ошибка авторизации: {e}')
        return

    app_title = input("Введите название приложения: ")
    short_name = input("Введите короткое имя приложения: ")

    app = create_telegram_app(cookies, app_title, short_name)
    if app:
        with open("config.py", "w") as f:
            f.write(f"api_id = '{app['app_id']}'\n")
            f.write(f"api_hash = '{app['app_hash']}'\n")
            f.write(f"phone_number = '{phone_number}'\n")

        print('Конфигурация приложения сохранена в config.py')
    else:
        print("Не удалось создать приложение. Проверьте введенные данные и попробуйте снова.")
