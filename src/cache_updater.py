import asyncio
from telethon import TelegramClient
from participants_cache import load_cache, save_cache
from accounts import load_accounts
import os

async def update_cache():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_dir = os.path.join(base_dir, 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    accounts = load_accounts()
    for account in accounts:
        session_file = os.path.join(data_dir, f'session_{account["phone_number"]}.session')
        client = TelegramClient(session_file, account['api_id'], account['api_hash'])
        await client.start(account['phone_number'])

        cache = load_cache()
        for chat_id in cache:
            participants = await client.get_participants(chat_id)
            cache[chat_id] = participants
        save_cache(cache)

        await client.disconnect()

    print("Cache updated successfully.")

if __name__ == "__main__":
    asyncio.run(update_cache())
