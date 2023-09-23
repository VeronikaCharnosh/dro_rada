import telebot
from telebot import types


bot = telebot.TeleBot('6648171588:AAHXlel6-fD4PZ7G5l7Q--_gQsE5RFV-f8o')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привіт! Що ж обери кнопку', reply_markup=first_menu())


def first_menu():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('💡 Про місто')
    markup.row(btn1)
    btn2 = telebot.types.KeyboardButton('ТІЦ рекомендує')
    btn3 = telebot.types.KeyboardButton('Як дістатися та де переночувати')
    markup.row(btn2, btn3)
    btn4 = telebot.types.KeyboardButton('Контакти ТІЦ м. Дрогобича')
    btn5 = telebot.types.KeyboardButton('Тематичні карти')
    markup.row(btn4, btn5)
    btn6 = telebot.types.KeyboardButton('Регіон')
    btn7 = telebot.types.KeyboardButton('Сувеніри')
    markup.row(btn6, btn7)
    return markup

def menu_for_recomend():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Варто відвідати')
    btn2 = telebot.types.KeyboardButton('Музей')
    btn3 = telebot.types.KeyboardButton('Події')
    btn4 = telebot.types.KeyboardButton('Екскурсії')
    btn5 = telebot.types.KeyboardButton('Гіди')
    btn6 = telebot.types.KeyboardButton('Гастро фішки')
    btn7 = telebot.types.KeyboardButton('Назад у головне меню')
    markup.row(btn1, btn2, btn3)
    markup.row(btn4, btn5, btn6)
    markup.row(btn7)
    return markup

def menu_for_column3():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Готелі/ апартаменти')
    btn2 = telebot.types.KeyboardButton('Транспорт')
    btn3 = telebot.types.KeyboardButton('Назад у головне меню')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    return markup


@bot.message_handler(content_types=['text'])
def text_handler(message):
    cid = message.chat.id
    if message.text.strip() == '💡 Про місто':
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton('💡Коротка інформація', callback_data = 'short_info')
        markup.add(btn1)
        bot.send_message(cid, 'Деяка корисна інформація про нас', reply_markup = markup)
    elif message.text.strip() == 'ТІЦ рекомендує':
        bot.send_message(cid, 'ТІЦ рекомендує', reply_markup = menu_for_recomend())
    elif message.text.strip() == 'Варто відвідати':
        bot.send_message(cid, '1. Площа Ринок\n\
2.Вул. Тараса Шевченка вулиця нафтоаих магманатів\n\
3.Вул. Іана Франка\n\
4.Вул. Лесі Українки\n\
5. Церкви\n\
6.Пам`ятники\n\
7. топ 5 локацій з сайту\n\
8.Вуличний музей, посилання на сайт\n ')
    elif message.text.strip() == 'Музей':
        bot.send_message(cid, '6 локацій музею,інормація, ціна і год роботи\n\
назва музею фото години роботи і посилання на сайт\n ') 
    elif message.text.strip() == 'Події':
        bot.send_message(cid, '1.куди піти дрогобич\n\
2.театр/ кінотеатр де знаходиться, фото, тел для довідок\n ') 
    elif message.text.strip() == 'Екскурсії':
        bot.send_message(cid, '1.солеварня\n\
2.підняття на вежу\n\
3.театралізована\n\
4.шпацер\n\
5.екскурсія в дворику\n\
6.екскурсія містом\n ')
    elif message.text.strip() == 'Гіди':
        bot.send_message(cid, '1. перелік гідів\n\
2. фото спеціалізація сови телефон')
    elif message.text.strip() == 'Гастро фішки':
        bot.send_message(cid, '1. Заклади харчування\n\
2. фото гастрофішки + посилання на інсту')
    elif message.text.strip() == 'Як дістатися та де переночувати':
        bot.send_message(cid, 'Як дістатися та де переночувати', reply_markup = menu_for_column3())
    elif message.text.strip() == 'Назад у головне меню':
        bot.send_message(cid, 'головне меню', reply_markup = first_menu())
    elif message.text.strip() == 'Готелі/ апартаменти':
        bot.send_message(cid, '1.Бомбонєрка\n\
2.зефір\n\
3.будинок самарянина\n\
4.лимон\n\
5.нова хата')
    elif message.text.strip() == 'Транспорт':
        bot.send_message(cid, ' <b>Громадський</b>\n\
1.Автостанція\n\
2.Ж/Д\n\
3.прокат велосипедів\n\
4.самокати\n\n\
<b>Таксі</b>', parse_mode='html')     
    elif message.text.strip() == 'Контакти ТІЦ м. Дрогобича':  
        bot.send_message(cid, 'Фото, тел, пошта, вул, соц мережі') 
    elif message.text.strip() == 'Тематичні карти':
        bot.send_message(cid, '1. посилання на сайт\n\
2. карта стецюкa')    
    elif message.text.strip() == 'Регіон':
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton('Борислав', callback_data = 'boryslav')
        btn2 = telebot.types.InlineKeyboardButton('Трускавець', callback_data = 'truskavets')
        btn3 = telebot.types.InlineKeyboardButton('Нагуєвичі', callback_data = 'nahuevychi')
        btn4 = telebot.types.InlineKeyboardButton('Тустань', callback_data = 'tustan')
        btn5 = telebot.types.InlineKeyboardButton('Стебник', callback_data = 'stebnyk')
        btn6 = telebot.types.InlineKeyboardButton('Стрий', callback_data = 'stryi')
        btn7 = telebot.types.InlineKeyboardButton('Залужани', callback_data = 'zaluzhany')
        btn8 = telebot.types.InlineKeyboardButton('Меденичі', callback_data = 'medenychi')
        btn9 = telebot.types.InlineKeyboardButton('Східниця', callback_data = 'skhidnytsia')
        btn10 = telebot.types.InlineKeyboardButton('Сколе', callback_data = 'skole')
        markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10)
        bot.send_message(cid, 'Виберіть регіон', reply_markup = markup)
    elif message.text.strip() == 'Сувеніри':
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton('Можливість замовити', callback_data = 'possible')
        markup.add(btn1)
        bot.send_message(cid, 'Сувеніри', reply_markup = markup)


@bot.callback_query_handler(func = lambda call: True)
def inline_menu(call):
    cid = call.message.chat.id
    data = call.data
    if data == "short_info":
        bot.send_message(cid, 'Посилання на сайт міської ради - https://drohobych-rada.gov.ua')
    elif data == "boryslav":
        bot.send_message(cid, f"{data}")
        bot.send_message(cid, "to be updated")
    elif data == "truskavets":
        bot.send_message(cid, f"{data}")
        bot.send_message(cid, "to be updated")
    elif data == "nahuevychi":
        bot.send_message(cid, f"{data}")
        bot.send_message(cid, "to be updated")
    elif data == "tustan":
        bot.send_message(cid, f"{data}")
        bot.send_message(cid, "to be updated")
    elif data == "stebnyk":
        bot.send_message(cid, f"{data}")
        bot.send_message(cid, "to be updated")
    elif data == "stryi":
        bot.send_message(cid, f"{data}")
        bot.send_message(cid, "to be updated")
    elif data == "zaluzhany":
        bot.send_message(cid, f"{data}")
        bot.send_message(cid, "to be updated")
    elif data == "medenychi":
        bot.send_message(cid, f"{data}")
        bot.send_message(cid, "to be updated")
    elif data == "skhidnytsia":
        bot.send_message(cid, f"{data}")
        bot.send_message(cid, "to be updated")
    elif data == "skole":
        bot.send_message(cid, f"{data}")
        bot.send_message(cid, "to be updated")
    elif data == "possible":
        bot.send_message(cid, "to be updated")
    

bot.infinity_polling()