import telebot

bot = telebot.TeleBot('7471516624:AAEYEfBVEyoDh1NeoJk0gJrGqvtZYtX2o40')

@bot.message_handler(commands=['start'])
def start_message(msg):
    user_id = msg.from_user.id
    bot.send_message(user_id, f'Здравствуйте, (имя) 🌺 \n'
                              'Добро пожаловать на нашу кампанию! \n'
                              'Что хотели бы узнать?')


bot.polling(non_stop=True)