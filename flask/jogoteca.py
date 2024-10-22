from flask import Flask, flash,render_template,request,redirect,session,url_for

class Jogo:
    def __init__(self,nome,categoria,console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1=Jogo('tetris','puzzle','atari')
jogo2=Jogo('mario kart','corrida','nintendo ds')
jogo3=Jogo("mortal kombat","luta","ps5")
jogos=[jogo1,jogo2]


class Usuario:
    def __init__(self,nome,nickname,senha):
        self.nome=nome
        self.nickname=nickname
        self.senha=senha
usuario1 = Usuario("ernesto", "e", "senha")
usuario2 = Usuario("camila", "cami", "123")
usuarios = {usuario1.nickname: usuario1, usuario2.nickname: usuario2}

app=Flask(__name__) #faz uma refencia ao próprio arquivo
app.secret_key="ernesto"

@app.route("/")
def index():  
    return render_template("lista.html",titulo="Jogos",jogos=jogos)


@app.route("/novo")
def novo():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect(url_for('login',proxima=url_for('novo')))
    return render_template("novo.html",titulo="Novo jogo")


@app.route("/criar", methods=['POST'],)
def criar():
    nome=request.form['nome']
    categoria=request.form['categoria']
    console=request.form['console']
    jogo=Jogo(nome,categoria,console)
    jogos.append(jogo)
    return redirect(url_for('index'))



@app.route("/login")
def login():
    proxima=request.args.get('proxima')
    return render_template("login.html",proxima=proxima)
    

@app.route("/autenticar", methods=['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(f"Usuário {session['usuario_logado']} logado com sucesso!")
            
            proxima_pagina = request.form['proxima']
            if not proxima_pagina:
                proxima_pagina = url_for('index')
                
            return redirect(proxima_pagina)
    
    flash("Erro no login")
    return redirect(url_for('login'))


@app.route("/logout")
def logout():
    session['usuario_logado']=None
    flash("Logout efetuado com sucesso")
    return redirect(url_for('index'))