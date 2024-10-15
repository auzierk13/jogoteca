from dataclasses import dataclass
from flask import Flask, redirect, render_template, request

@dataclass
class Game:
    nome: str
    categoria:str
    console:str

game1 = Game('Tetris', 'Puzzle', 'Atari')
game2 = Game('God of War', 'Hack n Slash', 'PS2')
game3 = Game('Mortal Kombat', 'Luta', 'PS2')
games = [game1, game2, game3]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='Games', games=games)

@app.route('/novo', methods=["GET"])
def novo():
    return render_template('novo.html', titulo='New Game')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    game = Game(nome, categoria, console)
    games.append(game)
    return redirect("/")

@app.route("/login")
def login():
    return render_template("login.html", title= "Login")

@app.route("/autenticar", methods=["POST"])
def autenticar():
    user = request.form["user"]
    passwd = request.form["passwd"]

    if user =="admin" and passwd =="123":
        return redirect("/novo")
    else:
        return redirect("/login")

app.run(debug=True)