import os
from flask import Flask, send_from_directory
from telegram.ext import Updater

app = Flask(__name__, static_folder='Landing')


TOKEN = os.getenv("TOKEN_BOT")
updater = Updater(TOKEN, use_context=True)

@app.route('/')
def home():
    return send_from_directory('Landing', 'index.html')

if __name__ == '__main__':

    updater.start_polling()

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)