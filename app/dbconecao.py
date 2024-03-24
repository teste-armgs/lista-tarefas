import mysql.connector

def conectar_banco():
    host = 'localhost'
    usuario = 'root'
    senha = ''
    banco = 'dblista_tarefa'

    try:
        # Estabelecer conexão com o banco de dados
        conexao = mysql.connector.connect(
            host=host,
            user=usuario,
            password=senha,
            database=banco
        )
        print("Conexão bem-sucedida ao banco de dados!")
        return conexao

    except mysql.connector.Error as erro:
        print("Erro ao conectar ao banco de dados:", erro)
        return None
    
