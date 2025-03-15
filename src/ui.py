# ui.py
from typing import Dict, Any

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
        print(f"{'Entity name:':<25} {title}")
        print(f"{'Entity ID:':<25} {entity_id}\n{'='*75}")
    
    @staticmethod
    def get_invite_count() -> int:
        while True:
            try:
                count = int(input("Enter the number of users to invite: "))
                if count <= 0:
                    print("Please enter a positive number.")
                    continue
                return count
            except ValueError:
                print("Please enter a valid number.")
    
    @staticmethod
    def get_entity_input(prompt: str) -> str:
        return input(f"[{prompt}] Enter chat ID or link: ")
    
    @staticmethod
    def print_error(message: str):
        print(f"\n{'='*75}\nError: {message}\n{'='*75}")
    
    @staticmethod
    def print_success(message: str):
        print(f"\n{'='*75}\n{message}\n{'='*75}")
        
    @staticmethod
    def wait_for_exit():
        print("\nPress any key to exit...")
        input()
