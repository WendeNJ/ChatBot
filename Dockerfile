FROM python:3.11-slim

LABEL authors="Wenderson"

WORKDIR /app
COPY ProgramPrincipal .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "Inicializacao/ChatBotFuria.py"]
