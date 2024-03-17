class ListTask:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, tarefa, priori, status):
        if not self.tarefas:
            self.tarefas.append({'tarefa': tarefa, 'prioridade': priori, 'status': status})
        else:
            for i, t in enumerate(self.tarefas):
                if int(priori) < int(t['prioridade']):
                    self.tarefas.insert(i, {'tarefa': tarefa, 'prioridade': priori, 'status': status})
                    return
                elif int(priori) == int(t['prioridade']):
                    self.tarefas.insert(i+1, {'tarefa': tarefa, 'prioridade': priori, 'status': status})
                    return

    def finalizar(self, indice_tarefa):
        if 0 <= indice_tarefa < len(self.tarefas):
            self.tarefas[indice_tarefa]['status'] = 'Concluído'

    def filtrar(self, priori):
        copia = self.tarefas.copy
        temp = []
        if not copia:
            print("Nenhuma tarefa encontrada.")
        elif priori.lower() == '4':
            return copia
        elif priori in ['1', '2', '3']:
            for tarefa in copia:
                if tarefa['prioridade'].lower().strip() == priori.lower().strip():
                    temp.append(tarefa)
            return temp
        else:
            print("Opção invalida")
            return []



    def exibir(self, tarefas):
        if not self.tarefas:
            print("Nenhuma tarefa encontrada.")
        else:
            for indice, tarefa in enumerate(tarefas):
                print(f"{indice + 1}. {tarefa['tarefa']} - Prioridade: {tarefa['prioridade']} - Status: {tarefa['status']}")

def main():
    list_task = ListTask()

    while True:
        print("\nGerenciador de Tarefas \n1. Adicionar Tarefa"+
              "\n2. Marcar Concluída \n3. Filtrar por Prioridade \n4. Sair")

        opcao = input("Digite sua escolha: ")

        if opcao == '1':
            tarefa = input("Digite a tarefa: ")
            priori = input("Digite a prioridade (1: Alta/2: Média/3: Baixa): ")
            status = 'Pendente'
            if priori in ['1', '2', '3']:
                list_task.adicionar(tarefa, priori, status)
                print("Tarefa adicionada com sucesso!")
            else:
                print("Escolha inválida. Por favor, tente novamente.")

        elif opcao == '2':
            list_task.exibir(list_task.tarefas)
            indice_tarefa = int(input("Digite o índice da tarefa a marcar como concluída: ")) - 1
            list_task.finalizar(indice_tarefa)
            print("Tarefa marcada como concluída!")

        elif opcao == '3':
            priori = input("Digite a prioridade para filtrar (1: Alta/2: Média/3: Baixa/4: Todas): ")
            if priori in ['1', '2', '3', '4']:
                tarefas_filtradas = list_task.filtrar(priori)
                list_task.exibir(tarefas_filtradas)
            else:
                print("Escolha inválida. Por favor, tente novamente.")

        elif opcao == '4':
            print("Saindo...")
            break

        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
