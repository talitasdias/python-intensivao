from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

#criar a funcionalidada de enviar mensagem
@socketio.on("message")
def gerenciar_msg(mensagem):
    send(mensagem, broadcast=True)

# Criar a 1ª página = 1ª rota (caminho) = "/"
@app.route("/") #decorator -> atribui uma função para o que for especificado abaixo dele
def homepage():
    return render_template("homepage.html")


# Rodar o app
socketio.run(app, host="192.168.1.6")