from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:110102ee@localhost:5432/jogoteca'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Jogo(db.Model):
    __tablename__ = 'jogos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome


with app.app_context():
    db.create_all()

    
    usuarios = [
        Usuario(nome="Bruno Divino", nickname="BDd", senha="alohomora"),
        Usuario(nome="Camila Ferreira", nickname="Mila", senha="paozinho"),
        Usuario(nome="Guilherme Louro", nickname="Cake", senha="python_eh_vida")
    ]
    jogos = [
        Jogo(nome='Tetris', categoria='Puzzle', console='Atari'),
        Jogo(nome='God of War', categoria='Hack n Slash', console='PS2'),
        Jogo(nome='Mortal Kombat', categoria='Luta', console='PS2'),
        Jogo(nome='Valorant', categoria='FPS', console='PC'),
        Jogo(nome='Crash Bandicoot', categoria='Hack n Slash', console='PS2'),
        Jogo(nome='Need for Speed', categoria='Corrida', console='PS2')
    ]

    db.session.add_all(usuarios)
    db.session.add_all(jogos)
    db.session.commit()

    
    all_usuarios = Usuario.query.all()
    print(' -------------  Usuários:  -------------')
    for user in all_usuarios:
        print(user.nickname, user.nome)

    all_jogos = Jogo.query.all()
    print(' -------------  Jogos:  -------------')
    for jogo in all_jogos:
        print(jogo.nome, jogo.categoria)
