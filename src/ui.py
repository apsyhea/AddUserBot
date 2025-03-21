from typing import Dict, Any
import logging

class ConsoleUI:
    @staticmethod
    def print_title():
        title = r"""
    ___   ___  ___  __  _____________  ___  ____  ______
   / _ | / _ \/ _ \/ / / / __/ __/ _ \/ _ )/ __ \/_  __/
  / __ |/ // / // / /_/ /\ \/ _// , _/ _  / /_/ / / /   
 /_/ |_/____/____/\____/___/___/_/|_/____/\____/ /_/    
        """
        print(title)

    @staticmethod
    def print_separator():
        print("\n" + "=" * 75 + "\n")

    @staticmethod
    def print_entity_info(title: str, entity_id: int):
        logging.info(f"Displaying entity info: {title} (ID: {entity_id})")
        print(f"{'Entity name:':<25} {title}")
        print(f"{'Entity ID:':<25} {entity_id}\n{'='*75}")

    @staticmethod
    def get_invite_count() -> int:
        while True:
            try:
                count = int(input("Enter the number of users to invite: "))
                if count <= 0:
                    print("Please enter a positive number.")
                    logging.warning("User entered non-positive invite count.")
                    continue
                logging.info(f"Invite count set to {count}")
                return count
            except ValueError:
                print("Please enter a valid number.")
                logging.warning("User entered invalid invite count.")

    @staticmethod
    def get_entity_input(prompt: str) -> str:
        input_value = input(f"[{prompt}] Enter chat ID or link: ")
        logging.info(f"User input for {prompt}: {input_value}")
        return input_value

    @staticmethod
    def print_error(message: str):
        logging.error(message)
        print(f"\n{'='*75}\nError: {message}\n{'='*75}")

    @staticmethod
    def print_success(message: str):
        logging.info(message)
        print(f"\n{'='*75}\n{message}\n{'='*75}")

    @staticmethod
    def wait_for_exit():
        logging.info("Waiting for user to exit.")
        print("\nPress any key to exit...")
        input()
