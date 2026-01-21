import logging
import yaml
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# إعداد السجلات (Logs) لمعرفة ما يحدث في البوت
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# دالة لتحميل التوكن من ملف yaml
def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

# أمر البداية /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="أهلاً بك! أنا بوت تجريبي مرفوع من GitHub."
    )

if __name__ == '__main__':
    config = load_config()
    TOKEN = config['bot_token']
    
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    print("البوت يعمل الآن...")
    application.run_polling()
 
