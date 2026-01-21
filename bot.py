import os
import time
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# ================== الإعدادات ==================
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

# ================== أوامر البوت ==================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 البوت التجريبي يعمل بنجاح!\n\n"
        "هذا بوت اختبار بدون GitHub Token ✅"
    )

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong! البوت شغال 100%")

# ================== التشغيل ==================
if __name__ == "__main__":
    if not BOT_TOKEN:
        logger.error("❌ لم يتم العثور على TELEGRAM_BOT_TOKEN في Secrets")
        exit(1)

    logger.info("✅ تم العثور على توكن تلجرام")
    logger.info("🚀 بدء تشغيل البوت التجريبي...")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping))

    # إبقاء العملية حية (مهم لـ GitHub Actions)
    def keep_alive():
        while True:
            time.sleep(60)

    logger.info("🤖 البوت يعمل الآن...")
    app.run_polling() 
