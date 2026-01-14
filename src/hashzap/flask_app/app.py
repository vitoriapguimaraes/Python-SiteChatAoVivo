from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from datetime import datetime

from hashzap.config import Config, logger

app = Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def home():
    return render_template("index.html")


@socketio.on("message")
def handle_message(data):
    """
    Gerencia mensagens recebidas.
    Espera um dicionário com 'usuario' e 'texto'.
    """
    usuario = data.get("usuario", "Anônimo")
    texto = data.get("texto", "")

    if not texto.strip():
        return

    timestamp = datetime.now().strftime("%H:%M")

    msg_formatada = {"usuario": usuario, "texto": texto, "timestamp": timestamp}

    logger.info(f"Mensagem de {usuario}: {texto}")

    # Broadcast da mensagem para todos os conectados
    emit("message", msg_formatada, broadcast=True)


@socketio.on("connect")
def handle_connect():
    logger.info("Novo cliente conectado")


@socketio.on("disconnect")
def handle_disconnect():
    logger.info("Cliente desconectado")


if __name__ == "__main__":
    logger.info(f"Iniciando servidor Flask na porta {Config.FLASK_PORT}...")
    socketio.run(app, host="0.0.0.0", port=Config.FLASK_PORT, debug=Config.DEBUG)
