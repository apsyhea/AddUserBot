# entity_service.py
from telethon import TelegramClient
from typing import Optional, Dict, Any, Tuple
import logging

class EntityResolutionService:
    @staticmethod
    async def resolve_entity(client: TelegramClient, entity_input: str) -> Optional[Any]:
        """Resolve a Telegram entity from an input string (URL or ID)"""
        try:
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
            entity = await client.get_entity(entity_id)
            return {
                'id': entity.id,
                'title': getattr(entity, 'title', None) or getattr(entity, 'first_name', 'Unknown')
            }
        except Exception as e:
            logging.error(f"Failed to get entity info for ID {entity_id}: {str(e)}")
            return None
