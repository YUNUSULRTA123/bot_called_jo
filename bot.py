import telebot 
from telebot import types
import sys
import os
sys.path.append(os.getcwd())

import telegram_token
from random import choice

TOKEN=telegram_token.token

bot = telebot.TeleBot(TOKEN)

it_jokes = [
    "Почему программисты не любят природу? Потому что там слишком много багов!",
    "Какой язык программирования предпочитает вампир? Python, потому что он любит кровь!",
    "Что скажет программист, увидев змею? 'О, Python!'",
    "Почему программисты не могут играть в прятки? Потому что хорошие программисты всегда найдут баги!",
    "Какой любимый напиток программиста? Java, конечно же!",
]

quotes = [
    "Путь в тысячу ли начинается с одного шага. — Лао-цзы",
    "Знание — сила. — Фрэнсис Бэкон",
    "Будь собой; все остальные роли уже заняты. — Оскар Уайльд",
    "Без труда не вытащишь и рыбку из пруда. — Русская пословица",
]

facts = [
    "Осьминоги имеют три сердца, и их кровь синего цвета.",
    "В космосе никто не услышит ваш крик — звук не распространяется в вакууме.",
    "Мёд — единственный продукт, который не портится. Учёные находили съедобный мёд в гробницах фараонов.",
    "Некоторые виды медуз бессмертны — они способны возвращаться в молодую форму после зрелости.",
    "В Антарктиде есть река, которая течёт подо льдом и никогда не замерзает — она называется река Блад-Фоллс.",
    "Человеческий мозг потребляет примерно 20% всей энергии тела, хотя составляет лишь около 2% массы.",
    "У бабочек есть рецепторы вкуса на лапках.",
    "Сатурн настолько лёгкий, что если бы был бассейн с водой достаточного размера, он бы в нём плавал.",
    "Каждую минуту в вашем теле умирают и заменяются около 300 миллионов клеток.",
    "На Венере день длится дольше, чем год — она вращается очень медленно вокруг своей оси."
]

@bot.message_handler(commands=['start','help'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Button 1")
    button2 = types.KeyboardButton("Button 2")
    keyboard.add(button1, button2) 
    bot.send_message(message.chat.id, "Добро пожаловать!", reply_markup=keyboard)

@bot.message_handler(commands=['info','jo'])
def info(message):
    bot.reply_to(message, """👋 Привет-привет! Я — твой дружелюбный бот-помощник по имени Джо 🤖✨

📌 Вот команды, которые я понимаю и на которые могу ответить:
➡️ /start и /help — начать наше увлекательное общение 🚀
➡️ /info и /jo — узнать обо мне и моих возможностях ℹ️
➡️ /coin — бросить монетку (ОРЕЛ или РЕШКА) 🪙
➡️ /itjokes - услышать шутки про IT 💻😂
➡️ /quote — получить вдохновляющую цитату 🌟
➡️ /fun_fact — узнать интересный факт 🌍
➡️ /car — получить информацию о твоей машине 🚗
💬 Просто напиши мне любое сообщение и я стану папугаем 🤣, а так я всегда готов поддержать разговор и помочь! 😊👍
""")

@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)

@bot.message_handler(commands=['itjokes'])
def it_joke(message):
    rand_joke = choice(it_jokes)
    bot.reply_to(message, rand_joke)

@bot.message_handler(commands=['quote'])
def quote(message):
    rand_quote = choice(quotes)
    bot.reply_to(message, rand_quote)

@bot.message_handler(commands=['fun_fact'])
def fact(message):
    rand_fact = choice(facts)
    bot.reply_to(message, rand_fact)

@bot.message_handler(commands=['car'])
def car_info(message):
    class Car():
        def __init__(self, color, brand):
            self.color = color
            self.brand = brand
        
        def info(self):
            return f"Цвет машины: {self.color}, Марка машины: {self.brand}"

    args = telebot.util.extract_arguments(message.text).split()

    if len(args) != 2:
        bot.reply_to(message, """
Чтобы получить информацию о вашей машине, введите команду следующим образом:
Пример использования: /car черный BMW""")

    color, brand = args
    my_car = Car(color, brand)
    bot.reply_to(message, my_car.info())

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    print("Бот запускается...")
    bot.polling()
