import os
import configparser
from typing import List, Dict, Any
import logging

class AccountRepository:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
        self.accounts_file = os.path.join(data_dir, 'accounts.ini')

    def load_accounts(self) -> List[Dict[str, Any]]:
        """Load accounts from the configuration file"""
        if not os.path.exists(self.accounts_file):
            self._create_template()
            logging.info(f"Template accounts.ini created at {self.accounts_file}")
            return []
        
        config = configparser.ConfigParser()
        config.read(self.accounts_file)
        
        accounts = []
        for section in config.sections():
            try:
                account = {
                    'phone_number': config[section]['phone_number'],
                    'api_id': int(config[section]['api_id']),
                    'api_hash': config[section]['api_hash']
                }
                accounts.append(account)
                logging.info(f"Loaded account: {account['phone_number']}")
            except (KeyError, ValueError) as e:
                logging.warning(f"Invalid account configuration in section {section}: {str(e)}")
        
        if not accounts:
            logging.warning("No valid accounts found in accounts.ini.")
        return accounts

    def _create_template(self):
        """Create a template accounts.ini file"""
        config = configparser.ConfigParser()
        config['Account1'] = {
            'phone_number': '+1234567890',
            'api_id': '12345',
            'api_hash': 'your_api_hash_here'
        }
        with open(self.accounts_file, 'w') as f:
            config.write(f)
        logging.info(f"Created accounts template at {self.accounts_file}")
