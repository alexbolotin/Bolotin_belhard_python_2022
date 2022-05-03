from concurrent.futures import Executor
from email import message
import telebot
from telebot import types
from config import TOKEN, open_weatther_token
import requests
import datetime

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands = ['start'])
def welcome_user(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('кнопка 1')
    item2 = types.KeyboardButton('Погода')
    item3 = types.KeyboardButton('Курсы валют')
    item4 = types.KeyboardButton('кнопка 4')

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, f'Привет {message.from_user.username}', reply_markup = markup)

@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.text == 'кнопка 1':
        msg = bot.send_message(message.chat.id, 'Напишите слово:')
        bot.register_next_step_handler(msg, change_message)
    elif message.text == 'Погода':
        msg = bot.send_message(message.chat.id, 'Напишите город, в котором хочешь узнать погоду:')
        bot.register_next_step_handler(msg, weather)
    elif message.text == 'Курсы валют':
        msg = bot.send_message(message.chat.id, 'Это может занять около 25 секунд 😔, напиши мне,в каком городе РБ тебя интересуют курсы: !!\n\
П.с. чем меньше город - тем меньше ждать 🙂')
        bot.register_next_step_handler(msg, exchange)

def change_message(message):
    text = message.text.lower()
    if text in ['привет','hi', 'hello']:
        bot.send_message(message.chat.id, 'и тебе привет')
    else:
        bot.send_message(message.chat.id, text[::-1])

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
                f'Погода в городе {city}:\n'
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

def exchange(message):
    try:
        now = datetime.datetime.now().strftime('%Y-%m-%d')
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
        bot.send_message(message.chat.id,f'Курсы валют на {now}\nВ городе {city}:')
        bot.send_message(message.chat.id, f'Курс покупки доллара: {usd_in};\nКурс продажи доллара: {usd_out};\n\
Курс покупки евро: {eur_in};\nКурс продажи евро: {eur_out};\nКурс покупки российского рубля: {rub_in};\nКурс продажи российского рубля: {rub_out}.\n'
        )
    except :
        bot.send_message(message.chat.id, 'проверьте название города!')

bot.polling(none_stop = True)