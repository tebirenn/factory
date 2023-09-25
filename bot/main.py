import telebot
import webbrowser
import requests
import os
from telebot import types
from dotenv import load_dotenv
load_dotenv('../.env')


TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: types.Message):
    answer = f'''Привет, <b>{message.from_user.first_name}!</b>\n
Все допустимые команды:
<b>/help</b> - Гид
<b>/register username</b> - Зарегистрировать свой TG на Factory
<b>/site</b> - Перейти на веб-сайт
<b>/id</b>- Узнать свой TG id
    '''
    bot.send_message(message.chat.id, answer, parse_mode='HTML')


@bot.message_handler(commands=['register'])
def register_user(message: types.Message):
    try:
        username = message.text.split()[1]
        try:
            url = 'http://159.89.4.57/authorize/tgregister/'
            data = {'username': username, 'tg_id': message.from_user.id}
            response = requests.post(url, data=data)

            if response.status_code == 200:
                bot.reply_to(message, 'Вы успешно зарегистрированы!', parse_mode='HTML')
            elif response.status_code == 404:
                bot.reply_to(message, f'Пользователь <b>{username}</b> не найден!', parse_mode='HTML')
        except Exception:
            bot.send_message(message.chat.id, 'Ошибка на стороне сервера! Попробуйте позже.', parse_mode='HTML')

    except IndexError:
        bot.reply_to(message, "Пожалуйста, укажите имя пользователя после команды /register через пробел.")


@bot.message_handler(commands=['id'])
def send_id(message: types.Message):
    bot.reply_to(message, f'Ваш ID: <b>{message.from_user.id}</b>', parse_mode='HTML')


@bot.message_handler(commands=['site'])
def site(message: types.Message):
    bot.send_message(message.chat.id, 'Посетите наш веб-сайт <a href="http://159.89.4.57/authorize">здесь</a>', parse_mode='html')
    webbrowser.open('http://159.89.4.57/authorize')


if __name__ == '__main__':
    bot.polling(none_stop=True, skip_pending=True)