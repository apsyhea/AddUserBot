import os
from telethon import TelegramClient
from typing import Dict, Any, Optional
import logging

class TelegramClientFactory:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir

    async def create_client(self, account: Dict[str, Any]) -> Optional[TelegramClient]:
        """Create and initialize a Telegram client for the given account"""
        try:
            session_file = os.path.join(self.data_dir, f'session_{account["phone_number"]}.session')
            client = TelegramClient(session_file, account['api_id'], account['api_hash'])
            await client.start(account['phone_number'])
            logging.info(f"Client initialized for {account['phone_number']}")
            return client
        except Exception as e:
            logging.error(f"Failed to create client for {account['phone_number']}: {str(e)}")
            return None
