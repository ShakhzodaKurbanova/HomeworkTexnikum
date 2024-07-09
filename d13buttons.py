from telebot import types

def choice_button():
# создать пространство для кнопки
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
# дальше создаем кнопки
    button1 = types.KeyboardButton('Википедия')
    button2 = types.KeyboardButton('Переводчик')
# добавляем кнопки в простанство
    kb.add(button1, button2)

    return kb