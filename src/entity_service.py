from telethon import TelegramClient
from typing import Optional, Dict, Any
import logging

class EntityResolutionService:
    @staticmethod
    async def resolve_entity(client: TelegramClient, entity_input: str) -> Optional[Any]:
        """Resolve a Telegram entity from an input string (URL or ID)"""
        try:
            logging.info(f"Resolving entity: {entity_input}")
            if entity_input.startswith('https://'):
                return await client.get_entity(entity_input)
            elif entity_input.isdigit():
                return await client.get_entity(int(entity_input))
            else:
                raise ValueError("Invalid ID or link format.")
        except Exception as e:
            logging.error(f"Failed to resolve entity '{entity_input}': {str(e)}")
            return None

    @staticmethod
    async def get_entity_info(client: TelegramClient, entity_id: int) -> Optional[Dict[str, Any]]:
        """Get information about a Telegram entity"""
        try:
            logging.info(f"Fetching info for entity ID: {entity_id}")
            entity = await client.get_entity(entity_id)
            info = {
                'id': entity.id,
                'title': getattr(entity, 'title', None) or getattr(entity, 'first_name', 'Unknown')
            }
            logging.info(f"Entity info retrieved: {info}")
            return info
        except Exception as e:
            logging.error(f"Failed to get entity info for ID {entity_id}: {str(e)}")
            return None
