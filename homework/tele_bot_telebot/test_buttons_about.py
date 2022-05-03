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
    

def keyboard_main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('test 1')
    item2 = types.KeyboardButton('test 2')
    item3 = types.KeyboardButton('test 3')
    item4 = types.KeyboardButton('Поговорим о тебе?')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'давай посмотрим, что я умею 🙂',reply_markup = markup)
    

@bot.message_handler(commands = ['start'])
def welcome_user(message):
    keyboard_main(message)

@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.text == 'test 1':
        msg = bot.send_message(message.chat.id, 'Напишите слово:')
        bot.register_next_step_handler(msg, change_message)

    elif message.text == 'test 2':
        msg = bot.send_message(message.chat.id, 'Напишите город, в котором хочешь узнать погоду:')
        bot.register_next_step_handler(msg, weather)

    elif message.text == 'test 3':
        msg = bot.send_message(message.chat.id, 'Это может занять около 25 секунд 😔, напиши мне,в каком городе РБ тебя интересуют курсы: !!\n\
П.с. чем меньше город - тем меньше ждать 🙂')
        bot.register_next_step_handler(msg, exchange)
        
    elif message.text == 'Поговорим о тебе?':
        markup = telebot.types.ReplyKeyboardRemove()
        msg = bot.send_message(message.from_user.id, 'Давай поговорим о тебе, напиши +, если согласен?', reply_markup = markup)
        bot.register_next_step_handler(msg, info)

    elif message.text == '/start':
        msg = bot.send_message(message.chat.id, 'Давай начнем все с начала! Нажимай Старт')
        bot.register_next_step_handler(msg, welcome_user(message))


def change_message(message):
    bot.send_message(message.chat.id, 'поговорим позже!')

def weather(message):
    bot.send_message(message.chat.id, 'поговорим о погоде позже!')
   

def exchange(message):
    bot.send_message(message.chat.id, 'поговорим о курсах позже!')


def info(message):
    text = message.text.lower()
    if text in ['да','давай', 'yes', 'y', 'ок', 'согласен','+']:
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
        msg = info_choice_buttons(message,txt)
        bot.register_next_step_handler(msg, animals)

    elif message.text == 'хобби':
        pass

    elif message.text == 'машины':
         pass

    elif message.text == 'путешествия':
         pass

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

def animals(message):
    if message.text == 'да':
        markup = telebot.types.ReplyKeyboardRemove()
        msg = bot.send_message(message.from_user.id, 'напиши, кто у тебя:', reply_markup = markup)
        bot.register_next_step_handler(msg, animals_end)
        
    elif message.text == 'нет':
        bot.send_message(message.chat.id, f'может пора завести, но это уже совсем другая история...')
        message.text = 'да'
        info(message)
    elif message.text == 'вернуться назад':
        message.text = 'да'
        info(message)

def animals_end(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    back = types.KeyboardButton('вернуться назад')
    markup.add(back)
    msg = bot.send_message(message.chat.id, f'Спасибо за ответ', reply_markup = markup)
    message.text = 'да'
    bot.register_next_step_handler(msg, info(message))

bot.polling(none_stop = True)  