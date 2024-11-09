
from flask import  flash, redirect, render_template, request, session, url_for
from jogoteca import db,app
from models import Jogo, Usuario


@app.route("/")
def index():  
    jogos= Jogo.query.order_by(Jogo.id)
    return render_template("lista.html",titulo="Jogos",jogos=jogos)


@app.route("/editar/<int:id>")
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect(url_for('login',proxima=url_for('editar')))
    
    jogo=Jogo.query.filter_by(id=id).first()
    return render_template("editar.html",titulo="Editando jogo",jogo=jogo)



@app.route("/novo")
def novo():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect(url_for('login',proxima=url_for('novo')))
    return render_template("novo.html",titulo="Criando jogo")



@app.route("/criar", methods=['POST'],)
def criar():
    nome=request.form['nome']
    categoria=request.form['categoria']
    console=request.form['console']
    
    jogo=Jogo.query.filter_by(nome=nome).first()

    if jogo:
        flash("Jogo ja existente")
        return redirect(url_for('index'))
    
    novo_jogo=Jogo(nome=nome,categoria=categoria,console=console)
    db.session.add(novo_jogo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/atualizar", methods=['POST'],)
def atualizar():
    jogo=Jogo.query.filter_by(id=request.form['id']).first()
    jogo.nome=request.form['nome']
    jogo.categoria=request.form['categoria']
    jogo.console=request.form['console']

    db.session.add(jogo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/deletar/<int:id>")
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect(url_for('login'))
    
    Jogo.query.filter_by(id=id).delete()
    db.session.commit()
    flash("Jogo deletado com sucesso")
    return redirect(url_for('index'))

@app.route("/login")
def login():
    proxima=request.args.get('proxima')
    return render_template("login.html",proxima=proxima)
    

@app.route("/autenticar", methods=['POST'])
def autenticar():
    usuario=Usuario.query.filter_by(nickname= request.form['usuario']).first()
    if usuario:
       
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