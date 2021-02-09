import telebot
from telebot import types

bot = telebot.TeleBot('1500810910:AAEA40SqqqlUxnqBA7iuw4w8yPuU-0ql9ng')


class Appeal:
    def __init__(self, autopark, defect, num_route, phone):
        self.defect = autopark
        self.autopark = defect
        self.num_route = num_route
        self.phone = phone

    def get_info(self):
        return f"""
        Причина: {self.defect}
        Автопарк: {self.autopark}
        Маршрут: {self.num_route}
        Телефон водителя: {self.phone}"""


temp = dict()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('Мобильный терминал не работает')
    itembtn2 = types.KeyboardButton('Стационар не работает')
    itembtn3 = types.KeyboardButton('Моб и стационар не работает')
    itembtn4 = types.KeyboardButton('Нет звука')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    msg = bot.send_message(chat_id, 'Описание неисправности', reply_markup=markup)
    bot.register_next_step_handler(msg, send_welcome2)


def send_welcome2(message):
    temp['autopark'] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    itembtn1 = types.KeyboardButton("SHYM-Bus")
    itembtn2 = types.KeyboardButton("T-Bus")
    itembtn3 = types.KeyboardButton("ИП Сулейменов")
    itembtn4 = types.KeyboardButton('Автоимпульс')
    itembtn5 = types.KeyboardButton('Автокомбинат')
    itembtn6 = types.KeyboardButton('Асыл')
    itembtn7 = types.KeyboardButton('Бек-Сервис')
    itembtn8 = types.KeyboardButton('Бекзат Сервис')
    itembtn9 = types.KeyboardButton("Береке Кит")
    itembtn10 = types.KeyboardButton("Корпорация Руслан")
    itembtn11 = types.KeyboardButton("КиУ")
    itembtn12 = types.KeyboardButton('Ман-Онтустик')
    itembtn13 = types.KeyboardButton('Мир и СО')
    itembtn14 = types.KeyboardButton('Ордабасы')
    itembtn15 = types.KeyboardButton('Сигма')
    itembtn16 = types.KeyboardButton('Экспресс ')
    itembtn17 = types.KeyboardButton('Greenbus service')
    itembtn18 = types.KeyboardButton('Абдуганиев')
    itembtn19 = types.KeyboardButton('СанжарМоторс')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10,
               itembtn11, itembtn12, itembtn13, itembtn14, itembtn15, itembtn16, itembtn17, itembtn18, itembtn19)

    msg = bot.send_message(message.chat.id, 'Выберите Автопарк', reply_markup=markup)
    bot.register_next_step_handler(msg, route)

def route(message):
    chat_id = message.chat.id
    temp['defect'] = message.text
    markup = types.ReplyKeyboardRemove(selective=False)
    msg = bot.send_message(chat_id, 'Введите маршрут автобуса', reply_markup=markup)
    bot.register_next_step_handler(msg, number)

def number(message):
    temp['num_route'] = message.text
    chat_id = message.chat.id
    markup = types.ReplyKeyboardRemove(selective=False)
    msg = bot.send_message(chat_id, 'Введите телефон номер водителя', reply_markup=markup)
    bot.register_next_step_handler(msg, data_processing)

def data_processing(message):
    temp['phone'] = message.text
    ap = Appeal(**temp)
    chat_id = message.chat.id
    group_id = -1001475404086
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(group_id, f'Поступила заявка:\n{ap.get_info()}', reply_markup=markup)
    bot.send_message(chat_id, f'Приняли Вашу заявку\n{ap.get_info()}', reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
