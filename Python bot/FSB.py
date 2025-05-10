from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
def start(update, context):
    update.message.reply_text('Привет! Этот бот может помочь!')

def clear(update, context):
    english = ["apple", "pineapple", "watermelon", "pinecone"]
    nomer = update.message.text
    update.message.reply_text(random.choice(english))
def text(update, context):
    #получаем текст от пользователя
    telnomer = update.message.text
    f = False
    for i in telnomer:
        if i.isdigit():
            f = True
            break
    clear_number = ""
    if f:
        for i in telnomer:
            if i.isdigit():
                clear_number += i
        update.message.reply_text(clear_number)
    else:
        address_str = (telnomer.upper())
        update.message.reply_text(address_str)
def main():
    updater = Updater("5866321892:AAG_EVUN4aYz_B46gsXnExKyg1rENLmKo7Q", use_context=True)
    dispatcher = updater.dispatcher
    #регистрируем команду /start и говорим, что после нее надо использовать функцию def start
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("clear", clear))
    #регистрируем получение текста и говорим, что после нее надо использовать функцию def text
    dispatcher.add_handler(MessageHandler(Filters.text, text))
    #регистрируем получение локации и говорим, что после нее надо использовать функцию def location

    #запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    #запускаем функцию def main
    main()