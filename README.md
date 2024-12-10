# Telegram Add UserBot

Telegram Add UserBot is a script for automatically adding users from one chat to another chat or channel using the Telethon library.

## Requirements

Supported platforms:
- Windows
- Linux
- Android+Termux (NON ROOT)

To run the script, you will need:

- Python 3.6+
- Git
- Installed dependencies listed in `requirements.txt`
- Authorization on https://my.telegram.org/appsand creation of an API configuration.

# Important!
If you are using Windows, you need to download and install GIT (https://gitforwindows.org/) and Python 3 from the Windows Store.

## Installation

All further actions are performed in the terminal for Windows/Linux or Termux on Android.

1. Clone the repository:

   ```sh
   git clone https://github.com/apsyhea/AddUserBot.git
   cd AddUserBot
2. Run `.bat` (in Windows) or `.sh` (in Linux). The first time you run it, `accounts.ini` will be created, which you need to fill in.
3. Restart script after update `accounts.ini`   
4. This is what the `accounts.ini` file looks like. It is created in the `data` directory.:
   ```sh
   [account_1]
   phone_number = your_phone_number
   api_id = your_api_id
   api_hash = your_api_hash
   ```
You need to fill it in for the script to work. Each new account should contain a new block (e.g., [account_2]).

## Usage
1. Enter the number of invitations, chat ID and channel ID where users will be added:
   ```sh
   Enter the number of invitations: 100
   [From?] Enter chat ID or link: 123456789
   [To?] Enter chat ID or link: 987654321
   ```
2. The script will start adding users, displaying the progress.
### Example output of the program (In this case, Telegram restrictions were encountered, see the "Important" section below.)
   ```sh
   python src/main.py
   
       ___   ___  ___  __  _____________  ___  ____  ______
      / _ | / _ \/ _ \/ / / / __/ __/ _ \/ _ )/ __ \/_  __/
     / __ |/ // / // / /_/ /\ \/ _// , _/ _  / /_/ / / /
    /_/ |_/____/____/\____/___/___/_/|_/____/\____/ /_/
   
   Enter the number of invitations: 10
   
   ===========================================================================
   
   [From?] Enter chat ID or link: 1655265504
   
   ===========================================================================
   
   Channel name:          TEST Chat
   Channel ID:            123456789
   ===========================================================================
   [To?] Enter chat ID or link: 1960888592
   
   ===========================================================================
   
   Channel name:          TEST Channel
   Channel ID:            987654321
   ===========================================================================
   Number of participants in the chat: 6611 (from cache)
   
   ===========================================================================
   Error: A wait of 2 hours 20 minutes 21 seconds is required.
   Full error message: A wait of 8421 seconds is required (caused by InviteToChannelRequest)
   ===========================================================================

   ```

## Important
Make sure you have the necessary permissions in the channel or chat where users are being added. At the first launch, you will be asked for a confirmation code and account password if you have 2fa enabled. The restrictions in the output above are temporary limitations on user invitations and are not related to spam blocking. The script logs already added users in the `added_users.txt` file to avoid duplicate requests.

Please note that a large number of simultaneous invitations can lead to unwanted complaints from users, which may result in spam blocking of the account.

## License
This project is licensed under the terms of the MIT license. See LICENSE for details.

If you need any further assistance or modifications, feel free to ask!

