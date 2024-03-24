import mysql.connector

class ListTask:
    def __init__(self):
        self.conexao = self.conectar_banco()
        if self.conexao is not None:
            self.cursor = self.conexao.cursor()
        else:
            print("Não foi possível conectar ao banco de dados.")
            exit()

    def conectar_banco(self):
        host = 'localhost'
        usuario = 'root'
        senha = ''
        banco = 'dblista_tarefa'

        try:
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

    def adicionar(self, tarefa, priori, status):
        try:
            sql = "INSERT INTO tarefas (nome, prioridade, status) VALUES (%s, %s, %s)"
            val = (tarefa, priori, status)
            self.cursor.execute(sql, val)
            self.conexao.commit()
            print("Tarefa adicionada com sucesso!")
        except mysql.connector.Error as erro:
            print("Erro ao adicionar a tarefa:", erro)

    def finalizar(self, indice_tarefa):
        try:
            sql = "UPDATE tarefas SET status = 'Concluído' WHERE idtarefa = (SELECT idtarefa FROM tarefas ORDER BY prioridade ASC LIMIT 1 OFFSET %s);"
            val = (indice_tarefa,)
            self.cursor.execute(sql, val)
            self.conexao.commit()
            print("Tarefa marcada como concluída!")
        except mysql.connector.Error as erro:
            print("Erro ao finalizar a tarefa:", erro)
    
    def exibir(self, priori):
        try:
            if priori == '4':
                sql = "SELECT * FROM `tarefas` ORDER BY `tarefas`.`prioridade` ASC"
                self.cursor.execute(sql)
            else:
                sql = "SELECT * FROM tarefas WHERE prioridade = %s"
                self.cursor.execute(sql, (priori,))
            tarefas = self.cursor.fetchall()
            if not tarefas:
                print("Nenhuma tarefa encontrada.")
                return []
            else:
                for indice, tarefa in enumerate(tarefas):
                    print(f"{indice + 1}. {tarefa[1]} - Prioridade: {tarefa[2]} - Status: {tarefa[3]}")
                tarefas_formatadas = [{'idtarefa': tarefa[0], 'nome': tarefa[1], 'prioridade': tarefa[2], 'status': tarefa[3]} for tarefa in tarefas]
                return tarefas_formatadas
        except mysql.connector.Error as erro:
            print("Erro ao filtrar as tarefas:", erro)
            return []
   
    def limpar_tarefas(self):
        try:
            # Remover todos os registros da tabela
            sql_delete = "DELETE FROM tarefas;"
            self.cursor.execute(sql_delete)
            
            # Reiniciar o valor auto_increment para a coluna idtarefa
            sql_reset_auto_increment = "ALTER TABLE tarefas AUTO_INCREMENT = 1;"
            self.cursor.execute(sql_reset_auto_increment)
            
            # Commit das alterações
            self.conexao.commit()


            print("Todos os dados da tabela 'tarefas' foram apagados com sucesso!")
        except mysql.connector.Error as erro:
            print("Erro ao limpar os dados da tabela 'tarefas':", erro)