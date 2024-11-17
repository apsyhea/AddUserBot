# Telegram Add UserBot

Telegram Add UserBot - это скрипт для автоматического добавления пользователей из одного чата в другой чат или канал на основе библиотеки Telethon.

## Требования

Поддерживаемые платформы:
- Windows
- Linux
- Android+trmux (NON ROOT)

Для работы скрипта вам потребуется:

- Python 3.6+
- Git
- Установленные зависимости, перечисленные в `requirements.txt`
- Авторизоваться на сайте https://my.telegram.org/apps и создать API конфигурацию.

# Важно!
Если вы используете Windows, необходимо скачать и установить GIT (https://gitforwindows.org/), а также Python 3 из магазина приложений Windows Store.

## Установка

Все дальнейшие действия проводятся в терминале Windows/Linux или Termux на Android.

1. Клонируйте репозиторий:

   ```sh
   git clone https://github.com/apsyhea/AddUserBot.git
   cd AddUserBot
2. Создайте виртуальное окружение и активируйте его:
   ```sh
    python -m venv venv
    source venv/bin/activate  # Для Unix или MacOS
    source venv/Scripts/Activate     # Для Windows

3. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   ```

4. Создайте файл `config.py`и добавьте ваши учетные данные:
   ```sh
   # config.py
   api_id = 'your_api_id'
   api_hash = 'your_api_hash'
   phone_number = 'your_phone_number'
   ```   
## Использование
1. Запустите скрипт:
   ```sh
   python main.py
   ```
2. Введите количество приглашений, ID чата и ID канала, куда будут добавляться пользователи:
   ```sh
   Введите количество приглашений: 10
   [Откуда?] Введите ID чата или ссылку:  123456789
   [Куда?] Введите ID чата или ссылку: 987654321
   ```
3. Скрипт начнет добавлять пользователей, отображая прогресс.
### Примерный вывод программы (В данном случае получены ограничения от Телеграмм, см. пункт "Важно" ниже.)
   ```sh
   python src/main.py

       ___   ___  ___  __  _____________  ___  ____  ______
      / _ | / _ \/ _ \/ / / / __/ __/ _ \/ _ )/ __ \/_  __/
     / __ |/ // / // / /_/ /\ \/ _// , _/ _  / /_/ / / /
    /_/ |_/____/____/\____/___/___/_/|_/____/\____/ /_/
   
   Введите количество приглашений: 10
   
   ===========================================================================
   
   [Откуда?] Введите ID чата или ссылку: 1655265504
   
   ===========================================================================
   
   Название канала:          MACAN Chat
   ID канала:                1655265504
   ===========================================================================
   [Куда?] Введите ID чата или ссылку: 1960888592
   
   ===========================================================================
   
   Название канала:          cbrphnk
   ID канала:                1960888592
   ===========================================================================
   Количество участников в чате: 6530 (из кэша)
   
   ===========================================================================
   Ошибка: Требуется ожидание 5 ч 54 м 26 с.
   ===========================================================================
   ```

## Важно
Убедитесь, что у вас есть права в канале или чате куда добавляются пользователи.
При первом запуске у вас запросит код подтверждения и пароль от аккаунта в случае если у вас 2fa
Ограниченя из вывода выше, это временные ограничения на приглашения пользователей, они не связаны со спам блоком.
Скрипт записывает уже добавленных пользователей в файл `added_users.txt`, чтобы избежать повторных запросов.

Обратите внимание, большое колличество одновременных приглашений повелкут за собой нежелательные жалобы пользователей что грозит спам-блокировкой аккаунта.

## Лицензия
Этот проект лицензирован на условиях лицензии MIT. См. LICENSE для подробностей.

