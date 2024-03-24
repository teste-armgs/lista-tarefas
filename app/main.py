from dbconecao import ListTask

def main():
    list_task = ListTask()

    while True:
        print("\nGerenciador de Tarefas \n1. Adicionar Tarefa"+
              "\n2. Marcar Concluída \n3. Exibir por Prioridade \n4. Sair")

        opcao = input("Digite sua escolha: ")

        if opcao == '1':
            tarefa = input("Digite a tarefa: ")
            priori = input("Digite a prioridade (1: Alta/2: Média/3: Baixa): ")
            status = 'Pendente'
            if priori in ['1', '2', '3']:
                list_task.adicionar(tarefa, priori, status)
            else:
                print("Escolha inválida. Por favor, tente novamente.")

        elif opcao == '2':
            list_task.exibir('4')
            indice_tarefa = int(input("Digite o índice da tarefa a marcar como concluída: "))
            list_task.finalizar(indice_tarefa)
            
        elif opcao == '3':
            priori = input("Digite a prioridade para exibir (1: Alta/2: Média/3: Baixa/4: Todas): ")
            if priori in ['1', '2', '3', '4']:
                list_task.exibir(priori)
            else:
                print("Escolha inválida. Por favor, tente novamente.")

        elif opcao == '4':
            print("Saindo...")
            break

        elif opcao == 'drop':
            print("Apagando os dados...")
            list_task.limpar_tarefas()

        else:
            print("Escolha inválida. Por favor, tente novamente.")

    list_task.cursor.close()
    list_task.conexao.close()

if __name__ == "__main__":
    main()
