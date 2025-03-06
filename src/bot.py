import logging
import threading
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from payments import get_payments

# Configuração do logging
logging.basicConfig(level=logging.INFO)

TELEGRAM_BOT_TOKEN = "SEU_TELEGRAM_BOT_TOKEN"

# Função para iniciar o bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Bem-vindo ao FlowPay! Monitorando pagamentos em tempo real.")

# Função para monitorar pagamentos no background
def monitor_payments():
    while True:
        get_payments()
        time.sleep(30)  # Checa pagamentos a cada 30 segundos

if __name__ == "__main__":
    # Inicia a thread de monitoramento
    thread = threading.Thread(target=monitor_payments, daemon=True)
    thread.start()

    # Configuração do bot
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()
