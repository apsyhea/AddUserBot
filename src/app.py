# app.py
import asyncio
import sys
import logging
from typing import List, Dict, Any

class Application:
    def __init__(self, 
                config,
                account_repository,
                client_factory,
                entity_service,
                invitation_service,
                ui,
                invite_logic):
        self.config = config
        self.account_repository = account_repository
        self.client_factory = client_factory
        self.entity_service = entity_service
        self.invitation_service = invitation_service
        self.ui = ui
        self.invite_logic = invite_logic
        
    async def run(self):
        try:
            # Load accounts
            accounts = self.account_repository.load_accounts()
            if not accounts:
                print(f"The accounts.ini template is created in the {self.config.data_dir} path.")
                print("Please fill in your account details.")
                return
                
            # Display UI
            self.ui.print_title()
            invite_count = self.ui.get_invite_count()
            self.ui.print_separator()
            
            # Process each account
            for account in accounts:
                client = await self.client_factory.create_client(account)
                if not client:
                    logging.error(f"Failed to initialize client for {account['phone_number']}")
                    continue
                    
                try:
                    # Create and execute command
                    from commands import InviteUsersCommand
                    command = InviteUsersCommand(
                        client,
                        self.entity_service,
                        self.invitation_service,
                        self.ui,
                        invite_count
                    )
                    
                    await command.execute()
                finally:
                    # Always disconnect client
                    await client.disconnect()
                    
        except KeyboardInterrupt:
            logging.info("Operation aborted by user")
            print("\nOperation aborted.")
        except Exception as e:
            logging.error(f"Application error: {str(e)}")
            print(f"\nAn error occurred: {e}")
        finally:
            self.ui.wait_for_exit()
