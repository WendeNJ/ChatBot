import requests
import websocket
import threading
import time
import os

def get_furia_live_match_id():
    token = os.getenv("PANDASCORE_TOKEN")
    url = f"https://api.pandascore.co/csgo/matches/running?token={token}"

    response = requests.get(url)

    if response.status_code == 200:
        matches = response.json()

        for match in matches:
            opponents = match.get('opponents', [])
            for opponent in opponents:
                team_name = opponent['opponent']['name']
                if 'FURIA' in team_name.upper():
                    match_id = match['id']
                    print(f"⚡ FURIA tá jogando! ID da partida: {match_id}")
                    return match_id
        print("❌ FURIA não está jogando agora.")
    else:
        print(f"Erro na requisição: {response.status_code}")
        time.sleep(30)
        return get_furia_live_match_id()

    return None

def on_message(ws, message):
    print(f"📈 Atualização do placar: {message}")

def on_error(ws, error):
    print(f"❌ Erro: {error}")

def on_close(ws, close_status_code, close_msg):
    print("🔒 Conexão encerrada. Tentando reconectar...")
    time.sleep(5)
    ws.run_forever()

def on_open(ws):
    print("🔓 Conexão aberta com o WebSocket!")

def conectar_websocket(match_id):
    token = os.getenv("PANDASCORE_TOKEN")
    ws_url = f"wss://live.pandascore.co/matches/{match_id}?token={token}"

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(ws_url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()

