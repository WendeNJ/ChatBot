from dotenv import load_dotenv
import os

load_dotenv()
from telebot import TeleBot

CHAVE_API = os.getenv("TELEGRAM_TOKEN")
bot = TeleBot(CHAVE_API)

if CHAVE_API is None:
    print("Erro: A chave da API não foi encontrada")
else:
    print("Chave da API carregada com sucesso!")
