# import os
# os.kill(os.getpid(), 9)
from threading import ExceptHookArgs
import telegram, time, math
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from telegram.message import Message

token_bot = '5083901620:AAHxQel-awAeB7lHxI_iQ9G25Q597NgXXJY'
bot = telegram.Bot(token_bot)
myid = '146277118'
updates = bot.getUpdates()
# for u in updates:
#     print(u.message)
    
# bot.sendMessage(chat_id = myid, text = 'hell-o-world')    

updater = Updater(token_bot, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context):
    user_text = update.message.text
    cur_time = time.time()
    if user_text == 'menu':
        bot.send_message(myid, text='hoy')
    
echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
