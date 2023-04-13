import telebot
from telebot import types
import random

token = "5882660038:AAFf6eBR-FHrMFVO695WPwkWGZ5oe1oGDrI"
bot = telebot.TeleBot(token)

hp = damage = 0
races = {"dragon": {"hp": 100000, "damage": 100000},
         "elf": {"hp": 10, "damage": 0},
         "human": {"hp": 30, "damage": 100},
         "bird": {"hp": 1, "damage": 0},
         "god": {"hp": 13848934989329, "damage": 293492802480}}
professions = {"warrior": {"hp": 100, "damage": 100},
               "doctor": {"hp": 10, "damage": 0},
               "бомж": {"hp": 110102929, "damage": 84859449095545}}
monsters = ["zombie", "rabbit", "музычка"]


def race_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for race in races.keys():
        keyboard.add(types.KeyboardButton(text=race))
    return keyboard


def professions_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for prof in professions.keys():
        keyboard.add(types.KeyboardButton(text=prof))
    return keyboard


def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("play")
    btn2 = types.KeyboardButton("about")
    keyboard.add(btn1, btn2)
    return keyboard


@bot.message_handler(commands=["start"])
def main_menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("play")
    btn2 = types.KeyboardButton("about")
    keyboard.add(btn1, btn2)
    bot.send_message(
        message.chat.id, "привет готов ли ты играть", reply_markup=keyboard)


def quest():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = types.KeyboardButton("в путь?")
    btn4 = types.KeyboardButton("назад")
    keyboard.add(btn3, btn4)
    return keyboard


def create_monsters():
    monstername = random.choice(monsters)
    monsterhp = random.randrange(1, 1000)
    monstersdamage = random.randrange(1, 1000000)
    return [monstername, monsterhp, monstersdamage]


@bot.message_handler(content_types=["text"])
def main(message):
    global hp, damage
    victim = create_monsters()
    if message.text == "play":
        bot.send_message(message.chat.id, "выбери расу",
                         reply_markup=race_menu())
    elif message.text == "about":
        bot.send_message(message.chat.id, "н и ч е г о")
    if message.text == "elf":
        hp += races["elf"]["hp"]
        damage += races["elf"]["damage"]
        bot.send_message(
            message.chat.id, f"you are elf, your hp = {hp}, damage = {damage}!", reply_markup=race_menu())
        image = open('11.jpg', "rb")
        bot.send_photo(message.chat.id, image)
    if message.text == "dragon":
        hp += races["dragon"]["hp"]
        damage += races["dragon"]["damage"]
        bot.send_message(
            message.chat.id, f"you are dragon, your hp = {hp}, damage = {damage}!", reply_markup=professions_menu())
        image = open('i-14-67.jpeg', "rb")
        bot.send_photo(message.chat.id, image)
    if message.text == "god":
        hp += races["god"]["hp"]
        damage += races["god"]["damage"]
        bot.send_message(
            message.chat.id, f"you are god, your hp = {hp}, damage = {damage}!", reply_markup=professions_menu())
        image = open('putin_zevs_molniy.jpg', "rb")
        bot.send_photo(message.chat.id, image)

    if message.text == "human":
        hp += races["human"]["hp"]
        damage += races["human"]["damage"]
        bot.send_message(
            message.chat.id, f"you are human, your hp = {hp}, damage = {damage}!", reply_markup=professions_menu())
        image = open('image045.jpg', "rb")
        bot.send_photo(message.chat.id, image)
    if message.text == "bird":
        hp += races["bird"]["hp"]
        damage += races["bird"]["damage"]
        bot.send_message(
            message.chat.id, f"you are bird, your hp = {hp}, damage = {damage}!", reply_markup=professions_menu())
        image = open('1614571595_9-p-golub-na-belom-fone-13.png', "rb")
        bot.send_photo(message.chat.id, image)
    if message.text == "doctor":
        hp += professions["doctor"]["hp"]
        damage += professions["doctor"]["damage"]
        bot.send_message(
            message.chat.id, f"you are doctor, your hp = {hp}, damage = {damage}!", reply_markup=quest())
        image = open('доктор врач.jpg', "rb")
        bot.send_photo(message.chat.id, image)
    if message.text == "warrior":
        hp += professions["warrior"]["hp"]
        damage += professions["warrior"]["damage"]
        bot.send_message(
            message.chat.id, f"you are warrior, your hp = {hp}, damage = {damage}!", reply_markup=quest())
        image = open('солтатик.jpg', "rb")
        bot.send_photo(message.chat.id, image)
    if message.text == "бомж":
        hp += professions["бомж"]["hp"]
        damage += professions["бомж"]["damage"]
        bot.send_message(
            message.chat.id, f"you are бомжr, your hp = {hp}, damage = {damage}!", reply_markup=quest())
        image = open('YpvcMYg5new.jpg', "rb")
        bot.send_photo(message.chat.id, image)
        a = random.randint(1, 2)
        if a == 1:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn3 = types.KeyboardButton("в путь?")
            btn4 = types.KeyboardButton("назад")
            keyboard.add(btn3, btn4)
            bot.send_message(message.chat.id, "никто не пришел",
                             reply_markup=quest())
        if a == 2:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn5 = types.KeyboardButton("драться")
            btn6 = types.KeyboardButton("уйти")
            keyboard.add(btn5, btn6)
            bot.send_message(
                message.chat.id, f"на вас напал {monsters}, что вы сделаете?", reply_markup=keyboard)
    if message.text == "драться":
        victim[1] -= damage
        if victim[1] <= 0:
            hp += 10
            damage += 20
            bot.send_message(
                message.chat.id, f"your hp = {hp}, your damage = {damage}", reply_markup=quest())
        if victim[1] > 0:
            hp -= victim[2]
            bot.send_message(
                message.chat.id, f"вас атакует монстер, твое хп {hp}, damage {damage}")
            if hp <= 0:
                bot.send_message(message.chat.id, "you died")
                image = open('был пацан и нет.jpg', "rb")
                bot.send_photo(message.chat.id, image)
            if hp > 0:
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn5 = types.KeyboardButton("драться")
                btn6 = types.KeyboardButton("уйти")
                keyboard.add(btn5, btn6)
                bot.send_message(message.chat.id, "че дальше?")
    if message.text == "уйти":
        pobeg = random.randint(1, 2)
        if pobeg == 1:
            bot.send_message(
                message.chat.id, "вы убежали, хотите продолжить драться?", reply_markup=quest())
        if pobeg == 2:
            hp -= victim[2]
            bot.send_message(message.chat.id, "вас пришли бить")
            image = open('бой.jpg', "rb")
            bot.send_photo(message.chat.id, image)
            if hp <= 0:
                bot.send_message(message.chat.id, "you died")
                image = open('был пацан и нет.jpg', "rb")
                bot.send_photo(message.chat.id, image)
            if hp > 0:
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn5 = types.KeyboardButton("драться")
                btn6 = types.KeyboardButton("уйти")
                keyboard.add(btn5, btn6)
                bot.send_message(message.chat.id, "че дальше?")


bot.polling(non_stop=True)
