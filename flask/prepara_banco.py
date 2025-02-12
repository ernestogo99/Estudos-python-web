import psycopg2
import psycopg2.extras


hostname = 'localhost'
database = 'jogoteca'
username = 'postgres'
pwd = '110102ee'
port_id = '5432'

conn = None
cursor = None

try:
   
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )
    
   
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    

    TABLES = {
        'Jogos': '''
            CREATE TABLE IF NOT EXISTS jogos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                categoria VARCHAR(40) NOT NULL,
                console VARCHAR(20) NOT NULL
            );
        ''',
        'Usuarios': '''
            CREATE TABLE IF NOT EXISTS usuarios (
                nome VARCHAR(20) NOT NULL,
                nickname VARCHAR(8) PRIMARY KEY,
                senha VARCHAR(100) NOT NULL
            );
        '''
    }

    for tabela_nome, tabela_sql in TABLES.items():
        print(f"Criando tabela {tabela_nome}: ", end=' ')
        cursor.execute(tabela_sql)
        print('OK')

 
    usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
    usuarios = [
        ("Bruno Divino", "BD", "alohomora"),
        ("Camila Ferreira", "Mila", "paozinho"),
        ("Guilherme Louro", "Cake", "python_eh_vida")
    ]
    cursor.executemany(usuario_sql, usuarios)

  
    jogos_sql = 'INSERT INTO jogos (nome, categoria, console) VALUES (%s, %s, %s)'
    jogos = [
        ('Tetris', 'Puzzle', 'Atari'),
        ('God of War', 'Hack n Slash', 'PS2'),
        ('Mortal Kombat', 'Luta', 'PS2'),
        ('Valorant', 'FPS', 'PC'),
        ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
        ('Need for Speed', 'Corrida', 'PS2')
    ]
    cursor.executemany(jogos_sql, jogos)

  
    cursor.execute('SELECT * FROM usuarios')
    print(' -------------  Usuários:  -------------')
    for user in cursor.fetchall():
        print(user['nickname'], user['nome'])

 
    cursor.execute('SELECT * FROM jogos')
    print(' -------------  Jogos:  -------------')
    for jogo in cursor.fetchall():
        print(jogo['nome'], jogo['categoria'])


    conn.commit()

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
   
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()
