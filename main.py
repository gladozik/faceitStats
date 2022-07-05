import telebot
from getFaceitStats import player_details

bot = telebot.TeleBot('5578820779:AAH26rL2XwIYswGLWxLhsyPSct31udR7TDI')


@bot.message_handler(commands=['start'])
def start(message):
    # markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton("Сколько Владу до 10?"))
    bot.send_message(message.chat.id, 'Команды: /start - начать /get_statistic - узнать, сколько Владу до 10 лвла',
                     parse_mode='html')


elo_until_10 = int(player_details["games"]["csgo"]["faceit_elo"])


@bot.message_handler(commands=['get_statistic'])
def get_statistic(message):
    bot.send_message(message.chat.id, f"Владу до 10 лвла еще {2001 - elo_until_10} эло")


bot.polling(none_stop=True)
