import logging
from telegram.ext import CommandHandler

def start(update, context):
    """Responde ao comando /start."""
    update.message.reply_text('Bem-vindo ao Crypto Pay Bot!')

def setup_handlers(dispatcher):
    """Configura os handlers para os comandos do bot."""
    dispatcher.add_handler(CommandHandler('start', start))
