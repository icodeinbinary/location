# Location Sender Bot

This program sends your current GPS location to a Telegram bot when executed.

## Setup Instructions

1. Create a Telegram bot:
   - Open Telegram and search for "BotFather"
   - Send /newbot command and follow instructions
   - Copy the bot token provided

2. Get your Telegram Chat ID:
   - Send a message to your bot
   - Visit: https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   - Look for "chat":{"id": XXXXXXXXX} and copy the ID

3. Install requirements:
   ```
   pip install -r requirements.txt
   ```

4. Edit location_sender.py:
   - Replace YOUR_BOT_TOKEN_HERE with your actual bot token
   - Replace YOUR_CHAT_ID_HERE with your chat ID

5. Run the program:
   ```
   python location_sender.py
   ```

The program will send your current location to your Telegram bot when executed.
