from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
import random
pictures = [
    'phot/pc1.jpeg', "phot/pc2.jpeg", "phot/pc3.jpeg", "phot/pc4.jpeg"
]
# info_pictures = [
#     ["шишка 1",'phot/11.png'], ["шишка 2", "phot/22.png"], ["шишка 3", "phot/33.png"]
# ]

info_user = {"spam":[]}
def start(update, context):
    button_list = [
        [KeyboardButton('Система и шкала оценок'), KeyboardButton('Расположение кабинетов')],
        [KeyboardButton('Расписание')]
    ]
    reply_markup = ReplyKeyboardMarkup(button_list, resize_keyboard=True, one_time_keyboard=True)
    req = update.message.text.lower()
    info_user["first_name"] = (update["message"]["chat"]["first_name"])
    # print(info_user)
    update.message.reply_text(f'Привет, {info_user["first_name"]}! Этот бот был создан для помощи новичкам, поступившим в НШ.\nЗдесь ты можешь найти информацию по нескольким ключевым темам в школе.\nВнизу есть кнопки, нажимая на которые, можно получить ответы на соответствующие темы.', reply_markup=reply_markup)
def clear(update, context):
    english = ["apple", "pineapple", "watermelon", "pinecone"]
    nomer = update.message.text
    update.message.reply_text(random.choice(english) + "\nПасхалка?")

def text(update, context):
    req = update.message.text.lower()
    if "привет" in req or 'здравсв' in req or 'салам' in req:
        update.message.reply_text("Расписание")
    elif "назад" in req:
        back(update, context)
    elif "система и шкала оценок" in req:
        mark(update, context)
    elif "расписание" in req:
        schedule(update, context)
    # elif "факты про школу" in req:
    #     fact = random.choice(info_pictures)
    #     # update.message.reply_text(fact[0])
    #     send_facts(update, context)
    elif "10 класс" in req:
        schedule10(update,text)
    elif "11 класс" in req:
        schedule11(update, text)
    elif "9 класс" in req:
        schedule9(update,text)
    elif "100-балльная система" in req:
        update.message.reply_text("В школе используется 100-балльная система, которая по словам департамента образования имеет несколько явных приемуществ над пятибалльной, а именно:\n-Даёт более точную оценку знаний учащегося\n-Помогает точнее определить уровень знаний\n-Чётче показывает, где у ученика есть пробелы в знаниях")
    elif "расположение кабинетов" in req:
        cabinets(update, context)
    elif "театральный зал" in req:
        update.message.reply_text("На первом этаже, сразу рядом с входом, находится Театральный зал, или ТЗ.\nВ нём проводятся ассамблеи, защиты проектов, фестивали и другие мероприятия, в которых предстоит участвовать.")
    elif "индивидуальный учебный план" in req:
        update.message.reply_text("В начале года каждый ученик заполняет свой собственный Индивидуальный учебный план (дальше ИУП), в котором он выбирает интересующие его предметы для изучения.\nГлавный плюс ИУПа - в его гибкости: каждый ученик может выбрать предметы на свой вкус и цвет и совершенно в разных областях знаний.\nИУП является отличным оптимизатором времени, так как за 2 класса старшей школы необходимо многое успеть, и ИУП с этим отлично помогает, распределяя учебное время наиболее эффективным способом.")
    elif "специальные кабинеты" in req:
        update.message.reply_text("В школе есть несколько специальных кабинетов, отличающихся от обычных. К ним можно отнести: Фаблаб, где можно что-то смастерить; Кулинариум, в котором можно приготовить себе поесть; Лекторий, в который можно собрать целую параллель и другие.\nВпрочем, в таких кабинетах иногда проводят и обычные уроки.")
    elif "виды работ" in req:
        update.message.reply_text("В школе есть 2 типа заданий: констатирующие и формирующие работы. К формирующим работам относятся такие активности как: тренировочные задания, домашние задания, работа на уроке, самостоятельная работа - все активности, которые помогают научиться. Констатирующие же работы - это контрольные и проверочные работы, и именно из оценок за констатирующие работы выставляется оценка за триместр.\nНекоторые считают, что формирующие работы необязательны, но они в корне неправы: если средний балл за формирующие работы выше, чем за констатирующие, можно попросить учителя поднять триместровую оценку за счёт формирующих работ.")
    elif "этажи и уроки" in req:
        floors(update, context)
    elif "конвертация оценок" in req:
        update.message.reply_text("Так как в России законом утверждена пятибалльная система, то в аттестат ученика все оценки записываются в пятибалльной системе, что означает, что из 100-балльной происходит конвертация. Происходит она по следующей схеме:\n- Пятёрка - от 85 до 100 баллов\n- Четверка - от 70 до 84 баллов\n- Тройка - от 50 до 69 баллов\nНу а дальше все наверное поняли, что идёт двойка)")
    else:
        info_user["spam"].append(str(req))
def back(update, context):
    button_list = [
        [KeyboardButton('Система и шкала оценок'), KeyboardButton('Расположение кабинетов')],
        [KeyboardButton('Расписание')]
    ]
    reply_markup = ReplyKeyboardMarkup(button_list, resize_keyboard=True, one_time_keyboard=False)
    update.message.reply_text("Чем ещё могу быть полезен?", reply_markup=reply_markup)
def mark(update, context):
    button_list = [
        [KeyboardButton('100-балльная система'), KeyboardButton('Индивидуальный учебный план')],
        [KeyboardButton('Виды работ'), KeyboardButton('Конвертация оценок')]
    ]
    reply_markup = ReplyKeyboardMarkup(button_list, resize_keyboard=True, one_time_keyboard=False)
    update.message.reply_text("В школе используется 100-балльная система оценивания, по словам учителей, такая система по сравнению с пятибалльной системой более гибкая и точная.\nВместо контрольных и проверочных работ проверка знаний проводится по констатирующим работам, а формирующие работы способствуют развитию знаний и умений. Из баллов по констатирующим работам формируется оценка за триместр, которую иногда возможно поднять с помощью формирующих работ (ДЗ, работа на уроке и т.д.)", reply_markup=reply_markup)
def cabinets(update,context):
    button_list = [
        [KeyboardButton('Этажи и уроки'), KeyboardButton('Специальные кабинеты'),
        KeyboardButton("Театральный зал")]
    ]
    reply_markup = ReplyKeyboardMarkup(button_list, resize_keyboard=True, one_time_keyboard=False)
    update.message.reply_text("В школе все время придется переходить по кабинетам, ведь для разных уроков есть разные кабинеты.\nТакже в школе есть несколько специальных кабинетов со специальными функциями", reply_markup=reply_markup)
def schedule(update, context):
    button_list = [
        [KeyboardButton('9 класс'), KeyboardButton('10 класс'),
         KeyboardButton("11 класс")]
        ]
    reply_markup = ReplyKeyboardMarkup(button_list, resize_keyboard=True, one_time_keyboard=False)
    update.message.reply_text("Перед началом учебного года, реккомендую посмотреть на расписание каждого урока, чтобы в первые дни учебы не бегать по школе, ища нужный кабинет)", reply_markup=reply_markup)
def schedule10(update, context):
    update.message.reply_text("Расписание для 10 класса можно посмотреть по ссылке:\nhttps://drive.google.com/file/d/1xsGEmNP3ia9qmxVTGB_CWaVNkFJDps8N/view")
def schedule11(update, context):
    update.message.reply_text("Расписание для 11 класса можно посмотреть по ссылке:\nhttps://drive.google.com/file/d/1xsGEmNP3ia9qmxVTGB_CWaVNkFJDps8N/view")
def schedule9(update,context):
    update.message.reply_text("Расписание для 9 класса можно посмотреть по ссылке:\nhttps://drive.google.com/drive/folders/1WaGcSYuMRTWuE0LdQXzZ_Lwl0s34MApZ")
def floors(bot, update):
    update.bot.send_photo(chat_id=bot.message.chat_id, photo=open("Схема новая.png", "rb"))
# def send_facts(bot, update):
#     fact = random.choice(info_pictures)
#     update.bot.send_photo(chat_id=bot.message.chat_id, photo=open(fact[1], 'rb'))
def main():
    updater = Updater("5866321892:AAG_EVUN4aYz_B46gsXnExKyg1rENLmKo7Q", use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("clear", clear))
    dispatcher.add_handler(MessageHandler(Filters.text, text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()