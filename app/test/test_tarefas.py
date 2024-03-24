import unittest
from main import ListTask

class TestTarefas(unittest.TestCase):

    def setUp(self):
        self.list_task = ListTask()

    def test_criar_tarefas(self):
        self.list_task.limpar_tarefas()
        self.list_task.adicionar("Tarefa de teste", "2", "Pendente")
        tarefas = self.list_task.exibir('4')
        self.assertEqual(len(tarefas), 1)
        self.assertEqual(tarefas[0]['nome'], "Tarefa de teste")
        self.assertEqual(tarefas[0]['prioridade'], 2)
        self.assertEqual(tarefas[0]['status'], "Pendente")

    def test_filtrar_por_prioridade(self):
        self.list_task.limpar_tarefas()
        self.list_task.adicionar("Tarefa de alta prioridade", "1", "Pendente")
        self.list_task.adicionar("Tarefa de baixa prioridade", "3", "Pendente")
        self.list_task.adicionar("Tarefa de média prioridade", "2", "Pendente")
        self.list_task.adicionar("Tarefa2 de alta prioridade", "1", "Pendente")

        alta_prioridade = self.list_task.exibir('1')
        self.assertEqual(len(alta_prioridade), 2)
        self.assertEqual(alta_prioridade[0]['prioridade'], 1)

        todas_as_prioridades = self.list_task.exibir('4')
        self.assertEqual(len(todas_as_prioridades), 4)

    def test_concluir_tarefa(self):
        self.list_task.limpar_tarefas()
        self.list_task.adicionar("Tarefa de teste", "2", "Pendente")
        self.list_task.finalizar(0)
        tarefas_concluidas = self.list_task.exibir('4')
        self.assertEqual(tarefas_concluidas[0]['status'], "Concluído")

    def test_filtrar_por_prioridade_invalida(self):
        self.list_task.limpar_tarefas()
        self.list_task.adicionar("Tarefa de teste", "2", "Pendente")
        filtradas = self.list_task.exibir('5')
        self.assertEqual(len(filtradas), 0)

if __name__ == '__main__':
    unittest.main()
