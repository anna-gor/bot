import telebot

bot = telebot.TeleBot('1320536909:AAFmjzIQDxsVVGHUoO5h7neWtha2CM_ZINo')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


bot.polling()