import configparser
import os

# Path to the configuration file
config_dir = os.path.join('data')
config_file = os.path.join(config_dir, 'accounts.ini')

# Ensure the data directory exists
if not os.path.exists(config_dir):
    os.makedirs(config_dir)

# Function to create a template accounts.ini file
def create_template():
    config = configparser.ConfigParser()
    config['account_1'] = {
        'phone_number': '+1234567890',
        'api_id': 'YOUR_API_ID_1',
        'api_hash': 'YOUR_API_HASH_1'
    }
    with open(config_file, 'w') as f:
        config.write(f)

def load_accounts():
    if not os.path.exists(config_file):
        create_template()
        print(f"The accounts.ini template is created in the ADDUSERBOT/data path.\nPlease fill in your account details.")
        exit(0)
    
    config = configparser.ConfigParser()
    config.read(config_file)
    accounts = []

    for section in config.sections():
        phone_number = config[section]['phone_number']
        api_id = config[section]['api_id']
        api_hash = config[section]['api_hash']
        accounts.append({
            'phone_number': phone_number,
            'api_id': api_id,
            'api_hash': api_hash
        })
    
    return accounts

def save_account(phone_number, api_id, api_hash):
    config = configparser.ConfigParser()
    if os.path.exists(config_file):
        config.read(config_file)
    
    section_name = f'account_{len(config.sections()) + 1}'
    config[section_name] = {
        'phone_number': phone_number,
        'api_id': api_id,
        'api_hash': api_hash
    }

    with open(config_file, 'w') as f:
        config.write(f)
