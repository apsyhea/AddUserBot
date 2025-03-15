# invitation_service.py
from telethon import TelegramClient
import logging
from typing import Tuple, Optional

class InvitationService:
    def __init__(self, invite_logic_module):
        self.invite_logic = invite_logic_module
        
    async def invite_users(self, 
                          client: TelegramClient, 
                          source_entity: any, 
                          target_entity: any, 
                          count: int) -> Tuple[bool, Optional[str]]:
        """Invite users from source to target entity"""
        try:
            error_message = await self.invite_logic.invite_users(
                client, source_entity, target_entity, count
            )
            
            if error_message:
                return False, error_message
            return True, None
        except Exception as e:
            error_message = f"Invitation process failed: {str(e)}"
            logging.error(error_message)
            return False, error_message
