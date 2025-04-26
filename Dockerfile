
FROM python:3.11-slim


LABEL authors="Wenderson"


WORKDIR /ProgramPrincipal/Inicializacao
COPY ProgramPrincipal/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ProgramPrincipal .


EXPOSE 5000


CMD ["python", "ChatBotFuria.py"]
