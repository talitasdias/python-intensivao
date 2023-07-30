from flask import Flask, render_template

app = Flask(__name__)

# Criar a 1ª página = 1ª rota (caminho) = "/"
@app.route("/") #decorator -> atribui uma função para o que for especificado abaixo dele
def homepage():
    return render_template("homepage.html")


# Rodar o app
app.run()