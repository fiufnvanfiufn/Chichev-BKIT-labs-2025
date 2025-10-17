import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from config import BOT_TOKEN

bot = telebot.TeleBot("8040078848:AAGO4qrDMPEI39YuK81lsrZ6U6-dfbeUmMo")

active_workers = {}

def main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    btn_start = KeyboardButton("Начать работу")
    btn_stop = KeyboardButton("Закончить работу")
    btn_check = KeyboardButton("Кто работает")

    keyboard.add(btn_start, btn_stop)
    keyboard.add(btn_check)

    return keyboard

def add_worker(user_id, username, branch_name="main"):
    if user_id in active_workers:
        return False

    active_workers[user_id] = {
        "username": username,
        "branch_name": branch_name
    }
    return True

def remove_worker(user_id):
    if user_id in active_workers:
        del active_workers[user_id]
        return True
    return False

def get_active_workers():
    return list(active_workers.values())

def is_someone_working():
    return len(active_workers) > 0

def is_user_working(user_id):
    return user_id in active_workers



@bot.message_handler(commands=['start'])
def start_command(message):
    text = """Бот для отслеживания работы в Git

Управление:
    Начать работу - отметить что ты работаешь
    Закончить работу - отметить завершение
    Кто работает - посмотреть активных
"""
    bot.send_message(message.chat.id, text, reply_markup=main_keyboard())

@bot.message_handler(func=lambda message: message.text == "Начать работу")
def start_work(message):
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name

    if is_someone_working():
        workers = get_active_workers()
        worker_list = "\n".join([f"• {w['username']} ({w['branch_name']})" for w in workers])
        bot.send_message(message.chat.id, f"Уже работает:\n{worker_list}")
        return

    if add_worker(user_id, username):
        bot.send_message(message.chat.id, "Вы начали работу в ветке main!")
    else:
        bot.send_message(message.chat.id, "Вы уже работаете!")

@bot.message_handler(func=lambda message: message.text == "Закончить работу")
def stop_work(message):
    user_id = message.from_user.id

    if remove_worker(user_id):
        bot.send_message(message.chat.id, "Вы закончили работу!")
    else:
        bot.send_message(message.chat.id, "Вы не начинали работу!")

@bot.message_handler(func=lambda message: message.text == "Кто работает")
def check_workers(message):
    workers = get_active_workers()

    if not workers:
        bot.send_message(message.chat.id, "Сейчас никто не работает")
    else:
        worker_list = "\n".join([f"• {w['username']} ({w['branch_name']})" for w in workers])
        bot.send_message(message.chat.id, f"Сейчас работают:\n{worker_list}")

@bot.message_handler(func=lambda message: True)
def unknown_command(message):
    bot.send_message(message.chat.id, "Не понимаю команду. Используй кнопки ниже!",
                     reply_markup=main_keyboard())

if __name__ == "__main__":
    bot.infinity_polling()
