# invite_logic.py
from telethon import types
from telethon.tl.functions.channels import InviteToChannelRequest
from tqdm import tqdm
import time
import os
from participants_cache import load_cache, save_cache

async def invite_users(client, chat_id, channel_id, invite_count):
    start_time = time.time()

    # Load participants from cache
    cache = load_cache()
    participants = cache.get(chat_id)

    if not participants:
        participants = await client.get_participants(chat_id)
        cache[chat_id] = participants
        save_cache(cache)
        print(f"Количество участников в чате: {len(participants)} (получено за {time.time() - start_time:.2f} сек.)")
    else:
        print(f"Количество участников в чате: {len(participants)} (из кэша)")

    added_users_file = os.path.join('data', 'added_users.txt')

    try:
        with open(added_users_file, "r") as file:
            added_users = set(map(int, file.read().splitlines()))
    except FileNotFoundError:
        added_users = set()

    count = 0
    error_message = None

    for user in participants:
        if count >= invite_count:
            break

        if user.id not in added_users:
            try:
                await client(InviteToChannelRequest(types.PeerChannel(channel_id), [types.InputUser(user.id, user.access_hash)]))
                added_users.add(user.id)
                count += 1
            except Exception as e:
                if "A wait of" in str(e):
                    wait_time = int(str(e).split()[3])
                    hours, remainder = divmod(wait_time, 3600)
                    minutes, seconds = divmod(remainder, 60)
                    error_message = f"Требуется ожидание {hours} ч {minutes} м {seconds} с."
                    return error_message
                elif "Bots can only be admins in channels" in str(e):
                    error_message = "Боты могут быть только администраторами в каналах."
                    return error_message

    with open(added_users_file, "w") as file:
        file.write("\n".join(map(str, added_users)))

    print(f"Завершено за {time.time() - start_time:.2f} сек.")

    return error_message
