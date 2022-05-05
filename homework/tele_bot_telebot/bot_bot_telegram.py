from concurrent.futures import Executor
from email import message
import telebot
from telebot import types
from config import TOKEN, open_weatther_token
import requests
import datetime

bot = telebot.TeleBot(TOKEN)

def keyboard_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('/start')
    markup.add(item1)
    bot.send_message(message.chat.id, 'начинаем с начала?',reply_markup = markup)

@bot.message_handler(commands = ['start'])
def welcome_user(message, txt = None):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Игра')
    item2 = types.KeyboardButton('Погода')
    item3 = types.KeyboardButton('Курсы валют')
    item4 = types.KeyboardButton('Поговорим о тебе?')
    markup.add(item1, item2, item3, item4)
    if txt is None:
        bot.send_message(message.chat.id, f'Привет {message.from_user.username}\nДавай посмотрим, что я умею!', reply_markup = markup)
    else:
        bot.send_message(message.chat.id, txt, reply_markup = markup)

@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.text == 'Игра':
        markup = telebot.types.ReplyKeyboardRemove()
        msg = bot.send_message(message.chat.id, 'Давай поиграем!\nНапишите слово:', reply_markup = markup)
        bot.register_next_step_handler(msg, change_message)

    elif message.text == 'Погода':
        markup = telebot.types.ReplyKeyboardRemove()
        msg = bot.send_message(message.chat.id, 'Напишите город, в котором хочешь узнать погоду:', reply_markup = markup)
        bot.register_next_step_handler(msg, weather)

    elif message.text == 'Курсы валют':
        markup = telebot.types.ReplyKeyboardRemove()
        msg = bot.send_message(message.chat.id, 'Это может занять около 25 секунд 😔, напиши мне,в каком городе РБ тебя интересуют курсы: !!\n\
П.с. чем меньше город - тем меньше ждать 🙂', reply_markup = markup)
        bot.register_next_step_handler(msg, exchange)
        
    elif message.text == 'Поговорим о тебе?':
        markup = telebot.types.ReplyKeyboardRemove()
        msg = bot.send_message(message.from_user.id, 'Давай поговорим о тебе, напиши +, если согласен?', reply_markup = markup)
        bot.register_next_step_handler(msg, info)

    elif message.text == '/start':
        msg = bot.send_message(message.chat.id, 'Давай начнем все с начала! Нажимай Старт')
        bot.register_next_step_handler(msg, welcome_user(message))

def change_message(message):
    text = message.text.lower()
    bot.send_message(message.chat.id, text[::-1])
    bot.send_message(message.chat.id, '😂😂😂')
    end_func(message)

def weather(message):
    emodji = {
            'Clear': 'Ясно \U00002600',
            'Clouds': 'Облачно \U00002601',
            'Rain': 'Дождь \U00002614',
            'Drizzle': 'Ясно \U00002614',
            'Thunderstorm': 'Гроза \U000026A1',
            'Snow': 'Снег \U0001F328',
            'Mist': 'Туман \U0001F23B'
            }

    try:
        r = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weatther_token}&units=metric'
            )
        data = r.json()
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        city = data['name']
        cur_temp = data['main']['temp']
        cur_humidity = data['main']['humidity']
        cur_pressure = data['main']['pressure']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        wind_speed = data['wind']['speed']
        sunrise_time = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_time = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        weather_emodzi = data['weather'][0]['main']
        if  weather_emodzi in emodji:
            weather_em = emodji[weather_emodzi]
        else:
            weather_em = 'Происходит что то странное, посмотри в окно'
        bot.send_message(message.chat.id, f'Сегодня ***{now}***\n'
                f'Погода в городе {city.capitalize()}:\n'
                f'Температура: {cur_temp} °С\n'
                f'{weather_em}\n'
                f'Влажность: {cur_humidity} %\n'
                f'Давление: {cur_pressure} мм.рт.ст\n'
                f'Максимальная температура: {temp_max} °С\n'
                f'Минимальная температура: {temp_min} °С\n'
                f'Скорость ветра: {wind_speed} м.с\n'
                f'Время рассвета: {sunrise_time}\n'
                f'Время заката: {sunset_time}\n'
                f'Хорошего Вам дня!!\n\n'
        )

    except :
        bot.send_message(message.chat.id, 'проверьте название города!')
    
    end_func(message)

def exchange(message):
    try:
        now = datetime.datetime.now().strftime('%d-%m-%Y')
        city = message.text
        url = f'https://belarusbank.by/api/kursExchange?city={city}' 
        r = requests.get(url)
        data = r.json()
        usd_in = data[0]['USD_in']
        usd_out = data[0]['USD_out']
        eur_in = data[0]['EUR_in']
        eur_out = data[0]['EUR_out']
        rub_in = data[0]['RUB_in']
        rub_out = data[0]['RUB_out']
        bot.send_message(message.chat.id,f'Курсы валют на {now}\nВ городе {city.capitalize()}:')
        bot.send_message(message.chat.id, f'Курс покупки USD: {usd_in};\nКурс продажи USD: {usd_out};\n\
Курс покупки EUR: {eur_in};\nКурс продажи EUR: {eur_out};\nКурс покупки RUB: {rub_in};\nКурс продажи RUB: {rub_out}.\n'
        )
    except :
        bot.send_message(message.chat.id, 'проверьте название города!')
    end_func(message)



def info(message):
    text = message.text.lower()
    if text in ['да','давай', 'yes', 'y', 'ок', 'согласен','+', 'вернуться назад']:
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('животные')
        item2 = types.KeyboardButton('хобби')
        item3 = types.KeyboardButton('машины')
        item4 = types.KeyboardButton('путешествия')
        back = types.KeyboardButton('вернуться в начало')
        markup.add(item1, item2, item3, item4, back)
        msg = bot.send_message(message.chat.id, 'выбери категорию, о которой хотел бы поговорить:',reply_markup = markup)
        bot.register_next_step_handler(msg, info_choice)        
    else:
         bot.send_message(message.chat.id, 'значит в другой раз')
         keyboard_start(message)

def info_choice(message):
    if message.text == 'животные':
        txt = 'у тебя есть домашние животные?'
        txt1 = 'напиши, кто у тебя:'
        txt2 = 'может пора завести, но это уже совсем другая история...'
        msg = info_choice_buttons(message,txt)
        bot.register_next_step_handler(msg, info_ask_1,txt1,txt2)

    elif message.text == 'хобби':
        txt = 'у тебя есть хобби?'
        txt1 = 'напиши, какое:'
        txt2 = 'может пора начать чем то увлекаться? Но это уже совсем другая история...'
        msg = info_choice_buttons(message,txt)
        bot.register_next_step_handler(msg, info_ask_1,txt1,txt2)

    elif message.text == 'машины':
        txt = 'у тебя есть машина?'
        txt1 = 'напиши, какая марка:'
        txt2 = 'может пора задумать о покупки своего личного авто? Но это уже совсем другая история...'
        msg = info_choice_buttons(message,txt)
        bot.register_next_step_handler(msg, info_ask_1,txt1,txt2)

    elif message.text == 'путешествия':
        txt = 'Любишь путешествовать?'
        txt1 = 'напиши, в какую страну ты бы посоветовал сьездить:'
        txt2 = 'Туризм и путешествия наверное не для всех... но это уже совсем другая история...'
        msg = info_choice_buttons(message,txt)
        bot.register_next_step_handler(msg, info_ask_1,txt1,txt2)

    elif message.text == 'вернуться в начало':
        bot.send_message(message.chat.id, f'значит поговорим в другой раз')
        keyboard_start(message)
        bot_message(message)

def info_choice_buttons(message,txt):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('да')
    item2 = types.KeyboardButton('нет')
    back = types.KeyboardButton('вернуться назад')
    markup.add(item1, item2, back)
    msg = bot.send_message(message.chat.id, txt, reply_markup = markup)
    return msg

def info_ask_1(message,txt1,txt2):
    if message.text == 'да':
        markup = telebot.types.ReplyKeyboardRemove()
        msg = bot.send_message(message.from_user.id, txt1, reply_markup = markup)
        bot.register_next_step_handler(msg, end_func)
        
    elif message.text == 'нет':
        bot.send_message(message.chat.id, txt2)
        message.text = 'да'
        end_func(message)
        
    elif message.text == 'вернуться назад':
        message.text = 'да'
        end_func(message)

def end_func(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    back = types.KeyboardButton('вернуться в основное меню')
    markup.add(back)
    msg = bot.send_message(message.chat.id, 'Спасибо, что воспользовались нашим сервисом!', reply_markup = markup)
    txt = 'ну что, продолжим общение?'
    bot.register_next_step_handler(msg, welcome_user, txt)

bot.polling(none_stop = True)  