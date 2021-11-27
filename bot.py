import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/sticker.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("💜 Мой репозиторий")
	item2 = types.KeyboardButton("😈 Написать мне в личку")
	item3 = types.KeyboardButton("👾Фото зла")
	item4 = types.KeyboardButton("☄Гороскоп на сегодня")

	markup.add(item1, item2,item3,item4)

	bot.send_message(message.chat.id, "Привет тебе от краба, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '💜 Мой репозиторий':
			bot.send_message(message.chat.id, 'https://github.com/nami70')
		elif message.text == '😈 Написать мне в личку':
			bot.send_message(message.chat.id, 'https://t.me/TattisUnelmat')
		elif message.text == '👾Фото зла':
			bot.send_message(message.chat.id, 'https://www.instagram.com/prosto_nami/?hl=ru')
		elif message.text == '☄Гороскоп на сегодня':
			bot.send_message(message.chat.id, 'Я не верю в гороскопы. А вы? 🤣🤣🤣')
		else:
			bot.send_message(message.chat.id, 'Возможно что-то пошло не так, но несмотря на это, возьми меня на работу.😇😇😇')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods