from dataclasses import dataclass
from flask import Flask, session, redirect, render_template, request

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
app.secret_key = "Aula5"
@app.route('/')
def index():
    if "user" in session:
        return render_template('lista.html', title='Games', games=games)
    else:
        return redirect("/login")

@app.route('/novo', methods=["GET"])
def novo():
    if "user" in session:
        return render_template('novo.html', title='New Game')
    else:
        return redirect("/login")

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
        session["user"] = user
        return redirect("/")
    else:
        return redirect("/login")

@app.route("/logon")
def logon():
    session.clear()
    return redirect("/login")
app.run(debug=True)