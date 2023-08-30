
import telegram
from telegram.ext import Updater, CommandHandler

def start(update, context):
    # دریافت اطلاعات در صورت استفاده از دستور /start
    user = update.message.from_user
    chat_id = update.message.chat_id

    # دریافت ایپی کاربر
    user_ip = update.message.from_user['id']

    # ارسال ایپی کاربر به ادمین
    admin_chat_id = '1668896742'
    bot.send_message(chat_id=admin_chat_id, text=f'New user IP: {user_ip}')

def main():
    # تنظیم توکن ربات تلگرام خود
    token = '5307073299:AAG2h0nuNRxn3OBA7fhFlLcCA1Bd-DuVTXg'
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    # اضافه کردن handler برای دستور /start
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # برقراری ارتباط با سرور تلگرام و استدلال شروع برنامه
    updater.start_polling()

if __name__ == '__main__':
    main()
