import config
import telebot
import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://sinoptik.ua/погода-бровари")
html = BS(r.content, "html.parser")
bot = telebot.TeleBot(config.token)

for el in html.select("#content"):
    t_min = el.select(".temperature .min")[0].text
    t_max = el.select(".temperature .max")[0].text
    text = el.select(".wDescription .description")[0].text

    print(t_min + ',' + t_max + "\n" + text)

@bot.message_handler(commands=["start","help"])
def main(message):
    bot.send_message(message.chat.id, "Привет, погода на сегодня: " + "\n" + t_min + ',' + t_max + "\n" + text)



if __name__ == "__main__":
    bot.polling(none_stop=True)