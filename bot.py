from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
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
    "Сумніваєшся? Згадай, скільки вже пройдено 💪",
    "Дозволь собі бути гордою за себе 💖",
    "Ти 💎 — головна героїня своєї історії 📖",
    "Життя не репетиція. Грай по-крупному 🎭",
    "В тобі вже є все, що потрібно 💗",
    "Ще одна дія 👣 — ще один крок до мрії 🌈"
]

# Список заспокійливих фраз
calming_quotes = [
    "Все добре, ти справляєшся 🌸",
    "Зроби глибокий вдих 🧘‍♀️ Видих — ти в безпеці 💗",
    "Не поспішай. У тебе є час 🕊",
    "Твої емоції — це нормально 💌",
    "Ти маєш право на відпочинок 🌙",
    "Усе минеться, ти сильна 💪",
    "Сьогодні ти вже зробила достатньо 💞"
]

# Команда /start з кнопками
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💪 Мотивуй мене!", callback_data="motivate")],
        [InlineKeyboardButton("🧘 Заспокой мене", callback_data="calm")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привіт! Я твій Мотиваційний Бот 🤖✨\nНатисни кнопку нижче, щоб отримати заряд натхнення!",
        reply_markup=reply_markup
    )

# Обробка натискання кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "motivate":
        quote = random.choice(motivational_quotes)
    elif query.data == "calm":
        quote = random.choice(calming_quotes)
    else:
        quote = "Я тебе підтримую ❤️"

    await query.edit_message_text(quote)

# Запускаємо бота
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))
app.run_polling()
