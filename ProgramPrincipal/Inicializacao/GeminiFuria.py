import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()


class GeminiFURIA:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest')

    def perguntar(self, pergunta):
        resposta = self.model.generate_content(
            f"Você é o Furinha da FURIA. Responda em português, traga a informaçao para o usuario, voce e simpatico, e fala em tom de torcedor: {pergunta}"
        )
        return resposta.text