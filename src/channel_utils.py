# channel_utils.py
from urllib.parse import urlparse
import emoji

async def get_channel_id(client, url):
    parsed_url = urlparse(url)
    path = parsed_url.path.strip('/')
    try:
        channel = await client.get_entity(path)
        print(f"ID канала: {channel.id}")
        return channel.id
    except Exception as e:
        print(f"Ошибка при получении ID канала: {e}")
        return None

def remove_emojis(text):
    return ''.join(char for char in text if char not in emoji.EMOJI_DATA)

async def get_channel_info(client, channel_id):
    try:
        channel = await client.get_entity(channel_id)
        title = remove_emojis(channel.title)
        return {
            'title': title,
            'id': channel.id
        }
    except Exception as e:
        print(f"Ошибка при получении информации о канале: {e}")
        return None
