import asyncio
import logging
from config import AppConfig, setup_logging
from client_factory import TelegramClientFactory
from account_repository import AccountRepository
from entity_service import EntityResolutionService
from invitation_service import InvitationService, invite_users  # Импорт invite_users
from ui import ConsoleUI
from app import Application

def main():
    # Инициализация конфигурации
    config = AppConfig.create_default()
    setup_logging(config)
    
    # Логгирование для проверки работы программы
    logging.info("Приложение запускается...")

    # Инициализация компонентов
    account_repository = AccountRepository(config.data_dir)
    client_factory = TelegramClientFactory(config.data_dir)
    entity_service = EntityResolutionService()
    invitation_service = InvitationService(invite_users)  # Передача invite_users
    ui = ConsoleUI()
    
    # Создание и запуск приложения
    app = Application(
        config=config,
        account_repository=account_repository,
        client_factory=client_factory,
        entity_service=entity_service,
        invitation_service=invitation_service,
        ui=ui,
        invite_logic=invite_users  # Передаём invite_users как аргумент
    )
    
    # Асинхронный запуск приложения
    asyncio.run(app.run())


if __name__ == "__main__":
    main()
