# бот name = get_course
# username = course_skillfactory_bot
# token = 6206307771:AAE2DVn-eska9L-p1l-KO0oNAKUuUIGj7Bo
# t.me/course_skillfactory_bot

import telebot
from config import keys, TOKEN
from extensions import APIException, getAPI

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text='Чтобы начать работу введите команду бота в следующем формате :\n \
<имя валюты, цену которой хотите узнать> \n \
<имя валюты, в которой надо узнать цену первой валюты>\n \
<количество переводимой валюты>\n \n \
Список всех доступных валют /values '
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text='Доступные валюты:'
    for key in keys.keys(): # перебираем все ключи
        text='\n'.join((text,key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    vals = message.text.split()
    try:
        if len(vals) != 3:
            raise APIException('Неправильное количество параметров')
        quote, base, amount = vals
        res=getAPI.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        bot.reply_to(message, res)

#bot.polling(none_stop=True)
bot.polling()