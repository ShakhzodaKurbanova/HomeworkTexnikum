import telebot
import d13buttons as buttons


# Создаем объект бота
bot = telebot.TeleBot('7427194700:AAG2ITEqH8vGLmkHlmHsufT5eH_ENMXneuU')


# Обработка команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    bot.send_message(user_id, f'Здравствуйте, {user_name}! Добро пожаловать в мой бот!',
                     reply_markup=buttons.choice_button())


# Обработка текстовых сообщений
@bot.message_handler(content_types=['text'])
def text_message(message):
    user_id = message.from_user.id
    if message.text.lower() == 'википедия':
        bot.send_message(user_id, 'Введите слово')
        # Переход на этап википедии
        bot.register_next_step_handler(message, wiki)
    elif message.text.lower() == 'переводчик':
        bot.send_message(user_id, 'Введите слово для перевода')
        # Переход на этап перевода
        bot.register_next_step_handler(message, translate)


def wiki(message):
    user_id = message.from_user.id
    if message.text.lower() == 'коты':
        bot.send_message(user_id, 'https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%88%D0%BA%D0%B0')
    elif message.text.lower() == 'питон':
        bot.send_message(user_id, 'https://ru.wikipedia.org/wiki/%D0%9F%D0%B8%D1%82%D0%BE%D0%BD%D1%8B')
    else:
        bot.send_message(user_id, 'Я не знаю(((')


def translate(message):
    user_id = message.from_user.id
    if message.text.lower() == 'привет':
        bot.send_message(user_id, 'Hello')
    elif message.text.lower() == 'пока':
        bot.send_message(user_id, 'Bye')
    else:
        bot.send_message(user_id, 'Я такого не знаю((')


# Запуск бота
bot.polling(non_stop=True)