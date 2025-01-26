from flask import Flask, render_template, request, jsonify
from telegram import Bot
import asyncio
import os

app = Flask(__name__)

# Replace these with your actual Telegram bot token
TELEGRAM_BOT_TOKEN = "6480432275:AAGmcGl0WOtPptSM8BTMN_vynpZulh8M4lM"
# Replace with your Telegram chat ID
CHAT_ID = "1074750898"

async def send_to_telegram(latitude, longitude):
    """Send location to Telegram bot"""
    try:
        # Initialize the bot
        bot = Bot(token=TELEGRAM_BOT_TOKEN)

        # Send location message
        await bot.send_message(
            chat_id=CHAT_ID,
            text=f"📍 Current Location:\nLatitude: {latitude}\nLongitude: {longitude}\n"
            f"Google Maps Link: https://www.google.com/maps?q={latitude},{longitude}"
        )
        # Also send as actual location message
        await bot.send_location(
            chat_id=CHAT_ID,
            latitude=latitude,
            longitude=longitude
        )
        return True
    except Exception as e:
        print(f"Error sending location: {str(e)}")
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-location', methods=['POST'])
def send_location():
    try:
        data = request.json
        latitude = data['latitude']
        longitude = data['longitude']
        
        # Run the async function to send to Telegram
        success = asyncio.run(send_to_telegram(latitude, longitude))
        
        if success:
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': 'Failed to send location to Telegram'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    # Get port from environment variable (Render sets this automatically)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
