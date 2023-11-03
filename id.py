from telebot import TeleBot

bot = TeleBot('токен бота')


@bot.message_handler()
def get_id(message):
    print(message.chat.id)
