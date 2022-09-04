import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings 
logging.basicConfig(filename='bot.log', level=logging.INFO)

def great_user(update, context):
    print('Вызван \Start')
    update.message.reply_text('Привет, пользователь')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', great_user)) #Объявляем реакцию на команду Start
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал')
    mybot.start_polling() #Запуск постоянных обновлений
    mybot.idle()  #непрерывная работа


main()