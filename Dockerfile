
FROM python:3.11-slim


LABEL authors="Wenderson"

WORKDIR /ProgramPrincipal/Inicializaçao

COPY ./ProgramPrincipal /ProgramPrincipal/
COPY ./requirements.txt /ProgramPrincipal/Inicializaçao/

RUN pip install --no-cache-dir -r requirements.txt






EXPOSE 5000


CMD ["python", "/ProgramPrincipal/Inicializaçao/ChatBotFuria.py"]
