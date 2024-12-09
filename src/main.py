import asyncio
from telethon import TelegramClient, types
from user_input import get_invite_count
from channel_utils import get_channel_id, get_channel_info
from invite_logic import invite_users
import config
import os

def print_separator():
    print("\n" + "=" * 75 + "\n")

def print_title():
    title = r"""
    ___   ___  ___  __  _____________  ___  ____  ______
   / _ | / _ \/ _ \/ / / / __/ __/ _ \/ _ )/ __ \/_  __/
  / __ |/ // / // / /_/ /\ \/ _// , _/ _  / /_/ / / /   
 /_/ |_/____/____/\____/___/___/_/|_/____/\____/ /_/    
    """
    print(title)

def print_channel_info(title, channel_id):
    print(f"{'Channel name:':<25} {title}")
    print(f"{'Channel ID:':<25} {channel_id}\n{'='*75}")

# Ensure the data directory exists in the root directory of the project
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
data_dir = os.path.join(base_dir, 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

session_file = os.path.join(data_dir, 'session_name.session')
client = TelegramClient(session_file, config.api_id, config.api_hash)

print_title()
invite_count = get_invite_count()
print_separator()

try:
    chat_id_input = input('[From?] Enter chat ID or link: ')
    print_separator()

    async def main():
        await client.start(config.phone_number)

        try:
            # Check the type of input value
            if chat_id_input.startswith('https://'):
                chat_id = await client.get_peer_id(chat_id_input)
            elif chat_id_input.isdigit():
                chat_id = int(chat_id_input)
            else:
                raise ValueError("Invalid ID or link.")
            
            chat_info = await get_channel_info(client, chat_id)
            if not chat_info:
                print("Error retrieving chat information.")
                return
            print_channel_info(chat_info['title'], chat_info['id'])
        except ValueError as e:
            print(e)
            return

        channel_url = input('[To?] Enter chat ID or link: ')
        print_separator()
        channel_id = int(channel_url) if channel_url.isdigit() else await get_channel_id(client, channel_url)
        if channel_id is None:
            return

        channel_info = await get_channel_info(client, channel_id)
        if not channel_info:
            print("Error retrieving channel information.")
            return
        print_channel_info(channel_info['title'], channel_info['id'])

        error_occurred = await invite_users(client, chat_id, channel_id, invite_count)
        if error_occurred:
            print(f"\n{'='*75}\nError: {error_occurred}\n{'='*75}")

        await client.disconnect()

    asyncio.run(main())

except KeyboardInterrupt:
    print("\nOperation aborted.")
