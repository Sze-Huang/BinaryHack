# import telebot
# import time
# import googl
import urllib
import configparser
from lxml.html import fromstring
from requests import get
# from telebot import types
from urllib.parse import urlencode, urlparse, parse_qs
 


def long_url(text):
    text = urllib.parse.quote_plus(text)
    # long_url = 'https://google.com/search?q='+ text
    raw = get('https://google.com/search?q='+ text).text
    page = fromstring(raw)
	
    link = []
    for result in page.cssselect(".r a"):
        print (result)
        url = result.get("href")
        if url.startswith("/url?"):
            url = parse_qs(urlparse(url).query)['q']
        # print(url[0])
        link.append(url[0])
    # print ("testing")
    # print (link[0])
	
    
    return link[0]

# orderlist = [];
# def	list(order):
    # orderlist.append(order)
    # return orderlist

bot = telebot.TeleBot('477303162:AAFnoyqx-1qXaJ4BJ8BBGjQ8x1IrX39u8J0')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Howdy, welcome to this bot! Ask me anything :)")

	
@bot.message_handler(commands=['info'])
def send_welcome(message):
    info = ('This bot is under development!\n'
        'If you have any question or suggestion,\n'
        'please, talk to me!\n')
    bot.reply_to(message, info)

@bot.message_handler(commands=['orderlist'])
def send_welcome(message):
    info = ("Add your order list by adding one by one. Use: '/add xxx' to update the list.\n")
    bot.reply_to(message, info)	
	
# orderlist = [];
# @bot.message_handler(commands=['add'])
# def handle_message(message):
    # # info = ("Your order list:\n")
    # orderlist.append(message.text)
    # bot.reply_to(message, "Your order list:\n" + message +'\n')	
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    #print(message.text)
#    long_url = 'a'
    url = long_url(message.text)
    #print(url)
    bot.reply_to(message, 'I don\'t know, but I can search for you:\n'+ url)

try: 
    bot.polling(none_stop=True)
except urllib.error.HTTPError:
    time.sleep(10)


while True:
    time.sleep(20)

