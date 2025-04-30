from django.core.management.base import BaseCommand

from av_back.av_back import settings
from av_back.av_back.settings import TELEGRAM_BOT_API_KEY

from telebot import TeleBot
from telebot import types

bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)


class Command(BaseCommand):
  	# Используется как описание команды обычно
    help = 'Just a command for launching a Telegram bot.'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2) # Сохранение обработчиков
        bot.load_next_step_handlers()				# Загрузка обработчиков
        bot.infinity_polling()

    @bot.message_handler(commands=['start'])
    def start(message):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Поздороваться")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "👋 Привет! Я твой проводник по лучшим акциям для автомобилистов Беларуси!", reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):

        if message.text == '👋 Поздороваться':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
            btn1 = types.KeyboardButton('Хочу получать инфу по розыгрышам')
            btn2 = types.KeyboardButton('Хочу получать инфу по акциям')
            btn3 = types.KeyboardButton('Хочу зарегестрироваться на av')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос',
                             reply_markup=markup)  # ответ бота


        elif message.text == 'Хочу получать инфу по розыгрышам':
            bot.send_message(message.from_user.id,
                             'Инфа',
                             parse_mode='Markdown')

        elif message.text == 'Хочу получать инфу по акциям':
            bot.send_message(message.from_user.id,
                             'Инфа',
                             parse_mode='Markdown')

        elif message.text == 'Хочу зарегестрироваться на av':
            bot.send_message(message.from_user.id,
                             'Подробно про советы по оформлению публикаций прочитать по ' + '[ссылке](http://localhost:3000/register)',
                             parse_mode='Markdown')

    bot.polling(none_stop=True, interval=0)