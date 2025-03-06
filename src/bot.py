from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from payments import create_invoice
from payments_module import get_user_transactions
import requests
import sys
print(sys.path)  # Isso mostra os caminhos que o Python está procurando os módulos
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from payments import get_user_transactions



TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("No TELEGRAM_BOT_TOKEN provided. Please set the TELEGRAM_BOT_TOKEN environment variable.")

# Função para criar uma invoice a partir do Telegram
def ordem(update: Update, context: CallbackContext):
    if len(context.args) < 1:
        update.message.reply_text("❌ Use: /ordem <valor> (exemplo: /ordem 10)")
        return
    
    amount = context.args[0]  # Obtém o valor enviado pelo usuário
    pay_url = create_invoice(amount)  # Cria a invoice

    if pay_url:
        update.message.reply_text(f"✅ Ordem criada! Pague aqui: {pay_url}")
    else:
        update.message.reply_text("❌ Erro ao criar ordem de pagamento. Tente novamente!")



API_TOKEN = "SEU_API_TOKEN_AQUI"
API_URL = "https://pay.crypt.bot/api/"
HEADERS = {
    "Crypto-Pay-API-Token": API_TOKEN,
    "Content-Type": "application/json"
}

def get_balance():
    """Consulta o saldo disponível na carteira"""
    response = requests.get(f"{API_URL}getBalance", headers=HEADERS)
    data = response.json()
    
    if not data.get("ok"):
        return "❌ Erro ao buscar saldo."
    
    balance = data["result"]["balance"]
    currency = data["result"]["currency"]
    return f"💰 Seu saldo disponível: {balance} {currency}"

def saldo(update: Update, context: CallbackContext):
    balance_info = get_balance()
    update.message.reply_text(balance_info)

def get_user_transactions(user_id):
    """Busca transações e retorna apenas as do usuário específico"""
    response = requests.get(f"{API_URL}getInvoices", headers=HEADERS)
    data = response.json()
    
    if not data.get("ok"):
        return "❌ Erro ao buscar extrato."

    transactions = []

    for invoice in data["result"]["items"]:
        if invoice.get("payload") == str(user_id):  # Filtra transações do usuário
            transactions.append(f"💰 {invoice['amount']} {invoice['currency']} - {invoice['status']}")

    if not transactions:
        return "📭 Nenhuma transação encontrada para você."

    return "\n".join(transactions)

def extrato(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    transactions_list = get_user_transactions(user_id)
    update.message.reply_text(f"📋 Seu Extrato:\n\n{transactions_list}")

def menu(update: Update, context: CallbackContext):
    commands = (
        "📌 *Comandos Disponíveis:*\n"
        "/start - Inicia o atendimento\n"
        "/ordem <valor> - Cria uma ordem de pagamento\n"
        "/saldo - Consulta seu saldo disponível\n"
        "/extrato - Lista suas últimas transações\n"
        "/menu - Exibe este menu\n"
    )
    update.message.reply_text(commands, parse_mode="Markdown")

if __name__ == "__main__":
    updater = Updater("SEU_TELEGRAM_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ordem", ordem, pass_args=True))
    dp.add_handler(CommandHandler("saldo", saldo))
    dp.add_handler(CommandHandler("extrato", extrato))
    dp.add_handler(CommandHandler("menu", menu))

    updater.start_polling()
    updater.idle()

# Função para iniciar o bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 Olá! Bem-vindo ao FlowPay.\n\nUse /menu para ver as opções disponíveis.")

if __name__ == "__main__":
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("invoice", invoice, pass_args=True))
    
    updater.start_polling()
    updater.idle()
