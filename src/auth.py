import telebot
import random
import string
import requests
from conf import TELEGRAM_BOT_TOKEN, FASTAPI_URL

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Welcome! Please share your name and phone number to authenticate.")
    bot.send_message(message.chat.id, "Press the button below to share your phone number.", reply_markup=telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True).row(
        telebot.types.KeyboardButton('Share Phone Number', request_contact=True)
    ))

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    if message.contact:
        user_id = message.contact.user_id
        user_auth_data = {
            "_id": user_id,
            "first_name": message.contact.first_name,
            "phone_number": message.contact.phone_number
        }
        response = requests.post(f"{FASTAPI_URL}/add_user", json=user_auth_data)
        if response.status_code != 200:
            bot.send_message(message.chat.id, "Возникла ошибка при обработке данных")
            return
        bot.send_message(message.chat.id, "Вы успешно авторизировались")




bot.polling()