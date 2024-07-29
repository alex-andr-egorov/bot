import telebot
import requests
from bs4 import BeautifulSoup as BS
from telebot import types
token = "7073152220:AAFW_sv8I_1WKfJGUnWirgRELbF12SWQlBw"

r = requests.get("https://sinoptik.ua/погода-бровари")
html = BS(r.content, "html.parser")
bot = telebot.TeleBot(token)

# parser
for el in html.select("#content"):
    t_min = el.select(".temperature .min")[0].text
    if "мин." in t_min:
        t_min = t_min.replace("мин.", "🥶")
    t_max = el.select(".temperature .max")[0].text
    if "макс." in t_max:
            t_max = t_max.replace("макс.","🥵" )
    text = el.select(".wDescription .description")[0].text
    if "облака" in text:
        text = text.replace("облака ", "облака ☁️")
    if "облаками" in text:
        text = text.replace("облаками", "облаками ⛅")
    if "Без осадков." in text:
        text = text.replace("Без осадков.", "\nБез осадков 🌂.")
    else:
        text += '☂️'
    if "ясной" in text:
        text = text.replace("ясной", "ясной 🌞")
    if "ясной" in text:
        text = text.replace("солнце", "солнце ☀️")
# see in terminal
    print(t_min + t_max + "\n" + text.strip())

#command in bot
@bot.message_handler(commands=["start","help"])
# def send_welcome(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     key1 = types.KeyboardButton('START')
#     markup.add(key1)
#     bot.send_message(message.chat.id, "Нажмите кнопку 'START' для начала:", reply_markup=markup)

def main(message):
        bot.send_message(message.chat.id,
                         "Привет, погода на сегодня: " + "\n" + t_min + "\n" + t_max + "\n" + text.strip())


# start bot
if __name__ == "__main__":
    bot.polling(none_stop=True)
