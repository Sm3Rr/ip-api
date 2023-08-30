
import telebot

# توکن ربات خود را در اینجا قرار دهید
TOKEN = '5307073299:AAG2h0nuNRxn3OBA7fhFlLcCA1Bd-DuVTXg'

# ایجاد یک نمونه از کلاس TeleBot با استفاده از توکن ربات
bot = telebot.TeleBot(TOKEN)

# تعریف یک دستور
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "hello wellcome")

# تعریف یک پیام عادی
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# راه اندازی ربات و ورود به حالت شنود
bot.polling()
