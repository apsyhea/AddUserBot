import asyncio
from telethon import types
from telethon.tl.functions.channels import InviteToChannelRequest
from tqdm import tqdm
import time
import os
from participants_cache import load_cache, save_cache
import logging

# Setup logging
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
log_dir = os.path.join(base_dir, 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
logging.basicConfig(filename=os.path.join(log_dir, 'invite.log'), level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

async def invite_users(client, chat_id, channel_id, invite_count):
    start_time = time.time()

    # Specify the correct path for the cache in the root directory of the project
    cache_dir = os.path.join(base_dir, 'data')
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    # Load participants from cache
    cache = load_cache()
    participants = cache.get(chat_id)

    if not participants:
        # If participants are not in cache, fetch them
        participants = await client.get_participants(chat_id)
        cache[chat_id] = participants
        save_cache(cache)
        print(f"Number of participants in the chat: {len(participants)} (fetched in {time.time() - start_time:.2f} seconds)")
    else:
        print(f"Number of participants in the chat: {len(participants)} (from cache)")

    added_users_file = os.path.join(cache_dir, 'added_users.txt')

    try:
        with open(added_users_file, "r") as file:
            added_users = set(map(int, file.read().splitlines()))
    except FileNotFoundError:
        added_users = set()

    count = 0
    error_message = None

    for user in tqdm(participants):
        if count >= invite_count:
            break

        if user.id not in added_users:
            try:
                await client(InviteToChannelRequest(types.PeerChannel(channel_id), [types.InputUser(user.id, user.access_hash)]))
                added_users.add(user.id)
                count += 1
                logging.info(f"User {user.id} invited successfully.")
                # Add delay between invitations
                await asyncio.sleep(2)  # Delay of 2 seconds, can be increased if necessary
            except Exception as e:
                logging.error(f"Error inviting user {user.id}: {str(e)}")
                if "A wait of" in str(e):
                    wait_time = int(str(e).split()[3])
                    hours, remainder = divmod(wait_time, 3600)
                    minutes, seconds = divmod(remainder, 60)
                    error_message = f"A wait of {hours} hours {minutes} minutes {seconds} seconds is required. \nFull error message: {str(e)}"
                    logging.info(error_message)
                    return error_message
                else:
                    error_message = f"An error occurred: {str(e)}"
                    logging.info(error_message)
                    return error_message

    with open(added_users_file, "w") as file:
        file.write("\n".join(map(str, added_users)))

    logging.info(f"Completed in {time.time() - start_time:.2f} seconds.")
    print(f"Completed in {time.time() - start_time:.2f} seconds.")

    return error_message
