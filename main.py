from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, CallbackQueryHandler, filters
import requests
import nest_asyncio
nest_asyncio.apply()

# Установите nest_asyncio если работаете в Jupyter/Colab
# import nest_asyncio
# nest_asyncio.apply()

TOKEN = "TG TOKEN"
API_KEY = "API TOKEN"  # Получите бесплатный ключ на https://www.exchangerate-api.com/

# Топ-10 популярных валют для конвертации
POPULAR_CURRENCIES = {
    "USD": "🇺🇸 Доллар США",
    "EUR": "🇪🇺 Евро",
    "TRY": "🇹🇷 Турецкая лира",
    "THB": "🇹🇭 Тайский бат",
    "KZT": "🇰🇿 Казахстанский тенге",
    "JPY": "🇯🇵 Японская иена",
    "CNY": "🇨🇳 Китайский юань",
    "GEL": "🇬🇪 Грузинский лари",
    "AED": "🇦🇪 ОАЭ дирхам",
    "MVR": "🇲🇻 Мальдивская руфия",

}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 *Конвертер валют из RUB* \n\n"
        "Введите сумму в рублях (например: 1000 или 500.50)",
        parse_mode="Markdown"
    )

async def handle_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        amount = float(update.message.text)
        context.user_data['amount_rub'] = amount
        
        # Получаем актуальные курсы
        response = requests.get(f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/RUB")
        data = response.json()
        
        if data.get("result") != "success":
            raise Exception("Ошибка получения курсов")
            
        context.user_data['rates'] = data['conversion_rates']
        
        # Создаем кнопки
        keyboard = []
        for currency_code, currency_name in POPULAR_CURRENCIES.items():
            keyboard.append([InlineKeyboardButton(
                f"{currency_name} ({currency_code})", 
                callback_data=f"convert_{currency_code}"
            )])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            f"Выберите валюту для конвертации {amount} RUB:",
            reply_markup=reply_markup
        )
            
    except ValueError:
        await update.message.reply_text("Пожалуйста, введите корректную сумму (например: 1000 или 500.50)")
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {str(e)}")

async def convert_currency(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    currency_code = query.data.split('_')[1]
    amount_rub = context.user_data.get('amount_rub', 1)
    rates = context.user_data.get('rates', {})
    
    try:
        if not rates:
            raise Exception("Курсы не загружены")
            
        rate = rates.get(currency_code)
        if not rate:
            raise Exception("Валюта не найдена")
            
        result = amount_rub * rate
        currency_name = POPULAR_CURRENCIES.get(currency_code, currency_code)
        
        await query.edit_message_text(
            f"💱 *Результат конвертации:*\n\n"
            f"• {amount_rub:.2f} RUB = {result:.2f} {currency_code}\n"
            f"• Курс: 1 RUB = {rate:.6f} {currency_code}\n\n"
            f"Для нового расчета введите сумму в рублях",
            parse_mode="Markdown"
        )
        
    except Exception as e:
        await query.edit_message_text(f"Ошибка конвертации: {str(e)}")

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_amount))
    application.add_handler(CallbackQueryHandler(convert_currency, pattern="^convert_"))
    
    application.run_polling()

if __name__ == "__main__":
    main()