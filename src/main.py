# main.py
import asyncio
import sys
from config import AppConfig, setup_logging
from client_factory import TelegramClientFactory
from account_repository import AccountRepository
from entity_service import EntityResolutionService
from invitation_service import InvitationService
from ui import ConsoleUI
import invite_logic  # Original invite_logic module
from app import Application

def main():
    # Initialize configuration
    config = AppConfig.create_default()
    setup_logging(config)
    
    # Initialize components
    account_repository = AccountRepository(config.data_dir)
    client_factory = TelegramClientFactory(config.data_dir)
    entity_service = EntityResolutionService()
    invitation_service = InvitationService(invite_logic)
    ui = ConsoleUI()
    
    # Create and run application
    app = Application(
        config,
        account_repository,
        client_factory,
        entity_service,
        invitation_service,
        ui,
        invite_logic
    )
    
    asyncio.run(app.run())

if __name__ == "__main__":
    main()
