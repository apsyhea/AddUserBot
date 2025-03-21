import asyncio
import logging

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
                logging.info("Нет доступных аккаунтов. Завершение работы.")
                return

            # Отображение пользовательского интерфейса
            self.ui.print_title()
            invite_count = self.ui.get_invite_count()
            self.ui.print_separator()

            # Обработка каждого аккаунта
            for account in accounts:
                logging.info(f"Начало работы с аккаунтом: {account['phone_number']}")
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
                    logging.info(f"Успешно выполнена команда для {account['phone_number']}")
                except Exception as e:
                    logging.error(f"Ошибка во время выполнения команды для {account['phone_number']}: {str(e)}")
                finally:
                    # Обязательно отключаем клиента
                    await client.disconnect()
                    logging.info(f"Клиент {account['phone_number']} успешно отключён.")

        except KeyboardInterrupt:
            logging.info("Операция прервана пользователем.")
            print("\nОперация была прервана.")
        except Exception as e:
            logging.error(f"Ошибка приложения: {str(e)}")
            print(f"\nПроизошла ошибка: {e}. Проверьте логи для деталей.")
        finally:
            logging.info("Завершение работы приложения.")
            self.ui.wait_for_exit()

# Функция для настройки логгирования с поддержкой UTF-8
def setup_logging():
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"  # Указание кодировки UTF-8
    )
    logging.info("Логгирование успешно настроено.")
