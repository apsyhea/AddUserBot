import asyncio
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
            # Загрузка аккаунтов
            accounts = self.account_repository.load_accounts()
            if not accounts:
                print(f"Файл accounts.ini создан по пути: {self.config.data_dir}.")
                print("Пожалуйста, заполните данные аккаунтов.")
                return

            # Отображение пользовательского интерфейса
            self.ui.print_title()
            invite_count = self.ui.get_invite_count()
            self.ui.print_separator()

            # Обработка каждого аккаунта
            for account in accounts:
                client = await self.client_factory.create_client(account)
                if not client:
                    logging.error(f"Не удалось инициализировать клиент для {account['phone_number']}")
                    continue

                try:
                    # Импорт команды
                    from commands import InviteUsersCommand
                    command = InviteUsersCommand(
                        client=client,
                        entity_service=self.entity_service,
                        invitation_service=self.invitation_service,
                        ui=self.ui,
                        invite_count=invite_count
                    )
                    
                    # Выполнение команды
                    await command.execute()
                finally:
                    # Обязательно отключаем клиента
                    await client.disconnect()

        except KeyboardInterrupt:
            logging.info("Операция прервана пользователем.")
            print("\nОперация была прервана.")
        except Exception as e:
            logging.error(f"Ошибка приложения: {str(e)}")
            print(f"\nПроизошла ошибка: {e}")
        finally:
            self.ui.wait_for_exit()
