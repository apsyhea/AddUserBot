import os
from telethon import TelegramClient, types
import asyncio
from telethon.tl.functions.channels import InviteToChannelRequest
from tqdm import tqdm

def create_config_if_needed():
    # Проверка наличия config.py
    if not os.path.isfile("config.py"):
        from create_config import create_config
        create_config()
        if not os.path.isfile("config.py"):
            exit(1)

create_config_if_needed()

# Импортирование конфигурации после её создания
import config

client = TelegramClient('session_name', config.api_id, config.api_hash)

invite_count = int(input("Введите количество приглашений: "))
chat_id = int(input("Введите ID чата: "))
channel_id = int(input('ID канала, куда будут добавляться пользователи: '))

async def main():
    await client.start(config.phone_number)

    # Получаем объект канала, куда будем добавлять пользователей
    channel = await client.get_entity(types.PeerChannel(channel_id))

    # Получаем список участников из указанного чата
    participants = await client.get_participants(chat_id)

    # Загрузка списка уже добавленных пользователей из файла
    try:
        with open("added_users.txt", "r") as file:
            added_users = set(map(int, file.read().splitlines()))
    except FileNotFoundError:
        added_users = set()

    count = 0  # Счетчик успешных приглашений

    # Создаем и отображаем строку прогресса
    with tqdm(total=invite_count, desc="Приглашения отправлены") as pbar:
        for user in participants:
            if count >= invite_count:
                break  # Прекращаем, если достигнуто максимальное количество приглашений

            if user.id not in added_users:  # Проверяем, был ли пользователь добавлен ранее
                try:
                    await client(InviteToChannelRequest(channel, [types.InputUser(user.id, user.access_hash)]))
                    added_users.add(user.id)  # Добавляем пользователя в список добавленных
                    count += 1  # Увеличиваем счетчик успешных приглашений
                    pbar.update(1)  # Обновляем строку прогресса
                except Exception as e:
                    if "A wait of" in str(e) or "Bots can only be admins in channels" in str(e):
                        continue  # Пропускаем сообщения о задержке и административных ограничениях

    # Сохраняем обновленный список добавленных пользователей в файл
    with open("added_users.txt", "w") as file:
        file.write("\n".join(map(str, added_users)))

    await client.disconnect()

with client:
    client.loop.run_until_complete(main())
