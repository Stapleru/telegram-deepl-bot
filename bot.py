
import deepl
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

env_auth_key = "DEEPL_AUTH_KEY"
env_bot_token = "BOT_TOKEN"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Для перевода с английского на русский - просто введите текст")

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    result = translator.translate_text(update.message.text, source_lang='EN', target_lang='RU') 
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Перевод: ' + result.text)

if __name__ == '__main__':

    auth_key = os.getenv(env_auth_key)
    bot_token = os.getenv(env_bot_token)

    if auth_key == None or bot_token == None:
         raise Exception(
            f"Please provide auth key and via the {env_auth_key} and {env_bot_token} environment variables"
        )

    translator = deepl.Translator(auth_key)
    translator.get_usage()

    application = ApplicationBuilder().token(bot_token).build()
    
    translate_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), translate)
    start_handler = CommandHandler('start', start)

    application.add_handler(start_handler)
    application.add_handler(translate_handler)
    
    application.run_polling()