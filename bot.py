from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from telegram import Update, ReplyKeyboardMarkup
from dotenv import load_dotenv
import os
import random

# Завантажуємо токен з .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Список мотиваційних фраз
motivational_quotes = [
    "Ти можеш усе. Просто почни 🔥",
    "Сьогодні ідеальний день, щоб стати кращою версією себе ✨",
    "Роби, що можеш з тим, що маєш, там, де ти є 💪",
    "Твій успіх не за горами 🏔 Він уже в дорозі ✨",
    "Не зупиняйся 💥 Шлях формується під час руху 🚶‍♀️",
    "Ніхто не зробить це замість тебе — але ти можеш 🔥",
    "Навіть маленький крок — це вже рух вперед 🦶",
    "Ти не просто молодець, ти мегамолодець! 🌈",
    "Не чекай ідеального моменту ✨ Створи його 🔥",
    "Сумніваєшся? Згадай, скільки вже пройдено 💪"
]

# Список заспокійливих фраз
calming_quotes = [
    "Все добре, ти справляєшся 🌸",
    "Зроби глибокий вдих 🧘‍♀️ Видих — ти в безпеці 💗",
    "Не поспішай. У тебе є час 🕊",
    "Твої емоції — це нормально 💌",
    "Ти маєш право на відпочинок 🌙",
    "Усе минеться, ти сильна 💪",
    "Сьогодні ти вже зробила достатньо 💞",
    "Світ не впаде, якщо ти відпочинеш 🫶",
    "Піклуйся про себе так, як про найкращу подругу 💖",
    "Тиша — теж відповідь. І вона лікує 🤍"
]

# Команда /start з постійною клавіатурою
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['💪 Мотивуй мене!', '🧘 Заспокой мене']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
    await update.message.reply_text(
        "Привіт! Я твій Мотиваційний Бот 🤖✨\nНатисни кнопку нижче, щоб отримати підтримку!",
        reply_markup=reply_markup
    )

# Обробка натискань на кнопки
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == '💪 Мотивуй мене!':
        await update.message.reply_text(random.choice(motivational_quotes))
    elif text == '🧘 Заспокой мене':
        await update.message.reply_text(random.choice(calming_quotes))
    else:
        await update.message.reply_text("Натисни одну з кнопок нижче 😊")

# Запуск
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
