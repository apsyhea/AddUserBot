# commands.py
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from telethon import TelegramClient

class Command(ABC):
    @abstractmethod
    async def execute(self) -> bool:
        pass

class InviteUsersCommand(Command):
    def __init__(self, 
                client: TelegramClient,
                entity_service,
                invitation_service,
                ui,
                invite_count: int):
        self.client = client
        self.entity_service = entity_service
        self.invitation_service = invitation_service
        self.ui = ui
        self.invite_count = invite_count
        
    async def execute(self) -> bool:
        # Get source entity
        source_input = self.ui.get_entity_input("From?")
        self.ui.print_separator()
        
        source_entity = await self.entity_service.resolve_entity(self.client, source_input)
        if not source_entity:
            self.ui.print_error("Could not resolve source entity")
            return False
            
        source_info = await self.entity_service.get_entity_info(self.client, source_entity.id)
        if not source_info:
            self.ui.print_error("Error retrieving source entity information")
            return False
            
        self.ui.print_entity_info(source_info['title'], source_info['id'])
        
        # Get target entity
        target_input = self.ui.get_entity_input("To?")
        self.ui.print_separator()
        
        target_entity = await self.entity_service.resolve_entity(self.client, target_input)
        if not target_entity:
            self.ui.print_error("Could not resolve target entity")
            return False
            
        target_info = await self.entity_service.get_entity_info(self.client, target_entity.id)
        if not target_info:
            self.ui.print_error("Error retrieving target entity information")
            return False
            
        self.ui.print_entity_info(target_info['title'], target_info['id'])
        
        # Execute invitation
        success, error = await self.invitation_service.invite_users(
            self.client, source_entity, target_entity, self.invite_count
        )
        
        if not success:
            self.ui.print_error(error)
            return False
            
        self.ui.print_success(f"Successfully invited users from {source_info['title']} to {target_info['title']}")
        return True
